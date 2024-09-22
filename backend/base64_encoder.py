import base64

# Replace 'yourfile.txt' with the path to your file
with open('yourfile.txt', 'rb') as file:
    encoded_string = base64.b64encode(file.read())
    print(encoded_string.decode('utf-8'))