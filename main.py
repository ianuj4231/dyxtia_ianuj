from fastapi import FastAPI
from app.transaction_models import TransactionOuter
from app.service_logic import (
    find_average_value, find_largest_inflow, find_largest_outflow, find_net_cash_flow, find_no_of_inflow, find_no_of_outflow, find_total_inflow, find_total_outflow
)




app = FastAPI()

@app.get("/")
def first_example():
    return {"GFG Example": "FastAPI"}


@app.get("/health")
def first_example():
    return {"health_status": "ok"}




@app.post("/analyze-file")
def first_example( req_body:TransactionOuter  ):
    
    transactions = req_body.transactions

    no_of_inflow = find_no_of_inflow(transactions)
    no_of_outflow=find_no_of_outflow(transactions)
    sum_of_total_inflow   = find_total_inflow(transactions)
    sum_of_total_outflow  = find_total_outflow(transactions)
    average = find_average_value(transactions)
    largest_inflow = find_largest_inflow(transactions)
    largest_outflow =  find_largest_outflow(transactions)
    net_cash_flow= find_net_cash_flow(sum_of_total_inflow, sum_of_total_outflow)
    
    risk_flags=[]
    
    
    if largest_outflow > 0.5 * (sum_of_total_outflow):
        risk_flags.append("Large single outflow detected")

    if no_of_inflow  < no_of_outflow:
        risk_flags.append("Low inflow frequency")  


    if net_cash_flow<0:
        risk_flags.append("Negative net cash flow")


    # Readiness Classification
    # Return a simple readiness band classification:
    # • strong
    # • structured
    # • requires_clarification
    

    band=""
    score=0
    if no_of_inflow >  no_of_outflow :
        score +=1

    if  no_of_inflow > no_of_outflow  and  net_cash_flow>0:
        score+=2
    
    if score==3:
        band="strong"
    elif score==1:
        band="structured"
    else:
        band="requires clarfication"
        



    return {
        
        "no_of_inflow": no_of_inflow,
        "no_of_outflow": no_of_outflow,
        "sum_of_total_inflow": sum_of_total_inflow,
        "sum_of_total_outflow": sum_of_total_outflow,
        "average": average,
        "largest_inflow": largest_inflow,
        "largest_outflow":  largest_outflow,
        "net_cash_flow": net_cash_flow,
        "risk_flags" : risk_flags,
        "classification_band": band
        }




