def dictionary_of_metrics(items):
    """
   Calculates the mean, median, variance, standard deviation, minimum and maximum of of list of items
    
    Args:
        items (list): list containing numerical values.
    
    Returns:
        dict:   dict with keys 'mean', 'median', 'std', 'var', 'min', and 'max', 
                corresponding to the mean, median, standard deviation, variance, minimum and maximum 
                of the input list, respectively
    
    Examples:
        >>> dictionary_of_metrics(gauteng)
        {'mean': 26244.42,
        'median': 24403.5,
         'var': 108160153.17,
         'std': 10400.01,
         'min': 8842.0,
         'max': 39660.0}      
        
    """
    dictionary= {'mean':np.mean(items).round(2),
         'median':np.median(items).round(2),
         'var':np.var(items, ddof = 1).round(2),
         'std':np.std(items, ddof = 1).round(2),
         'min':np.min(items).round(2),
         'max':np.max(items).round(2)
        }
    return dictionary