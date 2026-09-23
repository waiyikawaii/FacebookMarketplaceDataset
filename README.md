# Facebook Marketplace Dataset
EDA and analysis of the Facebook Live Sellers in Thailand dataset (7,050 posts from 10 Thai fashion &amp; cosmetics retailers). Explores engagement metrics, post types, and publishing patterns using Python, pandas, and visualization libraries.

# Facebook Live Sellers in Thailand – Data Analysis

An exploratory data analysis (EDA) of the **Facebook Live Sellers in Thailand** dataset, examining engagement patterns across 7,050 posts from 10 Thai fashion and cosmetics retailers.

## 📌 Overview

This project analyzes social commerce activity on Facebook Live, focusing on how different post types and publishing times influence customer engagement. Using Python, pandas, and visualization libraries, it uncovers trends in reactions, comments, and shares — providing insights for sellers looking to optimize their content strategy.

## 📂 Dataset

- **Title:** Facebook Live Sellers in Thailand Dataset
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Facebook+Live+Sellers+in+Thailand)
- **Format:** CSV (tabular)
- **Instances:** 7,050 rows
- **Attributes:** 16 (14 after removing redundant columns)
- **Missing Values:** Present — handled during preprocessing

### Attribute Information

| Attribute | Description |
|---|---|
| `status_id` | Unique identifier for each status post |
| `status_published` | Date and time when the post was published |
| `status_type` | Nature of post (video, photo, status, link) |
| `num_reactions` | Total reactions (likes, loves, wow, haha, sad, angry) |
| `num_comments` | Number of comments received |
| `num_shares` | Number of shares received |
| `num_likes` | Number of "Like" reactions |
| `num_loves` | Number of "Love" reactions |
| `num_wows` | Number of "Wow" reactions |
| `num_hahas` | Number of "Haha" reactions |
| `num_sads` | Number of "Sad" reactions |
| `num_angrys` | Number of "Angry" reactions |
| *(+ additional engagement & categorical attributes)* | |

## ❓ Analysis Questions

1. What is the distribution of post types (video, photo, status, link)?
2. Which post type generates the most reactions, comments, and shares?
3. How does engagement vary across the 10 sellers?
4. What are the peak publishing times (hour, day, month)?
5. What is the distribution of each reaction type (likes, loves, wow, haha, sad, angry)?
6. Are there correlations between reactions, comments, and shares?
7. How do missing values impact the dataset?
8. What trends can be observed in engagement over time?

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** pandas, numpy, matplotlib, seaborn
- **Environment:** Jupyter Notebook / Python script

## 📁 Repository Structure
