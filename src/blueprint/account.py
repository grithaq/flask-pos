from flask import Blueprint, redirect, request, url_for, render_template
from form.form_customer import CustomerForm
from models import Customer
from extensions import db


customer_blueprint = Blueprint("customer_blueprint", __name__)

@customer_blueprint.route("/customer/")
def list_customer():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@customer_blueprint.route("/customer/add/", methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    if request.method=='POST':
        if form.validate_on_submit:
            print("Valdi")
            customer = Customer()
            customer.first_name = form.first_name.data            
            customer.last_name = form.last_name.data
            customer.address = form.address.data
            customer.phone_number = form.phone_number.data
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for('customer_blueprint.list_customer'))
    return render_template("add_customer.html", form=form)

@customer_blueprint.route("/customer/<id>/delete")
def delete_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customer_blueprint.list_customer'))