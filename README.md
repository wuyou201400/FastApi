# FastAPI 示例项目

这是一个简单的FastAPI示例项目，展示了基本的API开发功能。

## 项目结构
最外层的FastApi是简单示例
里面的FastApi文件夹是使用了数据库和登录验证且是一对多关系的示例：
cd FastApi后执行启动命令

## 安装依赖 
pip install -r requirements.txt


## 启动命令
uvicorn app.main:app --reload --port 8005
<!-- main: 是包含 FastAPI 实例的 Python 文件名（不带 .py 扩展名）。
app: 是 FastAPI 实例的名称。
--reload: 在开发过程中启用自动重载功能，以便在代码更改时自动重启服务器。 -->

## 访问地址
http://127.0.0.1:8005/docs/

1. 安装依赖：`pip install -r requirements.txt`
2. 运行应用：`uvicorn app.main:app --reload`
3. 访问文档：`http://localhost:8005/docs和http://localhost:8005/redoc`


http://localhost:8005/users

先Authrize登录后调用接口，使用current_user获取当前用户信息