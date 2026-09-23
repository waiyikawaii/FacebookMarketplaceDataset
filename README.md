# Facebook Marketplace Dataset
EDA and analysis of the Facebook Live Sellers in Thailand dataset (7,050 posts from 10 Thai fashion &amp; cosmetics retailers). Explores engagement metrics, post types, and publishing patterns using Python, pandas, and visualization libraries.

# Facebook Live Sellers in Thailand – Machine Learning Case Project

A machine learning project using the **Facebook Live Sellers in Thailand** dataset to analyse and predict engagement levels of social commerce posts using classification and regression models.

## 📌 Overview

This project uses **7,050 Facebook posts** from **10 Thai fashion and cosmetics retailers**. It applies machine learning techniques to analyse engagement such as reactions, comments and shares.

The project covers the full ML process, including **data cleaning, feature engineering, model training, evaluation and analysis**.

## 🎯 Problem Statement

This project aims to:

* **Predict engagement levels** based on post type, timing and other features.
* **Identify important features** related to customer engagement.
* **Analyse patterns** in reactions, comments and shares.

## 📂 Dataset

* **Title:** Facebook Live Sellers in Thailand Dataset
* **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Facebook+Live+Sellers+in+Thailand)
* **Rows:** 7,050
* **Columns:** 16
* **Missing Values:** Present — handled during preprocessing

### Main Attributes

| Attribute          | Description                               |
| ------------------ | ----------------------------------------- |
| `status_id`        | Unique ID for each post                   |
| `status_published` | Date and time of the post                 |
| `status_type`      | Type of post (video, photo, status, link) |
| `num_reactions`    | Total number of reactions                 |
| `num_comments`     | Number of comments                        |
| `num_shares`       | Number of shares                          |
| `num_likes`        | Number of likes                           |
| `num_loves`        | Number of love reactions                  |
| `num_wows`         | Number of wow reactions                   |
| `num_hahas`        | Number of haha reactions                  |
| `num_sads`         | Number of sad reactions                   |
| `num_angrys`       | Number of angry reactions                 |

## 🛠️ Tech Stack

* Python
* pandas
* NumPy
* matplotlib
* seaborn
* scikit-learn

## 🚀 How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python "ML_Facebook Live Sellers Dataset.py"
```
