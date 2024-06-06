# 目录

- [效果展示](#效果展示-1)
- [功能浅析](#功能浅析-2)
    - [QTextStream](#qtextstream-1)
        - [1. 格式化输出](#1-格式化输出-1)
        - [2. 读写操作](#2-读写操作-2)
        - [3. 字符编码](#3-字符编码-3)
        - [4. 实例化](#4-实例化-4)
        - [5. 设置和查询](#5-设置和查询-5)
        - [主要方法](#主要方法-6)
        - [使用示例](#使用示例-7)
            - [写入文本到文件](#写入文本到文件-1)
            - [从文件读取文本](#从文件读取文本-2)

---
# 效果展示 <a id="效果展示-1"></a>

<iframe width="800" height="520" src="dir_file.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>.

# 功能浅析 <a id="功能浅析-2"></a>
主要展示 文件和目录相关的类的常用函数
## QTextStream <a id="qtextstream-1"></a>
`QTextStream` 是 Qt 框架中的一个类，它提供了一种方便的方式来处理文本输入和输出。`QTextStream` 可以用于多种数据流，包括文件、字符串、以及任何实现了 `QIODevice` 的对象。它支持格式化输入输出操作，使得文本处理变得更加简单和直观。

### 1. 格式化输出 <a id="1-格式化输出-1"></a>
`QTextStream` 可以方便地格式化数字、字符串等数据类型为文本形式，并输出到指定的数据流中。

### 2. 读写操作 <a id="2-读写操作-2"></a>
它支持基本的读写操作，包括插入者（`operator<<`）和提取者（`operator>>`）运算符，可以用于输入和输出。

### 3. 字符编码 <a id="3-字符编码-3"></a>
`QTextStream` 能够处理不同编码的文本数据，例如 UTF-8、Latin-1 等。

### 4. 实例化 <a id="4-实例化-4"></a>
`QTextStream` 可以与各种数据源一起使用，例如：
- `QFile` 对象来处理文件读写。
- `QString` 对象来处理字符串。
- 自定义 `QIODevice` 对象。

### 5. 设置和查询 <a id="5-设置和查询-5"></a>
`QTextStream` 允许你设置和查询流的状态，如字段宽度、填充字符、精度、数字基数（十进制、十六进制等）。

### 主要方法 <a id="主要方法-6"></a>
- `QTextStream(QIODevice *device)`: 创建一个新的 `QTextStream` 对象，关联到指定的 `QIODevice`。
- `void setDevice(QIODevice *device)`: 设置文本流的设备。
- `QIODevice *device() const`: 返回与文本流关联的设备。
- `void setFieldAlignment(QTextStream::FieldAlignment alignment)`: 设置字段对齐方式。
- `void setFieldWidth(int width)`: 设置字段宽度。
- `void setNumberFlags(QTextStream::NumberFlags flags)`: 设置数字格式标志。
- `void setRealNumberPrecision(int precision)`: 设置浮点数的精度。
- `QTextCodec *codec() const`: 获取当前使用的字符编码。

### 使用示例 <a id="使用示例-7"></a>
以下是如何使用 `QTextStream` 来读写文本的示例：

#### 写入文本到文件 <a id="写入文本到文件-1"></a>
```cpp
QFile file("example.txt");
if (file.open(QIODevice::WriteOnly | QIODevice::Text)) {
    QTextStream out(&file);
    out << "This is a test" << endl;
    out << 123 << " is a number" << endl;
    file.close();
}
```

#### 从文件读取文本 <a id="从文件读取文本-2"></a>
```cpp
QFile file("example.txt");
if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
    QTextStream in(&file);
    QString line;
    while (in.readLineInto(&line)) {
        qDebug() << line;
    }
    file.close();
}
```