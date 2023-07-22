import qrcode
# from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.ERROR_CORRECT_H,
                   box_size=10,
                   border=3)
qr.add_data("https://github.com/ItsUtkarshhh")
qr.make(fit=True)

img = qr.make_image(fill_color="red",
                    back_color="blue")

img.save("My_Github.png")