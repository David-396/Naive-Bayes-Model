from client_side.client import Client
# from client_side.menu import Menu

# main = Menu()
# main.run()

client = Client('http://127.0.0.1:8000')
client.run()