# Data Types

Xác định kiểu của một đối tượng bằng hàm `type()`.

`type(object, bases, dict)`

* `object`: Bắt buộc. Nếu chỉ truyền một tham số, `type()` sẽ trả về kiểu của đối tượng.
* `bases`: Tùy chọn. Xác định các lớp cơ sở. //TODO
* `dict`: Tùy chọn. Xác định namespace chứa định nghĩa của lớp. //TODO

# Example

```python
print(type('Asabeneh'))   # str
print(type(10))           # int
print(type(3.14))         # float
print(type(True))         # bool
print(type([1, 2, 3, 4])) # list

# TODO: update later
```
