def create_payment_urls(upi_id):
    phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
    paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
    google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
    return phonepe_url, paytm_url, google_pay_url
