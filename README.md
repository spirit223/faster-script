# 快手平台自动上传视频脚本
## 脚本功能
进入快手平台后将指定文件夹下的视频一次性上传到快手, 等待平台审核
## 启动方式
1. 克隆本项目到本地
    ```shell
    git clone git@github.com:spirit223/faster-script.git
    # 或者
    git clone https://github.com/spirit223/faster-script.git
    ```
2. 创建虚拟环境
    ```shell
    # 进入项目根目录
    cd .../faster-script
    # 创建虚拟环境
    python -m venv .venv
    # 激活虚拟环境
    cd .venv/Scripts/
    activate.bat
    ```
3. 安装依赖库
   ```shell
   pip install -r requirements.txt
   ```
4. 启动脚本
   ```shell
   python main.py
   ```

## todo
- 文件上传现在只提供最大等待时长, 考虑从页面获取到 `上传成功` 元素则结束等待