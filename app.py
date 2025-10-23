from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.form['message']
        # Here you can implement any logic to generate a reply
        reply_message = f"You said: {user_message}"
        return render_template('reply.html', reply=reply_message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
