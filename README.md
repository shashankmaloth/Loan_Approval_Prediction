"# Loan_Approval_Prediction" 
# Loan Approval Prediction 

This project predicts whether a loan application will be **approved or rejected** based on applicant details using **Machine Learning**.  
It uses classification algorithms trained on historical loan data to assist financial institutions in making data-driven decisions.  

---

## 📊 Dataset
The dataset (`loan-predictionUC.csv.xlsx`) contains applicant and loan-related information such as:

- **Applicant details**: Gender, Marital Status, Education, Dependents  
- **Financial info**: Applicant Income, Co-applicant Income, Loan Amount, Loan Term  
- **Loan details**: Credit History, Property Area  
- **Target variable**: Loan_Status (Y/N)

---

## ⚙️ How It Works
1. Load and preprocess dataset (handle missing values, encode categorical features).
2. Train machine learning model(s) (e.g., Logistic Regression, Decision Tree, Random Forest).
3. Evaluate model using accuracy, precision, recall, F1-score.
4. Predict loan approval for new applicants.

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone https://github.com/shashankmaloth/Loan_Approval_Prediction.git
cd Loan_Approval_Prediction


---
2️⃣ Install Dependencies

Make sure you have Python 3.x installed, then install the required libraries:

pip install pandas numpy scikit-learn matplotlib seaborn

3️⃣ Run the Script
python Loan_Prediction.py
