from functions.table_index import table_index

def action_table(acting_value,opposing_value):
    """
    Looks up value along the DC Heroes action table.
    """
    if acting_value <= 0:
        raise ValueError("The acting value must be a positive integer.")
    if opposing_value < 0:
        raise ValueError("The opposing value must be a non-negative integer.")
    if not isinstance(acting_value,int) or not isinstance(opposing_value,int):
        raise TypeError("Both values must be integers.")
    row_ind = table_index(acting_value)
    col_ind = table_index(opposing_value)
    if col_ind == 0:
        if row_ind <= 1:
            return 6
        elif row_ind <= 2:
            return 5
        elif row_ind <= 4:
            return 4
        else:
            return 3
    else:
        d = col_ind - row_ind # d is for difference in indices.
        if d <= -5:
            return 3
        elif d <= -3:
            return d + 8
        elif d <= 2:
            return 2*d + 11
        elif d <= 5:
            return 3*d + 9
        elif d <= 9:
            return 4*d + 4
        else:
            return 5*d - 5

