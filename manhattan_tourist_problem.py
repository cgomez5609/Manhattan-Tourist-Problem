import numpy as np

def get_values(rosalind_file):
    """
    Function that extracts the necessary data from .txt Rosalind
    file to convert to the following:
        n: number of vertical values
        m: number of horizontal values
        vert: Matrix of vertical values
        hori: Matrix of horizontal values
    """
    # Read in file and assign n and m values
    f = open(rosalind_file, 'r')
    content = f.readline().split()
    n = int(content[0])
    m = int(content[1])
    
    values = []
    for i in f:
        values.append(i)
    
    new_list = []
    for i in values:
        new_list.append(i.strip())
        
    # index of of the '-' that separates matrices
    dash = new_list.index('-')
    
    # Creation of two matrices 
    x = []
    y = []
    for line in range(len(new_list)):
        if line < dash:
            x.append(values[line].split())
        elif line > dash:
            y.append(values[line].split())
      
    #Converting all values to integer data types
    vert = np.array(x)
    vert = vert.astype(int)
    hori = np.array(y)
    hori = hori.astype(int)
    
    return n, m, vert, hori

def length_of_longest_path(n, m, vert, hori, arr):
    """
    Takes in 5 parameters:
        n: number of vertical values
        m: number of horizontal values
        vert: Matrix of vertical values
        hori: Matrix of horizontal values
        arr: newly created 2D array that must be a n+1 * m+1!
    Calculates longest path for Manhattan Tourist Problem. To begin with, 
    calculates the first row and column, then calculates the remaining values.
    """
    # Get the values for the first vertical and horizonal lines
    for i in range(1,n+1):
        arr[i][0] = arr[i-1][0] + vert[i-1][0] 
    for j in range(1, m+1):
        arr[0][j] = arr[0][j-1] + hori[0][j-1]          
        
    # Get values of the remaining rows and columns
    for i in range(1, n+1):
        for j in range(1, m+1): 
            if (arr[i-1][j] + vert[i-1][j]) > (arr[i][j-1] + hori[i][j-1]):
                arr[i][j] = arr[i-1][j] + vert[i-1][j]
            else:
                arr[i][j] = arr[i][j-1] + hori[i][j-1]

def main():
    file = 'manhat_tour.txt'
    n,m,vert,hori = get_values(file)
    
    # Creation of a n+1 * m+1 array using numpy
    arr = np.zeros((n+1, m+1))
    
    length_of_longest_path(n, m, vert, hori, arr)
       
    # convert to int from float
    print(int(arr[n][m]))


if __name__ == "__main__":
    main()