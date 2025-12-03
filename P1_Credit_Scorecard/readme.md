# Project Goal
Simulate Risk Analyst role through python and pandas, developing a simplified credit portfolio scorecard. Primary goal is to identify deviations in denial rates across different demographics and DTI risk categories, and to build a predictive model for loan denial.

## ETL Simulation
 + Extract and filter raw data
 + Transform and create features
    + Target variable **action_taken** was encoded using LabelEncoder.
    + DTI bucketing converted raw debt_to_income_ratio into two simple risk categories: 'Low/Standard Risk' and 'High/Watch Risk'.
    + Binary column (**Denial**) created to identify events of denial (1 for Denied, 0 for Approved).
 + Load & Aggregate Data
    + Pandas' *groupby()* function aggregated data to create a summary scorecard. Calculated **Denial Rate** across all *applicant_race-1* and *DTI_Category*

## Key Deliverables and Findings
**1. Scorecard Analysis** Scorecard quantifies **Denial Rate** across DTI categories and applicant races, highlighting variance.
 
 **2. Logistic Regression Model**
   
    Model was trained on selected features to predict loan denial (binary classification).
    + **Key Finding:** Model achieved 86% Precision but only 40% Recall, indicating a high rate of missed true denials (false negatives).
    + **Interpretation:** Coefficients were used to identify features (e.g., income, loan\_amount, race, DTI) that increase or decrease the **log-odds of denial**.
 
 **3. Visualization**
   
    Correlation heatmap and rate charts are used to visualize feature relationships and denial concentration.
 
 **4. Final Output**
   
    The aggregated scorecard is exported for immediate use in reporting tools: *P1_Exhibit_Final_Scorecard.csv*

 ## Tools
 + Language: Python
 + Libraries: Pandas, Matplotlib, Seaborn, **Scikit-learn (sklearn)**
 + Environment: Jupyter Notebooks (VS Code)
 + Version Control: Git

## Data Source
 + [Home Mortgage Discolsure Act (HMDA) Loan Data](https://ffiec.cfpb.gov/data-browser/data/2023?category=states)
 