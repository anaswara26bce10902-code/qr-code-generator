from input_handler import get_upi_id
from payment_urls import create_payment_urls
from qr_generator import generate_qr_codes

upi_id = get_upi_id()

phonepe_url,paytm_url,google_pay_url = create_payment_urls(upi_id)


phonepe_qr, paytm_qr, google_pay_qr = generate_qr_codes(phonepe_url,paytm_url, google_pay_url)


phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

