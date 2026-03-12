import gradio as gr
import pandas as pd
import plotly.express as px

from data_sources import get_meta_ads_data, get_samcart_data
from transform import combine_data


def load_dashboard(start_date, end_date):
    meta_ads_data = get_meta_ads_data(start_date, end_date)
    samcart_data = get_samcart_data(start_date, end_date)

    df, metrics = combine_data(meta_ads_data, samcart_data)

    fig = px.line(
        df,
        x="date",
        y=["spend", "revenue"],
        markers=True,
        title="Spend vs Revenue by Date"
    )

    metrics_df = pd.DataFrame(
        [{"Metric": key, "Value": value} for key, value in metrics.items()]
    )

    return metrics_df, df, fig


with gr.Blocks(title="Analytics Dashboard Prototype") as demo:
    gr.Markdown("# Analytics Dashboard Prototype")
    gr.Markdown(
        "Simple prototype combining Meta Ads and SamCart data into a unified dashboard."
    )

    with gr.Row():
        start_date = gr.Textbox(label="Start Date", value="2026-03-01", placeholder="YYYY-MM-DD")
        end_date = gr.Textbox(label="End Date", value="2026-03-07", placeholder="YYYY-MM-DD")

    load_btn = gr.Button("Load Dashboard")

    gr.Markdown("## KPI Metrics")
    metrics_table = gr.Dataframe(label="Metrics", interactive=False)

    gr.Markdown("## Combined Daily Data")
    data_table = gr.Dataframe(label="Merged Dataset", interactive=False)

    gr.Markdown("## Trend Chart")
    chart = gr.Plot()

    load_btn.click(
        fn=load_dashboard,
        inputs=[start_date, end_date],
        outputs=[metrics_table, data_table, chart]
    )

demo.launch()