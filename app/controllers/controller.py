from flask import render_template
from app import app
from app.models.order_list import orders

@app.route("/")
def greet():
    return "Welcome to the Book Shop"

@app.route('/orders')
def order():
    return render_template('index.html', title='Order List', orders_list=orders)

@app.route("/orders/<index>")
def order_by_index(index):
    chosen_order = orders[int(index)]
    return render_template('order.html', title="Order", order=chosen_order)