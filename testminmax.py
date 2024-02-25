import numpy as np

class Player:
    def __init__(self, num_stone, num_points):
        self.num_stone = num_stone
        self.num_points = num_points


def game_end(akm):
    return akm < 2


def evaluation(akm, num_points1, num_points2):
    print("  ", num_points1, "  ", num_points2)
    return num_points1 - num_points2


def minimax(akm, num_points1, num_points2, depth, is_maximizing):
    if game_end(akm) or depth == 0:
        return evaluation(akm, num_points1, num_points2), None
    if is_maximizing:
        max_eval = -np.inf
        for ai1_move in [2, 3]:
            num_points1d = num_points1
            num_points2d = num_points2
            if ai1_move > 2 and akm > 2:
                num_points1 += 3
                akm -= 3
            else:
                if akm >= 2:
                    num_points1 += 2
                    akm -= 2
            if akm % 2 == 0 and num_points1 - num_points1d - ai1_move >= 0:
                num_points2 += 2
            if akm % 2 == 1 and num_points1 - num_points1d - ai1_move >= 0:
                num_points1 += 2
            eval, _ = minimax(akm, num_points1, num_points2, depth - 1, False)
            #print("1evaluated  ", eval, "  takes ", ai1_move, "  ", num_points1, "  ", num_points2)
            num_points1 = num_points1d
            num_points2 = num_points2d
            if eval>max_eval:
                ai_move=ai1_move
            max_eval = max(max_eval, eval)

        return max_eval, ai_move
    else:
        min_eval = np.inf
        for ai2_move in [2, 3]:
            num_points1d = num_points1
            num_points2d = num_points2
            if ai2_move > 2 and akm > 2:
                num_points2 += 3
                akm -= 3
            else:
                if akm >= 2:
                    num_points2 += 2
                    akm -= 2
            if akm % 2 == 0 and num_points2 - num_points2d - ai2_move >= 0:
                num_points1 += 2
            if akm % 2 == 1 and num_points2 - num_points2d - ai2_move >= 0:
                num_points2 += 2
            eval, _ = minimax(akm, num_points1, num_points2, depth - 1, True)
            #print("2evaluated  ", eval, "  takes ", ai2_move, "  ", num_points1, "  ", num_points2)
            num_points1 = num_points1d
            num_points2 = num_points2d
            if eval<min_eval:
                ai_move = ai2_move
            min_eval = min(min_eval, eval)

        return min_eval, ai_move

def best_move(akm, num_points1, num_points2, depth, is_maximizing):
    best_eval = -np.inf if is_maximizing else np.inf
    best_move = None
    
    eval,ai_move = minimax(akm, num_points1, num_points2, depth, True)
    
    if eval > best_eval and is_maximizing or eval < best_eval and (not is_maximizing):
        print(best_eval)
        best_eval = eval
        print(best_eval)
        best_move = ai_move
    print(f"AI1: I take {best_move}" if is_maximizing else f"AI2: I take {best_move}")
    return best_move

def main():

    depth = 100
    human = Player(0, 0)
    ai1 = Player(0, 0)
    ai2 = Player(0, 0)
    print("akmenu sk.: ")
    akm = int(input())
    
    while True:
        # ai1_move = int(input())
        ai1_move = best_move(akm, ai1.num_points, ai2.num_points, depth, True)
        if ai1_move > 2 and akm > 2:
            ai1.num_points += 3
            akm -= 3
        else:
            if akm >= 2:
                ai1.num_points += 2
                akm -= 2
        if akm % 2 == 0:
            ai2.num_points += 2
        if akm % 2 == 1:
            ai1.num_points += 2
        print(f"akm: {akm}   Eval: {ai1.num_points - ai2.num_points}")
        print(f"Score:    {ai1.num_points}   {ai2.num_points}")
        if game_end(akm):
            break

        ai2_move = best_move(akm, ai1.num_points, ai2.num_points, depth, False)
        if ai2_move > 2 and akm > 2:
            ai2.num_points += 3
            akm -= 3
        else:
            if akm >= 2:
                ai2.num_points += 2
                akm -= 2
        if akm % 2 == 0:
            ai1.num_points += 2
        if akm % 2 == 1:
            ai2.num_points += 2
        print(f"akm: {akm}   Eval: {ai1.num_points - ai2.num_points}")
        print(f"Score:    {ai1.num_points}   {ai2.num_points}")
        if game_end(akm):
            break
    print(f"Eval: {ai1.num_points - ai2.num_points}")
    print(f"{ai1.num_points}   {ai2.num_points}")
    print("end")
    
if __name__ == "__main__":
    main()
