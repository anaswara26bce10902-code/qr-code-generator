# Project Statement: UPI Payment QR Code Generator
## Problem Statement
In the digital transcation ecosystem across India, the Unified Payment Interface (UPI) is the primary method for peer-to-peer and merchant-to-customer payments.However,m replying on manual text-based sharing of UPI IDs (e.g., ;user@upi') creates several operational challenges:
1. **High Error Rate:** Manually typing long, case-sensitive UPI addresses frequently leads to typos, failed payments, or transfers to wrong accounts.
2. **Checkout friction:** users are forced to switch back and forth between messaging or browser apps ro copy-paste payment details into their preferred payment app.
3. **Lack of Instant, offline Assets:** Small merchants and developers often lack a simple,lightweight tool to generate and preview payment QR codes instantly without relying on paid third-party payment gateway dashboards or APIs.

## Proposed Solution 
The **UPI Payment QR code Generator** is an automated, lightweight Python script designed to steamline payment address by converting raw UPI inputs intoinstant, visual payment assests.

### Key Deliverables:
- **Input Processing:** Prompts the user for a valid UPI ID directly via terminal.
- **NPCI Scheme Alignment:** Formats deep-Link URIs adhering to NPCI standerd  ('upi://pay?pa=...').
- **Multi-App Asset Creation:** Automatically generates and exports individual '.png' QR code image files for major apps (**phonepe**, **paytm**,and  **google pay**).
- **Instant Visual Verification:**Automatically opens desktop image previews using Pillow ('PIL') for immediate scanning and verification.
## Scope of the Project

### In-Scope
- Single-input terminal workflow for UPI ID entry.
- Dynamite creation of NPCI-formatted payment links.
-Batch saving of PNG image assests ('phonepe_qr.png', 'paytm_qr.png', 'google_pay_qr.png').
- Local image preview pop-ups using PIL.


## Out-of-Scope (Future Enhancements)
- Graphics User Interface (GUI) via Tkinter or PyQt.
- Web-based interface or API endpoint deployment.
- Dynamic transaction amount and real-time payment status verification.