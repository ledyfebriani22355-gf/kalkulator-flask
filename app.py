from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    hasil = None

    if request.method == 'POST':
        angka1 = float(request.form['angka1'])
        angka2 = float(request.form['angka2'])
        operasi = request.form['operasi']

        if operasi == 'tambah':
            hasil = angka1 + angka2
        elif operasi == 'kurang':
            hasil = angka1 - angka2
        elif operasi == 'kali':
            hasil = angka1 * angka2
        elif operasi == 'bagi':
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                hasil = "Tidak bisa dibagi dengan 0"

    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)