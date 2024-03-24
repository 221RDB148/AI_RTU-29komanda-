import time

class Player:
    def __init__(self, num_stone, num_points):
        self.num_stone = num_stone
        self.num_points = num_points


def game_end(akm):
    return akm < 2


def evaluation(akm, num_points1, num_points2):
    #print("  ", num_points1, "  ", num_points2)
    return num_points1 - num_points2


def pointscalc(move, player, akm, num_points1, num_points2): 
    if player == "ai1":
        akmd = akm
        if move > 2 and akm > 2:
            num_points1 += 3
            akmd -= 3
        else:
            if akm >= 2:
                move = 2
                num_points1 += 2
                akmd -= 2
        if akmd % 2 == 0 and move<=akm:
            num_points2 += 2
        if akmd % 2 == 1  and move<=akm:
            num_points1 += 2
        akm = akmd
    else:
        akmd=akm
        if move > 2 and akm > 2:
            num_points2 += 3
            akmd -= 3
        else:
            if akm >= 2:
                move = 2
                num_points2 += 2
                akmd -= 2
        if akmd % 2 == 0  and move<=akm:
            num_points1 += 2
        if akmd % 2 == 1  and move<=akm:
            num_points2 += 2
        akm = akmd
    return num_points1, num_points2, akm

memo = {}  # memoize dict

def minimax(akm, num_points1, num_points2, depth, is_maximizing, alpha, beta): 
    if (akm, num_points1, num_points2, depth, is_maximizing) in memo:
        return memo[(akm, num_points1, num_points2, depth, is_maximizing)] #return eval, ai_move for already visited node

    if game_end(akm) or depth <= 0:
        memo[(akm, num_points1, num_points2, depth, is_maximizing)] = (evaluation(akm, num_points1, num_points2), None) #store gameend nodes
        return evaluation(akm, num_points1, num_points2), None

    if is_maximizing:
        max_eval = -float('inf')
        for ai1_move in [2, 3]:
            num_points1d = num_points1
            num_points2d = num_points2
            akmdd = akm
            num_points1, num_points2, akm = pointscalc(ai1_move, "ai1", akm, num_points1, num_points2)
            eval, _ = minimax(akm, num_points1, num_points2, depth - 1, False, alpha, beta)
            num_points1 = num_points1d
            num_points2 = num_points2d
            akm = akmdd
            if eval > max_eval:
                max_eval = eval
                ai_move = ai1_move
            alpha  = max(alpha , eval)
            if beta <= alpha:
                break
        memo[(akm, num_points1, num_points2, depth, is_maximizing)] = (max_eval, ai_move) #store every visited node
        return max_eval, ai_move
    else:
        min_eval = float('inf')
        for ai2_move in [2, 3]:
            num_points1d = num_points1
            num_points2d = num_points2
            akmdd = akm
            num_points1, num_points2, akm = pointscalc(ai2_move, "ai2", akm, num_points1, num_points2)
            eval, _ = minimax(akm, num_points1, num_points2, depth - 1, True, alpha, beta)
            num_points1 = num_points1d
            num_points2 = num_points2d
            akm = akmdd
            if eval < min_eval:
                min_eval = eval
                ai_move = ai2_move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        memo[(akm, num_points1, num_points2, depth, is_maximizing)] = (min_eval, ai_move) #store every visited node
        return min_eval, ai_move

def best_move(akm, num_points1, num_points2, depth, is_maximizing): 
    start = time.time()
    eval, ai_move = minimax(akm, num_points1, num_points2, depth, is_maximizing, -float('inf'), float('inf'))
    print(f"AI1: I take {ai_move}" if is_maximizing else f"AI2: I take {ai_move}")
    print(f"Time to think: {time.time()-start}")
    print(f"Depth: {depth}")
    return ai_move

def main():
    ai1 = Player(0, 0)
    ai2 = Player(0, 0)
    print("akmenu sk.: ")
    akm = int(input())
    depth = akm/2 #ok for depth to be float, it tops the value anyway
    timetoplay = time.time()
    while True:
        #ai1_move = int(input())
        ai1_move = best_move(akm, ai1.num_points, ai2.num_points, depth, True)
        ai1.num_points, ai2.num_points, akm = pointscalc(ai1_move, "ai1", akm, ai1.num_points, ai2.num_points)
        print(f"akm: {akm}   Eval: {ai1.num_points - ai2.num_points}")
        print(f"Score:    {ai1.num_points}   {ai2.num_points}")
        if game_end(akm):
            break
        depth = akm/2
        ai2_move = best_move(akm, ai1.num_points, ai2.num_points, depth, False)
        ai1.num_points, ai2.num_points, akm = pointscalc(ai2_move, "ai2", akm, ai1.num_points, ai2.num_points)
        print(f"akm: {akm}   Eval: {ai1.num_points - ai2.num_points}")
        print(f"Score:    {ai1.num_points}   {ai2.num_points}")
        if game_end(akm):
            break
    print(f"Eval: {ai1.num_points - ai2.num_points}")
    print(f"{ai1.num_points}   {ai2.num_points}")
    print("end")
    print(f"Time to play: {time.time()-timetoplay}")

if __name__ == "__main__":
    main()


