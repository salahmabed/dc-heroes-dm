def table_index(val):
    """
    Find the number of the column or row along the DC Heroes action or result table.

    Keyword arguments:
    val -- the value being converted
    """
    if val <= 0:
        return 0
    elif val <= 12:
        return (val+1)//2
    elif val <= 30:
        return (val+8)//3
    else:
        return (val+34)//5