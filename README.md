# Facebook Marketplace Dataset
EDA and analysis of the Facebook Live Sellers in Thailand dataset (7,050 posts from 10 Thai fashion &amp; cosmetics retailers). Explores engagement metrics, post types, and publishing patterns using Python, pandas, and visualization libraries.

# Facebook Live Sellers in Thailand – Machine Learning Case Project

A machine learning project using the **Facebook Live Sellers in Thailand** dataset to analyse engagement patterns and apply clustering techniques on social commerce posts.

---

## 📌 Overview

This project uses **7,050 Facebook posts** from **10 Thai fashion and cosmetics retailers**. It applies data analysis and machine learning techniques to understand engagement metrics such as reactions, comments, and shares.

The project covers the full ML workflow — data cleaning, feature engineering, exploratory analysis, and **K-Means clustering** with the elbow method.

---

## 🎯 Problem Statement

This project aims to:

- Analyse how the **time of upload** affects the number of reactions.
- Identify **correlations** between reactions, comments, and shares.
- Apply **K-Means clustering** to segment posts based on engagement.
- Use the **elbow method** to find the optimal number of clusters.
- Understand **post type distribution** and average engagement per type.

---

## 📂 Dataset

- **Title:** Facebook Live Sellers in Thailand Dataset
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Facebook+Live+Sellers+in+Thailand)
- **Rows:** 7,050
- **Columns:** 16 (14 after removing redundant columns)
- **Missing Values:** Present — handled during preprocessing

### Main Attributes

| Attribute | Description |
|---|---|
| `status_id` | Unique ID for each post |
| `status_published` | Date and time of the post |
| `status_type` | Type of post (video, photo, status, link) |
| `num_reactions` | Total number of reactions |
| `num_comments` | Number of comments |
| `num_shares` | Number of shares |
| `num_likes` | Number of like reactions |
| `num_loves` | Number of love reactions |
| `num_wows` | Number of wow reactions |
| `num_hahas` | Number of haha reactions |
| `num_sads` | Number of sad reactions |
| `num_angrys` | Number of angry reactions |

---

## ❓ Case Questions

1. How does the time of upload (`status_published`) affect `num_reactions`?
2. Is there a correlation between `num_reactions` and other engagement metrics such as `num_comments` and `num_shares`? If so, what is the strength and direction?
3. Use `status_type`, `num_reactions`, `num_comments`, `num_shares`, `num_likes`, `num_loves`, `num_wows`, `num_hahas`, `num_sads`, and `num_angrys` to train a **K-Means clustering model**.
4. Use the **elbow method** to find the optimum number of clusters.
5. What is the count of different types of posts in the dataset?
6. What is the average value of `num_reactions`, `num_comments`, and `num_shares` for each post type?

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** pandas, NumPy, matplotlib, seaborn, scikit-learn
- **Environment:** Jupyter Notebook / Python script

---

## 🚀 How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python "ML_Facebook Live Sellers Dataset.py"
