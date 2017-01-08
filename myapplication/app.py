from flask import Flask, render_template, request
import whois

app = Flask(__name__)

#Index page
@app.route("/")
def my_form():
    return render_template("index.html")

#Get host info
@app.route("/hostlocation", methods=['GET','POST'])
def my_form_hostlocation():
	if request.method == 'GET':
		return redirect(url_for('my_form'))
	domain_name = request.form['domain'].lstrip()
	location = whois.whois(domain_name)['city']

	return render_template('location.html', domain_data=domain_name, location_data=location)

if __name__ == "__main__":
    app.run(debug=True)