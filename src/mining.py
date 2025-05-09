from mlxtend.frequent_patterns import fpgrowth, association_rules

def mine_itemsets(basket, min_support=0.01):
    return fpgrowth(basket, min_support=min_support, use_colnames=True)

def extract_rules(itemsets, metric="lift", min_threshold=1.0):
    return association_rules(itemsets, metric=metric, min_threshold=min_threshold)
