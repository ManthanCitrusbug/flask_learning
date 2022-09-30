from flask import Flask, flash, render_template, redirect, url_for
from forms import RegistraionForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e670ea4ac75d3720402ec47951f08494'

@app.route("/register", methods=['GET', 'POST'])
def index(): 
    form = RegistraionForm()
    if form.validate_on_submit():
        print(form.username.errors)
        flash(f"Registered successfully {form.username.data}", "success")
        return redirect(url_for("home"))
    return render_template('register.html', form=form)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug =True)