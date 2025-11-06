deal183 = {
    "basic": 183,
    "innerCall": 0.08,
    "outerCall": 0.1393,
    "localCall": 0.1349,
    "innerSms": 1.1287,
    "outerSms": 1.4803,
}

deal383 = {
    "basic": 383,
    "innerCall": 0.07,
    "outerCall": 0.1304,
    "localCall": 0.1217,
    "innerSms": 1.1127,
    "outerSms": 1.2458,
}

deal983 = {
    "basic": 983,
    "innerCall": 0.06,
    "outerCall": 0.1087,
    "localCall": 0.1018,
    "innerSms": 0.9572,
    "outerSms": 1.1243,
}

CinnerCall = int(input())
CouterCall = int(input())
ClocalCall = int(input())
CinnerSms = int(input())
CouterSms = int(input())


def calculate_cost(deal, CinnerCall, CouterCall, ClocalCall, CinnerSms, CouterSms):
    total = 0
    total += deal["innerCall"] * CinnerCall
    total += deal["outerCall"] * CouterCall
    total += deal["localCall"] * ClocalCall
    total += deal["innerSms"] * CinnerSms
    total += deal["outerSms"] * CouterSms
    total = total if total > deal["basic"] else deal["basic"]
    return total


A183 = calculate_cost(deal183, CinnerCall, CouterCall, ClocalCall, CinnerSms, CouterSms)
A383 = calculate_cost(deal383, CinnerCall, CouterCall, ClocalCall, CinnerSms, CouterSms)
A983 = calculate_cost(deal983, CinnerCall, CouterCall, ClocalCall, CinnerSms, CouterSms)

# find the lowest
min = 0
minPlan = ""
if A183 < A383 and A183 < A983:
    min = A183
    minPlan = "183"
elif A383 < A183 and A383 < A983:
    min = A383
    minPlan = "383"
elif A983 < A183 and A983 < A383:
    min = A983
    minPlan = "983"

print(int(min))
print(minPlan)
