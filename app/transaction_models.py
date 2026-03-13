from pydantic import BaseModel
from typing import List
class Transaction(BaseModel):
    date:str
    amount:float
    description:str

class TransactionOuter(BaseModel):
    business_name:str
    loan_amount_requested:float
    transactions:List[Transaction]