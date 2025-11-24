
# 📊 **Deaths Due to Cancer — Data Analysis & Visualization**
_A Python-based global cancer mortality analytics project_

---

## 🧾 **Overview**
This project presents a comprehensive analytical study of **global cancer-related mortality**, using computational techniques to uncover country-wise trends, visualize patterns, and support epidemiological research.

Using Python’s data ecosystem, the project applies **data cleaning, exploratory analysis, visualization, and database export**, making it a complete end-to-end analytical pipeline.

---

## 🎯 **Objectives**
1. **Quantify and compare** cancer-related death rates across countries and cancer classifications.  
2. **Identify high-risk regions** and evaluate temporal patterns in global cancer mortality.  
3. **Demonstrate transparent, reproducible** methodologies using open-source tools.  
4. Provide clear **visual insights** for policymakers, researchers, and health analysts.

---

## 📂 **Project Features**
✔ Interactive console-driven menu  
✔ Statistical summaries (mean, median, quartiles, etc.)  
✔ Trend analysis across years  
✔ Country-level aggregations  
✔ Multi-type cancer category analysis  
✔ Multiple visualizations:  
- Bar charts  
- Line charts  
- Histograms  
- Pie charts  

✔ Optional MySQL export for persistent storage

---

## 🛠 **Methodology**

### **1. Data Extraction & Loading**
- Data loaded from a CSV file (`deaths.csv`) or a relational database.  
- Imported using **pandas** with validation, exception handling, and structural verification.

### **2. Data Cleaning & Preparation**
- Removal of redundant fields  
- Renaming and standardization of columns  
- Null handling and population normalization  
- Deriving additional computed fields (e.g., total deaths)

### **3. Exploratory Data Analysis (EDA)**
- Statistical profiling using pandas & numpy  
- Country-wise and year-wise segmentation  
- Extraction of high-mortality regions  

### **4. Visualization**
Visuals generated with Matplotlib:
- Bar charts (top cancer-burden countries)  
- Histograms (distribution patterns)  
- Time-series line charts (global & per-country trends)  
- Pie charts (top contributors)  

### **5. Optional MySQL Export**
- SQLAlchemy and PyMySQL used to export cleaned datasets to MySQL for large-scale storage and advanced analysis.  

---

## ▶️ **How to Use the Program**

### **1. Prepare the Dataset**
Place the dataset file:  
```
deaths.csv
```
in the same directory as the Python script.

### **2. Run the Main Script**
Launch the analysis tool by running:
```bash
python main.py
```

### **3. Use the Interactive Menu**
The console provides options to:  
1. Display dataset  
2. Perform analysis  
3. Generate charts  
4. Export to MySQL  

### **4. Export to MySQL (Optional)**
Provide valid MySQL credentials in the script to enable automatic export.

---

## 📦 **Requirements**

Install all dependencies with:

```bash
pip install pandas matplotlib numpy sqlalchemy pymysql
```

Required libraries:  
- Python 3.x  
- pandas  
- numpy  
- matplotlib  
- SQLAlchemy  
- PyMySQL  

---

## 🎓 **Academic Significance**
This project delivers an analytically rigorous and reproducible framework for understanding **global oncological burdens**. By integrating computation, visualization, and epidemiological context, it contributes to:

- Public health informatics  
- Cross-country mortality comparison  
- Policy-level strategic planning  
- Foundations for predictive modeling and future epidemiological studies  

---

## 📁 **Recommended Repository Structure**

```
├── main.py
├── deaths.csv
├── /screenshots
│   ├── main_menu.png
│   ├── summary_stats.png
│   ├── bar_chart.png
│   └── ...
├── README.md
└── requirements.txt
```

---

## 📜 **License**
This project may be published under MIT License or any license of your choice.

---

## 🤝 **Contributing**
Pull requests are welcome!  
Feel free to submit improvements in documentation, visualization enhancement, or dataset updates.

---

## ⭐ If you use this repository, please consider starring it!
