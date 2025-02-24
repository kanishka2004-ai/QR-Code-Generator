import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = input("Please enter the URL: ")

if data.startswith("http://") or data.startswith("https://"):
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("test.png")
    print("QR code generated and saved as test.png")
else:
    print("Invalid Input. Please enter a valid URL starting with http:// or https://")
