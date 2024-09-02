from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        # Process reservation data
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']

        # Here you would insert the reservation into a database
        # For example:
        # db.insert_reservation(date, time, guests)

        return redirect(url_for('confirmation'))
    return render_template('reserve.html')

@app.route('/confirmation')
def confirmation():
    return "Reservation confirmed!"

if __name__ == '__main__':
    app.run(debug=True)
