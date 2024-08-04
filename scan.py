import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

user_records = []

create_user = lambda name, email: {'name': name, 'email': email}

insert_user = lambda user: user_records.append(user)

fetch_all_users = lambda: user_records

def generate_qr_code(data):
    img = qrcode.make(data)
    img.save('imgqr.png')
    print("Image generated and saved as imgqr.png")

def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_data_raw = decode(img)
    if decoded_data_raw:
        decoded_data = decoded_data_raw[0].data.decode('utf-8')
        return decoded_data
    return ""

def RegisterUserFromSmartScan(image_path):
    user_data = decode_qr_code(image_path)
    
    records = user_data.split('\n')
    
    for record in records:
        try:
            name, email = record.split(',')
            
            new_user = create_user(name, email)
            
            insert_user(new_user)
        except ValueError:
            print(f"Skipping invalid record: {record}")
    
    print("Registered Users:")
    for user in fetch_all_users():
        print(f"Name: {user['name']}, Email: {user['email']}")