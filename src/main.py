import pandas as pd
import time
import os
import psutil

from ingest import load_data
from preprocess import create_basket
from mining import mine_itemsets, extract_rules
from visualize import plot_top_items

def get_memory_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / 1024 / 1024  # in MB
    return round(mem, 2)

def run():
    print("🛒 MARKET BASKET ANALYSIS - FP-GROWTH VERSION")
    start_time = time.time()

    print("📥 Step 1: Loading data...")
    df = load_data("data/retail_data.csv")
    print(f"✅ Loaded {len(df)} rows. Memory used: {get_memory_usage()} MB")

    # Debug mode: sample rows to test quickly
    DEBUG_MODE = False
    if DEBUG_MODE:
        df = df.head(10000)
        print("⚠️ DEBUG MODE ON: Using only 10,000 rows.")

    print("🧹 Step 2: Applying filters - United Kingdom, December 2010...")
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df = df[df['Country'] == 'United Kingdom']
    df = df[df['Date'].dt.month == 12]
    df = df[df['Date'].dt.year == 2010]
    print(f"✅ Filtered down to {len(df)} rows. Memory used: {get_memory_usage()} MB")

    print("🧺 Step 3: Creating basket matrix...")
    # Drop items bought less than N times
    item_counts = df['Itemname'].value_counts()
    df = df[df['Itemname'].isin(item_counts[item_counts > 10].index)]
    print(f"✅ Removed rare items. Remaining unique items: {df['Itemname'].nunique()}")
    basket = create_basket(df)
    print(f"✅ Basket shape: {basket.shape}. Memory used: {get_memory_usage()} MB")

    print("⛏️ Step 4: Running FP-Growth (min_support=0.01)...")
    t0 = time.time()
    itemsets = mine_itemsets(basket, min_support=0.02)
    print(f"✅ Found {len(itemsets)} frequent itemsets in {round(time.time() - t0, 2)}s.")

    print("🔗 Step 5: Extracting association rules (lift ≥ 1.0)...")
    t0 = time.time()
    rules = extract_rules(itemsets, metric="lift", min_threshold=1.0)
    print(f"✅ Generated {len(rules)} rules in {round(time.time() - t0, 2)}s.")

    print("💾 Step 6: Saving output to CSV...")
    os.makedirs("output", exist_ok=True)
    itemsets.to_csv("output/frequent_itemsets.csv", index=False)
    rules.to_csv("output/association_rules.csv", index=False)
    print("✅ Output saved. Memory used:", get_memory_usage(), "MB")

    print("📊 Step 7: Plotting top itemsets...")
    plot_top_items(itemsets)

    print(f"\n🏁 DONE! Total runtime: {round(time.time() - start_time, 2)} seconds")
    print("🧠 Peak memory used:", get_memory_usage(), "MB")

if __name__ == "__main__":
    run()
