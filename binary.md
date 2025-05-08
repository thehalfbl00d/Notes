START
    found = 0
    while found != 1:
        node = current_node
        if num < node:
            current_node = left
        elif num > node:
            current_node = right
        elif num == node:
            found = 1
            break
END

START
    smallest = current_node
    if smalles < current_node.left:
        smallest = current_node.left
    elif smallest < current_node.right:
        smallest = current_node.right
    elif num == node:
        found = 1
        break
EXIT

findMinimum()
{

}



## DRAW BINARY TREES IN EXAMS AND 