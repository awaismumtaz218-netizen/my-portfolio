from flask import Flask, render_template

application = Flask(__name__)
app = application  # alias, useful for local `flask run`


@application.route('/')
def home():
    return render_template('index.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/projects')
def projects():
    return render_template('projects.html')


@application.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    # Local development only. In production, gunicorn runs this via the Procfile.
    application.run(host='0.0.0.0', port=8000, debug=True)
