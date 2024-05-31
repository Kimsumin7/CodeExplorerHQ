#Double buffering방법-tracer(), update()

#기본 설정
import turtle as t
import random #장애물을 랜덤으로 소환하기 위한 랜덤함수

# 창 크기 및 기타 설정
t.setup(600, 400) #창 크기
t.title("점프! 점프!") #상단 타이틀명
t.bgcolor("#0B4629") #배경색
t.penup() #터틀이 움직일 때 선 그리기X
t.color("white") #선 색
t.goto(0, 120) #터틀 움직임 x,y좌표
t.write("Jump! Jump!", False, "center", ("나눔바른펜", 25)) #배경에 뜨는 글자 설정
t.goto(-300, -100) #프로그램 시작 시 터틀을 왼쪽 아래 모서리로 이동
t.pensize(3) #펜 굵기 설정
t.pendown() #터틀이 이동 시 선 그어짐
t.goto(300, -100) #그어지는 선 좌표
t.penup() #터틀이 움직일 때 선 그리기X

# 더블 버퍼링 활성화
t.tracer(0, 0) #화면을 부드럽게 하기 위한 그래픽 라이브러리 함수

# 플레이어 생성
player = t.Turtle() #터틀 객체 생성
player.color("#FFCC1D") #터틀 색상
player.shape("square") #터틀 모양
player.penup() #터틀이 움직일 때 선 그리기X
player.goto(-200, -85) #터틀 선 위로 위치

# 장애물 리스트
obstacles = [] #리스트 선언

# 점프 관련 변수 초기화
is_jumping = False #터틀이 점프 중이 아닐때 땅에 위치
jump_speed = 8 #점프 스피드 설정
gravity = -0.5 #떨어지는 중력 설정
vertical_speed = 0 #플레이어 수직 속도 변수 초기화

# 점프 기능
def jump(x, y): #마우스 클릭 이벤트
    global is_jumping, vertical_speed #전역 변수 2개 선언
    if not is_jumping and player.ycor() == -85:  # 땅에 있을 때만 점프 가능
        is_jumping = True #터틀이 점프 중일때
        vertical_speed = jump_speed #터틀이 위로 점프할 수 있게 하는 값

# 장애물 생성 함수
def create_obstacle():
    obstacle = t.Turtle() #새로운 장애물 생성
    obstacle.color("red") #색상 설정
    obstacle.shape("square") #장애물 모양
    obstacle.penup() #터틀이 움직일 때 선 그리기X
    obstacle.goto(300, -85) #터틀 움직임 x,y좌표
    obstacles.append(obstacle) #장애물을 장애물 리스트에 추가
    t.ontimer(create_obstacle, random.randint(1000, 3000)) #1~3초 간격으로 장애물 생성

# 장애물 이동 함수
def move_obstacles(): #장애물들이 왼쪽으로 이동 설정
    for obstacle in obstacles: #장애물 작업 반복
        obstacle.setx(obstacle.xcor() - 5) #장애물들 이동 -5속도
        if obstacle.xcor() < -300: #장애물 x좌표가 -300보다 작아지면
            obstacle.hideturtle() #로 숨김
            obstacles.remove(obstacle) #숨김 후 제거 

# 충돌 감지 함수
def is_collision(player, obstacle):
    distance = player.distance(obstacle) #터틀과 장애물 거리 측정
    if distance < 20:  # 플레이어와 장애물 사이의 거리가 20픽셀 미만이면 충돌
        return True #참일 경우를 반환
    return False #거리가 20이상이면 충돌 발생x라고 인식

# 게임 루프
def game_loop():
    global is_jumping, vertical_speed #함수 내에서 전역 변수 사용할 것임을 명시

    move_obstacles() #를 호출하여 장애물 이동

    if is_jumping:
        player.sety(player.ycor() + vertical_speed) #터틀을 수직 방향으로 이동
        vertical_speed += gravity #터틀 수직 속도 설정, 중력에 따라 증감
        if player.ycor() <= -85: #터틀이 땅(선)위에 머무르게 함
            player.sety(-85) 
            is_jumping = False #터틀이 다시 점프할 수 있게 함
            vertical_speed = 0 #터틀이 점프할 때 적용되는 속도 초기화

    # 충돌 검사
    for obstacle in obstacles: #모든 장애물에 대한 충돌 검사
        if is_collision(player, obstacle): #장애물 간의 충돌 여부 확인
            t.goto(0, 0) #터틀을 중앙으로 이동시킴
            t.color("red") #텍스트 색상
            t.write("Game Over", False, "center", ("Arial", 30, "bold")) #게임오버 시 뜨는 문구 설정
            t.hideturtle() #화살표 머리 모양 숨김
            t.update() #화면 업데이트
            return  # 게임 루프 종료

    t.update()  # 화면 업데이트
    t.ontimer(game_loop, 16) #게임 루프를 16ms마다 호출하여 게임이 계속 실행될 수 있게 함

# 클릭 이벤트 바인딩
t.onscreenclick(jump) #화면 클릭&터틀점프 연결

# 게임 시작
create_obstacle() #장애물 생성
game_loop() #게임 루프 실행

t.done() #사용자가 창을 닫을 때까지 대기
