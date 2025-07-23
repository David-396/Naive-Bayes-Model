from run_server import server_run

CLASSIFIER_IP = 'cls_server_container__v2.0'
CLASSIFIER_PORT = 8001

MAIN_SERVER_IP = 'main_server_container__v2.0'
MAIN_SERVER_PORT = 8000


# starting the server
if __name__ == "__main__":
    try:
        server_run(classifier_ip=CLASSIFIER_IP, classifier_port=CLASSIFIER_PORT, host=MAIN_SERVER_IP, port=MAIN_SERVER_PORT)

    except Exception as e:
        print(f'--- {e} ---')
