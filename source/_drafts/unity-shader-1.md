---
title: unity shader 基础学习 1-轮廓
tags: unity, shader
---

unity中的着色器和材质的语言叫做ShaderLab。着色器程序是使用Cg/HLSL语言编写的。

这里以一个轮廓线shader为例，讲述unity中如何使用shader。

<!--more-->

## 使用自定义shader

1. 在场景中创建一个cube。
![1](/images/unity-shader-start-1.png)

    可以在Inspector面板看到新创建的cube所使用的Material如下
![2](/images/unity-shader-start-2.png)

2. 在工程中创建一个Materials文件夹，在Materials文件夹中右键[Create]=>[Shader]=>[Standard Surface Shader]创建一个shader， 右键[Create]=>[Material]创建一个Material。
![3](/images/unity-shader-start-3.png)

3. 将MyMaterial材质指定给cube。
![4](/images/unity-shader-start-4.png)

4. 选中MyMaterial材质，在Inspector面板中可以看到，默认shader是standard。将创建的shader拖拽到Inspector面板的MyMaterial区域，可以修改材质所使用的的shader。
![5](/images/unity-shader-start-5.png)

5. 在物体的Inspector面板中，可以看到MeshRender组件中有material和shader的设置面板，在scene和game模式下都可以设置material，切换material里的shader，设置shader的参数等。
![6](/images/unity-shader-start-6.png)

阅读下面链接，可以进一步了解unity里的shader
- [ShaderTut1](https://docs.unity3d.com/Manual/ShaderTut1.html)
- [ShaderTut2](https://docs.unity3d.com/Manual/ShaderTut2.html)
- [Unity3D Shader 新手教程](http://www.cnblogs.com/polobymulberry/p/4314147.html)


## 模型扩大法实现轮廓
大概思路是使用目标物体的mesh创建一个`GameObject`，对这个新建的`GameObject`使用轮廓线shader，shader很简单，就是将模型顶点沿法线方向移动一段距离，然后设置成轮廓线颜色，最后将这个模型的正面剔除就可以了。

也可以不新建GameObject，直接在原物体上使用shader进行类似的操作。这里不复制GameObject，只依靠shader实现轮廓线效果。




## 小提示
2. mesh复用











https://www.shadertoy.com/view/MlKSWc
https://www.shadertoy.com/view/MdfcWn
https://www.shadertoy.com/view/4dfcR7
https://www.shadertoy.com/view/MdByW1

https://www.shadertoy.com/view/MtcXRf

magic zhen
https://www.shadertoy.com/view/MlGGDt
https://www.shadertoy.com/view/MlyGzm
https://www.shadertoy.com/view/Xl33zH
https://www.shadertoy.com/view/MsKGDR
https://www.shadertoy.com/view/4l2XWh
https://www.shadertoy.com/view/ltj3Wc

轮廓+粒子+溶解
https://www.shadertoy.com/view/MdX3zr

cartoon
https://www.shadertoy.com/view/4t2GRm
https://www.shadertoy.com/view/XlBGzm
https://www.shadertoy.com/view/MsB3W1
https://www.shadertoy.com/view/Xlf3Rj

https://www.shadertoy.com/loved?from=60&num=12



