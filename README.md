# 🛒 Market Basket Analysis Pipeline

A complete end-to-end Market Basket Analysis pipeline using the FP-Growth algorithm with Streamlit dashboard, confidence/lift filters, and product keyword search.

---

## 📦 Features

- Ingests real-world retail transaction data
- Filters by country (e.g., United Kingdom) and date (e.g., December 2010)
- Removes rare items for better performance
- Uses FP-Growth (faster than Apriori) for frequent itemset mining
- Generates association rules with confidence and lift
- Interactive **Streamlit Dashboard**:
  - Filter rules by confidence/lift
  - Search rules by product keyword
  - View top frequent itemsets

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Pandas** for data manipulation
- **mlxtend** for FP-Growth and rule mining
- **Streamlit** for interactive dashboard
- **Matplotlib** for itemset plots

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/market-basket-analysis.git
cd market-basket-analysis
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Data

Place your retail CSV file in `data/` and name it:

```bash
data/retail_data.csv
```

(You can rename `Assignment-1_Data.csv` with semicolon separator.)

---

## 🧪 Run the Pipeline

```bash
python src/main.py
```

Generates:
- `output/frequent_itemsets.csv`
- `output/association_rules.csv`

---

## 📊 Launch the Dashboard

```bash
streamlit run dashboard.py
```

### Dashboard Features:
- Filter rules by **confidence** and **lift**
- Keyword search for **item names**
- Top frequent itemsets bar chart

---

## 📁 Project Structure

```
market-basket-analysis/
├── data/
│   └── retail_data.csv
├── output/
│   ├── frequent_itemsets.csv
│   └── association_rules.csv
├── src/
│   ├── ingest.py
│   ├── preprocess.py
│   ├── mining.py
│   ├── visualize.py
│   └── main.py
├── dashboard.py
├── requirements.txt
└── README.md
```

---

## ✅ Tips

- Change `min_support` in `main.py` for more/less rules
- Use keyword filters like "bag", "lamp", "candle" to narrow results
- View memory/logs in terminal for debug insights

---

## 🤝 Contributing

Fork, commit, and pull request are welcome. Let’s make analytics better together!

> Built with 💙 by Krishna Sathvik
