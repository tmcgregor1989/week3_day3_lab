from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Customer Orders', activeOrders = orders)


@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', title="customer name", currentOrder = orders[int(index)])

