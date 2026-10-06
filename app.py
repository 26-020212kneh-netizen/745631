import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="숫자 맞히기 게임",
    page_icon="🎯",
    layout="centered"
)

# 게임 초기화
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.best_score = None


# 게임 리셋 함수
def reset_game():
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False


# 제목
st.title("🎯 숫자 맞히기 게임")
st.write("1부터 100 사이의 숫자를 맞혀보세요!")

st.divider()

# 최고 기록
if st.session_state.best_score is not None:
    st.info(f"🏆 최고 기록: {st.session_state.best_score}번")

# 게임이 끝나지 않았다면
if not st.session_state.game_over:

    # 숫자 입력
    guess = st.number_input(
        "숫자를 입력하세요",
        min_value=1,
        max_value=100,
        step=1
    )

    # 확인 버튼
    if st.button("🎯 정답 확인", use_container_width=True):

        st.session_state.attempts += 1

        if guess < st.session_state.answer:
            st.warning("⬆️ 더 큰 숫자입니다!")

        elif guess > st.session_state.answer:
            st.warning("⬇️ 더 작은 숫자입니다!")

        else:
            st.session_state.game_over = True

            # 최고 기록 갱신
            if (
                st.session_state.best_score is None
                or st.session_state.attempts < st.session_state.best_score
            ):
                st.session_state.best_score = st.session_state.attempts

            st.success(
                f"🎉 정답입니다! "
                f"정답은 {st.session_state.answer}였습니다."
            )

            st.balloons()

# 게임 종료 상태
else:

    st.success(
        f"🎉 축하합니다!\n\n"
        f"{st.session_state.attempts}번 만에 정답을 맞혔습니다!"
    )

# 현재 시도 횟수
st.write(f"🔢 현재 시도 횟수: **{st.session_state.attempts}회**")

st.divider()

# 새 게임 버튼
if st.button("🔄 새 게임", use_container_width=True):
    reset_game()
    st.rerun()
