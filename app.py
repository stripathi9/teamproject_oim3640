
from flask import Flask, render_template, request
from helper import output


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"]) 
def get_recipe():
    if request.method == "POST":
        dish = request.form["Dish"]
        cuisine = request.form["Cuisine"]
        diet = request.form["Diet"]
        allergies = request.form["Allergies"]
        time = request.form["Time"]
        random_dish = output(dish, cuisine, diet, allergies, time)
        if cuisine  == "":
            return render_template("input_page.html")   
        random_dish = output(dish, cuisine, diet, allergies, time)
        while random_dish == False:
            return render_template("error_page.html")
        return render_template("result_page.html", result = random_dish)
    return render_template("input_page.html")



if __name__ == '__main__':
    app.run(port = 3000, debug=True)