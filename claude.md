# CLAUDE.md - streamlit-app プロジェクト設定

## プロジェクト概要

CSVデータ（売上・会員）を読み込み、集計・可視化を行うStreamlitアプリ。

## ディレクトリ構成

```
streamlit-app/
├── app.py                  # エントリーポイント・トップ画面
├── pages/
│   ├── 1_overview.py       # データ概要（件数・型・欠損確認）
│   ├── 2_summary.py        # KPIサマリー
│   ├── 3_timeseries.py     # 時系列分析
│   ├── 4_store_product.py  # 店舗・商品分析
│   └── 5_member.py         # 会員分析
├── utils/
│   └── data_loader.py      # CSV読込・結合・前処理（共通処理）
├── data/
│   ├── Sales_Data.csv
│   └── Member_Data.csv
├── CLAUDE.md
└── requirements.txt
```

## データ仕様

### Sales_Data.csv（1,000行 × 7列）
| カラム名 | 型 | 説明 |
|---|---|---|
| Transaction_ID | int | トランザクションID |
| Transaction_Date | str | 取引日時（例: 2024/5/1 0:00） |
| Member_ID | int | 会員ID（Member_Dataと結合キー） |
| Product_ID | int | 商品ID（1〜50） |
| Store_ID | int | 店舗ID（1〜20） |
| Quantity | int | 購買数量（1〜4） |
| Amount | int | 購買金額（510〜10,000） |

### Member_Data.csv（300行 × 4列）
| カラム名 | 型 | 説明 |
|---|---|---|
| Member_ID | int | 会員ID（結合キー） |
| Gender | str | 性別（Male / Female） |
| Age | int | 年齢（18〜80歳、平均51歳） |
| Days_Since_Registration | int | 登録からの日数 |

### 結合方法
```python
merged = pd.merge(sales, member, on='Member_ID')
```

## 各ページの役割

### utils/data_loader.py
- CSVの読み込み・結合・前処理を一元管理
- `@st.cache_data` で読み込みをキャッシュする
- 前処理: Transaction_Dateをdatetime型に変換、年代区分（age_group）の列を追加

### app.py
- アプリタイトルとサイドバーの説明を表示するトップ画面
- データのアップロード機能（st.file_uploader）は実装しない
  - 理由: dataフォルダのCSVを直接読み込む方式にする

### pages/1_overview.py
- データの件数・カラム・型・欠損値を表示
- `st.dataframe` でデータのプレビューを表示

### pages/2_summary.py
- KPIを `st.metric` で横並び表示（総売上・平均購買額・取引件数・平均個数）

### pages/3_timeseries.py
- 月別売上推移（折れ線グラフ）
- 曜日別取引件数（棒グラフ）

### pages/4_store_product.py
- 店舗別売上Top10（横棒グラフ）
- 商品別販売数Top10（横棒グラフ）

### pages/5_member.py
- 性別×平均購買額（棒グラフ）
- 年代別×平均購買額（棒グラフ）
- 年齢分布ヒストグラム
- Amount × Quantity 散布図（hue=Gender）

## 技術スタック

| ライブラリ | バージョン | 用途 |
|---|---|---|
| streamlit | 最新安定版 | UIフレームワーク |
| pandas | 最新安定版 | データ処理・集計 |
| matplotlib | 最新安定版 | グラフ描画 |
| seaborn | 最新安定版 | グラフ描画（統計可視化） |

## コーディング規約

- **コメント**: 必ず日本語でコメントを書く
- **関数名**: スネークケース（例: `load_data`, `show_summary`）
- **変数名**: 英語小文字のスネークケース（例: `sales_df`, `merged_df`）
- **言語**: Python
- **型ヒント**: 不要（シンプルさを優先）

## 実装時の注意事項

- `@st.cache_data` をデータ読み込み関数に必ず付ける（再読み込み防止）
- グラフは `st.pyplot(fig)` で表示する（`plt.show()` は使わない）
- 各ページの先頭で `st.title()` または `st.header()` でページタイトルを設定する
- グラフを描画するたびに `fig, ax = plt.subplots()` で新しいfigureを作る
- `plt.tight_layout()` をグラフ表示前に呼び出す

## 実装ステップ（順番通りに進める）

1. 仮想環境の作成・有効化
2. requirements.txt の作成・ライブラリインストール
3. utils/data_loader.py の実装
4. app.py の実装
5. pages/ を1ファイルずつ実装（1_overview → 2_summary → 3_timeseries → 4_store_product → 5_member）
6. 動作確認（`streamlit run app.py`）