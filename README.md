# Python Study

Python的3.0版本，常被称为Python 3000，或简称Py3k。相对于Python的早期版本，这是一个较大的升级。为了不带入过多的累赘，Python 3.0在设计的时候没有考虑向下兼容。

> **由于Mac是自带python2.7的，建议不要直接升级，而是安装双Python**，安装教程：
[Mac安装Python2和Python3、pip2和pip3、ipython2和ipython3](https://www.jianshu.com/p/3701ff3399dd)

**链接内核心内容**

#### 1.Homebrew的安装
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
> Homebrew安装成功后，会自动创建目录 /usr/local/Cellar 来存放Homebrew安装的程序。 这时你在命令行状态下面就可以使用 brew 命令了

⚠️**注意：如果在安装过程中返回400，可以在几分钟后尝试重新安装。**

#### 2.安装Python3
```
brew install python # 这一步安装了python3和pip3
python3 -V  # 测试
pip3 -V  # 测试
```

#### 3.安装pip2
```
brew install python@2 # 这一步安装了python3和pip3
python -V  # 测试
pip2 -V  # 测试
```

#### 4.安装ipython2和ipython3
```
pip3 install ipython 
ipython3 # 测试
pip install ipython
ipython # 测试
```
---

#### VScode 插件篇
+ 安装Python扩展，如果前面安装的anaconda的路径已经加入到path环境变量中，这里跟着提示操作就可以，vscode会自动找到系统python的位置，调试时如果发现提示pylint没有安装，可以通过pip或者conda安装，参看[Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)
+ 安装Jupyter、Path Intellisense、vscode-python-docstring等扩展，直接参看扩展说明以及[Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)即可，都很直观
+ 安装Settings Sync，用于同步配置，将配置保存到github gist，参看扩展说明一步步操作即可，快捷键Shift + Alt + U上传配置
![插件](https://s2.ax1x.com/2019/01/05/F7n7sP.png)
