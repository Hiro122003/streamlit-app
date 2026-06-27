import streamlit as st
from utils.data_loader import load_sales_data

# ページタイトル
st.title("KPIサマリー")

# データ読み込み
sales_df = load_sales_data()

# KPI値の集計
total_sales = sales_df["Amount"].sum()
avg_amount = sales_df["Amount"].mean()
transaction_count = len(sales_df)
avg_quantity = sales_df["Quantity"].mean()

# 4つのKPIを横並びで表示
col1, col2, col3, col4 = st.columns(4)

col1.metric("総売上", f"¥{total_sales:,}")
col2.metric("平均購買額", f"¥{avg_amount:,.0f}")
col3.metric("取引件数", f"{transaction_count:,} 件")
col4.metric("平均購買個数", f"{avg_quantity:.1f} 個")
