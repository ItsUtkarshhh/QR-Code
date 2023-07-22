import qrcode
from PIL import Image

# qrcode.QRCode(), this function creates an object that allows you to customize the QR Code generation process.
# Here you can
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.ERROR_CORRECT_H,
                   box_size=10,
                   border=3)

qr.add_data("https://github.com/ItsUtkarshhh")

# .make() : a primary function used to generate a QR Code!
# It takes the "Data" you want to encode as the input and returns a qrcode.image.pip.PilImage object representing the qr code!
qr.make(fit=True)

img = qr.make_image(fill_color="red",
                    back_color="blue")

img.save("My_Github.png")