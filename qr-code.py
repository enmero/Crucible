import qrcode

data = "https://crucibleapp.in"
img = qrcode.make(data)
name = "crucibleapp.png"
img.save(name)

print(f"QR Code saved as {name}")
