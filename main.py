import qrcode
import qrcode.image.svg
# img=qrcode.make("Hello World!This is Aryaman")
# img.save("mycode.png")
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=50,
                 border=2)
qr.add_data("https://www.youtube.com/watch?v=8AYy-BcjRXg")
qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")
img.save("advanced.png")

# factory=qrcode.image.svg.SvgPathImage
# svg_img=qrcode.make("Hello World!",image_factory=factory)
# svg_img.save("myqr.svg")