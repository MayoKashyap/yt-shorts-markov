def engagementBucket(seconds): 
    if seconds <= 3: 
        return "zombie"
    elif seconds <= 10: 
        return "fast"
    elif seconds <= 20: 
        return "normal"
    elif seconds <= 30: 
        return "slow"
    else: 
        return "linger"

engagementScore = {"zombie": 0, "fast": 1, "medium": 2, "slow": 3, "linger": 4}
engagement = ['zombie', 'fast', 'normal', 'slow', 'linger']

