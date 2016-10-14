### 安装python-pip
yum -y install python-pip
### 清理cache
yum clean all

### 升级pip
pip install --upgrade pip

### 安装virtualenv
pip install virtualenv
### 创建虚拟环境
virtualenv venv
### 激活虚拟环境
source bin/activate
### 离开
(env) [root@iZ25zrelpocZ virtualenv]# deactivate 


### pip安装requirements.txt依赖
pip install -r requirements.txt
### 查看当前已安装包是否可升级
pip list --outdated
### 升级pip已安装所有包
pip list --outdated | grep '^[a-z]* (' | cut -d " " -f 1 | xargs pip install -U 
### pip生成requirements.txt文件
pip freeze > requirements.txt