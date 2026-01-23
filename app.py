from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")

    else:
        gender = request.form.get("gender")
        race_ethnicity = request.form.get("race_ethnicity")
        parental_level_of_education = request.form.get("parental_level_of_education")
        lunch = request.form.get("lunch")
        test_preparation_course = request.form.get("test_preparation_course")

        # ✅ validation (prevents None)
        if not gender or not race_ethnicity or not parental_level_of_education or not lunch or not test_preparation_course:
            return render_template("home.html", results="❌ Please select all dropdown values")

        reading_score = request.form.get("reading_score")
        writing_score = request.form.get("writing_score")

        if not reading_score or not writing_score:
            return render_template("home.html", results="❌ Please enter reading and writing scores")

        try:
            reading_score = int(reading_score)
            writing_score = int(writing_score)
        except:
            return render_template("home.html", results="❌ Scores must be numbers only")

        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score,
        )

        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template("home.html", results=round(results[0], 2))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
