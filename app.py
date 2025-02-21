from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Sample data
cars = [
    {'id': 1, 'model': 'BMW i8', 'available': True},
    {'id': 2, 'model': 'AUDI Q7', 'available': True},
    {'id': 3, 'model': 'Ford Mustang', 'available': True},
    {'id': 4, 'model': 'HONDA AMAZE', 'available': False},
]

rentals = []

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/rent/<int:car_id>', methods=['POST'])
def rent_car(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car and car['available']:
        car['available'] = False
        rentals.append(car)
        flash(f'You have rented {car["model"]}!', 'success')
    else:
        flash('Car is not available for rent.', 'danger')
    return redirect(url_for('index'))

@app.route('/return/<int:car_id>', methods=['POST'])
def return_car(car_id):
    car = next((car for car in rentals if car['id'] == car_id), None)
    if car:
        car['available'] = True
        rentals.remove(car)
        flash(f'You have returned {car["model"]}.', 'success')
    else:
        flash('Car not found in your rentals.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)