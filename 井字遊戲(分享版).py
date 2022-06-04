import sys
import os
import numpy as np
import pygame


WHITE = (242, 235, 211)
BLACK = (75, 102, 99)
BG_COLOR = (61, 189, 172)

#背景
BG_IMG = pygame.image.load(os.path.join("pygame" , "九宮格.png"))

# 遊戲視窗
DIS_TO_BOUNDARY = 100  
MATRIX_LEN = 3  
SQUARE_LEN = BG_IMG.get_width() / MATRIX_LEN  
screen_len = BG_IMG.get_width() + 2 * DIS_TO_BOUNDARY  

# 3種結果
WIN_STR = "WINNER!"  
DRAW_STR = "DRAW"  
LOOSER_STR = "LOOSER"  

#初始化
pygame.init()
screen = pygame.display.set_mode((screen_len, screen_len))  


game_difficulty = "hard"


def matrix_pos_to_screen_pos(row, col):
    return (DIS_TO_BOUNDARY + col * SQUARE_LEN,
            DIS_TO_BOUNDARY + row * SQUARE_LEN)


def draw_chess_piece():
    for row in range(len(board_matrix)):
        for col in range(len(board_matrix[row])):
            screen_pos = matrix_pos_to_screen_pos(row, col)
            screen_pos = (screen_pos[0] + SQUARE_LEN / 2,
                          screen_pos[1] + SQUARE_LEN / 2)
            if board_matrix[row][col] == 1:  
              
                pygame.draw.circle(screen, BLACK, screen_pos, SQUARE_LEN // 3)
            if board_matrix[row][col] == -1:
                pygame.draw.circle(screen, WHITE, screen_pos, SQUARE_LEN // 3)


def draw():
    screen.fill(BG_COLOR) 
    screen_pos = (DIS_TO_BOUNDARY, DIS_TO_BOUNDARY)
    screen.blit(BG_IMG, screen_pos)
    draw_chess_piece()
    pygame.display.update() 


def init_game():
    global board_matrix
    board_matrix = np.zeros((MATRIX_LEN, MATRIX_LEN), dtype=int)  # 初始棋盘为空


def in_chessboard_area(click_pos):
    is_in_width = DIS_TO_BOUNDARY <= click_pos[0] <= screen_len - \
                  DIS_TO_BOUNDARY
    is_in_height = DIS_TO_BOUNDARY <= click_pos[1] <= screen_len - \
                   DIS_TO_BOUNDARY
    return is_in_height and is_in_width


def to_matrix_pos(pos):  
    x = (pos[0] - DIS_TO_BOUNDARY) // SQUARE_LEN
    y = (pos[1] - DIS_TO_BOUNDARY) // SQUARE_LEN
    return int(x), int(y)


def make_move(pos):# 若點擊的位子為空 放入黑子
    if board_matrix[pos[1]][pos[0]] == 0:
        board_matrix[pos[1]][pos[0]] = 1


def is_player_turn(matrix):  #是否玩家回合
    result = np.count_nonzero(matrix == 0) % 2 == 1  # 棋盤陣列裡面如果數值為零的個數是奇數
    return result


def ai_make_move_easy():     #注意! 這裡tim改成照順序擺  
    for row in range(len(board_matrix)):
        for col in range(len(board_matrix[row])):
            if board_matrix[row][col] == 0:
                board_matrix[row][col] = -1
                return


def make_move_if_two_in_row():
    # 有行或列要變成一串時把它堵住
    for row in range(len(board_matrix)):
        for col in range(len(board_matrix[row])):
            if board_matrix[row, col] == 0 and (sum(board_matrix[row, :]) == 2 or sum(board_matrix[:, col]) == 2):
                board_matrix[row, col] = -1
                return
    # 對角線的部分
    top_left_diagonal = board_matrix[0, 0] + \
                        board_matrix[1, 1] + board_matrix[2, 2]
    top_right_diagonal = board_matrix[0, 2] + \
                         board_matrix[1, 1] + board_matrix[2, 0]
    if top_left_diagonal == 2:
        if board_matrix[0, 0] == 0:
            board_matrix[0, 0] = -1
            return
        elif board_matrix[1, 1] == 0:
            board_matrix[1, 1] = -1
            return
        elif board_matrix[2, 2] == 0:
            board_matrix[2, 2] = -1
            return
    elif top_right_diagonal == 2:
        if board_matrix[0, 2] == 0:
            board_matrix[0, 2] = -1
            return
        elif board_matrix[1, 1] == 0:
            board_matrix[1, 1] = -1
            return
        elif board_matrix[2, 0] == 0:
            board_matrix[2, 0] = -1
            return


def ai_make_move_medium():
    num_chess = np.count_nonzero(board_matrix)
    make_move_if_two_in_row()
    if num_chess == np.count_nonzero(board_matrix):
        ai_make_move_easy()


def get_all_possible_results_score(current_board_matrix):
    all_possible_result_scores = []
    # 判斷還有沒有空格
    if np.count_nonzero(current_board_matrix) < (MATRIX_LEN * MATRIX_LEN):
        for row in range(len(current_board_matrix)):
            for col in range(len(current_board_matrix)):
                if current_board_matrix[row, col] == 0:
                    new_board = np.copy(current_board_matrix)
                    new_board[row, col] = 1 if is_player_turn(
                        new_board) else -1
                    results = [check_horizontal_win(new_board), check_vertical_win(new_board),
                               check_diagonal_winner(new_board), check_draw(new_board)]
                    # 判斷結果
                    if len([x for x in results if x == "W"]):
                        all_possible_result_scores.append(-10)
                    elif len([x for x in results if x == "L"]):
                        all_possible_result_scores.append(10)
                    elif len([x for x in results if x == "D"]):
                        all_possible_result_scores.append(0)
                    else:
                        all_possible_result_scores.extend(
                            get_all_possible_results_score(new_board))
    return all_possible_result_scores


def ai_make_move_hard():
    num_chess = np.count_nonzero(board_matrix)
    # ai有兩個連線時就擺第三個 (ai win)
    make_move_if_two_in_row()

    if np.count_nonzero(board_matrix) == num_chess:
        max_scores = ((-1, -1), -sys.maxsize - 1)
        for row in range(len(board_matrix)):
            for col in range(len(board_matrix)):
                if board_matrix[row, col] == 0:
                    new_board = np.copy(board_matrix)
                    new_board[row, col] = -1
                    score = sum(get_all_possible_results_score(new_board))
                    if score > max_scores[1]:
                        max_scores = ((row, col), score)
        board_matrix[max_scores[0][0], max_scores[0][1]] = -1


def ai_make_move():
    if game_difficulty == "easy":
        ai_make_move_easy()
    elif game_difficulty == "medium":
        ai_make_move_medium()
    else:
        ai_make_move_hard()


def should_restart():  # 在來一局的部分
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # 點擊是視窗可以再來一局爛遊戲
                return True
            if event.type == pygame.QUIT:
                # 退出
                return False


def display_end_game(result):
    screen.fill(BG_COLOR)  
    font = pygame.font.Font(None, 70)  

    winner_msg = font.render(result, True, BLACK)
    screen.blit(winner_msg, (screen_len / 3, screen_len / 3))
    pygame.display.flip()  

    if should_restart():
        init_game()
    else:
        global running
        running = False

##貼心小提示 直行橫列
def check_horizontal_win(matrix):
    #  列的檢查     
    for row in matrix:
        if sum(row) == 3:
            return WIN_STR
        elif sum(row) == -3:
            return LOOSER_STR
    return ""


def check_vertical_win(matrix):
    #  行的檢查
    for col in range(MATRIX_LEN):
        if sum(matrix[:, col]) == 3:
            return WIN_STR
        elif sum(matrix[:, col]) == -3:
            return LOOSER_STR
    return ""


def check_diagonal_winner(matrix):
    #  對角線檢查
    top_left_diagonal = matrix[0, 0] + matrix[1, 1] + matrix[2, 2]
    top_right_diagonal = matrix[0, 2] + matrix[1, 1] + matrix[2, 0]
    if top_left_diagonal == 3 or top_right_diagonal == 3:
        return WIN_STR
    elif top_left_diagonal == -3 or top_right_diagonal == -3:
        return LOOSER_STR
    return ""


def check_draw(matrix):
    # 棋盤滿了
    if np.count_nonzero(matrix == 0) == 0:
        return DRAW_STR
    return ""


def check_winner():
    results = [check_horizontal_win(board_matrix), check_vertical_win(board_matrix),
               check_diagonal_winner(board_matrix), check_draw(board_matrix)]

    results = [x for x in results if len(x) > 0]
    if len(results) > 0:  
        display_end_game(results[0])  # 結果

## +
def time_pause(current_time, elapse):
    while pygame.time.get_ticks() < current_time + elapse:
        pass


init_game()
running = True
while running:
    draw()  # 更新遊戲介面
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
        if is_player_turn(board_matrix) and event.type == pygame.MOUSEBUTTONUP:  
            click_pos = pygame.mouse.get_pos()
            if in_chessboard_area(click_pos):  
                matrix_pos = to_matrix_pos(click_pos)
                make_move(matrix_pos)  
                draw() 
                time_pause(pygame.time.get_ticks(), 100)
                check_winner()  
    if not is_player_turn(board_matrix) and running: 
        ai_make_move()  # AI下棋
        draw()  # 更新遊戲介面
        time_pause(pygame.time.get_ticks(), 100)  
        check_winner()  # 查看是否有人贏