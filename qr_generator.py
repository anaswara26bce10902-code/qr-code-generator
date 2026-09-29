import qrcode


def generate_qr_codes(phonepe_url, paytm_url, google_pay_url):
    phonepe_qr = qrcode.make(phonepe_url)
    paytm_qr = qrcode.make(paytm_url)
    google_pay_qr = qrcode.make(google_pay_url)

    phonepe_qr.save('phonepe_qr.png')
    paytm_qr.save('paytm_qr.png')
    google_pay_qr.save('google_pay_qr.png')

    return phonepe_qr, paytm_qr, google_pay_qr
