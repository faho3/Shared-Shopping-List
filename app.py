from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

shopping_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form['item']
        shopping_list.append(item)
        return redirect(url_for('index'))
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/remove/<int:index>', methods=['POST'])
def remove_item(index):
    del shopping_list[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
