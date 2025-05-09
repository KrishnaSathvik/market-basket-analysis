def create_basket(df):
    basket = (df.groupby(['BillNo', 'Itemname'])['Quantity']
                .sum().unstack().reset_index().fillna(0)
                .set_index('BillNo'))
    
    # Convert to boolean (optimized for Apriori)
    basket = basket.astype(bool)
    return basket
