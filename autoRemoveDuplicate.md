### Why duplicates are removed automatically in **set**?

In Python:

* A **set** is an *unordered collection* of **unique elements**.
* Internally, Python stores set elements using **hashing**.

👉 So when you write:

```python
unique_num = {1, 2, 2, 3}
print(unique_num)
```

Steps happening:

1. `1` → added to set.
2. `2` → added first time.
3. `2` again → Python checks its **hash**. It’s already present, so it **ignores** the duplicate.
4. `3` → added.

✅ Output:

```
{1, 2, 3}
```

---

### Another Example

```python
s = set([10, 20, 20, 30, 10])
print(s)
```

Output:

```
{10, 20, 30}
```

---

🔑 **Key Point**:
A `set` only keeps **unique elements**.
If you try to add the same element multiple times, it will only appear once.

---

**short comparison of list vs tuple vs set vs dict** (all built-in collections)
