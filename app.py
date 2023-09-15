from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')  # Placeholder, you'd need to create this template

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')  # Placeholder, you'd need to create this template

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Placeholder, you'd need to create this template

@app.route('/booking')
def booking():
    return render_template('booking.html')  # Placeholder, you'd need to create this template

if __name__ == '__main__':
    app.run(debug=True)
