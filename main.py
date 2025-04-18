import streamlit as st
import random as rd
# from openai import OpenAI
# import os

# os.environ["OPENAI_API_KEY"] = " 自分のAPIキーを入力 "
# client = OpenAI()

st.title(''':rainbow[人生ゲーム（GPT版）]''')

name = st.sidebar.text_input("あなたの名前は？")
sex = ["男性", "女性"]
sex_select = st.sidebar.pills("あなたの性別は？", sex, selection_mode="single")
st.sidebar.divider()

if "count" not in st.session_state:
    st.session_state.count = 0
if "age" not in st.session_state:
    st.session_state.age = 0
if "personality" not in st.session_state:
    st.session_state.personality = 0
if "job" not in st.session_state:
    st.session_state.job = 0
if "marriage" not in st.session_state:
    st.session_state.marriage = 0
if "child" not in st.session_state:
    st.session_state.child = 0
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

personality = [
    "ー",
    "理屈っぽい",
    "保守的",
    "楽観的",
    "心配性",
    "成長意欲が高い",
    "探究心がある",
    "要領が良い",
    "好奇心が旺盛",
    "物覚えが早い",
    "論理的",
    "聞き上手",
    "利他的",
    "社交性が高い",
    "協調性がある",
    "面倒見が良い",
    "気遣いができる",
    "行動力がある",
    "革新的",
    "正義感が強い",
    "発想が豊か",
    "独創的",
    "先見性がある",
    "決断力がある",
    "計画的",
    "責任感が強い",
    "統率力がある",
    "忍耐力がある",
    "集中力がある"
]

job = [
    "ー",
    "オフィス",
    "美容",
    "芸術",
    "資産・金融",    
    "医療",
    "国や海外",
    "旅行",
    "モノづくり",
    "オフィス",
    "科学・研究",
    "美容",
    "語学・教育・出版",
    "自然・動物",
    "冠婚葬祭",
    "健康・福祉",
    "健康・福祉",
    "乗り物",
    "芸術",
    "エンターテイメント",
    "エンターテイメント",
    "建築・インテリア",    
    "料理",    
    "モノづくり",
    "資産・金融",
    "科学・研究",
    "医療",
    "コンピュータ",
    "コンピュータ"
]

marriage = [
    "ー",
    "結婚",
    "離婚"
]

child = [
    "ー",
    "1",
    "2",
    "3"
]

initial_number = 21

if st.session_state.count > initial_number - 1:
    st.write("**終了！！**")

elif st.session_state.count <= initial_number:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        role_the_dice1 = st.button(''':blue[♠ サイコロを振る]''', key=1)
    with col2:
        role_the_dice2 = st.button(''':red[♥ サイコロを振る]''', key=2)
    with col3:
        role_the_dice3 = st.button(''':green[♣ サイコロを振る]''', key=3)
    with col4:
        role_the_dice4 = st.button(''':orange[♦ サイコロを振る]''', key=4)

    card_number = rd.randint(1, 13)
    dice_number = rd.randint(1, 6)
    point = card_number * dice_number

    if role_the_dice1:
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.spade_point += point
        st.write("🎲 " + str(dice_number) + " ： **" + str(st.session_state.age) + "歳**になりました。")

        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {"role": "user", "content": "あなたは人生ゲームの作成者です。日本人" + sex_select + str(st.session_state.age) + "歳、性格：" + str(st.session_state.personality) + "、職種：" + str(st.session_state.job) + "の仕事（学業）イベントを作成してください。内容は50文字以内で出力してください。" },
        #     ],
        # )
        # output_content = response.choices[0].message.content.strip()
        # st.write("♠ " + str(card_number) + " ： " + output_content)

        # response_image = client.images.generate(
        #     model="dall-e-3",
        #     prompt="日本人" + sex_select + str(st.session_state.age) + "歳、output_content",
        #     size="1024x1024",
        #     quality="standard",
        #     n=1,
        # )
        # output_image = response_image.data[0].url
        # st.image(output_image, width=400)

        st.write(" 仕事（学業）：**" + str(point) + "ポイント**を獲得しました。")

    elif role_the_dice2:
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.heart_point += point
        st.write("🎲 " + str(dice_number) + " ： **" + str(st.session_state.age) + "歳**になりました。")

        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {"role": "user", "content": "あなたは人生ゲームの作成者です。日本人" + sex_select + str(st.session_state.age) + "歳、性格：" + str(st.session_state.personality) + "、職種："+ str(st.session_state.job) + "の恋愛（友情）イベントを作成してください。内容は50文字以内で出力してください。" },
        #     ],
        # )
        # output_content = response.choices[0].message.content.strip()
        # st.write("♥ " + str(card_number) + " ： " + output_content)

        # response_image = client.images.generate(
        #     model="dall-e-3",
        #     prompt="日本人" + sex_select + str(st.session_state.age) + "歳、output_content",
        #     size="1024x1024",
        #     quality="standard",
        #     n=1,
        # )
        # output_image = response_image.data[0].url
        # st.image(output_image, width=400)

        st.write(" 恋愛（友情）： **" + str(point) + "ポイント**を獲得しました。")

    elif role_the_dice3:
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.club_point += point
        st.write("🎲 " + str(dice_number) + " ： **" + str(st.session_state.age) + "歳**になりました。")

        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {"role": "user", "content": "あなたは人生ゲームの作成者です。日本人" + sex_select + str(st.session_state.age) + "歳、性格：" + str(st.session_state.personality) + "、職種："+ str(st.session_state.job) + "の趣味イベントを作成してください。内容は50文字以内で出力してください。" },
        #     ],
        # )
        # output_content = response.choices[0].message.content.strip()
        # st.write("♣ " + str(card_number) + " ： " + output_content)

        # response_image = client.images.generate(
        #     model="dall-e-3",
        #     prompt="日本人" + sex_select + str(st.session_state.age) + "歳、output_content",
        #     size="1024x1024",
        #     quality="standard",
        #     n=1,
        # )
        # output_image = response_image.data[0].url
        # st.image(output_image, width=400)

        st.write(" 趣味 ： **" + str(point) + "ポイント**を獲得しました。")

    elif role_the_dice4:
        st.session_state.age += dice_number
        st.session_state.count += 1
        st.session_state.diamond_point += point
        st.write("🎲 " + str(dice_number) + " ： **" + str(st.session_state.age) + "歳**になりました。")

        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {"role": "user", "content": "あなたは人生ゲームの作成者です。日本人" + sex_select + str(st.session_state.age) + "歳、性格：" + str(st.session_state.personality) + "、職種："+ str(st.session_state.job) + "のお金イベントを作成してください。内容は50文字以内で出力してください。" },
        #     ],
        # )
        # output_content = response.choices[0].message.content.strip()
        # st.write("♦ " + str(card_number) + " ： " + output_content)

        # response_image = client.images.generate(
        #     model="dall-e-3",
        #     prompt="日本人" + sex_select + str(st.session_state.age) + "歳、output_content",
        #     size="1024x1024",
        #     quality="standard",
        #     n=1,
        # )
        # output_image = response_image.data[0].url
        # st.image(output_image, width=400)

        st.write(" お金 ： **" + str(point) + "ポイント**を獲得しました。")

    if st.session_state.count == 3:
        if st.session_state.heart_point == 0 and st.session_state.club_point == 0 and st.session_state.diamond_point == 0:
            st.session_state.personality = 1
        elif st.session_state.spade_point == 0 and st.session_state.club_point == 0 and st.session_state.diamond_point == 0:
            st.session_state.personality = 2
        elif st.session_state.spade_point == 0 and st.session_state.heart_point == 0 and st.session_state.diamond_point == 0:
            st.session_state.personality = 3
        elif st.session_state.spade_point == 0 and st.session_state.heart_point == 0 and st.session_state.club_point == 0:
            st.session_state.personality = 4
        elif st.session_state.spade_point >= st.session_state.heart_point and st.session_state.spade_point >= st.session_state.club_point and st.session_state.spade_point >= st.session_state.diamond_point:
            if st.session_state.heart_point >= st.session_state.club_point and st.session_state.heart_point >= st.session_state.diamond_point:
                if st.session_state.club_point >= st.session_state.diamond_point:
                    st.session_state.personality = 5
                elif st.session_state.club_point < st.session_state.diamond_point:
                    st.session_state.personality = 6
            if st.session_state.club_point >= st.session_state.heart_point and st.session_state.club_point >= st.session_state.diamond_point:
                if st.session_state.heart_point >= st.session_state.diamond_point:
                    st.session_state.personality = 7
                elif st.session_state.heart_point < st.session_state.diamond_point:
                    st.session_state.personality = 8
            if st.session_state.diamond_point >= st.session_state.heart_point and st.session_state.diamond_point >= st.session_state.club_point:
                if st.session_state.heart_point >= st.session_state.club_point:
                    st.session_state.personality = 9
                elif st.session_state.heart_point < st.session_state.club_point:
                    st.session_state.personality = 10
        elif st.session_state.heart_point >= st.session_state.spade_point and st.session_state.heart_point >= st.session_state.club_point and st.session_state.heart_point >= st.session_state.diamond_point:
            if st.session_state.spade_point >= st.session_state.club_point and st.session_state.spade_point >= st.session_state.diamond_point:
                if st.session_state.club_point >= st.session_state.diamond_point:
                    st.session_state.personality = 11
                elif st.session_state.club_point < st.session_state.diamond_point:
                    st.session_state.personality = 12
            if st.session_state.club_point >= st.session_state.spade_point and st.session_state.club_point >= st.session_state.diamond_point:
                if st.session_state.spade_point >= st.session_state.diamond_point:
                    st.session_state.personality = 13
                elif st.session_state.spade_point < st.session_state.diamond_point:
                    st.session_state.personality = 14
            if st.session_state.diamond_point >= st.session_state.spade_point and st.session_state.diamond_point >= st.session_state.club_point:
                if st.session_state.spade_point >= st.session_state.club_point:
                    st.session_state.personality = 15
                elif st.session_state.spade_point < st.session_state.club_point:
                    st.session_state.personality = 16
        elif st.session_state.club_point >= st.session_state.spade_point and st.session_state.club_point >= st.session_state.heart_point and st.session_state.club_point >= st.session_state.diamond_point:
            if st.session_state.spade_point >= st.session_state.heart_point and st.session_state.spade_point >= st.session_state.diamond_point:
                if st.session_state.heart_point >= st.session_state.diamond_point:
                    st.session_state.personality = 17
                elif st.session_state.heart_point < st.session_state.diamond_point:
                    st.session_state.personality = 18
            if st.session_state.heart_point >= st.session_state.spade_point and st.session_state.heart_point >= st.session_state.diamond_point:
                if st.session_state.spade_point >= st.session_state.diamond_point:
                    st.session_state.personality = 19
                elif st.session_state.spade_point < st.session_state.diamond_point:
                    st.session_state.personality = 20
            if st.session_state.diamond_point >= st.session_state.spade_point and st.session_state.diamond_point >= st.session_state.heart_point:
                if st.session_state.spade_point >= st.session_state.heart_point:
                    st.session_state.personality = 21
                elif st.session_state.spade_point < st.session_state.heart_point:
                    st.session_state.personality = 22
        elif st.session_state.diamond_point >= st.session_state.spade_point and st.session_state.diamond_point >= st.session_state.heart_point and st.session_state.diamond_point >= st.session_state.club_point:
            if st.session_state.spade_point >= st.session_state.heart_point and st.session_state.spade_point >= st.session_state.club_point:
                if st.session_state.heart_point >= st.session_state.club_point:
                    st.session_state.personality = 23
                elif st.session_state.heart_point < st.session_state.club_point:
                    st.session_state.personality = 24
            if st.session_state.heart_point >= st.session_state.spade_point and st.session_state.heart_point >= st.session_state.club_point:
                if st.session_state.spade_point >= st.session_state.club_point:
                    st.session_state.personality = 25
                elif st.session_state.spade_point < st.session_state.club_point:
                    st.session_state.personality = 26
            if st.session_state.club_point >= st.session_state.spade_point and st.session_state.club_point >= st.session_state.heart_point:
                if st.session_state.spade_point >= st.session_state.heart_point:
                    st.session_state.personality = 27
                elif st.session_state.spade_point < st.session_state.heart_point:
                    st.session_state.personality = 28
        st.write(name +" さんの性格は **" + personality[st.session_state.personality] + "** となりました。")

    if st.session_state.count == 5:
        if st.session_state.heart_point == 0 and st.session_state.club_point == 0 and st.session_state.diamond_point == 0:
            st.session_state.job = 1
        elif st.session_state.spade_point == 0 and st.session_state.club_point == 0 and st.session_state.diamond_point == 0:
            st.session_state.job = 2
        elif st.session_state.spade_point == 0 and st.session_state.heart_point == 0 and st.session_state.diamond_point == 0:
            st.session_state.job = 3
        elif st.session_state.spade_point == 0 and st.session_state.heart_point == 0 and st.session_state.club_point == 0:
            st.session_state.job = 4
        elif st.session_state.spade_point >= st.session_state.heart_point and st.session_state.spade_point >= st.session_state.club_point and st.session_state.spade_point >= st.session_state.diamond_point:
            if st.session_state.heart_point >= st.session_state.club_point and st.session_state.heart_point >= st.session_state.diamond_point:
                if st.session_state.club_point >= st.session_state.diamond_point:
                    st.session_state.job = 5
                elif st.session_state.club_point < st.session_state.diamond_point:
                    st.session_state.job = 6
            if st.session_state.club_point >= st.session_state.heart_point and st.session_state.club_point >= st.session_state.diamond_point:
                if st.session_state.heart_point >= st.session_state.diamond_point:
                    st.session_state.job = 7
                elif st.session_state.heart_point < st.session_state.diamond_point:
                    st.session_state.job = 8
            if st.session_state.diamond_point >= st.session_state.heart_point and st.session_state.diamond_point >= st.session_state.club_point:
                if st.session_state.heart_point >= st.session_state.club_point:
                    st.session_state.job = 9
                elif st.session_state.heart_point < st.session_state.club_point:
                    st.session_state.job = 10
        elif st.session_state.heart_point >= st.session_state.spade_point and st.session_state.heart_point >= st.session_state.club_point and st.session_state.heart_point >= st.session_state.diamond_point:
            if st.session_state.spade_point >= st.session_state.club_point and st.session_state.spade_point >= st.session_state.diamond_point:
                if st.session_state.club_point >= st.session_state.diamond_point:
                    st.session_state.job = 11
                elif st.session_state.club_point < st.session_state.diamond_point:
                    st.session_state.job = 12
            if st.session_state.club_point >= st.session_state.spade_point and st.session_state.club_point >= st.session_state.diamond_point:
                if st.session_state.spade_point >= st.session_state.diamond_point:
                    st.session_state.job = 13
                elif st.session_state.spade_point < st.session_state.diamond_point:
                    st.session_state.job = 14
            if st.session_state.diamond_point >= st.session_state.spade_point and st.session_state.diamond_point >= st.session_state.club_point:
                if st.session_state.spade_point >= st.session_state.club_point:
                    st.session_state.job = 15
                elif st.session_state.spade_point < st.session_state.club_point:
                    st.session_state.job = 16
        elif st.session_state.club_point >= st.session_state.spade_point and st.session_state.club_point >= st.session_state.heart_point and st.session_state.club_point >= st.session_state.diamond_point:
            if st.session_state.spade_point >= st.session_state.heart_point and st.session_state.spade_point >= st.session_state.diamond_point:
                if st.session_state.heart_point >= st.session_state.diamond_point:
                    st.session_state.job = 17
                elif st.session_state.heart_point < st.session_state.diamond_point:
                    st.session_state.job = 18
            if st.session_state.heart_point >= st.session_state.spade_point and st.session_state.heart_point >= st.session_state.diamond_point:
                if st.session_state.spade_point >= st.session_state.diamond_point:
                    st.session_state.job = 19
                elif st.session_state.spade_point < st.session_state.diamond_point:
                    st.session_state.job = 20
            if st.session_state.diamond_point >= st.session_state.spade_point and st.session_state.diamond_point >= st.session_state.heart_point:
                if st.session_state.spade_point >= st.session_state.heart_point:
                    st.session_state.job = 21
                elif st.session_state.spade_point < st.session_state.heart_point:
                    st.session_state.job = 22
        elif st.session_state.diamond_point >= st.session_state.spade_point and st.session_state.diamond_point >= st.session_state.heart_point and st.session_state.diamond_point >= st.session_state.club_point:
            if st.session_state.spade_point >= st.session_state.heart_point and st.session_state.spade_point >= st.session_state.club_point:
                if st.session_state.heart_point >= st.session_state.club_point:
                    st.session_state.job = 23
                elif st.session_state.heart_point < st.session_state.club_point:
                    st.session_state.job = 24
            if st.session_state.heart_point >= st.session_state.spade_point and st.session_state.heart_point >= st.session_state.club_point:
                if st.session_state.spade_point >= st.session_state.club_point:
                    st.session_state.job = 25
                elif st.session_state.spade_point < st.session_state.club_point:
                    st.session_state.job = 26
            if st.session_state.club_point >= st.session_state.spade_point and st.session_state.club_point >= st.session_state.heart_point:
                if st.session_state.spade_point >= st.session_state.heart_point:
                    st.session_state.job = 27
                elif st.session_state.spade_point < st.session_state.heart_point:
                    st.session_state.job = 28
        st.write(name + " さんの職業は **" + job[st.session_state.job] + "** に関する仕事となります。")

    if st.session_state.marriage == 0:
        if st.session_state.age > 20 and st.session_state.age < 40:
            if st.session_state.spade_point >= 35 and st.session_state.heart_point >= 35 and st.session_state.club_point >= 35 and st.session_state.diamond_point >= 35:
                st.session_state.marriage += 1
                st.write(name + " さんは **" + marriage[st.session_state.marriage] + "** しました。")

    if st.session_state.marriage == 1 and st.session_state.child == 0:
        if st.session_state.age > 21 and st.session_state.age < 41:
           if st.session_state.spade_point >= 40 and st.session_state.heart_point >= 40 and st.session_state.club_point >= 40 and st.session_state.diamond_point >= 40:
                st.session_state.child += 1
                st.write(name + " さんは **" + child[st.session_state.child] + " 人目**の子供を授かりました。")
    if st.session_state.marriage == 1 and st.session_state.child == 1:
        if st.session_state.age > 21 and st.session_state.age < 41:
          if st.session_state.spade_point >= 45 and st.session_state.heart_point >= 45 and st.session_state.club_point >= 45 and st.session_state.diamond_point >= 45:
                st.session_state.child += 1
                st.write(name + " さんは **" + child[st.session_state.child] + " 人目**の子供を授かりました。")
    if st.session_state.marriage == 1 and st.session_state.child == 2:
        if st.session_state.age > 21 and st.session_state.age < 41:
          if st.session_state.spade_point >= 50 and st.session_state.heart_point >= 50 and st.session_state.club_point >= 50 and st.session_state.diamond_point >= 50:
                st.session_state.child += 1
                st.write(name + " さんは **" + child[st.session_state.child] + " 人目**の子供を授かりました。")

    if st.session_state.marriage == 1:
        if st.session_state.age > 25 and st.session_state.age < 45:
            if st.session_state.spade_point >= 120:
                st.session_state.spade_point = 0
                st.session_state.marriage += 1
                st.write(name + " さんは仕事が忙しく **" + marriage[st.session_state.marriage] + "** しました。")
                st.write(" 離婚に伴い、仕事（学業）ポイントを失いました。")
            elif st.session_state.heart_point >= 120:
                st.session_state.heart_point = 0
                st.session_state.marriage += 1
                st.write(name + " さんは浮気が原因で **" + marriage[st.session_state.marriage] + "** しました。")
                st.write(" 離婚に伴い、恋愛（友情）ポイントを失いました。")
            elif st.session_state.club_point >= 120:
                st.session_state.club_point = 0
                st.session_state.marriage += 1
                st.write(name + " さんは価値観の違いで **" + marriage[st.session_state.marriage] + "** しました。")
                st.write(" 離婚に伴い、趣味ポイントを失いました。")
            elif st.session_state.diamond_point >= 120:
                st.session_state.diamond_point = 0
                st.session_state.marriage += 1
                st.write(name + " さんは投資に失敗し **" + marriage[st.session_state.marriage] + "** しました。")
                st.write(" 離婚に伴い、お金ポイントを失いました。")

    if st.session_state.count == initial_number:
        st.write(name + " さんの人生は **" + str(st.session_state.age) + " 歳**で幕を閉じました。")

    st.sidebar.text("サイコロの全回数： " + str(initial_number) + " 回")
    st.sidebar.text("サイコロの残り数： " + str(initial_number - st.session_state.count) + " 回")
    st.sidebar.text("現在の年齢： " + str(st.session_state.age) + " 歳")
    st.sidebar.text("性格： " + str(personality[st.session_state.personality]))
    st.sidebar.text("職業： " + str(job[st.session_state.job]))
    st.sidebar.text("結婚： " + str(marriage[st.session_state.marriage]))
    st.sidebar.text("子供： " + str(child[st.session_state.child]) + " 人")
    st.sidebar.text("仕事（学業）： " + str(st.session_state.spade_point) + " ポイント")
    st.sidebar.text("恋愛（友情）： " + str(st.session_state.heart_point) + " ポイント")
    st.sidebar.text("趣味： " + str(st.session_state.club_point) + " ポイント") 
    st.sidebar.text("お金： " + str(st.session_state.diamond_point) + " ポイント")
    st.sidebar.text("総合： " + str(st.session_state.spade_point + st.session_state.heart_point + st.session_state.club_point + st.session_state.diamond_point) + " ポイント")
    st.stop()
