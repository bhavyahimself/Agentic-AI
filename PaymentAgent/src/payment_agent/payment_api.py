import httpx
import logging

logger = logging.getLogger(__name__)

class PaymentAPIClient:
    def __init__(self):
        self.client = httpx.Client(
            base_url = "https://se-payment-verification-api.service.external.usea2.aws.prodigaltech.com"
        )