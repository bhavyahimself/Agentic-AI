import httpx
import logging
from models import LookUpRequest, ProcessPaymentRequest
from tenacity import retry, wait_exponential, stop_after_attempt
logger = logging.getLogger(__name__)

class PaymentAPIClient:
    def __init__(self):
        self.client = httpx.Client(
            base_url = "https://se-payment-verification-api.service.external.usea2.aws.prodigaltech.com",
            timeout=10,
            headers={
                "Content-Type": "application/json",
            }
        )

    @retry(stop=stop_after_attempt(3),wait=wait_exponential(multiplier=1, min=2, max=10))
    def lookup_account(self,request: LookUpRequest):
        try:
            response = self.client.post("/api/lookup-account", json=request.model_dump())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(
                "Lookup account failed",
                extra={
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            )
            raise e

    @retry(stop=stop_after_attempt(3),wait=wait_exponential(multiplier=1, min=2, max=10))
    def process_payment(self,request: ProcessPaymentRequest):
        try:
            response = self.client.post("/api/process-payment", json=request.model_dump())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(
                "Process payment failed",
                extra={
                    "status_code": e.response.status_code,
                    "response": e.response.text
                }
            )
            raise e