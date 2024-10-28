from flask import Flask, request, jsonify
import math
import random

app = Flask(__name__)


def complex_calculation(n):
    result = 0
    for i in range(n):
        result += math.sin(random.random()) * math.cos(random.random())
        result = math.sqrt(abs(result))
    return result


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    size = 200

    # Create a large list to consume memory
    memory_consumer = [0] * (size * 1024)

    # Add CPU-intensive operations
    for i in range(len(memory_consumer)):
        memory_consumer[i] = i

        # Perform complex calculations
        result = complex_calculation(2)  # Increase this number to increase CPU usage

        # Matrix-like operations
        # matrix_size = 5
        # for j in range(matrix_size):
        #     for k in range(matrix_size):
        #         x = math.sin(i + j) * math.cos(k)
        #         x = math.sqrt(abs(x))
        #         x = math.exp(math.fmod(x, 2))

    return jsonify(data)


if __name__ == '__main__':
    app.run()