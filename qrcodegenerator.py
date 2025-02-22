import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="https://www.linkedin.com/in/kanishka-saxena-844368250?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")
