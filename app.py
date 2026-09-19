from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home ():
    return """
    <h1> absensi karyawan google </h1>
    
    <form action="/absensi" method="post">
    <Label for="nama">Nama:</Label>
    <input type="text" id="nama" name="nama" required><br><br>
    <button type="submit">submit</button>
    </form>
    """

@app.route("/absensi", methods=["POST"])
def absensi():
    nama = request.form["nama"]

    with open("absensi.txt", "a") as file:
        file.write(f"{nama}\n")

    return f"{nama} berhasil absen. Terima kasih!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)