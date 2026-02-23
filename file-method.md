# Writelines

`writelines()` dùng để ghi nhiều dòng vào file.

## Cú pháp

`file.writelines(iterable)`

* `iterable`: iterable chứa các chuỗi cần ghi.

## Ví dụ

```python
lines = ["Learn Python\n", "Read book\n", "Exercise\n"]

file = open("todos.txt", "w")
file.writelines(lines)
file.close()
```
