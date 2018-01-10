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
![10](/images/unity-shader-start-10.png)

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

### 属性(Properties)
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

property type 属性值的类型，包括:
- Color – 表示纯色，使用了RGBA表示法
- 2D – 代表尺寸为2的幂次的纹理(如2,4,8,16...256,512)
- Rect – 代表纹理(texture)，不同于上面的纹理，此处纹理的大小不一定是2的幂次。
- Cube – 用于3d中的cube map，经常提到的天空盒就是使用了cube map。
- Range(min, max) – 在min和max之间的一个值，在面板中可用滑动条改变其值大小。
- Float – 任意一浮点数。
- Vector – 4维向量值，本质就是4个浮点数组成的类型。

default value 属性值的初始值，就相当于你的变量初始化的那个值。
- Color – (red,green,blue,alpha) 使用了RGBA这种格式的颜色，alpha指的是透明度，比如 (1,1,1,1)
- 2D/Rect/Cube – 初始化值可以使一个空字符串，或者"white", "black", "gray", "bump"(说明此纹理是一个凹凸纹理)
- Float/Range – 和浮点数初始化一样
- Vector – 4维向量，其中4个数均为浮点数 (x,y,z,w)

{options} 仅仅用于纹理类型，比如上面提到的2D，Rect，Cube，对于这些类型，如果没有options可填，至少要写一个空的{}，否则编译出错。可以使用空格将多个options(选项)分开 ，可用的options（选项）如下:
- TexGen texgenmode：纹理坐标自动生成的方式。可以是ObjectLinear, EyeLinear, SphereMap, CubeReflect, CubeNormal其中之一，这些方式和OpenGL中的纹理坐标生成方式相对应。注意当你写Vertex Function时，纹理坐标产生方式将被忽略。

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

### 标签(Tags)
表面着色器(Surface Shader)和片段着色器(Fragment Shader)

表面着色器可以用一个或多个标签(tags)进行修饰。这些标签的作用是告诉硬件何时去调用你的shader代码。
例如，我们使用：Tags {“RenderType” = “Opaque”}，这意味着当程序去渲染不透明的几何体时，将调用我们的shader，Unity定义了一系列这样的渲染过程。另一个很容易理解的标签就是Tags {“RenderType” = “Transparent”}，意味着我们的shader只会输出半透明或透明的像素值。

其它一些有用的标签，比如“IgnoreProjector”=“True”，意味着你渲染的物体不会受到projectors（投影仪）的影响。

“Queue”=“xxxx”（给shader所属的对象贴上渲染队列的标签）。当渲染的对象类型是透明物体时，Queue标签能产生一些非常有趣的效果。该标签决定了物体渲染的顺序（译者注：我猜测它的工作方式是这样的，一个场景中有很多个物体，当这些物体被渲染时，必须有一个渲染的顺序，比如背景应该比其他物体先渲染出来，否则背景会将之前渲染的物体遮挡住，具体方法是将背景使用的shader中贴上一个“Queue”=“Backfround”标签，这样使用该shader的物体将被贴上Background的标签。总之当渲染整个场景时，unity会根据这些渲染队列的标签决定按什么顺序去渲染对应标签所属的物体）。
- Background – 在所有其他物体渲染之前渲染，被用于天空盒或类似的背景效果。
- Geometry(默认tags为geometry) – 适用于大多数物体。非透明物体使用这种渲染顺序。
- AlphaTest – 进行alpha测试的像素（alpha-test是指当前像素的alpha小于一定的值就舍弃该像素）应该使用该渲染顺序。单独设置该渲染顺序是因为当在渲染完所有实体过后，渲染alpha测试的物体将更有效率。
- Transparent – 该渲染标签所属的物体将在标签为Geometry和AlphaTest之后的物体渲染，并且这些贴着Transparent的所有物体本身是从后往前依次渲染的。任何经过alpha-blended的物体都应该使用该标签（译者注：alpha-blended是指使用当前像素的alpha作为混合因子，来混合之前写入到缓存中像素值，注意此时shader是不能写入深度缓存的，因为关闭了写入深度缓存的功能，如果不关闭写入深度缓存，那么在进行深度检测的时候，它背后的物体本来我们是可以透过它被我们看到的，但由于深度检测时，小于它的深度就被剔除了，从而我们就看不到它后面的物体了），玻璃和粒子效果比较适合该渲染标签。
- Overlay – 该渲染标签适合覆盖效果，任何最后渲染的效果都可以使用该标签，比如透镜光晕。

有趣的是你可以给这些基本的渲染标签进行加加减减。这些预定义的值本质上是一组定义整数，Background = 1000， Geometry = 2000, AlphaTest = 2450， Transparent = 3000，最后Overlay = 4000。（译者注：从此处我们也可以一窥究竟，貌似数值大的后渲染。）这些预设值这对透明物体有很大影响，比如一个湖水的平面覆盖了你用广告牌制作的树，你可以对你的树使用“Queue”=”Transparent-102”，这样你的树就会绘制在湖水前面了。

### #pragma
`#pragma surface surf Lambert` 这段代码表示其中surface表示这是一个表面着色器，进行结果输出的函数名称为surf，其使用的光照模型为Lambert光照模型。

### 变量
浮点数类型（float）和向量值类型（vec）一般都会在末尾加上2，3，4这些数字（float2，float4，vec3…）表示该类型具体有几个元素组成。这种定义方式使数值操作变得更方便，你可以将其当做一个整体使用，或者单独使用其分量。

你可以使用.xyzw或.rgba来表明你使用的变量类型具体的含义，比如.xyzw可能表示的是旋转四元数，而.xyz表示位置或法向量，.rgba表示颜色。当然，你可以仅仅使用float作为单个浮点值类型。其实对.rgba等分量访问符的使用也称作swizzle，尤其是对颜色的处理，比如颜色空间的转换可能会用到它，比如color=color.abgr;

你将会遇到half（半精度）和double（双精度）类型，half（一般16bit）即正常float（一般32bit）的一半精度，double（一般64bit）是正常float的两倍精度（此处的倍数衡量的方式不是指表示的范围，而是表示可以使用的bit位数）。使用half经常是出于性能考虑的原因。还有一种区别于浮点数的定点数fixed，精度更低。

当你想将颜色值规范到0~1之间时，你可能会想到使用saturate函数（saturate(x)的作用是如果x取值小于0，则返回值为0。如果x取值大于1，则返回值为1。若x在0到1之间，则直接返回x的值.），当然saturate也可以使用变量的swizzled版本，比如saturate(somecolor.rgb);

你可以使用length函数得到一个向量的长度，比如float size = length(someVec4.xz);

### 如何从表面着色器输出信息


===================================
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



