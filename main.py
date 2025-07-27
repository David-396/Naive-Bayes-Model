from server_side.run_server import server_run



if __name__ == "__main__":
    try:
        server_run(host='0.0.0.0', port=8000)

    except Exception as e:
        print(f'--- {e} ---')