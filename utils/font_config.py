import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語表示が可能なフォント候補
# クラウド(Streamlit Cloud): packages.txt でインストールした IPAexGothic / IPAGothic
# ローカル(Windows): Meiryo / Yu Gothic / MS Gothic など
_JP_FONT_CANDIDATES = [
    "IPAexGothic",
    "IPAGothic",
    "Noto Sans CJK JP",
    "Meiryo",
    "Yu Gothic",
    "MS Gothic",
    "TakaoGothic",
]


def setup_japanese_font():
    """matplotlib / seaborn で日本語を表示できるフォントを設定する"""
    # 利用可能なフォント名の一覧を取得
    available = {f.name for f in fm.fontManager.ttflist}

    # 候補の中から最初に見つかった日本語フォントを採用
    for name in _JP_FONT_CANDIDATES:
        if name in available:
            plt.rcParams["font.family"] = name
            break

    # マイナス記号が豆腐(□)にならないようにする
    plt.rcParams["axes.unicode_minus"] = False
