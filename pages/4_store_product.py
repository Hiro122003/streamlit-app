import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import load_sales_data

# フォント設定（英語表示）
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ページタイトル
st.title("店舗・商品分析")

# データ読み込み
sales_df = load_sales_data()


# ── 店舗別売上Top10（横棒グラフ） ───────────────────────
st.subheader("店舗別売上 Top10")

# Store_IDでグループ集計して上位10件を抽出
store_sales = (
    sales_df.groupby("Store_ID")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
# 万円単位に変換
store_sales["Amount"] = store_sales["Amount"] / 10000
# Store_IDを文字列に変換してラベル表示
store_sales["Store_ID"] = "Store " + store_sales["Store_ID"].astype(str)

fig, ax = plt.subplots()
sns.barplot(data=store_sales, x="Amount", y="Store_ID", ax=ax)
ax.set_title("Store Sales Top10")
ax.set_xlabel("Sales (10k JPY)")
ax.set_ylabel("Store ID")
plt.tight_layout()
st.pyplot(fig)


# ── 商品別販売数Top10（横棒グラフ） ─────────────────────
st.subheader("商品別販売数 Top10")

# Product_IDでグループ集計して上位10件を抽出
product_sales = (
    sales_df.groupby("Product_ID")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
# Product_IDを文字列に変換してラベル表示
product_sales["Product_ID"] = "Product " + product_sales["Product_ID"].astype(str)

fig, ax = plt.subplots()
sns.barplot(data=product_sales, x="Quantity", y="Product_ID", ax=ax)
ax.set_title("Product Sales Top10")
ax.set_xlabel("Quantity")
ax.set_ylabel("Product ID")
plt.tight_layout()
st.pyplot(fig)
