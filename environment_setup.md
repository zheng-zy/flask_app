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