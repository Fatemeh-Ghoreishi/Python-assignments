import qrcode
text = input('Enter your desired text: ')
Qr = qrcode.make(text)
Qr.save("my_text.jpg")