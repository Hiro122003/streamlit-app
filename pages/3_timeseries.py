import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import load_sales_data
from utils.font_config import setup_japanese_font

# 日本語フォントを設定
setup_japanese_font()

# ページタイトル
st.title("時系列分析")

# データ読み込み
sales_df = load_sales_data()


# ── 月別売上推移（折れ線グラフ） ────────────────────────
st.subheader("月別売上推移")

# 月を抽出してグループ集計
monthly_sales = (
    sales_df.groupby(sales_df["Transaction_Date"].dt.to_period("M"))["Amount"]
    .sum()
    .reset_index()
)
# Period型を文字列に変換してmatplotlibで扱えるようにする
monthly_sales["Transaction_Date"] = monthly_sales["Transaction_Date"].astype(str)

# 万円単位に変換
monthly_sales["Amount"] = monthly_sales["Amount"] / 10000

fig, ax = plt.subplots()
ax.plot(monthly_sales["Transaction_Date"], monthly_sales["Amount"], marker="o")
ax.set_title("月別売上推移")
ax.set_xlabel("月")
ax.set_ylabel("売上（万円）")
ax.set_ylim(120, 150)
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
st.pyplot(fig)


# ── 曜日別取引件数（棒グラフ） ──────────────────────────
st.subheader("曜日別取引件数")

# 曜日番号（0=月〜6=日）を抽出してグループ集計
sales_df["weekday"] = sales_df["Transaction_Date"].dt.dayofweek
weekday_count = sales_df.groupby("weekday").size().reset_index(name="Transactions")

# 曜日ラベル（月〜日の順）
weekday_labels = ["月", "火", "水", "木", "金", "土", "日"]
weekday_count["Weekday"] = weekday_count["weekday"].map(lambda x: weekday_labels[x])

fig, ax = plt.subplots()
sns.barplot(data=weekday_count, x="Weekday", y="Transactions", order=weekday_labels, ax=ax)
ax.set_title("曜日別取引件数")
ax.set_xlabel("曜日")
ax.set_ylabel("取引件数")
plt.tight_layout()
st.pyplot(fig)
