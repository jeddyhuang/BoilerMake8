from flask import Flask,render_template,request
import interest
app = Flask(__name__, template_folder='template',static_folder='template\static')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form.to_dict()
        completer(form_data)
        return render_template('data.html')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

def completer(named):
    ticker = str(named['Name'])
    interest.get_finance(ticker)
    interest.get_searches(ticker)
    interest.prediction(ticker)
    interest.actual_prediction(ticker)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
