# 目录

- [效果展示](#效果展示-1)
- [功能浅析](#功能浅析-2)
    - [QTableView](#qtableview-1)
        - [1. 数据模型](#1-数据模型-1)
        - [2. 项的选择](#2-项的选择-2)
        - [3. 编辑功能](#3-编辑功能-3)
        - [4. 项的绘制](#4-项的绘制-4)
        - [5. 性能](#5-性能-5)
        - [6. 排序和搜索](#6-排序和搜索-6)
        - [7. 自定义行为](#7-自定义行为-7)
    - [QItemDelegate](#qitemdelegate-2)
        - [1. 自定义绘制](#1-自定义绘制-8)
        - [2. 创建编辑器](#2-创建编辑器-9)
        - [3. 设置编辑器数据](#3-设置编辑器数据-10)
        - [4. 获取编辑器数据](#4-获取编辑器数据-11)
        - [5. 更新编辑器几何](#5-更新编辑器几何-12)
        - [6. 尺寸提示](#6-尺寸提示-13)
        - [使用示例](#使用示例-14)
    - [QStandardItemModel](#qstandarditemmodel-3)
        - [插入行和列](#插入行和列-15)
        - [删除行和列](#删除行和列-16)
        - [获取行和列的数量](#获取行和列的数量-17)
        - [其他重要方法](#其他重要方法-18)
        - [使用示例](#使用示例-19)
    - [QItemSelectionModel](#qitemselectionmodel-4)
        - [1. 选择跟踪](#1-选择跟踪-20)
        - [2. 选择模式](#2-选择模式-21)
        - [3. 选择管理](#3-选择管理-22)
        - [4. 信号和槽](#4-信号和槽-23)
        - [5. 主要方法](#5-主要方法-24)
        - [6. 查询选择](#6-查询选择-25)
        - [7. 与视图控件的集成](#7-与视图控件的集成-26)
    - [QStandardItem](#qstandarditem-5)
        - [1. 构造函数](#1-构造函数-27)
        - [2. 文本和数据](#2-文本和数据-28)
        - [3. 图标](#3-图标-29)
        - [4. 编辑](#4-编辑-30)
        - [5. 选择状态](#5-选择状态-31)
        - [6. 工具提示](#6-工具提示-32)
        - [7. 拖放](#7-拖放-33)
        - [8. 子项管理](#8-子项管理-34)
        - [9. 项类型](#9-项类型-35)
        - [10. 检查状态](#10-检查状态-36)
        - [使用示例](#使用示例-37)
    - [代码解析](#代码解析-6)
        - [1.创建模型](#1-创建模型-38)
        - [2.设置每列的代理](#2-设置每列的代理-39)
        - [3.从文件中读取model](#3-从文件中读取model-40)
        - [4.将选中表格文字居左显示](#4-将选中表格文字居左显示-41)

---
# 效果展示 <a id="效果展示-1"></a>

<iframe width="800" height="500" src="model_view.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# 功能浅析 <a id="功能浅析-2"></a>
## QTableView <a id="qtableview-1"></a>
`QTableView` 是 Qt 框架中的一个控件，它提供了一个表格视图界面，用于显示和编辑二维数据集。`QTableView` 是 `QAbstractItemView` 的一个子类，通过与 `QAbstractItemModel` 的实例相连，提供了一种灵活的方式来展示和处理表格数据。

以下是 `QTableView` 的一些关键特性和使用方法：

### 1. 数据模型 <a id="1-数据模型-1"></a>
`QTableView` 使用 `QAbstractItemModel` 或其子类作为数据模型，模型负责存储数据并提供给视图显示。数据模型定义了表格中的行、列和单元格数据。

### 2. 项的选择 <a id="2-项的选择-2"></a>
`QTableView` 支持用户通过鼠标或键盘选择一个或多个单元格、行或列。支持的选项包括是否允许多选、选择行或列等。

### 3. 编辑功能 <a id="3-编辑功能-3"></a>
`QTableView` 支持编辑单元格数据。当用户双击某个单元格或按下 `F2` 键时，可以进入编辑模式。

### 4. 项的绘制 <a id="4-项的绘制-4"></a>
`QTableView` 使用 `QItemDelegate` 来绘制单元格。你可以通过设置自定义的委托来改变单元格的绘制方式。

### 5. 性能 <a id="5-性能-5"></a>
`QTableView` 针对大数据集进行了性能优化，支持虚拟滚动和按需绘制，可以高效地处理大量数据。

### 6. 排序和搜索 <a id="6-排序和搜索-6"></a>
`QTableView` 支持对列进行排序，并且可以启用搜索功能，允许用户快速查找数据。

### 7. 自定义行为 <a id="7-自定义行为-7"></a>
通过重写 `QTableView` 的事件处理函数，如 `keyPressEvent`、`mousePressEvent` 等，可以自定义键盘和鼠标事件的处理。
## QItemDelegate <a id="qitemdelegate-2"></a>
`QItemDelegate` 是 Qt 框架中的一个类，用于自定义 `QTableView`、`QTreeView`、`QListWidget`、`QTableWidget` 等项视图控件中项的绘制和编辑行为。`QItemDelegate` 作为代理，允许开发者控制每个项的外观和用户交互方式，而不需要修改视图控件本身的代码。

以下是 `QItemDelegate` 的一些关键特性：

### 1. 自定义绘制 <a id="1-自定义绘制-8"></a>
通过重写 `QItemDelegate` 的 `paint` 方法，可以自定义每个项的绘制方式。这使得开发者能够根据需要绘制文本、图标、复选框等。

```cpp
void paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const override;
```

### 2. 创建编辑器 <a id="2-创建编辑器-9"></a>
当用户开始编辑某个项时，`QItemDelegate` 的 `createEditor` 方法会被调用，以创建一个用于编辑的控件。

```cpp
QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option, const QModelIndex &index) const override;
```

### 3. 设置编辑器数据 <a id="3-设置编辑器数据-10"></a>
在编辑器创建后，`setEditorData` 方法用于将模型中的数据设置到编辑器控件中。

```cpp
void setEditorData(QWidget *editor, const QModelIndex &index) const override;
```

### 4. 获取编辑器数据 <a id="4-获取编辑器数据-11"></a>
当编辑完成，`setModelData` 方法用于将编辑器控件中的更改同步回模型。

```cpp
void setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const override;
```

### 5. 更新编辑器几何 <a id="5-更新编辑器几何-12"></a>
`updateEditorGeometry` 方法可以根据当前项的几何形状更新编辑器控件的几何形状。

```cpp
void updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index) const override;
```

### 6. 尺寸提示 <a id="6-尺寸提示-13"></a>
`sizeHint` 方法提供了一个机会来自定义每个项的尺寸，这对于调整列宽或行高非常有用。

```cpp
QSize sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const override;
```

### 使用示例 <a id="使用示例-14"></a>
```cpp
class CustomDelegate : public QItemDelegate {
public:
    void paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const override {
        // 绘制自定义背景颜色
        QBrush brush = option.state & QStyle::State_Selected ? Qt::red : Qt::blue;
        painter->fillRect(option.rect, brush);

        // 绘制文本
        painter->drawText(option.rect, Qt::AlignCenter, index.data(Qt::DisplayRole).toString());
    }
};
```
## QStandardItemModel <a id="qstandarditemmodel-3"></a>
`QStandardItemModel` 是 Qt 框架中用于管理项的模型，它提供了一系列的功能来操作模型中的行和列。以下是 `QStandardItemModel` 的一些关键方法，用于插入、删除行列以及获取行列数量：

### 插入行和列 <a id="插入行和列-15"></a>
- `insertRows(int row, int count, const QModelIndex &parent = QModelIndex())`: 在指定的行位置插入若干行。
- `insertColumns(int column, int count, const QModelIndex &parent = QModelIndex())`: 在指定的列位置插入若干列。

### 删除行和列 <a id="删除行和列-16"></a>
- `removeRows(int row, int count, const QModelIndex &parent = QModelIndex())`: 从指定的行位置删除若干行。
- `removeColumns(int column, int count, const QModelIndex &parent = QModelIndex())`: 从指定的列位置删除若干列。

### 获取行和列的数量 <a id="获取行和列的数量-17"></a>
- `rowCount(const QModelIndex &parent = QModelIndex()) const`: 获取模型中的行数。
- `columnCount(const QModelIndex &parent = QModelIndex()) const`: 获取模型中的列数。

### 其他重要方法 <a id="其他重要方法-18"></a>
- `setItem(int row, int column, QStandardItem *item)`: 在指定位置放置一个项。
- `setItemRoleForRow(int row, int role, const QVariant &value)`: 为一行设置特定角色的值。
- `setItemRoleForColumn(int column, int role, const QVariant &value)`: 为一列设置特定角色的值。
- `data(const QModelIndex &index, int role = Qt::DisplayRole) const`: 获取指定索引项的数据。
- `setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole)`: 设置指定索引项的数据。

### 使用示例 <a id="使用示例-19"></a>
以下是如何使用 `QStandardItemModel` 插入和删除行列的示例：

```cpp
QStandardItemModel *model = new QStandardItemModel(4, 3); // 初始化4行3列的模型

// 插入两行
model->insertRows(2, 2); // 在索引2的位置插入两行

// 插入三列
model->insertColumns(1, 3); // 在索引1的位置插入三列

// 删除一行
model->removeRows(0, 1); // 删除第一行

// 删除一列
model->removeColumns(0, 1); // 删除第一列

// 获取行数和列数
int rows = model->rowCount();
int columns = model->columnCount();
```
## QItemSelectionModel <a id="qitemselectionmodel-4"></a>
`QItemSelectionModel` 是 Qt 框架中的一个类，它提供了一个用于管理和跟踪项视图（如 `QTableView`、`QTreeView`、`QListWidget` 等）中当前选中项的模型。这个模型是可选的，并且可以与任何实现了 `QAbstractItemView` 的视图控件一起使用。

以下是 `QItemSelectionModel` 的一些关键特性：

### 1. 选择跟踪 <a id="1-选择跟踪-20"></a>
`QItemSelectionModel` 跟踪用户或程序代码所做的选择，并提供接口来查询当前的选择。

### 2. 选择模式 <a id="2-选择模式-21"></a>
- **单选**：一次只能选择一个项。
- **多选**：可以同时选择多个项。
- **无选择**：不允许选择任何项。

### 3. 选择管理 <a id="3-选择管理-22"></a>
`QItemSelectionModel` 允许你添加或删除单个项、行、列或多个项的范围到当前选择中。

### 4. 信号和槽 <a id="4-信号和槽-23"></a>
`QItemSelectionModel` 发出以下信号：
- `selectionChanged(const QItemSelection &selected, const QItemSelection &deselected)`：当选择发生变化时发出。
- `currentChanged(const QModelIndex &current, const QModelIndex &previous)`：当当前项发生变化时发出。

### 5. 主要方法 <a id="5-主要方法-24"></a>
- `select(const QModelIndex &index, QItemSelectionModel::SelectionFlags command)`：根据指定的命令选择或反选一个项。
- `clear()`：清除当前的选择。
- `columnSelect(int column, QItemSelectionModel::SelectionFlags command)`：选择或反选某一列中的所有项。
- `rowSelect(int row, QItemSelectionModel::SelectionFlags command)`：选择或反选某一行中的所有项。
- `clearCurrent()`：清除当前项。

### 6. 查询选择 <a id="6-查询选择-25"></a>
- `selectedIndexes() const`：返回当前选中的所有项的索引列表。
- `hasSelection() const`：检查是否有项被选中。

### 7. 与视图控件的集成 <a id="7-与视图控件的集成-26"></a>
`QItemSelectionModel` 通常由视图控件（如 `QTableView`）创建和管理。视图控件负责创建选择模型，并将其与自身的选择行为集成。

## QStandardItem <a id="qstandarditem-5"></a>
`QStandardItem` 类提供了一系列的方法来创建和管理表格或列表中的项。以下是一些常用的 `QStandardItem` 相关函数及其简要介绍：

### 1. 构造函数 <a id="1-构造函数-27"></a>
- `QStandardItem(const QString &text = QString())`: 创建一个带有指定文本的新项。
- `QStandardItem(int rows, int columns)`: 创建一个具有指定行数和列数的新项。

### 2. 文本和数据 <a id="2-文本和数据-28"></a>
- `setText(const QString &text)`: 设置项的显示文本。
- `text() const`: 获取项的显示文本。
- `setData(int role, const QVariant &value)`: 为指定的角色设置项的数据。
- `data(int role) const`: 根据指定的角色获取项的数据。

### 3. 图标 <a id="3-图标-29"></a>
- `setIcon(const QIcon &icon)`: 设置项的图标。
- `icon() const`: 获取项的图标。

### 4. 编辑 <a id="4-编辑-30"></a>
- `setEditable(bool editable)`: 设置项是否可编辑。
- `isEditable() const`: 检查项是否可编辑。

### 5. 选择状态 <a id="5-选择状态-31"></a>
- `setSelected(bool select)`: 设置项是否被选中。
- `isSelected() const`: 检查项是否被选中。

### 6. 工具提示 <a id="6-工具提示-32"></a>
- `setToolTip(const QString &toolTip)`: 设置项的工具提示文本。
- `toolTip() const`: 获取项的工具提示文本。

### 7. 拖放 <a id="7-拖放-33"></a>
- `setDragEnabled(bool enable)`: 设置项是否支持拖动。
- `setDropEnabled(bool enable)`: 设置项是否支持放置。

### 8. 子项管理 <a id="8-子项管理-34"></a>
- `appendRow(QStandardItem *item)`: 在项的末尾添加一行子项。
- `insertRow(int row, QStandardItem *item)`: 在指定位置插入一行子项。
- `removeRow(int row)`: 删除指定行的子项。
- `child(int row) const`: 获取指定行的子项。

### 9. 项类型 <a id="9-项类型-35"></a>
- `type() const`: 获取项的类型。

### 10. 检查状态 <a id="10-检查状态-36"></a>
- `setCheckState(Qt::CheckState state)`: 设置项的复选框状态。
- `checkState() const`: 获取项的复选框状态。

### 使用示例 <a id="使用示例-37"></a>
以下是如何使用 `QStandardItem` 的一些方法的示例：

```cpp
QStandardItemModel *model = new QStandardItemModel();

// 创建一个标准项
QStandardItem *item = new QStandardItem("Example Item");
item->setIcon(QIcon(":/icons/example.png")); // 设置图标
item->setEditable(false); // 设置为不可编辑
item->setToolTip("This is an example item."); // 设置工具提示

// 设置数据
item->setData(123, Qt::UserRole); // 设置用户自定义角色的数据

// 检查复选框状态
item->setCheckState(Qt::Checked);

// 将项添加到模型
model->setItem(0, 0, item);
```
## 代码解析 <a id="代码解析-6"></a>
### 1.创建模型 <a id="1-创建模型-38"></a>
```cpp
theModel = new QStandardItemModel(2,FixedColumnCount,this); //创建数据模型
theSelection = new QItemSelectionModel(theModel);//Item选择模型
connect(theSelection,SIGNAL(currentChanged(QModelIndex,QModelIndex)),
        this,SLOT(on_currentChanged(QModelIndex,QModelIndex)));

//为tableView设置数据模型
ui->tableView->setModel(theModel); //设置数据模型
ui->tableView->setSelectionModel(theSelection);//设置选择模型
```
### 2.设置每列的代理 <a id="2-设置每列的代理-39"></a>
```cpp

class QWComboBoxDelegate : public QItemDelegate
{
    Q_OBJECT

public:
    QWComboBoxDelegate(QObject *parent=0);

    //自定义代理组件必须继承以下4个函数
    QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option,
                          const QModelIndex &index) const Q_DECL_OVERRIDE;

    void setEditorData(QWidget *editor, const QModelIndex &index) const Q_DECL_OVERRIDE;
    void setModelData(QWidget *editor, QAbstractItemModel *model,
                      const QModelIndex &index) const Q_DECL_OVERRIDE;
    void updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option,
                              const QModelIndex &index) const Q_DECL_OVERRIDE;
};
//为各列设置自定义代理组件
ui->tableView->setItemDelegateForColumn(0,&intSpinDelegate);  //测深，整数
ui->tableView->setItemDelegateForColumn(1,&floatSpinDelegate);  //浮点数
ui->tableView->setItemDelegateForColumn(2,&floatSpinDelegate); //浮点数
ui->tableView->setItemDelegateForColumn(3,&floatSpinDelegate); //浮点数
ui->tableView->setItemDelegateForColumn(4,&comboBoxDelegate); //Combbox选择型
```
### 3.从文件中读取model <a id="3-从文件中读取model-40"></a>
```cpp
void MainWindow::iniModelFromStringList(QStringList& aFileContent)
{ //从一个StringList 获取数据，初始化Model
    int rowCnt=aFileContent.count(); // 第1行是标题头，
    theModel->setRowCount(rowCnt-1); //数据行数

    QString header,aLineText;
    QStandardItem   *aItem;
    QStringList     headerList,tmpList;

//设置表头
    header=aFileContent.at(0);//第1行是表头
//    headerList=header.split(QRegExp("\\s+"),QString::SkipEmptyParts); //QRegExp过时了
    headerList=header.split(QRegularExpression("\\s+"));    //一个或多个空格、TAB等分隔符隔开的字符串
    if (!headerList.isEmpty() && headerList.last().isEmpty()) { // 去除末尾空格
        headerList.removeLast();
    }
    theModel->setHorizontalHeaderLabels(headerList); //设置表头文字

//设置表格数据
    int i,j;
    for (i=1;i<rowCnt;i++)
    {
        aLineText=aFileContent.at(i); //获取stringList的一行
//        tmpList=aLineText.split(QRegExp("\\s+"),QString::SkipEmptyParts);//一个或多个空格、TAB等分隔符隔开的字符串分解为多个字符串
        tmpList=aLineText.split(QRegularExpression("\\s+"));    //一个或多个空格、TAB等分隔符隔开的字符串分解为多个字符串
        for (j=0;j<FixedColumnCount-1;j++)
        {
            aItem=new QStandardItem(tmpList.at(j));//创建item
            theModel->setItem(i-1,j,aItem); //为模型的某个行列位置设置Item
        }
        aItem=new QStandardItem(headerList.at(j));//最后一列是Checkable,设置
        aItem->setCheckable(true);
        if (tmpList.at(j)=="0")
            aItem->setCheckState(Qt::Unchecked);
        else
            aItem->setCheckState(Qt::Checked);
        theModel->setItem(i-1,j,aItem); //为模型的某个行列位置设置Item
    }
}
```
### 4.将选中表格文字居左显示 <a id="4-将选中表格文字居左显示-41"></a>
```cpp
void MainWindow::on_actAlignLeft_triggered()
{
    if (!theSelection->hasSelection())
        return;

    QModelIndexList selectedIndix=theSelection->selectedIndexes();

    QModelIndex aIndex;
    QStandardItem   *aItem;

    for (int i=0;i<selectedIndix.count();i++)
    {
        aIndex=selectedIndix.at(i);
        aItem=theModel->itemFromIndex(aIndex);
        aItem->setTextAlignment(Qt::AlignLeft);
    }
}
```