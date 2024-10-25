from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    size = 15

    # Create a large list to consume memory
    memory_consumer = [0] * (size * 1024 )  # Each element is roughly 8 bytes, so this creates size MB of data

    # Modify the list to prevent optimization
    for i in range(len(memory_consumer)):
        memory_consumer[i] = i

    return jsonify(data)


if __name__ == '__main__':
    app.run()