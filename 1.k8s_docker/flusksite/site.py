from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def show_ip():
    # получаем hostname контейнера
    hostname = socket.gethostname()
    # получаем IP-адрес по hostname
    ip_address = socket.gethostbyname(hostname)
    return f"<h2>IP контейнера: {ip_address}</h2>"

if __name__ == "__main__":
    # слушаем на всех интерфейсах внутри контейнера
    app.run(host="0.0.0.0", port=4000)
