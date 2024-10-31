from flask import Blueprint, render_template
import plotly.express as px
import pandas as pd

marbalism_bp = Blueprint('marbalism', __name__)

@marbalism_bp.route('/marbalism')
def marbalism():
    # Sample data for visualization
    df = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Values": [10, 20, 30, 40]
    })

    # Create a bar chart using Plotly
    fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")

    # Convert the Plotly figure to JSON for rendering in the template
    graphJSON = fig.to_json()

    return render_template('marbalism.html', graphJSON=graphJSON)
