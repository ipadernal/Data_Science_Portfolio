# Project Goal
Simulate Risk Analyst role through python and pandas, developing a simplified credit portfolio scorecard. Primary goal is to identify deviations in denial rates across different demographics and DTI risk categories.

## ETL Simulation
 + Extract and filter raw data
 + Transform and create features
    + DTI bucketing converted raw debt_to_income_ratio into two simple risk categories: 'Low/Standard Risk' and 'High/Watch Risk'.
    + Binary column (Denied) created to identify events of denial
 + Load & Aggregate Data
    + Pandas' *groupby()* function aggregated data to create a summary scorecard. Calculated **Denial Rate** across all *derived_race* and *DTI_Category*

## Key Deliverables and Findings
**1. Visualization** 
 Barchart visually separates denial rates, highlights where risk is concentrated
 **2. Variance Report**
 Highest denial rate is observed in the 'Free Form Text Only' group within the 'Low/Standard' DTI category, at a peak rate of 52.9%
 **3. Final Output**
 The aggregated scorecard is exported for immediate use in reporting tools:
 *P1_Exhibit_Final_Scorecard.csv*

 ##Tools
 + Language: Python
 + Libraries: Pandas, Matplotlib, Seaborn
 + Environment: Jupyter Notebooks (VS Code)
 + Version Control: Git