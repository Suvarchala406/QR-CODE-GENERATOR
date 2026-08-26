import qrcode

# Your Google Drive link
data = "https://drive.google.com/drive/folders/1NYwEtOAvM-6Dq34uCkZ4qtZJrLcZEFdJ"

# Generate QR code
img = qrcode.make(data)

# Save it
img.save("my_qrcode.png")

print("QR Code generated successfully!")