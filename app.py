import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("formatted_output.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales ($)"
    }
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)