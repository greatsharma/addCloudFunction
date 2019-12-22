from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/str/', methods=['GET'])
def concat():
    try:
        val1 = request.args.get('val1')
        val2 = request.args.get('val2')

        response = {
            'val1': val1,
            'val2': val2,
            'concated': val1+val2
        }
    except Exception:
        response = {
            'status': {
                'code': 400,
                'msg': 'Bad request! specify both values'
            }
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
