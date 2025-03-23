from flask import Flask, request, render_template

# Inisialisasi Flask
app = Flask(__name__)

# List untuk menyimpan data
data = []

# Route untuk halaman utama
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama'].strip()
        pesan = request.form['pesan'].strip()

        #menambahkan data ke list
        if nama and pesan:
            data.append({'nama': nama, 'pesan': pesan})

    return render_template('index.html', data=data)

# Menjalan aplikasi
if __name__ == '__main__':
    app.run(debug=True)