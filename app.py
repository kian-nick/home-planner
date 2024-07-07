from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"idea_boards": []}

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/idea_boards', methods=['GET', 'POST'])
def idea_boards():
    data = load_data()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title and description:
            data['idea_boards'].append({"title": title, "description": description})
            save_data(data)
        return redirect(url_for('idea_boards'))
    return render_template('idea_boards.html', boards=data['idea_boards'])

@app.route('/delete_board/<int:index>')
def delete_board(index):
    data = load_data()
    if 0 <= index < len(data['idea_boards']):
        data['idea_boards'].pop(index)
        save_data(data)
    return redirect(url_for('idea_boards'))

# ... other routes ...
@app.route('/room_planners')
def room_planners():
    return render_template('room_planners.html')

@app.route('/budget_calculator')
def budget_calculator():
    return render_template('budget_calculator.html')

if __name__ == '__main__':
    app.run(debug=True)