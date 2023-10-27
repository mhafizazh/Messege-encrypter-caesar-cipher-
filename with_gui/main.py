from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


# @app.route("/email-sent", methods=["POST"])
# def receive_data():
    # stock_name = request.form["stock_name"]
    # email = request.form["email"]
    # company_name = request.form["company_name"]
    # result = get_info(company_name=company_name, stock_code=stock_name)
    # return render_template("email_sent_page.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)