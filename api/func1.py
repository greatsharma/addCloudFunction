from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/', methods=['GET'])
def add():
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))

        response = {
            'num1': num1,
            'num2': num2,
            'sum': num1 + num2
        }
    except Exception:
        response = {
            'status': {
                'code': 400,
                'msg': 'Bad request! specify both numbers'
            }
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
