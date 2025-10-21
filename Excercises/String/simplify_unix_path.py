class Solution(object):
    def simplifyPath(self, path):
        folders = path.split("/")
        res = ""
        for f in folders:
            if f == "" or f == ".": continue
            if f == "..":
                res = res.rsplit("/", 1)[0]
                continue
            res += "/"
            res += f
        return res if res != "" else "/"
    

""" version 2 more efficient using stack """
class Solution(object):
    def simplifyPath(self, path):
        folders = path.split("/")
        stack = []
        for f in folders:
            if f == "" or f == ".": continue
            if f == "..":
                if stack: stack.pop()
                continue
            stack.append(f)
        res = ""
        for f in stack:
            res += "/"
            res += f 
        return res if res != "" else "/"