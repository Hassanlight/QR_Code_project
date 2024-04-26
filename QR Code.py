#My Qr_Code Project for Linkedin
import qrcode as qr
from PIL import Image

QR_code = qr.QRCode(version=1,
                    error_correction=qr.constants.ERROR_CORRECT_H,
                    box_size=10, border=4)

# Add data to the QR code
QR_code.add_data("https://www.linkedin.com/in/bilal-hassan-783249231/")


QR_code.make()


img = QR_code.make_image(fill_color="blue", back_color="white")


img.save("My_QR.png")
