from flask import Blueprint, redirect, request, url_for, render_template
from form.form_item import CategoryForm, ItemForm
from models import Category, Item
from extensions import db, UPLOAD_FOLDER
import os

item_blueprint = Blueprint("item_blueprint", __name__)


@item_blueprint.route('/category/')
def list_category():
    categories = Category.query.all()
    return render_template("category.html", categories=categories)

@item_blueprint.route('/category/add', methods=['GET', 'POST'])
def add_category():
    form = CategoryForm()
    if request.method=="POST":
        if form.validate_on_submit:
            category = Category()
            category.name = form.name.data
            db.session.add(category)
            db.session.commit()
            return redirect(url_for("item_blueprint.list_category"))
    return render_template("add_category.html", form=form)

@item_blueprint.route('/category/<id>/delete')
def delete_category(id):
    category = Category.query.filter_by(id=id).first()
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("item_blueprint.list_category"))


@item_blueprint.route("/category/<id>/item/add", methods=['GET', 'POST'])
def add_item(id):
    form = ItemForm()
    if request.method=="POST" and form.validate_on_submit:
        item = Item()
        item.name = form.name.data
        item.desctiption = form.description.data
        item.price = form.price.data
        item.stock = form.stock.data
        item.category_id = id
        if form.image.data!=None:
            file = form.image.data
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            item.image = os.path.join("/static/media", filename)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('item_blueprint.list_category'))
    return render_template("add_item.html", form=form, id=id)