def tower_of_hanoi(n, source, destination, spare, ):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 
    
    tower_of_hanoi(n - 1, source, spare, destination, ) # this function makes space for the big disk at destination
    print(f"Move disk {n} from {source} to {destination}") # this function moved the big disk to destination
    tower_of_hanoi(n - 1, spare, destination, source, ) # this function moves the small disks to destination

# Example usage
tower_of_hanoi(4, 'A', 'C', 'B')