import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from utils.data_loader import load_merged_data, load_member_data

# 日本語フォントの設定（文字化け防止）
matplotlib.rcParams["font.family"] = "MS Gothic"

# ページタイトル
st.title("会員分析")

# 結合データ・会員データの読み込み
merged_df = load_merged_data()
member_df = load_member_data()


# ── 性別×平均購買額（棒グラフ） ─────────────────────────
st.subheader("性別×平均購買額")

# GenderでグループしてAmountの平均を集計
gender_avg = merged_df.groupby("Gender")["Amount"].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=gender_avg, x="Gender", y="Amount", ax=ax)
ax.set_title("性別×平均購買額")
ax.set_xlabel("性別")
ax.set_ylabel("平均購買額（円）")
plt.tight_layout()
st.pyplot(fig)


# ── 年代別×平均購買額（棒グラフ） ───────────────────────
st.subheader("年代別×平均購買額")

# age_groupでグループしてAmountの平均を集計
age_avg = merged_df.groupby("age_group", observed=True)["Amount"].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=age_avg, x="age_group", y="Amount", ax=ax)
ax.set_title("年代別×平均購買額")
ax.set_xlabel("年代")
ax.set_ylabel("平均購買額（円）")
plt.tight_layout()
st.pyplot(fig)


# ── 年齢分布ヒストグラム ─────────────────────────────────
st.subheader("年齢分布")

fig, ax = plt.subplots()
sns.histplot(data=member_df, x="Age", bins=20, ax=ax)
ax.set_title("年齢分布")
ax.set_xlabel("年齢（歳）")
ax.set_ylabel("人数（人）")
plt.tight_layout()
st.pyplot(fig)


# ── Amount × Quantity 散布図（hue=Gender） ───────────────
st.subheader("購買金額 × 購買数量")

fig, ax = plt.subplots()
sns.scatterplot(data=merged_df, x="Quantity", y="Amount", hue="Gender", ax=ax)
ax.set_title("購買金額 × 購買数量（性別色分け）")
ax.set_xlabel("購買数量（個）")
ax.set_ylabel("購買金額（円）")
plt.tight_layout()
st.pyplot(fig)
