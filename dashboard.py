import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ast

st.set_page_config(layout="wide")
st.title("🛒 Market Basket Analysis Dashboard")

# Load data
itemsets = pd.read_csv("output/frequent_itemsets.csv")
rules = pd.read_csv("output/association_rules.csv")

# Convert string to list for antecedents/consequents if needed
def extract_items(frozenset_str):
    return frozenset_str.replace("frozenset(", "").replace(")", "").replace("{", "").replace("}", "").replace("'", "").split(", ")

rules["antecedents"] = rules["antecedents"].apply(extract_items)
rules["consequents"] = rules["consequents"].apply(extract_items)

# Sidebar filters
st.sidebar.header("🔍 Filter Rules")

# Confidence & lift sliders
confidence_min, confidence_max = st.sidebar.slider("Confidence Range", 0.0, 1.0, (0.5, 1.0), 0.01)
lift_min, lift_max = st.sidebar.slider("Lift Range", 0.0, 5.0, (1.0, 3.0), 0.1)

# Product keyword filter
keyword = st.sidebar.text_input("Product name contains (optional):").lower()

# Filter logic
filtered_rules = rules[
    (rules['confidence'] >= confidence_min) &
    (rules['confidence'] <= confidence_max) &
    (rules['lift'] >= lift_min) &
    (rules['lift'] <= lift_max)
]

if keyword:
    filtered_rules = filtered_rules[
        filtered_rules['antecedents'].apply(lambda x: any(keyword in item.lower() for item in x)) |
        filtered_rules['consequents'].apply(lambda x: any(keyword in item.lower() for item in x))
    ]

# Show filters summary
st.sidebar.markdown(f"✅ {len(filtered_rules)} rules match your filters.")

# Main content
st.subheader("📊 Top Frequent Itemsets")
st.dataframe(itemsets.sort_values(by="support", ascending=False).head(10))

st.subheader("📋 Filtered Association Rules")
st.dataframe(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Plot top frequent itemsets
st.subheader("📈 Frequent Itemsets by Support")
top = itemsets.sort_values("support", ascending=False).head(10)
fig, ax = plt.subplots()
top.plot(kind='bar', x='itemsets', y='support', ax=ax, legend=False)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig)
