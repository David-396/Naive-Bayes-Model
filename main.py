from client_side.client import Client
# from client_side.menu import Menu

# main = Menu()
# main.run()

# open('data_handling/__init__.py', 'a').close()
# open('model/__init__.py', 'a').close()
# open('client_side/__init__.py', 'a').close()
# open('server_side/__init__.py', 'a').close()

client = Client('http://127.0.0.1:8000')
client.run()