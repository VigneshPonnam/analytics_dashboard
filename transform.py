import pandas as pd


def combine_data(meta_ads_data, samcart_data):
    ads_df = pd.DataFrame(meta_ads_data)
    sales_df = pd.DataFrame(samcart_data)

    merged_df = pd.merge(ads_df, sales_df, on="date", how="outer")

    numeric_cols = ["spend", "clicks", "impressions", "purchases", "revenue"]
    for col in numeric_cols:
        if col in merged_df.columns:
            merged_df[col] = merged_df[col].fillna(0)

    merged_df = merged_df.sort_values("date")

    total_spend = float(merged_df["spend"].sum())
    total_revenue = float(merged_df["revenue"].sum())
    total_purchases = int(merged_df["purchases"].sum())
    total_clicks = int(merged_df["clicks"].sum())

    roas = round(total_revenue / total_spend, 2) if total_spend > 0 else 0
    cpa = round(total_spend / total_purchases, 2) if total_purchases > 0 else 0
    conversion_rate = round((total_purchases / total_clicks) * 100, 2) if total_clicks > 0 else 0

    metrics = {
        "Total Spend": round(total_spend, 2),
        "Total Revenue": round(total_revenue, 2),
        "ROAS": roas,
        "Purchases": total_purchases,
        "CPA": cpa,
        "Conversion Rate (%)": conversion_rate
    }

    return merged_df, metrics