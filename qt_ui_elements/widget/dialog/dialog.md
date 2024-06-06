# 目录

- [效果展示](#效果展示-1)
- [功能浅析](#功能浅析-2)
    - [QDialog](#qdialog-1)
        - [1. 创建对话框](#1-创建对话框-1)
        - [2. 设置大小和布局](#2-设置大小和布局-2)
        - [3. 配置对话框行为](#3-配置对话框行为-3)
        - [4. 管理按钮](#4-管理按钮-4)
        - [5. 捕获按钮事件](#5-捕获按钮事件-5)
        - [6. 设置图标](#6-设置图标-6)
        - [7. 输入/输出](#7-输入-输出-7)
        - [8. 获取用户选择](#8-获取用户选择-8)
    - [代码解析](#代码解析-2)
        - [模态显示](#模态显示-9)
        - [非模态显示](#非模态显示-10)

---
# 效果展示 <a id="效果展示-1"></a>

<iframe width="580" height="400" src="dialog.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# 功能浅析 <a id="功能浅析-2"></a>
## QDialog <a id="qdialog-1"></a>
### 1. 创建对话框 <a id="1-创建对话框-1"></a>
- `QDialog(QWidget *parent = nullptr, Qt::WindowFlags flags = Qt::Dialog | Qt::MSWindowsFixedSizeDialogHint)`: 构造函数，用于创建对话框。`parent` 是对话框的父窗口，`flags` 指定窗口的属性。

### 2. 设置大小和布局 <a id="2-设置大小和布局-2"></a>
- `resize(int width, int height)`: 设置对话框的大小。
- `setFixedSize(int width, int height)`: 设置对话框的固定大小，禁止用户调整大小。
- `layout() const`: 获取对话框当前使用的布局。

### 3. 配置对话框行为 <a id="3-配置对话框行为-3"></a>
- `setModal(bool modal)`: 设置对话框是否为模态（阻塞其他窗口的交互）。
- `setWindowTitle(const QString &title)`: 设置对话框的标题。

### 4. 管理按钮 <a id="4-管理按钮-4"></a>
- `setWindowTitle(const QString &title)`: 设置对话框标题。
- `addButton(QWidget *button, QMessageBox::ButtonRole role)`: 向对话框添加按钮，并指定按钮的角色（例如，取消、确认等）。
- `button(QMessageBox::ButtonRole role)`: 获取具有指定角色的按钮。
- `exec()`: 显示对话框并进入事件循环，直到用户关闭对话框。

### 5. 捕获按钮事件 <a id="5-捕获按钮事件-5"></a>
- `accepted()`: 当用户点击“接受”（通常是“确定”或“是”）按钮时，触发此信号。
- `rejected()`: 当用户点击“拒绝”（通常是“取消”或“否”）按钮时，触发此信号。
- `done(int result)`: 结束对话框的事件循环，并将结果返回给调用 `exec()` 的代码。

### 6. 设置图标 <a id="6-设置图标-6"></a>
- `setIcon(const QIcon &icon)`: 设置对话框窗口的图标。

### 7. 输入/输出 <a id="7-输入-输出-7"></a>
- `open()`: 显示对话框，但不进入事件循环。
- `show()`: 显示对话框，可以指定显示方式（例如，正常、全屏等）。

### 8. 获取用户选择 <a id="8-获取用户选择-8"></a>
- `result()`: 获取用户通过按钮点击传递给对话框的结果代码。

## 代码解析 <a id="代码解析-2"></a>
### 模态显示 <a id="模态显示-9"></a>
```cpp
void MainWindow::on_actTab_SetSize_triggered()
{
    //模态对话框，动态创建，用过后删除
    QWDialogSize    *dlgTableSize=new QWDialogSize(this); //创建对话框
    //   dlgTableSize->setAttribute(Qt::WA_DeleteOnClose);
    //对话框关闭时自动删除对话框对象,用于不需要读取返回值的对话框
    //如果需要获取对话框的返回值，不能设置该属性，可以在调用完对话框后删除对话框
    Qt::WindowFlags    flags=dlgTableSize->windowFlags();
    dlgTableSize->setWindowFlags(flags | Qt::MSWindowsFixedSizeDialogHint); //设置对话框固定大小

    dlgTableSize->setRowColumn(theModel->rowCount(),theModel->columnCount()); //对话框数据初始化

    int ret=dlgTableSize->exec();// 以模态方式显示对话框，用户关闭对话框时返回 DialogCode值
    if (ret==QDialog::Accepted) //OK键被按下,对话框关闭，若设置了setAttribute(Qt::WA_DeleteOnClose)，对话框被释放，无法获得返回值
    { //OK键被按下，获取对话框上的输入，设置行数和列数
        int cols=dlgTableSize->columnCount();
        theModel->setColumnCount(cols);

        int rows=dlgTableSize->rowCount();
        theModel->setRowCount(rows);
    }
    delete dlgTableSize; //删除对话框
}
```
### 非模态显示 <a id="非模态显示-10"></a>
```cpp
void MainWindow::on_actTab_Locate_triggered()
{
    //创建 StayOnTop的对话框，对话框关闭时自动删除
    //通过控制actTab_Locate的enable属性避免重复点击
    //    ui->actTab_Locate->setEnabled(false); 已通过showEvent控制
    QWDialogLocate  *dlgLocate;//定位单元格对话框，show()调用，关闭时自己删除
    dlgLocate = new QWDialogLocate(this); //创建对话框，传递指针
    dlgLocate->setAttribute(Qt::WA_DeleteOnClose); //对话框关闭时自动删除对话框对象,用于不需要读取返回值的对话框
    Qt::WindowFlags    flags=dlgLocate->windowFlags(); //获取已有flags
    //对话框设置为固定大小和StayOnTop
    //    dlgLocate->setWindowFlags(flags |Qt::MSWindowsFixedSizeDialogHint |Qt::WindowStaysOnTopHint); //设置对话框固定大小,StayOnTop
    dlgLocate->setWindowFlags(flags | Qt::WindowStaysOnTopHint); //设置对话框固定大小,StayOnTop
    //对话框初始化设置
    dlgLocate->setSpinRange(theModel->rowCount(),theModel->columnCount());
    QModelIndex curIndex=theSelection->currentIndex();
    if (curIndex.isValid())
       dlgLocate->setSpinValue(curIndex.row(),curIndex.column());

    //对话框释放信号，设置单元格文字
    connect(dlgLocate,SIGNAL(changeCellText(int,int,QString&)),
                     this,SLOT(setACellText(int,int,QString&)));

    //对话框是否信号，设置action的属性
    connect(dlgLocate,SIGNAL(changeActionEnable(bool)),
                     this,SLOT(setActLocateEnable(bool)));

    //主窗口是否信号，修改对话框上的spinBox的值
    connect(this,SIGNAL(cellIndexChanged(int,int)),
                     dlgLocate,SLOT(setSpinValue(int,int)));

    dlgLocate->show(); //非模态显示对话框
}
```