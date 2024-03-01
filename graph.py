import matplotlib.pyplot as plt
        
class TreeNode:
    def __init__(self, value, geval, player):
        self.value = value
        self.geval = geval
        self.player = player
        self.left = None
        self.right = None

def create_binary_tree(root_value):
    root = TreeNode(root_value)
    stack = [root]
    
    while stack:
        current_node = stack.pop(0)
        if current_node.value > 1:
            left_value = current_node.value - 2
            right_value = current_node.value - 3
            
            # Skip negative values
            if left_value >= 0:
                current_node.left = TreeNode(left_value)
                stack.append(current_node.left)
            if right_value >= 0:
                current_node.right = TreeNode(right_value)
                stack.append(current_node.right)
    return root

def binarytree_pointscalc(player, move, akm, geval): #copy of the pointscalc with eval instead of individual points
    if player == "ai1":
        akmd = akm
        if move > 2 and akm > 2:
            geval += 3
            akmd -= 3
        else:
            if akm >= 2:
                move = 2
                geval += 2
                akmd -= 2
        if akmd % 2 == 0 and move<=akm:
            geval -= 2
        if akmd % 2 == 1  and move<=akm:
            geval += 2
        #akm = akmd
    else:
        akmd=akm
        if move > 2 and akm > 2:
            geval -= 3
            akmd -= 3
        else:
            if akm >= 2:
                move = 2
                geval -= 2
                akmd -= 2
        if akmd % 2 == 0  and move<=akm:
            geval += 2
        if akmd % 2 == 1  and move<=akm:
            geval -= 2
        #akm = akmd
    return geval
   
def create_binary_tree_eval(root_value):
    player = "ai1"
    root = TreeNode(root_value,0,player)
    stack = [root]
    geval = 0
    akm = root_value
    while stack:
        current_node = stack.pop(0)
        if current_node.value > 1:
            left_value = current_node.value - 2
            right_value = current_node.value - 3
            move = 2
            if current_node.player == "ai1":
                left_player = "ai2" 
                right_player = "ai2" 
            else:
                left_player = "ai1"
                right_player = "ai1" 

            if left_value >= 0:
                current_node.left = TreeNode(left_value, binarytree_pointscalc(current_node.player, 2, left_value+2, current_node.geval), left_player)
                stack.append(current_node.left)
            if right_value >= 0:
                current_node.right = TreeNode(right_value, binarytree_pointscalc(current_node.player, 3, right_value+3, current_node.geval), right_player)
                stack.append(current_node.right)
    return root
  
def plot_tree(root, x=0, y=0, spacing=20, ax=None):

    if ax is None:
        fig, ax = plt.subplots()
    if root:
        ax.plot(x, y, 'o', color='red')
        ax.text(x-1.8, y-5, f"{root.geval}", verticalalignment='top', horizontalalignment='center')
        ax.text(x+1.8, y-5, f"{root.value}", verticalalignment='top', horizontalalignment='center', color='g',alpha=0.8)
        
        if root.left:
            ax.plot([x, x-spacing], [y-spacing, y-50], color='black',alpha=0.1)
            plot_tree(root.left, x-spacing, y-50, spacing/2, ax)
        if root.right:
            ax.plot([x, x+spacing], [y-spacing, y-50], color='black',alpha=0.1)
            plot_tree(root.right, x+spacing, y-50, spacing/2, ax)
    ax.axis('off')

def main():
    depth = 100
    print("akmenu sk.: ")
    akm = int(input())
    
    root = create_binary_tree_eval(akm)

    plot_tree(root)
    plt.show()

if __name__ == "__main__":
    main()
    
