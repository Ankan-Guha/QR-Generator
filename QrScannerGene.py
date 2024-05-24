import qrcode
from qrcode.image.pil import PilImage

i = int(input("Enter the number of QR been got :"))
while True:
    
    features = qrcode.QRCode(version=1, box_size=40, border=3)
    
    typeOfQr = int(input("Enter\n1\t for just text entry\n2\t for links\n"))
    
    nameOfQr = input("Enter the details\n")
    if typeOfQr == 2:
        if not nameOfQr.startswith("http://") and not nameOfQr.startswith("https://"):
            nameOfQr = "https://" + nameOfQr
    
    features.add_data(nameOfQr)
    features.make(fit=True)
    fColor="black"
    bColor="white"
    change=input("'YES' To personal color \n'NO' for default :")
    if change=='YES':
        fColor=input("Enter color of code :")
        bColor=input("Enter background color :")
    generate_image = features.make_image(fill_color=fColor, back_color=bColor)
    nameOfImage = f"image_{i}.jpg"
    generate_image.save(nameOfImage)
    i += 1
    print(f"Saving QR code to {nameOfImage}")
    feedback = input("Input 'NO' to stop generating QR code, any other key to continue: ")
    if feedback.upper() == 'NO':
        break

print("THANKS FOR THE EXECUTION")
