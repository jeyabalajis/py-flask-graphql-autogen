def write_to_file(file_path: str, file_name: str, file_content: str):
    try:
        with open(file_path + "/" + file_name, 'w') as f:
            f.write(file_content)
    except Exception as e:
        print("Error! {}".format(str(e)))
    finally:
        f.close()
