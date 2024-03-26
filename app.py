from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def student_number():
    # Replace '123456' with your student number
    student_number = '200584973'

    # Format student number as JSON
    response = {
        "student_number": student_number
    }

    return jsonify(response)

@app.route('/webbook')
def dialogflow_text():
    # Text to be used by Dialogflow for integration
    dialogflow_text = "Sure..!! the books will collected from your nearest location soon...and the details will be update shortly on your email. We thank you person for the valuable donation:)"

    # Format student number as JSON
    response = {
        "student_number": student_number
    }
    return jsonify(dialogflow_text)

if __name__ == '__main__':
    app.run()
