from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = "templates"
app.static_folder = 'static'
@app.route('/index')
def index():
    name = "Truong"
    return render_template(
        "index.html",
        username = name
    )
@app.route('/loadAccount')
def loadAccount():
    acc = "Felix"
    return render_template(
        "account.html",
        account=acc
    );

@app.route('/Page01')
def loadPage():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return render_template(
        "Page01.html", seq=lst
    );

@app.route('/Page03')
def loadPage03():
    import pandas as pd
    data = {
        'Name': ['John', 'anna', 'Truong', 'Hoang'],
        'Age': ['20', '21', '34', '21'],
        'City': ['new york', 'ha noi', 'nam dinh', 'ninh binh'],
    }
    df = pd.DataFrame(data)
    html_data = df.to_html(classes='data', escape=False);
    return render_template(
        "Page03.html",
        table = html_data
    );

@app.route('/welcome/<pname>')
def welcome(pname):
    return render_template("welcome.html",
                           username = pname)
@app.route('/noAccount')
def noAccount():
    acc = ""
    return render_template(
        "account.html",
        account=acc
    );
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
