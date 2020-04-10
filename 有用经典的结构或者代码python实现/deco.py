class Solution2:
    def can_fill_boats(self, boxes):
        s = sum(boxes)
        r = s % 4
        d = s // 4

        if r == 0:
            return True
        else:
            return False

        # write code here
class Solution:

    def get_ipv4_nums(self, s):

        #bfs
        def dfs(s, segment, res, ip):
            if segment == 4:
                if s == '':
                    res.append(ip[1:])
                    print(res)
                return
            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], segment + 1, res, ip + '.' + s[:i])
                        if s[0] == '0':
                            break

        res = []
        dfs(s, 0, res, '')
        print(len(res))
ss=Solution()
s1="25525511135"
ss.get_ipv4_nums(s1)
