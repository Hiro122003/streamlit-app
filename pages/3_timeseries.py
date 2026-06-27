import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import load_sales_data

# フォント設定（英語表示）
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

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
ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (10k JPY)")
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
weekday_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
weekday_count["Weekday"] = weekday_count["weekday"].map(lambda x: weekday_labels[x])

fig, ax = plt.subplots()
sns.barplot(data=weekday_count, x="Weekday", y="Transactions", order=weekday_labels, ax=ax)
ax.set_title("Transactions by Weekday")
ax.set_xlabel("Weekday")
ax.set_ylabel("Transactions")
plt.tight_layout()
st.pyplot(fig)
