def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    result = series.copy()

    for _ in range(order):
        result = [result[i+1] - result[i] for i in range(len(result) - 1)]

    return result
    # Write code here