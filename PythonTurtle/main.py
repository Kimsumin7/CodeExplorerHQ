import turtle as t
import random

# 창 크기
t.setup(600, 400)
# 타이틀명
t.title("점프! 점프!")
# 배경색
t.bgcolor("#0B4629")

# 상단 글
t.penup()
# 글자색
t.color("white")
# 위치 조정
t.goto(0, 120)
# 제목 띄우기 설정
t.write("Jump! Jump!", False, "center", ("나눔바른펜", 25))
# 아래 선 위치 설정
t.goto(-300, -100)
t.pensize(3)
t.pendown()
t.goto(300, -100)

# 플레이어 생성
player = t.Turtle()
player.color("#FFCC1D")
player.shape("square")
player.penup()
player.goto(-200, -85)

# 장애물 리스트
obstacles = []

# 점프 관련 변수
is_jumping = False
jump_speed = 8    # 점프 초기 속도 (증가)
gravity = -0.5     # 중력 (낙하 가속도)
vertical_speed = 9 # 현재 수직 속도

# 점프 관련 변수
is_jumping = False
jump_speed = 8    # 점프 초기 속도 (증가)
gravity = -0.5     # 중력 (낙하 가속도)
vertical_speed = 0 # 현재 수직 속도

# 점프 기능
def jump(x, y):
    global is_jumping, vertical_speed
    if not is_jumping and player.ycor() == -85:  # 땅에 있을 때만 점프 가능
        is_jumping = True
        vertical_speed = jump_speed

# 장애물 생성 함수
def create_obstacle():
    obstacle = t.Turtle()
    obstacle.color("red")
    obstacle.shape("square")
    obstacle.penup()
    obstacle.goto(300, -85)
    obstacles.append(obstacle)
    t.ontimer(create_obstacle, random.randint(1000, 3000))  # 1~3초 후 새로운 장애물 생성

# 장애물 이동 함수
def move_obstacles():
    for obstacle in obstacles:
        obstacle.setx(obstacle.xcor() - 5)  # 장애물 이동 거리 조정
        # 화면 밖으로 나간 장애물 제거
        if obstacle.xcor() < -300:
            obstacle.hideturtle()
            obstacles.remove(obstacle)

# 게임 루프
def game_loop():
    global is_jumping, vertical_speed

    # 장애물 이동
    move_obstacles()
    
    # 플레이어 점프 및 낙하
    if is_jumping:
        player.sety(player.ycor() + vertical_speed)
        vertical_speed += gravity  # 중력 적용
        if player.ycor() <= -85:  # 땅에 도착했을 때
            player.sety(-85)
            is_jumping = False
            vertical_speed = 0  # 수직 속도 초기화
            jump_speed = 8      # 점프 속도 초기화

    # 16ms마다 게임 루프 실행 (약 60fps)
    t.ontimer(game_loop, 16)

# 클릭 이벤트 바인딩
t.onscreenclick(jump)

# 게임 시작
create_obstacle()
game_loop()

# 마침
t.done()