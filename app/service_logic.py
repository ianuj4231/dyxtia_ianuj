def find_no_of_inflow(transactions):
    count=0
    for t in transactions:
        if t.amount  >  0 :
            count=count+1

    return count


def find_no_of_outflow(transactions):
    count=0
    for t in transactions:
        if t.amount  <  0 :
            count=count+1

    return count



def find_total_inflow(transactions):
    sum=0
    for t in transactions:
        if t.amount> 0:
            sum+=t.amount
    return sum



def find_total_outflow(transactions):
    sum=0
    for t in transactions:
        if t.amount <  0:
            sum+=t.amount
    return abs(sum) 
    ## so if -340 is sum of -ve amounts.. so abs is outflow..




def find_average_value(transactions):
    
    if(len(transactions)==0):
        return 0 
    sumx=0
    for t in  transactions:
        sumx+=t.amount
    return sumx/len(transactions)


def find_largest_inflow(transactions):
    maxx=float('-inf')
    for t in transactions:
        if t.amount>0:
            maxx=max(maxx, t.amount)
    
    # [ 98, 78 
    ### if maxx was still int min... then trhere  was no ifnlow in input array... so

    if maxx==float('-inf'):
        return 0  
    
    return maxx


def find_largest_outflow(transactions):
    minn=float('inf')

    for t in transactions:
        if t.amount<0:
            minn=min(minn, t.amount)

    if minn==float('inf'):
        return 0

    return abs(minn)   



def find_net_cash_flow(  inflow, outflow ):
    return inflow-outflow