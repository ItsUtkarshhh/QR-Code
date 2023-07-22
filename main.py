import qrcode
from PIL import Image
# PIL is the Python Imaging Library!

# qrcode.QRCode(), this function creates an object that allows you to customize the QR Code generation process.
# Here you can specify the version (size) of QR code, error correction level, it can be High (H), Low (L) or Medium (M)!
# And also we can set the border size and the boz size using this method! 
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.ERROR_CORRECT_H,
                   box_size=10,
                   border=3)

# .add_data() allows you to add data, information or the whatever the detail you want to encode in your QR code!
qr.add_data("https://github.com/ItsUtkarshhh")

# .make() : a primary function used to generate a QR Code!
# It takes the "Data" you want to encode as the input and returns a qrcode.image.pip.PilImage object representing the qr code!
qr.make(fit=True)

# .make_image() : This method generates the QR code image a PIL image, here you can specify the fill color and bg color.
img = qr.make_image(fill_color="red",
                    back_color="blue")

# .save() : This method allows you to save the QR Code image to a file! here you can specify the file name and format! 
img.save("My_Github.png")
