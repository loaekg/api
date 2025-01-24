from flask import Flask, request, jsonify
import requests  # To forward requests to the local Python script

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def api():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Invalid request"}), 400
        
        # Process or forward data to the local Python script if needed
        # Example: Forward to a local endpoint
        local_response = {"message": "Processed request", "text": data["text"]}
        return jsonify(local_response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
