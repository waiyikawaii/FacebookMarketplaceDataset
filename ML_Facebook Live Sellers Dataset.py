#Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#Load the dataset
df=pd.read_csv('D:\Finlatics\Machine Learning\MLResearch\MLResearch\Facebook Dataset\Facebook_Marketplace_data.csv')

#Drop the empty columns
df=df.drop(columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Check shape and info
print("Shape:", df.shape)
print(df.info())
print(df.head())

#Cleaning Steps
#Convert status_published to datetime
df['status_published']=pd.to_datetime(df['status_published'])

#Check for missing values
print("Missing values:\n", df.isnull().sum())

#The dataset has 7050 rows but the description says 7050 instances — good.
#Some columns are "redundant" — num_reactions=num_likes+num_loves+num_wows+num_hahas+num_sads+num_angrys
#Verify:
reaction_sum=df[['num_likes','num_loves','num_wows','num_hahas','num_sads','num_angrys']].sum(axis=1)
print("Reactions match component sum:", (reaction_sum==df['num_reactions']).all())

'Q1: How does the time of upload (`status_published`)  affects the `num_reaction`?'
#Extract time-based features
df['hour']=df['status_published'].dt.hour
df['day_of_week']=df['status_published'].dt.day_name()
df['month']=df['status_published'].dt.month
df['year']=df['status_published'].dt.year
df['date']=df['status_published'].dt.date

#Average reactions by hour of day
hourly=df.groupby('hour')['num_reactions'].mean().reset_index()

sns.lineplot(data=hourly,x='hour',y='num_reactions',marker='o')
plt.title('Average Number of Reactions by Hour of Upload')
plt.xlabel('Hour of Day (0-23)')
plt.ylabel('Average Reactions')
plt.minorticks_on()
plt.grid(which='major',color='black',linewidth=0.5, linestyle='-')
plt.grid(which='minor', color='red', linewidth=0.5, linestyle=':')
plt.show()

#Average reactions by day of week
dow_order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
dow=df.groupby('day_of_week')['num_reactions'].mean().reindex(dow_order).reset_index()

plt.figure(figsize=(12,4))
ax=sns.barplot(data=dow, x='day_of_week', y='num_reactions', palette='viridis')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), ha='center', va='bottom', fontsize=10)
plt.title('Average Reactions by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Average Reactions')
plt.show()

#Reactions over time (monthly trend)
df['year_month']=df['status_published'].dt.to_period('M')
monthly=df.groupby('year_month')['num_reactions'].mean()
monthly.plot()
plt.title('Average Reactions Over Time (Monthly)')
plt.xlabel('Month')
plt.ylabel('Average Reactions')
plt.minorticks_on()
plt.grid(which='major',color='black',linewidth=0.5, linestyle='-')
plt.grid(which='minor', color='red', linewidth=0.5, linestyle=':')
plt.show()

'Q2: Is there a correlation between the number of reactions (num_reactions) and other engagement metrics such as comments (num_comments) and shares (num_shares)? If so, what is the strength and direction of this correlation?'
#Correlation matrix
engagement=df[['num_reactions','num_comments','num_shares','num_likes','num_loves','num_wows','num_hahas','num_sads','num_angrys']]
corr=engagement.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, cmap='PuBuGn', fmt='.2f')
plt.title('Correlation Heatmap of Engagement Metrics')
plt.show()

#Specific correlations with num_reactions
print(corr['num_reactions'].sort_values(ascending=False))

'Q3: Use the columns status_type, num_reactions, num_comments, num_shares, num_likes, num_loves, num_wows, num_hahas, num_sads, and num_angrys to train a K-Means clustering model on the Facebook Live Sellers dataset.'
#Numerical engagement columns
cluster_features=['num_reactions','num_comments','num_shares', 'num_likes','num_loves','num_wows','num_hahas','num_sads','num_angrys']

#status_type is text → convert to 0/1 columns (one-hot) so K-Means can use it
X_with_type=pd.get_dummies(df[['status_type'] + cluster_features],columns=['status_type'], drop_first=False)

#Scale
X_scaled_type=StandardScaler().fit_transform(X_with_type)
print("Feature matrix shape (with status_type):", X_scaled_type.shape)

#Train K-Means
kmeans=KMeans(n_clusters=5, init='k-means++', random_state=42, n_init=10)
y_kmeans=kmeans.fit_predict(X_scaled_type)

#Show cluster counts
df['cluster'] = y_kmeans
print(df['cluster'].value_counts().sort_index())

'Q4: Use the elbow method to find the optimum number of clusters.'
w=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled_type)
    w.append(kmeans.inertia_)

plt.figure(figsize=(8,4))
plt.plot(range(1,11), w, marker='o')
plt.title('The Elbow Method for Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.minorticks_on()
plt.grid(which='major',color='black',linewidth=0.5, linestyle='-')
plt.grid(which='minor', color='red', linewidth=0.5, linestyle=':')
plt.show()

#Print inertia values
for k, val in zip(range(1,11),w):
    print(f"k={k}: inertia={val:.2f}")

'Q5: What is the count of different types of posts in the dataset?'
post_counts=df['status_type'].value_counts()
print(post_counts)

ax=sns.countplot(data=df, x='status_type', palette='Set1')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), ha='center', va='bottom', fontsize=10)
plt.title('Count of Post Types')
plt.xlabel('Post Type')
plt.ylabel('Count')
plt.show()

'Q6: What is the average value of num_reaction, num_comments, num_shares for each post type?'
average=df.groupby('status_type')[['num_reactions','num_comments','num_shares']].mean()
print(average)

#visualize
ax=average.plot(kind='bar')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+p.get_width()/2., p.get_height()), ha='center', va='bottom', fontsize=10)
plt.title('Average Engagement Metrics by Post Type')
plt.xlabel('Post Type')
plt.ylabel('Average Count')
plt.xticks(rotation=0)
plt.show()