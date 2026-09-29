# Project Statement: UPI Payment QR Code Generator
## Problem Statement
In India's digital transaction system the Unified Payment Interface is the main method of carrying out peer-to-peer and merchant-to-customer payments. However, relying on the manual sharing of UPI IDs leads to a number of operational problems:
1. **High Error Rate:** When long, case-sensitive UPI addresses are typed in by hand, mistakes are likely to occur, resulting in failed payments or funds being transferred to the wrong accounts.
2. **Checkout friction:** users have to alternate between the messaging or browser apps and copy and paste the payment details into their favourite payment app.
3. **No immediate, offline assets:** Small merchants and developers usually do not have at their disposal a simple and lightweight tool which allows them to generate and preview payment QR codes instantly, without having to use the dashboards or APIs of paid third-party payment gateways.

## Proposed Solution 
The UPI Payment QR code Generator is a lightweight, automated Python script which is intended to simplify the process of generating a payment address by turning raw UPI inputs into instant visual payment assets.

### Key Deliverables:
- **Input Processing:** It requests the user to enter a valid UPI ID directly through the terminal.
- **NPCI Scheme Compliance:** Formats deep-link URIs following the NPCI standard.
– Automatic creation and export of separate '.png' QR code image files for the major apps.
- **Instant Visual Verification:** It automatically opens desktop image previews by using Pillow so that you can carry out immediate scanning and verification.
## Scope of the Project

### In-Scope
There is a workflow that involves a single input terminal for entering the UPI ID.
The creation of NPCI-formatted payment links.
Save a batch of PNG image assets.
- Use PIL to provide local image preview pop-ups.


## Out-of-Scope 
– A graphics user interface using Tkinter or PyQt.
- Deployment via a web-based interface or through an API endpoint.
- The amount for the transaction is dynamic and the payment status is verified in real time.
