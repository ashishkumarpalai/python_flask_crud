from flask import Flask, request, jsonify

app = Flask(__name__)
data = []

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data/<int:index>', methods=['GET'])
def get_data_item(index):
    if index < len(data):
        return jsonify(data[index])
    else:
        return 'Data item not found', 404

@app.route('/data', methods=['POST'])
def create_data():
    new_data = request.json
    data.append(new_data)
    return jsonify(new_data), 201

@app.route('/data/<int:index>', methods=['PUT'])
def update_data(index):
    if index < len(data):
        updated_data = request.json
        data[index] = updated_data
        return jsonify(updated_data)
    else:
        return 'Data item not found', 404

@app.route('/data/<int:index>', methods=['DELETE'])
def delete_data(index):
    if index < len(data):
        deleted_data = data.pop(index)
        return jsonify(deleted_data)
    else:
        return 'Data item not found', 404

if __name__ == '__main__':
    app.run(debug=True)
