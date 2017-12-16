---
title: windows上安装tensorflow
date: 2017-12-16 21:14:19
updated: 2017-12-16 21:14:19
tags: ml
categories: ml
---

### 访问 tensorflow 官网
方法一: 直接访问 https://tensorflow.google.cn

<!--more-->

方法二:
1. 修改 hosts 文件
windows的hosts文件的位置是 `C:\Windows\System32\drivers\etc\hosts` ，在hosts文件末尾添加如下内容：
```
64.233.188.121 www.tensorflow.org
```
2. 刷新dns缓存，在命令行执行下面命令(windows)：
```
ipconfig /flushdns
```
3. 在浏览器访问 www.tensorflow.org ，就可以浏览官网了。

### 在windows上编译安装

1. 安装cuda。在[官网](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal)下载安装包，按照默认选项安装就可以了。

2. 在NVIDIA官网的[cudnn](https://developer.nvidia.com/cudnn)页面，下载与cuda适配的cudnn，例如 **cudnn-9.1-windows10-x64-v7.zip**。压缩包里有bin、include、lib三个文件夹，解压到cuda的文件夹，例如 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.1` 。

3. 下载[swigwin](http://www.swig.org/download.html)并解压，例如解压到 `E:\share_v\code\swig-3.0.12` 。(注意是swigwin，里面有编译好的swig.exe)

4. 对照一下tensorflow的[cmake说明](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/cmake/README.md)，了解一下构建时的一些选项。

5. 使用cmake-gui打开`tensorflow/tensorflow/contrib/cmake`文件夹，添加如下的entry(路径根据实际情况来填)：
```
CUDNN_HOME=C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.1
SWIG_EXECUTABLE=E:/share_v/code/swigwin-3.0.12/swig.exe
PYTHON_EXECUTABLE=C:/Python36/python.exe
PYTHON_LIBRARIES=C:/Python36/libs/python36.lib
CMAKE_INSTALL_PREFIX=E:/share_v/code/tensorflow/tensorflow/contrib/cmake/build/tensorflow
```
    点击**configure**按钮，会自动列出一些entry，如果有红色的entry，则根据提示进行修改，再点击**configure**按钮，直到没有红色的entry为止。
    这里需要取消下面3项的勾选：
```
tensorflow_BUILD_CC_TESTS
tensorflow_ENABLE__SSL_SUPPORT
tensorflow_WIN_CPU_SIMD_OPTIONS
```
    具体配置如图:
    ![1](/images/install-tensorflow-1.png)

6. 点击**Generate**按钮生成vs2017解决方案。

7. 点击**open project**按钮打开vs2017，在vs2017中切换到Release编译选项，然后开始编译。

8. 编译的过程中会下载一些文件，需要留意一下这些下载地址能否访问到。
    如果`git clone`时提示 `... port 443: Timed out`，则表明这个地址被屏蔽了，为了简单省事，最好还是用shadowsocks。开启shadowsocks后，设置git的代理http/https协议(clone **https://**前缀的repo会走ss)
```
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
```
    编译完毕后，取消代理
```
git config --global --unset http.proxy
git config --global --unset https.proxy
```
    可查看一下git的配置
```
git config --global -l
```
    如果下载时走的是ssh协议，还需要配置ssh代理，即配置.ssh/config （确保安装了 NetCat）
```
Host github.com bitbucket.org
    ProxyCommand            nc -x 127.0.0.1:1080 %h %p
```

9. 编译过程中可能会有这样一个错误: `LINK : fatal error LNK1181: 无法打开输入文件“\pywrap_tensorflow_internal.lib”` 。这时需要修改**_beam_search_ops**、**_gru_ops**、**_lstm_ops**这3个项目的配置，具体修改如下:
    配置属性==>连接器==>常规==>附加库目录==>添加：`$(SolutionDir)$(Configuration)`
    ![2](/images/install-tensorflow-2.png)


### 通过pip安装
如果cuda和cudnn的版本符合pip包的要求，可以直接通过pip安装
`pip3 install tensorflow-gpu`
