from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Глобальна змінна для зберігання даних
data = {
    'temperature': None,
    'humidity': None
}

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/submit-data', methods=['POST'])
def submit_data():
    content = request.json
    print("Отримано дані:", content)
    data['temperature'] = content.get('temperature')
    data['humidity'] = content.get('humidity')
    return jsonify({'status': 'success'})

@app.route('/get-latest')
def get_latest():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
