class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # 初始化需要的字符计数器
        required_chars = collections.Counter(t)
        # 统计需要的字符总数
        required_count = len(t)
        # 初始化左右指针
        left = 0
        min_length = float('inf')
        min_window = ""

        for right, char in enumerate(s):
            # 如果当前字符在所需字符中，则更新所需字符计数器
            if char in required_chars:
                if required_chars[char] > 0:
                    required_count -= 1
                required_chars[char] -= 1

            # 当窗口包含所有所需字符时，尝试缩小左边界
            while required_count == 0:
                # 更新最小窗口
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]

                # 如果左边界字符是所需字符，则更新所需字符计数器
                if s[left] in required_chars:
                    required_chars[s[left]] += 1
                    if required_chars[s[left]] > 0:
                        required_count += 1

                # 移动左边界
                left += 1

        return min_window
