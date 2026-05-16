#返回函数
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))
print("--------------------------")

#dataclass 返回结构化数据
from dataclasses import dataclass
@dataclass
class SearchResult:
    items: list
    total: int
    page: int
def search(keyword):
    return SearchResult(items=["a","b"], total=2, page=0)
r = search("test")
print(r)
print("------------------------")

def append_item(item,result=None):
    if result is None:
        result = []
    result.append(item)
    return result
print("------------------------")

