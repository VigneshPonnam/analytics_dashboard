from datetime import datetime, timedelta
import random


def get_meta_ads_data(start_date: str, end_date: str):
    """
    Mock Meta Ads data.
    Replace this with real Meta Ads API integration later.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    data = []
    current = start
    while current <= end:
        spend = round(random.uniform(80, 250), 2)
        clicks = random.randint(40, 180)
        impressions = random.randint(2000, 9000)

        data.append({
            "date": current.strftime("%Y-%m-%d"),
            "platform": "Meta Ads",
            "spend": spend,
            "clicks": clicks,
            "impressions": impressions
        })
        current += timedelta(days=1)

    return data


def get_samcart_data(start_date: str, end_date: str):
    """
    Mock SamCart sales data.
    Replace this with real SamCart API integration later.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    data = []
    current = start
    while current <= end:
        purchases = random.randint(3, 18)
        revenue = round(purchases * random.uniform(35, 90), 2)

        data.append({
            "date": current.strftime("%Y-%m-%d"),
            "platform": "SamCart",
            "purchases": purchases,
            "revenue": revenue
        })
        current += timedelta(days=1)

    return data