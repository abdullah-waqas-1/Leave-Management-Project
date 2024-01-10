from flask import Flask, request, jsonify
from flask_cors import CORS
from bson import ObjectId
from backend import SupplierDB  # Import the backend code

app = Flask(__name__)
CORS(app)

supplier_db = SupplierDB()

@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    suppliers = supplier_db.get_suppliers()
    return jsonify(suppliers)

@app.route('/suppliers', methods=['POST'])
def add_supplier():
    data = request.json
    supplier_id = supplier_db.add_supplier(data)
    return jsonify({"message": "Supplier added successfully", "supplier_id": str(supplier_id)})

@app.route('/suppliers/<string:sup_id>', methods=['PUT'])
def update_supplier(sup_id):
    data = request.json
    result = supplier_db.update_supplier(sup_id, data)
    if result.modified_count > 0:
        return jsonify({"message": "Supplier updated successfully"})
    else:
        return jsonify({"error": "Supplier not found"})

@app.route('/suppliers/<string:sup_id>', methods=['DELETE'])
def delete_supplier(sup_id):
    result = supplier_db.delete_supplier(sup_id)
    if result.deleted_count > 0:
        return jsonify({"message": "Supplier deleted successfully"})
    else:
        return jsonify({"error": "Supplier not found"})

@app.route('/suppliers/search', methods=['POST'])
def search_suppliers():
    data = request.json
    search_by = data.get('search_by', '')
    search_txt = data.get('search_txt', '')
    suppliers = supplier_db.search_suppliers(search_by, search_txt)
    return jsonify(suppliers)

if __name__ == '__main__':
    app.run(debug=True)
