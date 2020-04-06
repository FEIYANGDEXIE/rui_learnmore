class Solution:
    def VerifySquenceOfBST(self, sequence):

        # write code here
        def bt(s):
            # print(s)

            if len(s) > 1:
                sep = s[-1]

                for i in range(len(s) - 1):
                    if s[i] > sep:
                        sep_index = i
                        break
                # print('s',sep_index)
                try:
                    for i in range(sep_index, len(s) - 1):
                        if s[i] < sep:
                            lab[0] = 1
                    bt(s[:sep_index])
                    bt(s[sep_index:len(s) - 1])
                except:
                    bt(s[:len(s) - 1])

        lab = [0]
        bt(sequence)
        # print(lab)
        if lab[0] == 1:
            return False
        else:
            return True

a=Solution()
a.VerifySquenceOfBST([4,6,7,5])