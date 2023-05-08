import os

def create_file_struct(dir_path='.'):
    # root (e.g. Desktop/MyServer)
    #   |
    #   |--> serv (e.g. MyServ)
    #   |      | --> settings.py
    #   |      | --> ctsc/cmds/routes.py
    #   |      | --> server.py
    #   |      | --> README.md
    serv_path = os.path.join(dir_path, '.serv')
    settings_path = os.path.join(serv_path, 'settings.py')
    requests_path = os.path.join(serv_path, 'requests.py')
    server_path = os.path.join(serv_path, 'server.py')
    README_path = os.path.join(serv_path, 'README.md')

    os.mkdir(serv_path)
    open(settings_path, 'x')
    open(requests_path, 'x')