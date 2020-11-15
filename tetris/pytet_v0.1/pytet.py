from matrix import * #matrix.py의 모든 함수들 가져오기

def draw_matrix(m):
    array = m.get_array() #matrix의 객체로 부터 array라는 리스트 생
    for y in range(m.get_dy()): #y는 matrix의 각 행을 말함.
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###
import random
rand=random.randrange(1,8)
def set_block(i,rand):
    if rand == 1:
        arrayBlk = [[[ 1, 1 ], [ 1, 1 ]],
                    [[ 1, 1 ], [ 1, 1 ]],
                    [[ 1, 1 ], [ 1, 1 ]],
                    [[ 1, 1 ], [ 1, 1 ]]]
    elif rand == 2:
        arrayBlk = [[[ 1, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ]],
                    [[ 0, 1, 1 ], [ 1, 1, 0 ], [ 0, 0, 0 ]],
                    [[ 0, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 1 ]],
                    [[ 0, 0, 0 ], [ 0, 1, 1 ], [ 1, 1, 0 ]]]
    elif rand == 3:
        arrayBlk = [[[ 1, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ]],
                    [[ 0, 1, 1 ], [ 0, 1, 0 ], [ 0, 1, 0 ]],
                    [[ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 1 ]],
                    [[ 0, 1, 0 ], [ 0, 1, 0 ], [ 1, 1, 0 ]]]
                    
    elif rand == 4:
        arrayBlk = [[[ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ]],
                    [[ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ]],
                    [[ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ]],
                    [[ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ]]]
    elif rand == 5:
        arrayBlk = [[[ 0, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 0 ]],
                    [[ 0, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 1 ]],
                    [[ 0, 0, 0 ], [ 1, 1, 1 ], [ 1, 0, 0 ]],
                    [[ 1, 1, 0 ], [ 0, 1, 0 ], [ 0, 1, 0 ]]]
    elif rand == 6:
        arrayBlk = [[[ 0, 1, 0 ], [ 1, 1, 0 ], [ 1, 0, 0 ]],
                    [[ 1, 1, 0 ], [ 0, 1, 1 ], [ 0, 0, 0 ]],
                    [[ 0, 0, 1 ], [ 0, 1, 1 ], [ 0, 1, 0 ]],
                    [[ 0, 0, 0 ], [ 1, 1, 0 ], [ 0, 1, 1 ]]]
    elif rand == 7:
        arrayBlk = [[[ 0, 1, 0 ], [ 1, 1, 1 ], [ 0, 0, 0 ]],
                    [[ 0, 1, 0 ], [ 0, 1, 1 ], [ 0, 1, 0 ]],
                    [[ 0, 0, 0 ], [ 1, 1, 1 ], [ 0, 1, 0 ]],
                    [[ 0, 1, 0 ], [ 1, 1, 0 ], [ 0, 1, 0 ]]]
    return arrayBlk[i]

    
### integer variables: must always be integer!
iScreenDy = 15 #높이를 15칸으로 정의
iScreenDx = 10 #폭을 10칸으로 정의
iScreenDw = 4 #둘러싼 벽의 두께를 4칸으로 정의
#matrix 중앙에 도형이 나오도록 하는 코드
top = 0 #나오는 도형의 좌측상단의 좌표y=0
left = iScreenDw + iScreenDx//2 - 2 #나오는 도형의 좌측상단의 x좌표
i=0

newBlockNeeded = False #bool 타입 변수, 도형 하나가 땅에 닿은 후 새로운 도형을 생성하기 위함.

arrayScreen = [    #초기화면 상태 정의, 2차원 배열, 0부분들이 게임이 진행되는 공간(1은 벽면을 뜻함.)
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
#iscreen(입력스크린)
oScreen = Matrix(iScreen)
#oscreen(출력스크린)
rand=random.randrange(1,8)
currBlk = Matrix(set_block(i,rand))
#화면에 나오는 블럭(4x4(위에 2차원 배열로 정의되어있음.)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
#4x4matrix를 떼어내기 위해 clip함수를 이용하여 변수 지정. top,left는 좌측상단의 좌표를 뜻함, top+currBlk.get_dy(), left+currBlk.get_dx()는 우측상단의 좌표.
tempBlk = tempBlk + currBlk
#덧셈하는 이유:게임 진행시 블럭들이 계속해서 쌓이기 때문.
oScreen.paste(tempBlk, top, left)
#oscreen에 붙여넣기를 함. iscreen이 아님. iscreen은 화면에 출력하는 대상이 아니고 oscreen을 화면에 출력.
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1 #왼쪽으로 이동하기위해 left-=1
    elif key == 'd': # move right
        left += 1 #오른쪽으로 이동하기위해 left+=1
    elif key == 's': # move down
        top += 1 
    elif key == 'w': # rotate the block clockwise 시계방향으로 회전
        i+=1
        if i==4:
            i=0
        currBlk=Matrix(set_block(i,rand))
        
    elif key == ' ': # drop the block
        while(tempBlk.anyGreaterThan(1)!=1):
            top+=1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx()) #위의 if문들로 top,left값이 조정될 수 있음.
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1): #충돌 테스트 시작.2라는 원소가 존재하면 충돌이 발생했다.anyGreaterThan:1보다 큰 원소가 하나라도 뜨는가?
        if key == 'a': # undo: move right
            left += 1 #충돌이 발생하였으므로 오른쪽으로 이동하기위해 left+=1
        elif key == 'd': # undo: move left
            left -= 1 
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise 반시계방향으로 회전
            i-=1
            if i==-1:
                i=3
            currBlk=Matrix(set_block(i,rand))
        elif key == ' ': # undo: move up
            top-=1
            newBlockNeeded = True

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        rand=random.randrange(1,8)
        currBlk = Matrix(set_block(i,rand)) #새로운 블록 생성
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1): #새로운 블록 생성 후 원래있던 블록과 충돌하면 종료하는 종료조건.
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
