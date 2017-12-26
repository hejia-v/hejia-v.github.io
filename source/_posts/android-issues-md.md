---
title: android开发中的一些经验
date: 2017-12-01 21:45:05
updated: 2017-12-01 21:45:05
tags: android
categories: android
---

记录一下android开发中的一些经验，本文将持续更新。

<!--more-->

## jar命令的使用

<a href="https://zh.wikipedia.org/wiki/JAR_(文件格式)">JAR</a>文件即 Java Archive File，是 Java 的一种文档格式。JAR 文件实际上就是 ZIP 文件，使用`unzip xxx.jar -d dest/`命令即可解压。

`jar`命令的说明如下：
![1](http://ozy76jm8o.bkt.clouddn.com/blog/images/android-issues-1.png)

下面是jar命令的一些常用用法：
1. 显示jar包
```
jar tvf hello.jar    # 查看hello.jar包的内容
```

2. 解压jar包
```
jar xvf hello.jar   # 解压hello.jar至当前目录
```

更多用法参考 [JAR命令&JAR包详解](http://blog.chinaunix.net/uid-692788-id-2681136.html)

## java的反编译
很多情况下，当我们使用别人的jar包时，很有可能会遇到一些问题，这时需要了解一下jar包里到底有些什么，方便定位问题所在。jar命令只是对jar包进行了一下解包，想查看其中的代码细节，还需要进行反编译。[Java Decompiler](http://jd.benow.ca)是一款比较好用的反编译软件，在实际使用中，能够反编译出大部分的java代码。eclipse、android studio安装Java Decompiler插件后，在使用第三方jar库时，会减少很多烦恼。

## 获取apk的签名和MD5指纹
在很多情况下，需要确认apk的签名。例如，接入渠道sdk后，sdk的初始化或者登陆、支付等功能出现了问题，就有可能是apk的SHA1签名与在渠道后台配置的SHA1签名不一致导致的。

获取apk的SHA1签名的一般步骤是:
1. 解压apk：`unzip testapp.apk`。
2. 找到解压出来的RSA文件。
3. 将终端切到RSA文件所在的目录, 在命令行输入 `keytool -printcert -file ./***.RSA` ，即可获取sha1签名和md5指纹。
具体操作如图
![2](http://ozy76jm8o.bkt.clouddn.com/blog/images/android-issues-2.png)

## apktool的使用
解包和打包
[apktool](https://ibotpeaches.github.io/Apktool/) 是一款逆向工程工具。在[这里](https://ibotpeaches.github.io/Apktool/documentation/)有相关的文档。

### 基础功能
1. 解压apk，生成可读的AndroidManifest.xml，
```
apktool d testapp.apk
```

2. 解压jar
```
apktool d foo.jar
```

3. smali调试，参考[wiki](https://github.com/JesusFreke/smali/wiki/smalidea)

### 查看apk里面的java源代码
1. 下载[dex2jar](https://github.com/pxb1988/dex2jar)
2. 使用unzip解压apk：`unzip testapp.apk`
3. 使用dex2jar将dex文件转换成jar文件
4. 使用jd-gui打开生成的classes-dex2jar.jar，就可以查看java源代码了

具体操作如图

![3](http://ozy76jm8o.bkt.clouddn.com/blog/images/android-issues-3.png)
![4](http://ozy76jm8o.bkt.clouddn.com/blog/images/android-issues-4.png)


### 修改apk里面的内容
1. 使用apktool解压apk，`apktool d testapp.apk`
2. 更新so包，比如可以将release版的so替换成debug版的so
3. 更新资源文件
4. 更改smali，smali的语法可以参考[这篇文章](http://blog.csdn.net/wdaming1986/article/details/8299996)
5. 打包回apk，打包出来的文件在apk文件夹中的dist目录下
6. 对重新打包后的apk文件进行签名
```
jarsigner -verbose -keystore yourKey.keystore -storepass yourPassword path/to/apk /path/to/keystore/file
```

## 查看apk的一些信息
使用android studio直接打开apk包，可以快速的浏览apk中的一些信息，但是会在用户文件夹生成一个临时工程，占用c盘资源。

## log查看

目前常用的获取android上面的log的方法有这些：
1. 直接使用logcat命令，一般是将logcat的输出重定向到文件，然后再在文件里查找需要的信息
2. 使用eclipse或者android studio的logcat窗口查看log。eclipse在非调试模式下，logcat窗口并不是很好用；android studio有一定几率连不上设备，这时很会恼火。
3. app收集log并显示在屏幕上，由于log有可能会刷新得很快，在设备的屏幕上，想定位到具体信息并不是很方便，并且这种方式对app的性能有一定的影响。

个人感觉比较好的方式是参考一下AirDroid，开发一个独立的app用于收集android上的log，这个app开启一个web服务，并将收集到的log输出到这个web上，在电脑上的浏览器中访问这个web，可以获取到设备上的实时log。

## 一些c/c++库在android上的编译

- 编译Boost，参考[Boost-for-Android](https://github.com/dec1/Boost-for-Android)
- 编译Python，参考python的[issue30386](https://bugs.python.org/issue30386)

## android studio引用外部工程
很多时候，库工程并不是放在项目文件夹下面，而是放在其他位置，常见的原因是想将这个库工程作为一个公共的库，在几个项目之间使用。

android studio中引用外部库的方法是这样的，在项目的settings.gradle文件中添加如下语句：
```
include ':BaiduLBS'
project(':BaiduLBS').projectDir = new File(settingsDir, '../platform/android/sdk/BaiduLBS')
```
即可添加相对路径在`../platform/android/sdk/BaiduLBS`处的外部库`BaiduLBS`。

## 横竖屏的问题
当手机进行横竖屏切换，弹出键盘，窗口大小发生变化等情况发生时，activity会重新走一遍OnCreate等生命周期方法。要避免这种行为，需要在AndroidManifest.xml中，为activity添加`android:configChanges`属性，例如
```xml
<activity
    android:name="com.xxx.MainActivity"
    android:configChanges="orientation|keyboardHidden|screenSize" >
</activity>
```
这时，当有orientation、keyboardHidden、screenSize情况发生时，就不会重建activity并调用OnCreate等方法，而是调用原实例的`onConfigurationChanged`方法。

## 游戏画面只有屏幕一半
在android手机上玩游戏时，经常会遇到这样一种情况，就是不知道做了一些什么操作，屏幕上只有部分(不一定是1/2)区域有游戏画面，其余区域是黑色的。

个人感觉是经过了某些操作，导致GLSurfaceView的Layout有问题。我使用下面的方法试了一下，能够很大程度的降低这种情况的发生
```java
// 固定为横屏
private void resetGLSurfaceViewSize() {
    DisplayMetrics dm = new DisplayMetrics();
    getWindowManager().getDefaultDisplay().getMetrics(dm);
    int w = dm.widthPixels;
    int h = dm.heightPixels;
    Log.d(TAG, "屏幕的分辨率为：" + w + "*" + h);
    if (w <= 0 || h <= 0) {
        return;
    }
    w = w > h ? w : h;
    h = w > h ? h : w;
    mGLSurfaceView.getLayoutParams().width = w;
    mGLSurfaceView.getLayoutParams().height = h;
}

@Override
public void onConfigurationChanged(Configuration newConfig) {
    super.onConfigurationChanged(newConfig);
    resetGLSurfaceViewSize();
}
```

## 多次点击app icon的问题
如果一个游戏接入了第3方的登录模块，当打开游戏弹出第3方的登录框时，按下home键回到桌面，再次点击这个游戏的icon，期望能返回游戏，并且登录框不被清除，这时需要将游戏activity的launchMode设置为singleTop，如下
```xml
<activity
    android:name="com.xxx.MainActivity"
    android:launchMode="singleTop" >
</activity>
```
