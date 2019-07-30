from database_fetch import get_bank, get_branch, Database_Connection_Error

def bankDetails(ifsc):
    try:
        rows = get_bank(ifsc)
        data = {}
        for row in rows:
            data['ifsc'] = row[0]
            data['branch'] = row[2]
            data['address'] = row[3]
            data['city'] = row[4]
            data['district'] = row[5]
            data['state'] = row[6]
        return data
    except Database_Connection_Error:
        return "Please try later"

def branchDetails(bank_name, city, limit = 20, offset = 0):
    try:
        rows = get_branch(bank_name, city, limit, offset)
        branches = []
        for row in rows:
            data = {}
            data['ifsc'] = row[0]
            data['branch'] = row[2]
            data['address'] = row[3]
            data['city'] = row[4]
            data['district'] = row[5]
            data['state'] = row[6]
            branches.append(data)
        return branches
    except Database_Connection_Error:
        return "Please try later"
