import collections

def process_input():
    m, n = [int(i) for i in input().split()]
    floods = []
    for _ in range(m*n):
        x, y = [int(i) for i in input().split()]
        floods += (x, y),
    return m, n, floods

def solution(m, n, floods):
    def isPossible(day):
        """
        Checks if it is possible to cross the matrix from left to right after floods[1...day] cells have been flooded
        """
        A = [[1 for _ in range(n)] for _ in range(m)]  # initially matrix is filled with only stones
        for i in range(day):
            x, y = floods[i]
            A[x-1][y-1] = 0     # mark flooded cells 
            
        q = collections.deque()
        for i in range(m):
            if A[i][0] == 1:
                q += (i, 0),
                A[i][0] = 0     # visited
                
        while q:
            x, y = q.popleft()
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=i<m and 0<=j<n and A[i][j] == 1:
                    if j == n-1:    # reached other side
                        return True
                    A[i][j] = 0     # visited
                    q += (i, j),
                        
        return False            

    res = 0
    max_days = len(floods)
    lo, hi = 1, max_days
    
    while lo <= hi:
        mid = (lo + hi) >> 1
        if isPossible(mid):
            res = mid 
            lo = mid + 1
        else:
            hi = mid - 1
    
    return res

if __name__ == '__main__':
    print(solution(*process_input()))