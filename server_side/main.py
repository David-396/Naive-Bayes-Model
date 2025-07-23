from run_server import server_run



# starting the server
if __name__ == "__main__":
    try:
        server_run(classifier_ip='127.0.0.1', classifier_port=8001, host='127.0.0.1', port=8000)

    except Exception as e:
        print(f'--- {e} ---')
