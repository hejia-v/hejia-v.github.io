---
title: 搭建hexo博客
date: 2017-11-24 20:17:06
updated: 2017-11-24 20:17:06
tags:
categories:
---

## 创建github仓库
在github上面创建一个仓库，名称是yourname.github.io，其中yourname是自己的github的名称，如果是其他自定义的名称，GitHub Pages 不会生效。目前GitHub Pages只能从master分支生成，因此最好创建一个hexo分支，用以存放hexo工程。

将yourname.github.io仓库clone到本地，并切换到hexo分支。

<!--more-->

## 创建hexo工程

首先安装node.js，然后通过如下命令安装hexo
```bash
npm install -g hexo
npm install -g hexo-cli
```
在本地的yourname.github.io文件夾中打开终端，通过如下命令创建hexo工程
```bash
hexo init ./temp  # 因为hexo进行初始化的文件夹必须是空的，所以在./temp文件夹中创建并初始化了一个hexo工程
mv -fv ./temp/* ./  # 将./temp中的hexo工程移动到yourname.github.io目录下
rm -rfv ./temp
```

hexo工程下面的几个文件和文件夹如下：
```plain
.
├── public # 存放的是生成的页面
├── scaffolds # 用于生成文章等的模板
├── source # 创建的各种文章
|   ├── _drafts
|   └── _posts
├── themes # 主题
├── _config.yml # 整个博客的配置
├── db.json # 解析source所得到的
└── package.json # npm配置信息
```
详细说明参考此[链接](https://hexo.io/docs/setup.html)。

完成后，将hexo工程推送到yourname.github.io的hexo分支，用以进行版本管理。

## 本地预览
在本地的yourname.github.io文件夾中打开终端，进入hexo分支，执行以下命令：
```bash
hexo clean
hexo generate
hexo server
```
打开浏览器输入：http://localhost:4000 ，就可以在本地预览博客了。

为了方便，以上命令可以缩减成一步：
```bash
hexo clean && hexo generate && hexo server
```

## 上传到github
修改hexo项目中的`_config.yml`文件：
```yml
deploy:
  type: git
  repo: https://github.com/yourname/yourname.github.io.git
  branch: master
```

安装依赖库：
```bash
npm install --save hexo-deployer-git
```

进行发布
```bash
hexo clean
hexo generate
hexo deploy
```
这时，hexo会将生成好的页面推送到github的master分支。在浏览器中输入 https://yourname.github.io ，就可以看到自己的博客了。

注意一下yourname.github.io项目的Setting -> GitHub Pages 设置中，是否勾选了*Enforce HTTPS*，如果勾选了，博客地址前面要确定是`https://`。

## 绑定个人域名（可选）
1. 购买域名。
2. 在项目的source文件夹下创建一个名为CNAME的文件，在里面写入购买的域名。例如：`yoursite.com`。
3. 在DNS中添加一条记录，如图
![1](/images/1.png)
其中**记录值**就是GitHub Pages的地址，ping一下可以获取到：
```bash
ping yourname.github.io
```
4. 再次部署博客，在浏览器打开自己的域名，就可以看到自己的博客了。

## 主题

hexo的主题放在themes文件夹，主题一般都有使用文档，按照上面的说明进行操作就可以了。当然也可以对主题进行一些修改，打造成自己喜爱的风格。

这里有一些比较不错的主题：
https://blog.keep.moe
https://otakism.com
http://www.chunqiuyiyu.com
http://blog.oniuo.com

## 添加图片

hexo博客中的图片通常使用七牛云存储来托管。

具体操作可以参考这篇[博客](http://www.jianshu.com/p/ec2c8acf63cd)。

TODO: 需要写个脚本处理本地预览和发布时的图片路径。

hexo clean && hexo generate && hexo server