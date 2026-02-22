#!/usr/bin/env python3
"""
捷途旅行者车机安装第三方软件教程
静态网页服务
"""

import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

def get_local_ip():
    """获取本地IP地址"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):
    """支持CORS的HTTP请求处理器"""

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def run_server(port=8000):
    """启动HTTP服务器"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSHTTPRequestHandler)

    local_ip = get_local_ip()

    print("=" * 80)
    print("捷途旅行者车机安装第三方软件教程 - 服务已启动")
    print("=" * 80)
    print(f"本地访问: http://localhost:{port}")
    print(f"局域网访问: http://{local_ip}:{port}")
    print(f"文件路径: {os.getcwd()}")
    print("=" * 80)
    print("按 Ctrl+C 停止服务器")
    print("=" * 80)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
