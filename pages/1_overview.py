import streamlit as st
from utils.data_loader import load_sales_data, load_member_data

# ページタイトル
st.title("データ概要")


# ── 売上データ ──────────────────────────────────────────
st.subheader("売上データ（Sales_Data.csv）")

# データ読み込み
sales_df = load_sales_data()

# 行数・列数をメトリクスで横並び表示
col1, col2 = st.columns(2)
col1.metric("行数", f"{len(sales_df):,} 件")
col2.metric("列数", f"{sales_df.shape[1]} 列")

# データのプレビュー（先頭5行）
st.caption("先頭5行のプレビュー")
st.dataframe(sales_df.head())

# カラムの型と欠損値数
st.caption("カラム情報（型・欠損値数）")
info_df = sales_df.dtypes.rename("データ型").to_frame()
info_df["欠損値数"] = sales_df.isnull().sum()
st.dataframe(info_df)


# ── 会員データ ──────────────────────────────────────────
st.subheader("会員データ（Member_Data.csv）")

# データ読み込み
member_df = load_member_data()

# 行数・列数をメトリクスで横並び表示
col3, col4 = st.columns(2)
col3.metric("行数", f"{len(member_df):,} 件")
col4.metric("列数", f"{member_df.shape[1]} 列")

# データのプレビュー（先頭5行）
st.caption("先頭5行のプレビュー")
st.dataframe(member_df.head())

# カラムの型と欠損値数
st.caption("カラム情報（型・欠損値数）")
info_df2 = member_df.dtypes.rename("データ型").to_frame()
info_df2["欠損値数"] = member_df.isnull().sum()
st.dataframe(info_df2)
