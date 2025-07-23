from server_side.run_server import server_run



# starting the server
if __name__ == "__main__":
    try:
        server_run(classifier_route='localhost:5000', host='0.0.0.0', port=8000)

    except Exception as e:
        print(f'--- {e} ---')