# 目录

- [效果展示](#效果展示-1)
- [功能浅析](#功能浅析-2)
    - [QTableWidget](#qtablewidget-1)
        - [1. 创建和基本配置](#1-创建和基本配置-1)
        - [2. 添加和修改条目](#2-添加和修改条目-2)
        - [3. 选择管理](#3-选择管理-3)
        - [4. 自定义绘制](#4-自定义绘制-4)
        - [5. 排序和搜索](#5-排序和搜索-5)
        - [6. 拖放支持](#6-拖放支持-6)
        - [代码展示](#代码展示-7)
            - [单元格编译后信号处理](#单元格编译后信号处理-1)
    - [QItemDelegate](#qitemdelegate-2)
        - [1. 绘制项](#1-绘制项-8)
        - [2. 创建编辑器](#2-创建编辑器-9)
        - [3. 设置编辑器数据](#3-设置编辑器数据-10)
        - [4. 获取编辑器数据](#4-获取编辑器数据-11)
        - [5. 更新编辑器几何](#5-更新编辑器几何-12)
        - [demo中使用示例](#demo中使用示例-13)

---
# 效果展示 <a id="效果展示-1"></a>

<iframe width="800" height="510" src="table_widget.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# 功能浅析 <a id="功能浅析-2"></a>
## QTableWidget <a id="qtablewidget-1"></a>
`QTableWidget` 是 Qt 框架中的一个控件，用于显示行列格式的数据。与 `QTableView` 不同，`QTableWidget` 是一个更高级别的、更易于使用的控件，它提供了一个简单的方式来创建和管理表格数据，而不需要设置和配置模型（`QAbstractItemModel`）。`QTableWidget` 适合用于小型或简单的表格数据展示。
### 1. 创建和基本配置 <a id="1-创建和基本配置-1"></a>
- **设置行列数**：使用 `setRowCount(int rows)` 和 `setColumnCount(int columns)` 方法设置表格的行数和列数。

### 2. 添加和修改条目 <a id="2-添加和修改条目-2"></a>
- **添加条目**：使用 `QTableWidgetItem* addItem(int row, int column, QTableWidgetItem::Type type)` 方法添加条目。
- **设置内容**：为每个条目设置文本、图标等，使用 `QTableWidgetItem::setText(const QString &text)` 和 `QTableWidgetItem::setIcon(const QIcon &icon)` 等方法。

### 3. 选择管理 <a id="3-选择管理-3"></a>
- **选择模式**：可以设置单选或多选模式，使用 `setSelectionMode(QAbstractItemView::SelectionMode mode)`。
- **选中项**：使用 `QTableWidgetItem* currentItem()` 和 `QList<QTableWidgetItem*> selectedItems()` 等方法获取当前选中的项。

### 4. 自定义绘制 <a id="4-自定义绘制-4"></a>
- **自定义项绘制**：可以为每个条目自定义绘制，通过重写 `QTableWidgetItem` 的 `paint()` 方法。
- **自定义单元格绘制**
```cpp
QWidget *customWidget = new QWidget; // 创建自定义控件
tableWidget->setCellWidget(row, column, customWidget); // 将控件添加到指定单元格
*********************************
QWidget *widget = new QWidget;
QTableWidgetItem *item = new QTableWidgetItem(widget);
tableWidget->setItem(row, column, item);
*********************************
// 指定某一列单元格使用自定义组件
MyDelegate *delegate = new MyDelegate(parent);
tableWidget->setItemDelegateForColumn(column, delegate);
```
### 5. 排序和搜索 <a id="5-排序和搜索-5"></a>
- **排序**：可以启用表格的排序功能，使用 `setSortingEnabled(bool enable)`。
- **搜索**：实现键盘搜索功能，通过处理 `QTableWidget` 的 `keyPressEvent(QKeyEvent *event)`。

### 6. 拖放支持 <a id="6-拖放支持-6"></a>
- **拖放**：可以启用拖放功能，使用 `setDragEnabled(bool enable)` 和 `setAcceptDrops(bool enable)`。

### 代码展示 <a id="代码展示-7"></a>
#### 单元格编译后信号处理 <a id="单元格编译后信号处理-1"></a>
```cpp
    QObject::connect(ui->tableInfo, &QTableWidget::itemChanged,
                     [&](QTableWidgetItem *item) {
                        // 阻止信号发射以避免递归 (setIcon会再触发itemChanged)
                        ui->tableInfo->blockSignals(true);
                         qDebug() << item->text() << item->type();
                        if (item->type() == MainWindow::ctSex) {
                            QString Sex = item->text();
                            if (Sex=="男")
                                item->setIcon(QIcon(":/images/icons/boy.ico"));
                            else
                                item->setIcon(QIcon(":/images/icons/girl.ico"));
                        }
                        // 恢复信号发射
                        ui->tableInfo->blockSignals(false);
                     });
```
## QItemDelegate <a id="qitemdelegate-2"></a>
`QItemDelegate` 是 Qt 框架中的一个抽象基类，它定义了用于自定义 `QTableView`、`QTableWidget` 或其他项视图控件中项的绘制和编辑行为的接口。通过实现 `QItemDelegate` 的子类，你可以控制项的外观、编辑器的创建、以及用户输入的处理。

以下是 `QItemDelegate` 的主要功能和用法：

### 1. 绘制项 <a id="1-绘制项-8"></a>
`QItemDelegate` 要求你实现 `paint` 方法，该方法用于绘制项视图中的项。

```cpp
void paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const;
```

- **painter**：用于绘制的 `QPainter` 对象。
- **option**：包含绘制选项的 `QStyleOptionViewItem`，如位置、状态、显示区域等。
- **index**：要绘制的项的模型索引。

### 2. 创建编辑器 <a id="2-创建编辑器-9"></a>
当项进入编辑模式时，你需要实现 `createEditor` 方法来创建一个编辑器控件。

```cpp
QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const;
```

- **parent**：编辑器控件的父控件。
- **option**：项的绘制选项。
- **index**：正在编辑的项的模型索引。

### 3. 设置编辑器数据 <a id="3-设置编辑器数据-10"></a>
当编辑器创建后，你需要将模型中的数据设置到编辑器中，这通过实现 `setEditorData` 方法完成。

```cpp
void setEditorData(QWidget *editor, const QModelIndex &index) const;
```

- **editor**：创建的编辑器控件。
- **index**：编辑器要显示数据的模型索引。

### 4. 获取编辑器数据 <a id="4-获取编辑器数据-11"></a>
编辑完成后，需要将编辑器中的更改同步回模型，这通过实现 `setModelData` 方法完成。

```cpp
void setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const;
```

- **editor**：编辑器控件。
- **model**：数据模型。
- **index**：编辑器更改要同步到的模型索引。

### 5. 更新编辑器几何 <a id="5-更新编辑器几何-12"></a>
如果需要，你还可以提供 `updateEditorGeometry` 方法来更新编辑器控件的几何形状。

```cpp
void updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const;
```

### demo中使用示例 <a id="demo中使用示例-13"></a>

```cpp
QWIntSpinDelegate::QWIntSpinDelegate(QObject *parent):QItemDelegate(parent)
{

}

QWidget *QWIntSpinDelegate::createEditor(QWidget *parent,
   const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(option);
    Q_UNUSED(index);

    QSpinBox *editor = new QSpinBox(parent);
    editor->setFrame(false);
    editor->setMinimum(0);
    editor->setMaximum(10000);

    return editor;
}

void QWIntSpinDelegate::setEditorData(QWidget *editor,
                      const QModelIndex &index) const
{
    int value = index.model()->data(index, Qt::EditRole).toInt();

    QSpinBox *spinBox = static_cast<QSpinBox*>(editor);
    spinBox->setValue(value);
}

void QWIntSpinDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
    QSpinBox *spinBox = static_cast<QSpinBox*>(editor);
    spinBox->interpretText();
    int value = spinBox->value();

    model->setData(index, value, Qt::EditRole);
}

void QWIntSpinDelegate::updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(index);
    editor->setGeometry(option.rect);
}

```
