SPECIALS = {
    'quot': '"',
    'apos': "'",
    'amp': '&',
    'gt': '>',
    'lt': '<',
    'frasl': '/',
}


class Solution:
    def entityParser(self, text: str) -> str:
        it = iter(text)
        res = ''
        while True:
            try:
                c = next(it)
            except StopIteration:
                break
            if c == '&':
                special = ''
                while True:
                    c = next(it)
                    if c == ';':
                        break
                    special += c
                special_ = SPECIALS.get(special)
                res += special_ or f"&{special};"
            else:
                res += c
        return res


print(Solution().entityParser(text="&amp; is an HTML entity but &ambassador; is not."))
print(Solution().entityParser(text="and I quote: &quot;...&quot;"))
print(Solution().entityParser(text="Stay home! Practice on Leetcode :)"))
