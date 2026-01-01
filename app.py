from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

QR_PATH = "static/qr_code.png"

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form["qrdata"]
        generate_qr_code(data, QR_PATH)
        return render_template("index.html", qr_image=QR_PATH)

    return render_template("index.html", qr_image=None)

@app.route("/download")
def download_qr():
    return send_file(QR_PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
