# 目录

- [效果展示](#效果展示-1)
- [功能浅析](#功能浅析-2)
    - [基础功能](#基础功能-1)
        - [选择器](#选择器-1)
        - [属性](#属性-2)
        - [示例](#示例-3)
        - [伪状态](#伪状态-4)
        - [注意事项](#注意事项-5)
    - [工程应用](#工程应用-2)

---
# 效果展示 <a id="效果展示-1"></a>

<iframe width="1000" height="800" src="qss.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# 功能浅析 <a id="功能浅析-2"></a>
## 基础功能 <a id="基础功能-1"></a>
### 选择器 <a id="选择器-1"></a>

QSS 使用选择器来选择应用样式的控件。以下是一些常见的选择器：

- 类型选择器：选择特定类型的控件，例如 `QPushButton`。
- 类选择器：选择具有特定类名的控件，例如 `.QPushButton`。
- ID 选择器：选择具有特定 ID 的控件，例如 `#myButton`。
- 属性选择器：选择具有特定属性的控件，例如 `[flat="false"]`。
- 后代选择器：选择一个控件的后代控件，例如 `QGroupBox QPushButton`。

### 属性 <a id="属性-2"></a>

QSS 允许您设置多种属性来改变控件的外观。以下是一些常用的 QSS 属性：

- `color`：文本颜色。
- `background-color`：背景颜色。
- `border`：边框样式。
- `font`：字体样式。
- `padding`：内边距。
- `margin`：外边距。
- `spacing`：子控件之间的间距。
- `background-image`：背景图像。
- `border-radius`：边框圆角。

### 示例 <a id="示例-3"></a>

这是一个简单的 QSS 示例，展示了如何改变一个按钮的背景颜色和文本颜色：

```css
QPushButton {
    background-color: blue;
    color: white;
}
```

在这个例子中，所有 `QPushButton` 类型的控件都会变成蓝色背景和白色文本。

### 伪状态 <a id="伪状态-4"></a>

QSS 还支持伪状态，这些是表示控件状态的附加选择器。例如，`:hover` 表示鼠标悬停状态，`:pressed` 表示按下状态。

```css
QPushButton:hover {
    background-color: lightblue;
}
```

在这个例子中，当鼠标悬停在按钮上时，按钮的背景颜色会变成浅蓝色。

### 注意事项 <a id="注意事项-5"></a>

- 并非所有 Qt 控件都支持 QSS 的所有属性。
- QSS 的性能可能不如直接使用 Qt 的绘图 API。
- 在复杂的 UI 中，过度使用 QSS 可能会导致性能问题。

## 工程应用 <a id="工程应用-2"></a>

1. 将通用的 qss 写到文件中添加进资源，可以统一管理。
2. 子控件qss没有设定的话会继承父控件的qss。