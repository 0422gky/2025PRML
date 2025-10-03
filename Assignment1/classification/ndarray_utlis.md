`numpy.ndarray` 是 **NumPy** 的核心数据结构，功能非常多。常用操作可以分为几大类：

---

## 1. **创建与基本属性**

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
```

* **属性**：

  * `a.shape` → `(2, 3)` （行列数）
  * `a.ndim` → `2` （维度数）
  * `a.size` → `6` （元素总数）
  * `a.dtype` → `int64` （元素类型）

* **创建**：

  * `np.zeros((2,3))` → 全零数组
  * `np.ones((3,))` → 全 1 数组
  * `np.arange(0, 10, 2)` → `[0,2,4,6,8]`
  * `np.linspace(0,1,5)` → 等间隔 `[0.,0.25,0.5,0.75,1.]`
  * `np.eye(3)` → 单位矩阵

---

## 2. **索引与切片**

```python
a[0, 1]     # 取第0行第1列 → 2
a[:, 1]     # 取所有行的第1列 → [2, 5]
a[0:2, 1:]  # 切片 → [[2,3],[5,6]]
```

* 支持布尔索引：

  ```python
  a[a > 2]  # → [3,4,5,6]
  ```
* 支持花式索引：

  ```python
  a[[0,1],[1,2]]  # → [2,6]
  ```

---

## 3. **形状操作**

```python
a.reshape(3,2)   # 改变形状 → (3,2)
a.flatten()      # 展平成一维
a.T              # 转置
```

* 合并/分割：

  ```python
  np.concatenate([a, a], axis=0)  # 按行拼接
  np.hstack([a, a])               # 按列拼接
  np.vsplit(a, 2)                 # 按行切分
  ```

---

## 4. **运算**

* **逐元素运算**（广播机制）：

  ```python
  a + 1         # 每个元素加 1
  a * 2         # 每个元素乘 2
  np.exp(a)     # 指数
  np.sqrt(a)    # 开方
  ```
* **矩阵运算**：

  ```python
  b = np.array([[1],[2]])
  a.dot(b)   # 矩阵乘法
  ```

---

## 5. **统计函数**

```python
a.sum()          # 总和
a.mean()         # 平均值
a.std()          # 标准差
a.min(), a.max() # 最小值，最大值
a.argmax()       # 最大值索引
a.cumsum()       # 累积和
```

---

## 6. **随机数**

```python
np.random.rand(2,3)     # 均匀分布 (0,1)
np.random.randn(2,3)    # 标准正态分布
np.random.randint(0,10,(2,2))  # 整数
```

---

## 7. **逻辑 & 比较**

```python
(a > 3).sum()         # 大于3的数量
np.all(a > 0)         # 是否所有元素都大于0
np.any(a == 2)        # 是否有等于2的元素
np.unique(a)          # 去重
```

---

✅ 总结一下：

* **属性类**：shape / ndim / dtype
* **索引切片**：普通索引 / 布尔索引 / 花式索引
* **形状操作**：reshape / flatten / transpose / 拼接拆分
* **运算**：逐元素运算 / 矩阵运算
* **统计**：sum / mean / max / argmax / std
* **随机数**：rand / randn / randint
* **逻辑比较**：any / all / unique

---
