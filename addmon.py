import requests
from requests.auth import HTTPBasicAuth

def main():
    # Авторизация через API VK
    vk_access_token = "vk api token"
    # Адрес сервера Minecraft и порт
    minecraft_server_address = "minecraft_server_address"
    minecraft_server_port = 256

    # Автоматизировать процесс входа на сайт
    url_login = "https://monitoringminecraft.ru/acc/vklogin"
    data_login = {"vk_access_token": vk_access_token}
    response_login = requests.post(url_login, data=data_login)

    # Проверка успешности входа
    if response_login.status_code == 20:
        print("Успешный вход на сайт!")
    else:
        print("Произошла ошибка при входе на сайт. Код ошибки:", response_login.status_code)
        return

    # Формирование данных для добавления сервера
    request_body = {"server": minecraft_server_address + ":" + str(minecraft_server_port), "java": "java -jar server.jar"}

    # Создание HTTP-запроса на добавление сервера
    url_add_server = "https://monitoringminecraft.ru/add-server"
    headers = {"Content-Type": "application/json"}
    response_add_server = requests.post(url_add_server, headers=headers, data=request_body)

    # Проверка успешности запроса
    if response_add_server.status_code == 20:
        print("Сервер успешно добавлен на сайт!")
    else:
        print("Произошла ошибка при добавлении сервера. Код ошибки:", response_add_server.status_code)

if __name__ == "__main__":
    main()