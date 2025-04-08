import streamlit as st
import random as rd

st.title("人生ゲーム（GPT版）")

name = st.sidebar.text_input("あなたの名前は？")
# year_of_birth = st.sidebar.text_input("あなたの生まれた年は？")
sex = ["男性", "女性"]
sex_select = st.sidebar.pills("あなたの性別は？", sex, selection_mode="single")
st.sidebar.divider()

if "count" not in st.session_state:
    st.session_state.count = 0

if "age" not in st.session_state:
    st.session_state.age = 0

if "spade_point" not in st.session_state:
    st.session_state.spade_point = 0

if "heart_point" not in st.session_state:
    st.session_state.heart_point = 0

if "club_point" not in st.session_state:
    st.session_state.club_point = 0

if "diamond_point" not in st.session_state:
    st.session_state.diamond_point = 0

if "total_point" not in st.session_state:
    st.session_state.total_point = 0

initial_number = 21
all_times = st.sidebar.text("サイコロの全回数： " + str(initial_number) + " 回")

if st.session_state.count > initial_number - 1:
    st.write("終了！！")

elif st.session_state.count <= initial_number:

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        role_the_dice1 = st.button("♠ サイコロを振る", key=1)
    
    with col2:
        role_the_dice2 = st.button("♥ サイコロを振る", key=2)
    
    with col3:
        role_the_dice3 = st.button("♣ サイコロを振る", key=3)
    
    with col4:
        role_the_dice4 = st.button("♦ サイコロを振る", key=4)

    card_number = rd.randint(1, 13)
    dice_number = rd.randint(1, 6)
    point = card_number * dice_number

    if role_the_dice1:
        st.write("♠ " + str(card_number) + " , " + "🎲 " + str(dice_number) + " が出ました。" + " 仕事（学業）：" + str(point) + "ポイントを獲得しました。")
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.spade_point += point

    elif role_the_dice2:
        st.write("♥ " + str(card_number) + " , " + "🎲 " + str(dice_number) + " が出ました。" + " 恋愛（友情）：" + str(point) + "ポイントを獲得しました。")
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.heart_point += point
 
    elif role_the_dice3:
        st.write("♣ " + str(card_number) + " , " + "🎲 " + str(dice_number) + " が出ました。" + " 趣味：" + str(point) + "ポイントを獲得しました。")
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.club_point += point

    elif role_the_dice4:
        st.write("♦ " + str(card_number) + " , " + "🎲 " + str(dice_number) + " が出ました。" + " お金：" + str(point) + "ポイントを獲得しました。")
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.diamond_point += point

    if st.session_state.age == 1:
        st.write("初めて「ママ」や「パパ」と言葉を発する。")
        st.image("gameimage_sample.png", width=400)
    elif st.session_state.age == 2:
        st.write("お気に入りの絵本のページを繰り返しめくる。")
        st.image("gameimage_sample.png", width=400)
    elif st.session_state.age == 3:
        st.write("お気に入りのぬいぐるみと「会話」して、新たな友達だと思うようになる。")
        st.image("gameimage_sample.png", width=400)
    elif st.session_state.age == 4:
        st.write("家族と一緒にスーパーに行き、自分でお菓子を選ぶ。")
        st.image("gameimage_sample.png", width=400)
    elif st.session_state.age == 5:
        st.write("ひらがなを覚えて、名前が書けるようになる。")
        st.image("gameimage_sample.png", width=400)
    elif st.session_state.age == 6:
        st.write("小学校に入学！新しい友達ができる。")
        st.image("gameimage_sample.png", width=400)

    role_count = st.sidebar.text("サイコロの残り数： " + str(initial_number - st.session_state.count) + " 回")
    grow_old = st.sidebar.text("現在の年齢： " + str(st.session_state.age) + " 歳")
    get_spade_point = st.sidebar.text("仕事（学業）： " + str(st.session_state.spade_point) + " ポイント")
    get_heart_point = st.sidebar.text("恋愛（友情）： " + str(st.session_state.heart_point) + " ポイント")
    get_club_point = st.sidebar.text("趣味： " + str(st.session_state.club_point) + " ポイント") 
    get_diamond_point = st.sidebar.text("お金： " + str(st.session_state.diamond_point) + " ポイント")
    get_total_point = st.sidebar.text("総合： " + str(st.session_state.spade_point + st.session_state.heart_point + st.session_state.club_point + st.session_state.diamond_point) + " ポイント")

    if st.session_state.count == initial_number:
        st.write(name + " さんは " + str(st.session_state.age) + " 歳で永眠しました。")
        st.stop()
