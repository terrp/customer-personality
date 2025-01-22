# Customer Personality Analysis Project

## Overview

This project analyzes customer data to identify distinct personality clusters and provide insights into customer behavior. The analysis uses clustering techniques to segment customers based on their spending patterns, demographic attributes, and preferences. By visualizing and summarizing the clusters, this project aims to support businesses in creating targeted marketing strategies and improving customer experiences.

## Objectives

Perform data preprocessing to clean and prepare the dataset.

Use dimensionality reduction techniques (e.g., PCA) to simplify data visualization.

Apply clustering algorithms to identify meaningful customer segments.

Visualize cluster distributions and explore the relationship between features and clusters.

Provide actionable insights based on the analysis.

## Dataset

The dataset used for this project is the Customer Personality Analysis dataset from Kaggle. The dataset contains demographic, spending, and transactional information about customers.

Key features include:

Income: Annual income of the customer.

Age: Customer's age.

Education: Level of education attained.

Spent: Total amount spent by the customer.

Family Size: Number of people in the family.

## Methodology

1. Data Preprocessing

Handle missing values by imputing or removing incomplete rows.

Normalize numerical features for consistent scaling.

Encode categorical features into numerical values for compatibility with machine learning algorithms.

2. Dimensionality Reduction

Use Principal Component Analysis (PCA) to reduce the dimensionality of the dataset for visualization while preserving the variance.

3. Clustering

Apply clustering algorithms such as K-Means or Hierarchical Clustering to segment customers into distinct groups.

Evaluate the optimal number of clusters using methods like the Elbow Method or Silhouette Score.

4. Visualization

Plot cluster distributions using Seaborn’s countplot and swarmplot.

Create boxenplots and other visualizations to compare features across clusters.

## Key Visualizations

Cluster Distribution: Displays the number of customers in each cluster using countplots.

Spending Patterns: Swarmplot combined with boxenplot to visualize spending habits across clusters.

### Tools & Libraries

Python: Programming language used for analysis.

Libraries:

Pandas: For data manipulation.

NumPy: For numerical computations.

Seaborn & Matplotlib: For data visualization.

Scikit-learn: For PCA and clustering algorithms.

### Installation

Clone the repository:

git clone git@github.com:terrp/customer-personality.git

Create a virtual environment:

python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate    # For Windows

Install dependencies:

pip install -r requirements.txt

Usage

Ensure the dataset is placed in the data/ directory.

Run the main analysis script:

python analysis.py

Visualizations and insights will be saved in the results/ directory.

Results

Identified key customer segments with unique spending patterns and preferences.

Visualizations highlight actionable insights, such as identifying high-value customers or specific demographics to target.

Challenges

Balancing cluster sizes to avoid bias in analysis.

Visualizing high-dimensional data in a meaningful way.

Future Work

Integrate additional customer datasets to enrich the analysis.

Develop predictive models to forecast customer behavior.

Create a dashboard for interactive exploration of customer insights.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Kaggle for providing the Customer Personality Analysis dataset.

Open-source libraries and the Python community for their tools and resources.