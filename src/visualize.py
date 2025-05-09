import matplotlib.pyplot as plt

def plot_top_items(itemsets, top_n=10):
    top = itemsets.sort_values("support", ascending=False).head(top_n)
    top.plot(kind="bar", x="itemsets", y="support", legend=False)
    plt.title("Top Frequent Itemsets")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
