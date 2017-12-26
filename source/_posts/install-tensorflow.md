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

### 安装cuda(win)
在nvidia的官网下载cuda的安装包，按照默认选项安装就可以了。如果不出意外，安装完毕后，cuda的bin文件夹会自动添加到环境变量。

在NVIDIA官网的[cudnn](https://developer.nvidia.com/cudnn)页面，下载与cuda适配的cudnn压缩包。解压后，会有bin、include、lib三个文件夹，将这三个文件夹拷贝到cuda的安装文件夹下面，并与cuda的bin、include、lib文件夹合并。

如果下载时的网络连接不稳定，推荐使用`wget -c url`命令下载。

### 通过pip安装
如果cuda和cudnn的版本符合pip包的要求，可以直接通过pip安装
`pip3 install tensorflow-gpu`

### 编译安装
我一般是在虚拟机里使用linux，而虚拟机无法使用gpu加速，因此暂时不考虑在虚拟机的linux里编译tensorflow。tensorflow的windows编译有很多问题，很麻烦。想在windows机器上自己编译，最好的方案是等待wsl支持gpu后，在wsl中编译tensorflow。在[OpenCL & CUDA GPU support](https://wpdev.uservoice.com/forums/266908-command-prompt-console-bash-on-ubuntu-on-windo/suggestions/16108045-opencl-cuda-gpu-support)，[Cannot find GPU devices on Bash](https://github.com/Microsoft/WSL/issues/829)可以关注一下wsl支持gpu的最新进展。

编译的过程中会下载一些文件，需要留意一下这些下载地址能否访问到。如果`git clone`时提示 `... port 443: Timed out`，则表明这个地址被屏蔽了，为了简单省事，最好还是用shadowsocks。开启shadowsocks后，设置git的http/https代理协议
```
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
```
编译完毕后，取消代理
```
git config --global --unset http.proxy
git config --global --unset https.proxy
```
可以查看一下git的配置
```
git config --global -l
```

为了避免路径中有空格造成的烦恼，建议目录使用符号链接，例如
```
mklink /D C:\CUDA "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA"
```

### 检测gpu是否开启
在python的交互环境下，输入如下代码，可以查看有哪些设备
```python
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```
实际上在tensorflow开始运行后，输出的log中会有device信息，可以判断是否启用了gpu。

### 测试
下面代码是之前的bp神经网络的tensorflow实现，可以用来测试一下
```python
# -*- coding:utf-8 -*-
import time
from sklearn import datasets
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def add_layer(inputs, dim_in, dim_out, layer_n, is_output_layer=False, y=None):
    layer_name = f'layer{layer_n}'

    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([dim_in, dim_out]))  # Weight中都是随机变量
            tf.summary.histogram(layer_name + "/weights", Weights)  # 可视化观看变量
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, dim_out]))  # biases推荐初始值不为0
            tf.summary.histogram(layer_name + "/biases", biases)  # 可视化观看变量
        with tf.name_scope('z'):
            z = tf.matmul(inputs, Weights) + biases  # inputs*Weight+biases
            tf.summary.histogram(layer_name + "/z", z)  # 可视化观看变量

        if is_output_layer:
            outputs = tf.nn.softmax(z, name='outputs')
            loss = tf.nn.softmax_cross_entropy_with_logits(logits=z, labels=y, name='loss')
            tf.summary.histogram(layer_name + '/loss', loss)  # 可视化观看变量
            return outputs, loss
        else:
            outputs = tf.nn.tanh(z)
            tf.summary.histogram(layer_name + "/outputs", outputs)  # 可视化观看变量
            return outputs, None


np.random.seed(0)
X_data, y_data = datasets.make_moons(200, noise=0.20)
num_examples = len(X_data)
ym_data = np.zeros((num_examples, 2))
ym_data[range(num_examples), y_data] = 1


# 生成一个带可展开符号的域
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, name='X')
    ys = tf.placeholder(tf.float32, name='y')

tf.set_random_seed(0)
# 三层神经网络，输入层（2个神经元），隐藏层（3神经元），输出层（2个神经元）
layer1, _ = add_layer(xs, 2, 3, 1)  # 隐藏层
predict_step, loss = add_layer(layer1, 3, 2, 2, True, ys)  # 输出层

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)  # 0.01学习率,minimize(loss)减小loss误差

init = tf.global_variables_initializer()

config = tf.ConfigProto()
# https://tensorflow.google.cn/tutorials/using_gpu#allowing_gpu_memory_growth
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# 合并到Summary中
merged = tf.summary.merge_all()

# 选定可视化存储目录
writer = tf.summary.FileWriter("./", sess.graph)

sess.run(init)  # 先执行init

start_time = time.time()
# 训练2w次
num_passes = 20000
for i in range(num_passes):
    sess.run(train_step, feed_dict={xs: X_data, ys: ym_data})
    if i % 50 == 0:
        result = sess.run(merged, feed_dict={xs: X_data, ys: ym_data})  # merged也是需要run的
        writer.add_summary(result, i)  # result是summary类型的，需要放入writer中，i步数（x轴）
time_cost = time.time() - start_time
summary_text = f'cost: {time_cost}'
print(summary_text)

# --------------------------- predict ---------------------------
def predict(x):
    predict = sess.run(predict_step, feed_dict={xs: x})
    return np.argmax(predict, axis=1)


def visualize(X, y):
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.show()
    plt.title("bp nn")

visualize(X_data, y_data)
```
运行完上面的脚本后，在该脚本目录下执行`tensorboard --logdir="./"`命令，就可以在浏览器中查看tensorboard。
