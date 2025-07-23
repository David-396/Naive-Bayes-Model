from run_server import server_run


CLS_SERVER_IP = 'localhost'
CLS_SERVER_PORT = 8001

MAIN_SERVER_IP = 'localhost'
MAIN_SERVER_PORT = 8000


# starting the server
if __name__ == "__main__":
    try:
        server_run(main_server_ip=MAIN_SERVER_IP,
                   main_server_port=MAIN_SERVER_PORT)

    except Exception as e:
        print(f'--- {e} ---')
