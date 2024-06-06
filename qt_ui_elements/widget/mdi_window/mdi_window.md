# 目录

- [效果展示](#效果展示-1)
- [功能浅析](#功能浅析-2)
    - [添加窗口](#添加窗口-1)
    - [mdi模式](#mdi模式-2)
    - [窗口级联展开](#窗口级联展开-3)
    - [窗口平铺展开](#窗口平铺展开-4)

---
# 效果展示 <a id="效果展示-1"></a>

<iframe width="800" height="520" src="mdi_window.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# 功能浅析 <a id="功能浅析-2"></a>
中间装纳窗口组件是 QMdiArea
## 添加窗口 <a id="添加窗口-1"></a>
```cpp
QFormDoc *formDoc = new QFormDoc(this); //
ui->mdiArea->addSubWindow(formDoc); //文档窗口添加到MDI
formDoc->show(); //在单独的窗口中显示
```
## mdi模式 <a id="mdi模式-2"></a>
```cpp
void QWMainWindow::on_actViewMode_triggered(bool checked)
{
    //MDI 显示模式
    if (checked) //Tab多页显示模式
    {
        ui->mdiArea->setViewMode(QMdiArea::TabbedView); //Tab多页显示模式
        ui->mdiArea->setTabsClosable(true); //页面可关闭
    }
    else ////子窗口模式
    {
        ui->mdiArea->setViewMode(QMdiArea::SubWindowView); //子窗口模式
    }
}
```
## 窗口级联展开 <a id="窗口级联展开-3"></a>
```cpp
ui->mdiArea->cascadeSubWindows();
```
## 窗口平铺展开 <a id="窗口平铺展开-4"></a>
```cpp
ui->mdiArea->tileSubWindows();
```