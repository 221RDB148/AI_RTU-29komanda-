import time

class Player: # player have stones and points, stones happen to be useless (cuz in the end points = stones) but is used for gui :)
    def __init__(self, num_stone, num_points):
        self.num_stone = num_stone
        self.num_points = num_points


def game_end(akm): #game is ending if there are no more possible moves
    return akm < 2


def evaluation(akm, num_points1, num_points2): #get heuristics score
    return num_points1 - num_points2


def pointscalc(move, player, akm, num_points1, num_points2): #calc children node for parent who asked it
    if player == "ai1": #check who made a move. players ane both named ai but who cares anyway
        if move > 2 and akm > 2: #if move is 3, [move > 2, else] covers every possible numeric input in program version without ui
            move = 3
            num_points1 += 3
            akm -= 3
        else: #if move is 2
            if akm >= 2:
                move = 2
                num_points1 += 2
                akm -= 2
        if akm % 2 == 0: #check if odd, also extra check if move is legal
            num_points2 += 2
        if akm % 2 == 1 :
            num_points1 += 2
    else: #same thing for player 2
        if move > 2 and akm > 2:
            move = 3
            num_points2 += 3
            akm -= 3
        else:
            if akm >= 2:
                move = 2
                num_points2 += 2
                akm -= 2
        if akm % 2 == 0:
            num_points1 += 2
        if akm % 2 == 1:
            num_points2 += 2
    return akm, num_points1, num_points2

memo = {}  # we store every minimax return values (incl. heuristic eval) in dictionary to check if game state that minimax was called with was already met before

def minimax(akm, num_points1, num_points2, depth, is_maximizing, alpha, beta): 
    if (akm, num_points1, num_points2, depth, is_maximizing) in memo:
        return memo[(akm, num_points1, num_points2, depth, is_maximizing)] #return eval, ai_move for already visited node

    if game_end(akm) or depth == 0:
        memo[(akm, num_points1, num_points2, depth, is_maximizing)] = (evaluation(akm, num_points1, num_points2), None) #store gameend nodes with eval
        return evaluation(akm, num_points1, num_points2), None

    if is_maximizing:
        max_eval = -float('inf')
        for ai1_move in [2, 3]: #moves 2 and 3 possible, check which one is better
            #minimax function expects (akm, num_points1, num_points2, depth, is_maximizing, alpha, beta), by doing *pointscalc(ai1_move, "ai1", akm, num_points1, num_points2) inside minimax below we give the minimax "akm, num_points1, num_points2" part returned by pointscalc
            eval, _ = minimax(*pointscalc(ai1_move, "ai1", akm, num_points1, num_points2), depth - 1, False, alpha, beta)  # * operator in python unpacks tuple, this way we dont store pointscalc function return values, but directly pass them to minimax, i only implemented this today
            if eval > max_eval: #minimax
                max_eval = eval
                ai_move = ai1_move
            alpha  = max(alpha , eval)
            if beta <= alpha: #alpha-beta, test terminal version of alpha-beta and minimax to compare total time to play for ai vs ai, for 70 akm alphabeta is 1.8-2 times faster than minimax
                break
        memo[(akm, num_points1, num_points2, depth, is_maximizing)] = (max_eval, ai_move) #store every visited node
        return max_eval, ai_move #returns best heuristics and best move for best_move function
    else: #minimizing
        min_eval = float('inf')
        for ai2_move in [2, 3]:
            eval, _ = minimax(*pointscalc(ai2_move, "ai2", akm, num_points1, num_points2), depth - 1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                ai_move = ai2_move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        memo[(akm, num_points1, num_points2, depth, is_maximizing)] = (min_eval, ai_move) #store every visited node
        return min_eval, ai_move 

def best_move(akm, num_points1, num_points2, depth, is_maximizing): #it exists to initialize minimax and evaluate total time to make the best move, it prints stuff when done minimaxing and returns best move to take
    start = time.time()
    eval, ai_move = minimax(akm, num_points1, num_points2, depth, is_maximizing, -float('inf'), float('inf'))
    print(f"AI1: I take {ai_move}" if is_maximizing else f"AI2: I take {ai_move}")
    print(f"Time to think: {time.time()-start}") #if Time to think: 0.0 that probably means node was visited before by minimax in early game!
    return ai_move 

def main():
    ai1 = Player(0, 0)
    ai2 = Player(0, 0)
    print("akmenu sk.: ")
    akm = int(input()) #input stones in terminal version of the game
    depth = 1000000
    timetoplay = time.time() #checks how much time it took to play (useful for ai vs ai)
    while True:
        #ai1_move = int(input()) #uncomment this and comment out the line below to play player1 as a human
        ai1_move = best_move(akm, ai1.num_points, ai2.num_points, depth, True)
        akm, ai1.num_points, ai2.num_points = pointscalc(ai1_move, "ai1", akm, ai1.num_points, ai2.num_points) #calc points for taken move
        print(f"akm: {akm}   Eval: {ai1.num_points - ai2.num_points}") #prints heuristic evaluation after taken move
        print(f"Score:    {ai1.num_points}   {ai2.num_points}")
        if game_end(akm): #check if no stones to take anymore
            break
        #ai2_move = int(input()) #uncomment this and comment out the line below to play player2 as a human
        ai2_move = best_move(akm, ai1.num_points, ai2.num_points, depth, False)
        akm, ai1.num_points, ai2.num_points = pointscalc(ai2_move, "ai2", akm, ai1.num_points, ai2.num_points)
        print(f"akm: {akm}   Eval: {ai1.num_points - ai2.num_points}")
        print(f"Score:    {ai1.num_points}   {ai2.num_points}")
        if game_end(akm): #check if no stones to take anymore
            break
    print(f"Eval: {ai1.num_points - ai2.num_points}") #prints at the end of the game
    print(f"{ai1.num_points}   {ai2.num_points}")
    print("end")
    print(f"Time to play: {time.time()-timetoplay}")

if __name__ == "__main__":
    main()


