# 8. QGridLayoutClass
A GridLayout class object presents with a grid of cells arranged in rows and columns. The class contains addWidget() method. Any widget can be added by specifying the number of rows and columns of the cell. Optionally, a spanning factor for row as well as column, if specified makes the widget wider or taller than one cell. Two overloads of addWidget() method are as follows:  

|Name|Usage|
|:--:|:---:|
|addWidget(QWidget, int r, int c)|Adds a widget at specified row and column|
|addWidget(QWidget, int r, int c, int rowspan, int columnspan)|Adds a widget at specified row and column and having specified width and/or height|

A child layout object can also be added at any cell in the grid.  

|Name|Usage|
|:--:|:---:|
|addLayout(QLayout, int r, int c)|Adds a layout object at specified row and column|