import qrcode

data = input("Enter text or link: ")

img = qrcode.make(data)

img.save("my_qr.png")

print("QR code generated!")
