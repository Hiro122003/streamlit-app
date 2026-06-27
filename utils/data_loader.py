import streamlit as st
import pandas as pd
from pathlib import Path

# CSVファイルのパスをプロジェクトルートからの相対パスで定義
SALES_CSV = Path("data/Sales_Data.csv")
MEMBER_CSV = Path("data/Member_Data.csv")


@st.cache_data
def load_sales_data():
    """売上データを読み込み、Transaction_DateをDatetime型に変換して返す"""
    df = pd.read_csv(SALES_CSV)
    # 日付文字列をdatetime型に変換
    df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
    return df


@st.cache_data
def load_member_data():
    """会員データを読み込んで返す"""
    df = pd.read_csv(MEMBER_CSV)
    return df


@st.cache_data
def load_merged_data():
    """売上データと会員データをMember_IDで結合し、age_group列を追加して返す"""
    sales_df = load_sales_data()
    member_df = load_member_data()

    # Member_IDをキーに内部結合
    merged_df = pd.merge(sales_df, member_df, on="Member_ID")

    # 年代区分列を追加
    merged_df["age_group"] = pd.cut(
        merged_df["Age"],
        bins=[0, 19, 29, 39, 49, 59, 200],
        labels=["~20", "20s", "30s", "40s", "50s", "60+"],
        right=True
    )

    return merged_df
