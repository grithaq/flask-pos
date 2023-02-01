from flask import Blueprint, redirect, request, url_for, render_template
from form.form_item import CategoryForm
from models import Category
from extensions import db

item_blueprint = Blueprint("item_blueprint", __name__)

@item_blueprint.route('/category/add', methods=['GET', 'POST'])
def add_category():
    form = CategoryForm()
    if request.method=="POST":
        if form.validate_on_submit:
            category = Category()
            category.name = form.name.data
            db.session.add(category)
            db.session.commit()
            return redirect(url_for("item_blueprint.add_category"))
    return render_template("add_category.html", form=form)