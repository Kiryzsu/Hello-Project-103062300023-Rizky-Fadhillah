from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia Anda

# Konfigurasi Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Ganti dengan server SMTP Anda
app.config['MAIL_PORT'] = 587  # Port server SMTP, biasanya 587 untuk TLS
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # Ganti dengan email pengirim
app.config['MAIL_PASSWORD'] = 'your_password'  # Ganti dengan password email pengirim
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        # Kirim email dengan link reset password
        msg = Message('Reset Password Request',
                      sender='your_email@example.com',
                      recipients=[email])
        msg.body = 'Klik link berikut untuk mereset password: http://example.com/reset-password'
        mail.send(msg)
        flash('Email pengaturan password telah dikirim.')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        msg = Message('Forgot Password',
                      sender='your_email@example.com',
                      recipients=[email])
        msg.body = 'Silakan ikuti instruksi berikut untuk reset password.'
        mail.send(msg)
        flash('Instruksi reset password telah dikirim ke email Anda.')
        return redirect(url_for('forgot_password'))
    return render_template('forgot-password.html')

if __name__ == '__main__':
    app.run(debug=True)
