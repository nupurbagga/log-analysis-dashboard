def log_analysis(contents):
    lines = contents.splitlines()

    fail = 0
    success = 0

    for line in lines:
        if "Failed Password" in line:
            fail += 1

        elif "Accepted Password" in line:
            success +=1

    
    return {
        "Failed attempts": fail,
        "Successful attempts": success 
    }