import copy
import json

from flask import Flask, request, jsonify, abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from models.lamp import Lamp

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET['user'],
    password=SECRET['password'],
    host=SECRET['host'],
    port=SECRET['port'],
    db=SECRET['db']
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class TableLamp(Lamp, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    style = db.Column(db.String(16), unique=False)
    count_of_bulbs = db.Column(db.Integer, unique=False)
    brand = db.Column(db.String(16), unique=False)
    price_in_uah = db.Column(db.Float, unique=False)
    room = db.Column(db.String(16), unique=False)
    height_in_mm = db.Column(db.Float, unique=False)
    width_in_mm = db.Column(db.Float, unique=False)
    type = db.Column(db.String(16), unique=False)

    def __init__(self, style, count_of_bulbs, brand, price_in_uah, room, height_in_mm, width_in_mm, type):
        super().__init__(style, count_of_bulbs, brand, price_in_uah, room, height_in_mm, width_in_mm)
        self.type = type


class TableLampSchema(ma.Schema):
    class Meta:
        fields = ('style', 'count_of_bulbs', 'brand', 'price_in_uah', 'room', 'height_in_mm', 'width_in_mm', 'type')


table_lamp_schema = TableLampSchema()
table_lamps_schema = TableLampSchema(many=True)


@app.route('/table_lamp', methods=['POST'])
def add_table_lamp():
    table_lamp = TableLamp(request.json('style'),
                           request.json('count_of_bulbs'),
                           request.json('brand'),
                           request.json('price_in_uah'),
                           request.json('room'),
                           request.json('height_in_mm'),
                           request.json('width_in_mm'),
                           request.json('type'))
    db.session.add(table_lamp)
    db.session.commit()
    return table_lamp_schema.jsonify(table_lamp)


@app.route('/table_lamp', methods=['GET'])
def get_table_lamps():
    all_table_lamps = TableLamp.query.all()
    result = table_lamps_schema.dump(all_table_lamps)
    return jsonify({'table_lamps': result})


@app.route('/table_lamp/<id>', methods=['GET'])
def get_table_lamp(id):
    table_lamp = TableLamp.query.get(id)
    if not table_lamp:
        abort(404)
    return table_lamp_schema.jsonify(table_lamp)


@app.route('/table_lamp/<id>', methods=['PUT'])
def update_table_lamp(id):
    table_lamp = TableLamp.query.get(id)
    if not table_lamp:
        abort(404)
    old_table_lamp = copy.deepcopy(table_lamp)
    table_lamp.style = request.json('style')
    table_lamp.count_of_bulbs = request.json('count_of_bulbs')
    table_lamp.brand = request.json('brand')
    table_lamp.price_in_uah = request.json('price_in_uah')
    table_lamp.room = request.json('room')
    table_lamp.height_in_mm = request.json('height_in_mm')
    table_lamp.width_in_mm = request.json('width_in_mm')
    table_lamp.type = request.json('type')
    db.session.commit()
    return table_lamp_schema.jsonify(old_table_lamp)


@app.route('/table_lamp/<id>', methods=['DELETE'])
def delete_table_lamp(id):
    table_lamp = TableLamp.query.get(id)
    if not table_lamp:
        abort(404)
    db.session.delete(table_lamp)
    db.session.commit()
    return table_lamp_schema.jsonify(table_lamp)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
