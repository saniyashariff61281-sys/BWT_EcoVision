from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Get input from user
            power = float(request.form["power"])
            hours = float(request.form["hours"])

            # Calculate energy, CO2 emission, and cost
            energy = power * hours  # in Wh
            co2 = energy * 0.5     # Example factor (grams)
            cost = energy * 0.01   # Example cost in ₹

            # Suggestion based on energy usage
            if energy > 1000:
                suggestion = "⚠ High energy usage! Reduce usage."
            else:
                suggestion = "✅ Energy efficient"

            # Prepare result to send to HTML
            result = {
                "energy": energy,
                "co2": co2,
                "cost": cost,
                "suggestion": suggestion
            }
        except ValueError:
            result = {
                "energy": 0,
                "co2": 0,
                "cost": 0,
                "suggestion": "❌ Invalid input, please enter numbers."
            }

    # Render the HTML template with results
    return render_template("index.html", result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)