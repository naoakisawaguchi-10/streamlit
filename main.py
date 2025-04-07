import streamlit as st
import random as rd

st.title("人生ゲーム（GPT版）")

name = st.sidebar.text_input("あなたの名前は？")
year_of_birth = st.sidebar.text_input("あなたの生まれた年は？")
sex = st.sidebar.text_input("あなたの性別は？")
st.sidebar.divider()

if "age" not in st.session_state:
    st.session_state.age = 0

role_the_dice1 = st.button("サイコロを振る")

if role_the_dice1:
    random_number = rd.randint(1, 6)
    st.write(random_number)
    st.session_state.age += random_number
    if st.session_state.age == 1:
        st.write("初めて「ママ」や「パパ」と言葉を発する。")
    elif st.session_state.age == 2:
        st.write("お気に入りの絵本のページを繰り返しめくる。")
    elif st.session_state.age == 3:
        st.write("お気に入りのぬいぐるみと「会話」して、新たな友達だと思うようになる。")
    elif st.session_state.age == 4:
        st.write("家族と一緒にスーパーに行き、自分でお菓子を選ぶ。")
    elif st.session_state.age == 5:
        st.write("ひらがなを覚えて、名前が書けるようになる。")
    elif st.session_state.age == 6:
        st.write("小学校に入学！新しい友達ができる。")

    st.write("現在の年齢は " + str(st.session_state.age) + " 歳です。")
