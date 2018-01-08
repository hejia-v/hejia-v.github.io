---
title: unity shader 基础学习 1-轮廓
tags:
    - unity
    - shader
---

unity中的着色器和材质的语言叫做ShaderLab。着色器程序是使用[Cg/HLSL](https://docs.unity3d.com/Manual/SL-ShadingLanguage.html)语法编写的。

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

## 本文用到的shader语法
### shaderlab的代码构成
![9](/images/unity-shader-start-9.png)

### CGINCLUDE/ENDCG
被这对关键字包起来的代码块，将被所有subshaders的所有pass共享。
```Shaderlab
CGINCLUDE
// ...
ENDCG
```

### 使用`#include`语句引入内建的shader include文件。
查看[官方文档](https://docs.unity3d.com/Manual/SL-BuiltinIncludes.html)可以了解详细内容。
```Shaderlab
CGPROGRAM
// ...
#include "UnityCG.cginc"
// ...
ENDCG
```

### shaderlab的属性部分
格式如下图
![7](/images/unity-shader-start-7.png)
![8](/images/unity-shader-start-8.png)

可以理解为属性值相当于一种全局变量，Unity的优势在于给这个全局变量赋值可以在Inspector面板进行。Properties（属性值）是所有Subshader代码中的共享的，意味着所有SubShader代码中都可以使用这些属性值。

常用的有这些
- `name ("display name", Range (min, max)) = number`：定义浮点数范围属性。
- `name ("display name", Color) = (number,number,number,number)`：定义颜色属性。
- `name ("display name", 2D) = "name" { options }`：定义2D纹理属性。
- `name ("display name", Rect) = "name" { options }`：定义长方形（非2次方）纹理属性。
- `name ("display name", Cube) = "name" { options }`：定义立方贴图纹理属性。
- `name ("display name", Float) = number`：定义浮点数属性。
- `name ("display name", Vector) = (number,number,number,number)`：定义一个四元素的容器（Vector4）属性。

更多内容可以查看这里
- [SL-Properties](https://docs.unity3d.com/Manual/SL-Properties.html)
- [SL-PropertiesInPrograms](https://docs.unity3d.com/Manual/SL-PropertiesInPrograms.html)

### 结构体数据成员的语义(Semantics)
在可编程流水线中，我们通常使用顶点声明(vertex declaration)来描述顶点结构的分量。
```hlsl
struct appdata {
    float4 vertex : POSITION;
    float3 normal : NORMAL;
};
```
我们需要一种方式来定义从顶点声明(就是上面的那个结构体)中的元素到顶点着色器的输入结构的数据成员的映射。我们在输入结构中通过为每个数据成员指定一种语义来定义这种映射。该语义(semantics)通过用法类型(usage-type)和用法索引(usage-index)来标识顶点声明中的每个元素。由数据成员的语义所标识的那个顶点元素就是被映射到该数据成员的那个元素。

用法类型即`float4 vertex : POSITION;`中的`POSITION`，指定了顶点分量的用途。例如，某一分量是作为位置向量，法向量还是纹理向量等。

用法索引即用法类型后面可能跟着的一个整数，例如`float4 vertex : POSITION1;`。取值范围一般在区间[0, 15]，具体需要看平台。如果不写用法索引，用法索引就默认是0。用法索引用于标识具有相同用法的多个顶点分量，例如，对于一个顶点的法向量，既要用它计算运动方向，又要用它计算扩展方向，在顶点声明中这样声明：`float3 moveDirection : NORMAL0;`、`float3 extendDirection : NORMAL1;`，即将顶点着色器的输入结构的法向量同时映射到了顶点声明中的这2个分量。

顶点着色器支持的常用输入用法包括：
- POSITION[n]  位置
- BLENDWEIGHTS[n]  融合权值
- BLENDINDICES[n]  融合权值
- NORMAL[n]  法向量
- PSIZE[n]  顶点的点尺寸
- DIFFUSE[n]  漫反射颜色
- SPECULAR[n]  高光颜色
- TEXCOORD[n]  纹理坐标
- TANGENT[n]  切向量
- BINNORMAL[n]  副法向量
- TESSFACTOR[n]  网格化因子

n为可选整数，一般取自区间[0, 15]。

顶点着色器支持的常用输出用法包括：
- POSITION[n]  位置
- PSIZE[n]  顶点的点尺寸
- FOG[n]  雾融合值
- COLOR[n]  顶点颜色。注意，可输出多个顶点颜色，这些颜色混合在一起生成最终颜色。
- TEXCOORD[n]  纹理坐标。注意，可能输出多个顶点纹理坐标。

n为可选整数，一般取自区间[0, 15]。

查看下面链接了解更多内容:
- [Semantics](https://msdn.microsoft.com/en-us/library/windows/desktop/bb509647.aspx)
- [SL-ShaderSemantics](https://docs.unity3d.com/Manual/SL-ShaderSemantics.html)
- [SL-VertexProgramInputs](https://docs.unity3d.com/Manual/SL-VertexProgramInputs.html)




===========
本文步骤，先照着那个翻译文过一遍，然后再补缺。

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



