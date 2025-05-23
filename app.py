from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulated light state
light_state = {"status": "OFF"}

@app.route('/')
def home():
    return render_template('index.html', light_status=light_state["status"])

@app.route('/control', methods=['POST'])
def control_light():
    action = request.json.get('action')
    if action in ["ON", "OFF"]:
        light_state["status"] = action
        return jsonify({"message": f"Light turned {action}", "status": light_state["status"]})
    return jsonify({"error": "Invalid action"}), 400

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"light_status": light_state["status"]})

if __name__ == '__main__':
    app.run(debug=True)
