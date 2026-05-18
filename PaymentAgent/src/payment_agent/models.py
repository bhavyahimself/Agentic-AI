from pydantic import BaseModel
from typing import Optional

class LookUpRequest(BaseModel):
    account_id: str

class LookUpResponse(BaseModel):
    account_id: str
    full_name: str
    dob: str
    aadhaar_last4: str
    pincode: str
    balance: float

class CardDetails(BaseModel):
    cardholder_name: str
    card_number: str
    cvv: str
    expiry_month: int
    expiry_year: int


class PaymentMethod(BaseModel):
    type: str
    card: CardDetails


class ProcessPaymentRequest(BaseModel):
    account_id: str
    amount: float
    payment_method: PaymentMethod

class PaymentSuccessResponse(BaseModel):
    success: bool
    transaction_id: str


class ErrorResponse(BaseModel):
    success: Optional[bool] = None
    error_code: str
    message: Optional[str] = None

