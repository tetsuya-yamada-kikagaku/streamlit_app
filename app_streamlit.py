# app_streamlit.py (Streamlit で動かします)
# streamlit run app_streamlit.py
# 「app_streamlit.py」の部分で、パスの指定をして起動させています。

import streamlit as st
import requests

st.title("じゃんけんアプリ")

st.write("あなたの手を選んでください：")

# ボタンの作成
col1, col2, col3 = st.columns(3)

with col1:
    rock_button = st.button("✊ グー")
with col2:
    paper_button = st.button("✋ パー")
with col3:
    scissors_button = st.button("✌️ チョキ")

# 選択された手を保存する変数
player_choice = None

if rock_button:
    player_choice = "rock"
elif paper_button:
    player_choice = "paper"
elif scissors_button:
    player_choice = "scissors"

# APIリクエスト
if player_choice:
    api_url = "https://janken-app.onrender.com/" #　FastAPI は、デフォルトで localhost:8000
    
    response = requests.post(
        api_url,
        json={"player_choice": player_choice}
    )
    
    if response.status_code == 200:
        data = response.json()
        
        # 日本語化
        choice_jp = {
            "rock": "グー",
            "paper": "パー",
            "scissors": "チョキ"
        }
        
        result_jp = {
            "win": "あなたの勝ち！",
            "lose": "あなたの負け...",
            "draw": "引き分け"
        }
        
        st.write("---")
        st.write(f"あなたの選択: {choice_jp[data['player_choice']]}")
        st.write(f"コンピュータの選択: {choice_jp[data['computer_choice']]}")
        st.write(f"結果: {result_jp[data['result']]}")
        
        # 結果に応じて色や絵文字を変更
        if data['result'] == 'win':
            st.success("🎉 おめでとうございます！")
        elif data['result'] == 'lose':
            st.error("😢 残念...")
        else:
            st.info("🤝 引き分けです")
    else:
        st.error("APIリクエストに失敗しました。")