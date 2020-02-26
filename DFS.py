


def dfs(adj,s):
    visited = set()
    stack = [s]
    visited.add(s)
    while stack:
        v=stack.pop()
        for i in range(0, len(adj[v])):
            w = adj[v][i]
            if w not in visited:
                stack.append(w)
                visited.add(w)
    return visited

adj=dict([('r', ['s','v']), ('v', ['r']), ('s', ['r']), ('w', ['t','x']), ('t', ['w','x','u']),
          ('x', ['w','t','u','y']),('u', ['t','x','y']),('y', ['u','x'])])
print(dfs(adj,'w'))

