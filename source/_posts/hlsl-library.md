---
title: HLSL 常用函数
date: 2017-12-01 08:15:02
updated: 2017-12-01 08:15:02
tags: shader
categories: shader
---

HLSL是[unity推荐](https://docs.unity3d.com/Manual/SL-ShadingLanguage.html)的shader语言，HLSL和Cg很相似。这里整理了一下网络上收集到的相关资料，方便自己学习和查询。

## HLSL固有函数
Intrinsic Functions (DirectX HLSL)

<!--more-->

| 函数名                                      | 用法                               | 描述                                | Description                              | Minimum shader model |
| ---------------------------------------- | -------------------------------- | --------------------------------- | ---------------------------------------- | -------------------- |
| [abs](http://preview.library.microsoft.com/en-us/library/bb509562) | abs(x)                           | 计算输入值的绝对值。                        | Absolute value (per component).          | 1<sup>1</sup>        |
| [acos](http://preview.library.microsoft.com/en-us/library/bb509563) | acos(x)                          | 返回输入值反余弦值。                        | Returns the arccosine of each component of x. | 1<sup>1</sup>        |
| [all](http://preview.library.microsoft.com/en-us/library/bb509564) | all(x)                           | 测试非0值。                            | Test if all components of x are nonzero. | 1<sup>1</sup>        |
| [AllMemoryBarrier](http://preview.library.microsoft.com/en-us/library/ff471350) |                                  |                                   | Blocks execution of all threads in a group until all memory accesses have been completed. | 5                    |
| [AllMemoryBarrierWithGroupSync](http://preview.library.microsoft.com/en-us/library/ff471351) |                                  |                                   | Blocks execution of all threads in a group until all memory accesses have been completed and all threads in the group have reached this call. | 5                    |
| [any](http://preview.library.microsoft.com/en-us/library/bb509565) | any(x)                           | 测试输入值中的任何非零值。                     | Test if any component of x is nonzero.   | 1<sup>1</sup>        |
| [asdouble](http://preview.library.microsoft.com/en-us/library/dd607357) |                                  |                                   | Reinterprets a cast value into a double. | 5                    |
| [asfloat](http://preview.library.microsoft.com/en-us/library/bb509570) | asfloat(x)                       |                                   | Convert the input type to a float.       | 4                    |
| [asin](http://preview.library.microsoft.com/en-us/library/bb509571) | asin(x)                          | 返回输入值的反正弦值。                       | Returns the arcsine of each component of x. | 1<sup>1</sup>        |
| [asint](http://preview.library.microsoft.com/en-us/library/bb509572) | asint(x)                         |                                   | Convert the input type to an integer.    | 4                    |
| [asuint](http://preview.library.microsoft.com/en-us/library/ff471354) |                                  |                                   | Reinterprets the bit pattern of a 64-bit type to a uint. | 5                    |
| [asuint](http://preview.library.microsoft.com/en-us/library/bb509573) | asuint(x)                        |                                   | Convert the input type to an unsigned integer. | 4                    |
| [atan](http://preview.library.microsoft.com/en-us/library/bb509574) | atan(x)                          | 返回输入值的反正切值。                       | Returns the arctangent of x.             | 1<sup>1</sup>        |
| [atan2](http://preview.library.microsoft.com/en-us/library/bb509575) | atan2(y, x)                      | 返回y/x的反正切值。                       | Returns the arctangent of of two values (x,y). | 1<sup>1</sup>        |
| [ceil](http://preview.library.microsoft.com/en-us/library/bb509577) | ceil(x)                          | 返回大于或等于输入值的最小整数。                  | Returns the smallest integer which is greater than or equal to x. | 1<sup>1</sup>        |
| [clamp](http://preview.library.microsoft.com/en-us/library/bb204824) | clamp(x, min, max)               | 把输入值限制在[min, max]范围内。             | Clamps x to the range [min, max].        | 1<sup>1</sup>        |
| [clip](http://preview.library.microsoft.com/en-us/library/bb204826) | clip(x)                          | 如果输入向量中的任何元素小于0，则丢弃当前像素。          | Discards the current pixel, if any component of x is less than zero. | 1<sup>1</sup>        |
| [cos](http://preview.library.microsoft.com/en-us/library/bb509583) | cos(x)                           | 返回输入值的余弦。                         | Returns the cosine of x.                 | 1<sup>1</sup>        |
| [cosh](http://preview.library.microsoft.com/en-us/library/bb509584) | cosh(x)                          | 返回输入值的双曲余弦。                       | Returns the hyperbolic cosine of x.      | 1<sup>1</sup>        |
| [countbits](http://preview.library.microsoft.com/en-us/library/ff471355) |                                  |                                   | Counts the number of bits (per component) in the input integer. | 5                    |
| [cross](http://preview.library.microsoft.com/en-us/library/bb509585) | cross(x, y)                      | 返回两个3D向量的叉积。                      | Returns the cross product of two 3D vectors. | 1<sup>1</sup>        |
| [D3DCOLORtoUBYTE4](http://preview.library.microsoft.com/en-us/library/bb509586) | D3DCOLORtoUBYTE4(x)              |                                   | Swizzles and scales components of the 4D vector xto compensate for the lack of UBYTE4 support in some hardware. | 1<sup>1</sup>        |
| [ddx](http://preview.library.microsoft.com/en-us/library/bb509588) | ddx(x)                           | 返回关于屏幕坐标x轴的偏导数。                   | Returns the partial derivative of x with respect to the screen-space x-coordinate. | 2<sup>1</sup>        |
| [ddx_coarse](http://preview.library.microsoft.com/en-us/library/ff471361) |                                  |                                   | Computes a low precision partial derivative with respect to the screen-space x-coordinate. | 5                    |
| [ddx_fine](http://preview.library.microsoft.com/en-us/library/ff471362) |                                  |                                   | Computes a high precision partial derivative with respect to the screen-space x-coordinate. | 5                    |
| [ddy](http://preview.library.microsoft.com/en-us/library/bb509589) | ddy(x)                           | 返回关于屏幕坐标y轴的偏导数。                   | Returns the partial derivative of x with respect to the screen-space y-coordinate. | 2<sup>1</sup>        |
| [ddy_coarse](http://preview.library.microsoft.com/en-us/library/ff471364) |                                  |                                   | Computes a low precision partial derivative with respect to the screen-space y-coordinate. | 5                    |
| [ddy_fine](http://preview.library.microsoft.com/en-us/library/ff471365) |                                  |                                   | Computes a high precision partial derivative with respect to the screen-space y-coordinate. | 5                    |
| [degrees](http://preview.library.microsoft.com/en-us/library/bb509590) | degrees(x)                       | 弧度到角度的转换                          | Converts x from radians to degrees.      | 1<sup>1</sup>        |
| [determinant](http://preview.library.microsoft.com/en-us/library/bb509591) | determinant(m)                   | 返回输入矩阵的值。                         | Returns the determinant of the square matrix m. | 1<sup>1</sup>        |
| [DeviceMemoryBarrier](http://preview.library.microsoft.com/en-us/library/ff471366) |                                  |                                   | Blocks execution of all threads in a group until all device memory accesses have been completed. | 5                    |
| [DeviceMemoryBarrierWithGroupSync](http://preview.library.microsoft.com/en-us/library/ff471367) |                                  |                                   | Blocks execution of all threads in a group until all device memory accesses have been completed and all threads in the group have reached this call. | 5                    |
| [distance](http://preview.library.microsoft.com/en-us/library/bb509592) | distance(x, y)                   | 返回两个输入点间的距离。                      | Returns the distance between two points. | 1<sup>1</sup>        |
| [dot](http://preview.library.microsoft.com/en-us/library/bb509594) | dot(x, y)                        | 返回两个向量的点积。                        | Returns the dot product of two vectors.  | 1                    |
| [dst](http://preview.library.microsoft.com/en-us/library/ff471368) |                                  |                                   | Calculates a distance vector.            | 5                    |
| [EvaluateAttributeAtCentroid](http://preview.library.microsoft.com/en-us/library/ff471394) |                                  |                                   | Evaluates at the pixel centroid.         | 5                    |
| [EvaluateAttributeAtSample](http://preview.library.microsoft.com/en-us/library/ff471395) |                                  |                                   | Evaluates at the indexed sample location. | 5                    |
| [EvaluateAttributeSnapped](http://preview.library.microsoft.com/en-us/library/ff471396) |                                  |                                   | Evaluates at the pixel centroid with an offset. | 5                    |
| [exp](http://preview.library.microsoft.com/en-us/library/bb509595) | exp(x)                           | 返回以e为底数，输入值为指数的指数函数值。             | Returns the base-e exponent.             | 1<sup>1</sup>        |
| [exp2](http://preview.library.microsoft.com/en-us/library/bb509596) | exp2(x)                          | 返回以2为底数，输入值为指数的指数函数值。             | Base 2 exponent (per component).         | 1<sup>1</sup>        |
| [f16tof32](http://preview.library.microsoft.com/en-us/library/ff471397) |                                  |                                   | Converts the float16 stored in the low-half of the uint to a float. | 5                    |
| [f32tof16](http://preview.library.microsoft.com/en-us/library/ff471399) |                                  |                                   | Converts an input into a float16 type.   | 5                    |
| [faceforward](http://preview.library.microsoft.com/en-us/library/bb509598) | faceforward(n, i, ng)            | 检测多边形是否位于正面。                      | Returns -n * sign(dot(i, ng)).           | 1<sup>1</sup>        |
| [firstbithigh](http://preview.library.microsoft.com/en-us/library/ff471400) |                                  |                                   | Gets the location of the first set bit starting from the highest order bit and working downward, per component. | 5                    |
| [firstbitlow](http://preview.library.microsoft.com/en-us/library/ff471401) |                                  |                                   | Returns the location of the first set bit starting from the lowest order bit and working upward, per component. | 5                    |
| [floor](http://preview.library.microsoft.com/en-us/library/bb509599) | floor(x)                         | 返回小于等于x的最大整数。                     | Returns the greatest integer which is less than or equal to x. | 1<sup>1</sup>        |
| [fmod](http://preview.library.microsoft.com/en-us/library/bb509601) | fmod(x, y)                       | 返回a / b的浮点余数。                     | Returns the floating point remainder of x/y. | 1<sup>1</sup>        |
| [frac](http://preview.library.microsoft.com/en-us/library/bb509603) | frac(x)                          | 返回输入值的小数部分。                       | Returns the fractional part of x.        | 1<sup>1</sup>        |
| [frexp](http://preview.library.microsoft.com/en-us/library/bb509604) | frexp(x, exp)                    | 返回输入值的尾数和指数                       | Returns the mantissa and exponent of x.  | 2<sup>1</sup>        |
| [fwidth](http://preview.library.microsoft.com/en-us/library/bb509608) | fwidth(x)                        | 返回 abs(ddx(x)) + abs(ddy(x)) 。 | Returns abs(ddx(x)) + abs(ddy(x))        | 2<sup>1</sup>        |
| [GetRenderTargetSampleCount](http://preview.library.microsoft.com/en-us/library/bb943996) | GetRenderTargetSampleCount()     |                                   | Returns the number of render-target samples. | 4                    |
| [GetRenderTargetSamplePosition](http://preview.library.microsoft.com/en-us/library/bb943997) | GetRenderTargetSamplePosition(x) |                                   | Returns a sample position (x,y) for a given sample index. | 4                    |
| [GroupMemoryBarrier](http://preview.library.microsoft.com/en-us/library/ff471403) |                                  |                                   | Blocks execution of all threads in a group until all group shared accesses have been completed. | 5                    |
| [GroupMemoryBarrierWithGroupSync](http://preview.library.microsoft.com/en-us/library/ff471404) |                                  |                                   | Blocks execution of all threads in a group until all group shared accesses have been completed and all threads in the group have reached this call. | 5                    |
| [InterlockedAdd](http://preview.library.microsoft.com/en-us/library/ff471406) |                                  |                                   | Performs a guaranteed atomic add of value to the dest resource variable. | 5                    |
| [InterlockedAnd](http://preview.library.microsoft.com/en-us/library/ff471407) |                                  |                                   | Performs a guaranteed atomic and.        | 5                    |
| [InterlockedCompareExchange](http://preview.library.microsoft.com/en-us/library/ff471409) |                                  |                                   | Atomically compares the input to the comparison value and exchanges the result. | 5                    |
| [InterlockedCompareStore](http://preview.library.microsoft.com/en-us/library/ff471410) |                                  |                                   | Atomically compares the input to the comparison value. | 5                    |
| [InterlockedExchange](http://preview.library.microsoft.com/en-us/library/ff471411) |                                  |                                   | Assigns value to dest and returns the original value. | 5                    |
| [InterlockedMax](http://preview.library.microsoft.com/en-us/library/ff471412) |                                  |                                   | Performs a guaranteed atomic max.        | 5                    |
| [InterlockedMin](http://preview.library.microsoft.com/en-us/library/ff471413) |                                  |                                   | Performs a guaranteed atomic min.        | 5                    |
| [InterlockedOr](http://preview.library.microsoft.com/en-us/library/ff471414) |                                  |                                   | Performs a guaranteed atomic or.         | 5                    |
| [InterlockedXor](http://preview.library.microsoft.com/en-us/library/ff471415) |                                  |                                   | Performs a guaranteed atomic xor.        | 5                    |
| [isfinite](http://preview.library.microsoft.com/en-us/library/bb509612) | isfinite(x)                      | 如果输入值为有限值则返回true，否则返回false。       | Returns true if x is finite, false otherwise. | 1<sup>1</sup>        |
| [isinf](http://preview.library.microsoft.com/en-us/library/bb509613) | isinf(x)                         | 如何输入值为无限的则返回true。                 | Returns true if x is +INF or -INF, false otherwise. | 1<sup>1</sup>        |
| [isnan](http://preview.library.microsoft.com/en-us/library/bb509614) | isnan(x)                         | 如果输入值为NAN或QNAN则返回true。            | Returns true if x is NAN or QNAN, false otherwise. | 1<sup>1</sup>        |
| [ldexp](http://preview.library.microsoft.com/en-us/library/bb509616) | ldexp(x, exp)                    | frexp的逆运算，返回 x * 2 ^ exp。         | Returns x * 2exp                         | 1<sup>1</sup>        |
| [length](http://preview.library.microsoft.com/en-us/library/bb509617) | length(v)                        |                                   | Returns the length of the vector v.      | 1<sup>1</sup>        |
| [lerp](http://preview.library.microsoft.com/en-us/library/bb509618) | lerp(x, y, s)                    | 对输入值进行插值计算。                       | Returns x + s(y - x).                    | 1<sup>1</sup>        |
| [lit](http://preview.library.microsoft.com/en-us/library/bb509619) | lit(n • l, n • h, m)             | 返回光照向量（环境光，漫反射光，镜面高光，1）。          | Returns a lighting vector (ambient, diffuse, specular, 1) | 1<sup>1</sup>        |
| [log](http://preview.library.microsoft.com/en-us/library/bb509620) | log(x)                           | 返回以e为底的对数。                        | Returns the base-e logarithm of x.       | 1<sup>1</sup>        |
| [log10](http://preview.library.microsoft.com/en-us/library/bb509621) | log10(x)                         | 返回以10为底的对数。                       | Returns the base-10 logarithm of x.      | 1<sup>1</sup>        |
| [log2](http://preview.library.microsoft.com/en-us/library/bb509622) | log2(x)                          | 返回以2为底的对数。                        | Returns the base-2 logarithm of x.       | 1<sup>1</sup>        |
| [mad](http://preview.library.microsoft.com/en-us/library/ff471418) |                                  |                                   | Performs an arithmetic multiply/add operation on three values. | 5                    |
| [max](http://preview.library.microsoft.com/en-us/library/bb509624) | max(x, y)                        | 返回两个输入值中较大的一个。                    | Selects the greater of x and y.          | 1<sup>1</sup>        |
| [min](http://preview.library.microsoft.com/en-us/library/bb509625) | min(x, y)                        | 返回两个输入值中较小的一个。                    | Selects the lesser of x and y.           | 1<sup>1</sup>        |
| [modf](http://preview.library.microsoft.com/en-us/library/bb509627) | modf(x, out ip)                  | 把输入值分解为整数和小数部分。                   | Splits the value x into fractional and integer parts. | 1<sup>1</sup>        |
| [mul](http://preview.library.microsoft.com/en-us/library/bb509628) | mul(x, y)                        | 返回输入矩阵相乘的积。                       | Performs matrix multiplication using x and y. | 1                    |
| [noise](http://preview.library.microsoft.com/en-us/library/bb509629) | noise(x)                         |                                   | Generates a random value using the Perlin-noise algorithm. | 1<sup>1</sup>        |
| [normalize](http://preview.library.microsoft.com/en-us/library/bb509630) | normalize(x)                     | 返回规范化的向量，定义为 x / length(x)。       | Returns a normalized vector.             | 1<sup>1</sup>        |
| [pow](http://preview.library.microsoft.com/en-us/library/bb509636) | pow(x, y)                        | 返回输入值的指定次幂。                       | Returns xy.                              | 1<sup>1</sup>        |
| [Process2DQuadTessFactorsAvg](http://preview.library.microsoft.com/en-us/library/ff471426) |                                  |                                   | Generates the corrected tessellation factors for a quad patch. | 5                    |
| [Process2DQuadTessFactorsMax](http://preview.library.microsoft.com/en-us/library/ff471427) |                                  |                                   | Generates the corrected tessellation factors for a quad patch. | 5                    |
| [Process2DQuadTessFactorsMin](http://preview.library.microsoft.com/en-us/library/ff471428) |                                  |                                   | Generates the corrected tessellation factors for a quad patch. | 5                    |
| [ProcessIsolineTessFactors](http://preview.library.microsoft.com/en-us/library/ff471429) |                                  |                                   | Generates the rounded tessellation factors for an isoline. | 5                    |
| [ProcessQuadTessFactorsAvg](http://preview.library.microsoft.com/en-us/library/ff471430) |                                  |                                   | Generates the corrected tessellation factors for a quad patch. | 5                    |
| [ProcessQuadTessFactorsMax](http://preview.library.microsoft.com/en-us/library/ff471431) |                                  |                                   | Generates the corrected tessellation factors for a quad patch. | 5                    |
| [ProcessQuadTessFactorsMin](http://preview.library.microsoft.com/en-us/library/ff471432) |                                  |                                   | Generates the corrected tessellation factors for a quad patch. | 5                    |
| [ProcessTriTessFactorsAvg](http://preview.library.microsoft.com/en-us/library/ff471433) |                                  |                                   | Generates the corrected tessellation factors for a tri patch. | 5                    |
| [ProcessTriTessFactorsMax](http://preview.library.microsoft.com/en-us/library/ff471434) |                                  |                                   | Generates the corrected tessellation factors for a tri patch. | 5                    |
| [ProcessTriTessFactorsMin](http://preview.library.microsoft.com/en-us/library/ff471435) |                                  |                                   | Generates the corrected tessellation factors for a tri patch. | 5                    |
| [radians](http://preview.library.microsoft.com/en-us/library/bb509637) | radians(x)                       | 角度到弧度的转换。                         | Converts x from degrees to radians.      | 1                    |
| [rcp](http://preview.library.microsoft.com/en-us/library/ff471436) |                                  |                                   | Calculates a fast, approximate, per-component reciprocal. | 5                    |
| [reflect](http://preview.library.microsoft.com/en-us/library/bb509639) | reflect(i, n)                    | 返回入射光线i对表面法线n的反射光线。               | Returns a reflection vector.             | 1                    |
| [refract](http://preview.library.microsoft.com/en-us/library/bb509640) | refract(i, n, R)                 | 返回在入射光线i，表面法线n，折射率为eta下的折射光线v。    | Returns the refraction vector.           | 1<sup>1</sup>        |
| [reversebits](http://preview.library.microsoft.com/en-us/library/ff471437) |                                  |                                   | Reverses the order of the bits, per component. | 5                    |
| [round](http://preview.library.microsoft.com/en-us/library/bb509642) | round(x)                         | 返回最接近于输入值的整数。                     | Rounds x to the nearest integer          | 1<sup>1</sup>        |
| [rsqrt](http://preview.library.microsoft.com/en-us/library/bb509643) | rsqrt(x)                         | 返回输入值平方根的倒数。                      | Returns 1 / sqrt(x)                      | 1<sup>1</sup>        |
| [saturate](http://preview.library.microsoft.com/en-us/library/bb509645) | saturate(x)                      | 把输入值限制到[0, 1]之间。                  | Clamps x to the range [0, 1]             | 1                    |
| [sign](http://preview.library.microsoft.com/en-us/library/bb509649) | sign(x)                          | 计算输入值的符号。                         | Computes the sign of x.                  | 1<sup>1</sup>        |
| [sin](http://preview.library.microsoft.com/en-us/library/bb509651) | sin(x)                           | 计算输入值的正弦值。                        | Returns the sine of x                    | 1<sup>1</sup>        |
| [sincos](http://preview.library.microsoft.com/en-us/library/bb509652) | sincos(x, out s, out c)          | 返回输入值的正弦和余弦值。                     | Returns the sine and cosine of x.        | 1<sup>1</sup>        |
| [sinh](http://preview.library.microsoft.com/en-us/library/bb509653) | sinh(x)                          | 返回x的双曲正弦。                         | Returns the hyperbolic sine of x         | 1<sup>1</sup>        |
| [smoothstep](http://preview.library.microsoft.com/en-us/library/bb509658) | smoothstep(min, max, x)          | 返回一个在输入值之间平稳变化的插值。                | Returns a smooth Hermite interpolation between 0 and 1. | 1<sup>1</sup>        |
| [sqrt](http://preview.library.microsoft.com/en-us/library/bb509662) | sqrt(x)                          | 返回输入值的平方根。                        | Square root (per component)              | 1<sup>1</sup>        |
| [step](http://preview.library.microsoft.com/en-us/library/bb509665) | step(a, x)                       | 返回（x >= a）? 1 : 0。                | Returns (x >= a) ? 1 : 0                 | 1<sup>1</sup>        |
| [tan](http://preview.library.microsoft.com/en-us/library/bb509670) | tan(x)                           | 返回输入值的正切值。                        | Returns the tangent of x                 | 1<sup>1</sup>        |
| [tanh](http://preview.library.microsoft.com/en-us/library/bb509671) | tanh(x)                          |                                   | Returns the hyperbolic tangent of x      | 1<sup>1</sup>        |
| [tex1D(s, t)](http://preview.library.microsoft.com/en-us/library/bb509672) |                                  | 1D纹理查询。                           | 1D texture lookup.                       | 1                    |
| [tex1D(s, t, ddx, ddy)](http://preview.library.microsoft.com/en-us/library/ff471388) |                                  |                                   | 1D texture lookup.                       | 2<sup>1</sup>        |
| [tex1Dbias](http://preview.library.microsoft.com/en-us/library/bb509673) | tex1Dbias(s, t)                  |                                   | 1D texture lookup with bias.             | 2<sup>1</sup>        |
| [tex1Dgrad](http://preview.library.microsoft.com/en-us/library/bb509674) | tex1Dgrad(s, t, ddx, ddy)        |                                   | 1D texture lookup with a gradient.       | 2<sup>1</sup>        |
| [tex1Dlod](http://preview.library.microsoft.com/en-us/library/bb509675) | tex1Dlod(s, t)                   |                                   | 1D texture lookup with LOD.              | 3<sup>1</sup>        |
| [tex1Dproj](http://preview.library.microsoft.com/en-us/library/bb509676) | tex1Dproj(s, t)                  |                                   | 1D texture lookup with projective divide. | 2<sup>1</sup>        |
| [tex2D(s, t)](http://preview.library.microsoft.com/en-us/library/bb509677) |                                  | 2D纹理查询。                           | 2D texture lookup.                       | 1<sup>1</sup>        |
| [tex2D(s, t, ddx, ddy)](http://preview.library.microsoft.com/en-us/library/ff471389) |                                  |                                   | 2D texture lookup.                       | 2<sup>1</sup>        |
| [tex2Dbias](http://preview.library.microsoft.com/en-us/library/bb509678) | tex2Dbias(s, t)                  |                                   | 2D texture lookup with bias.             | 2<sup>1</sup>        |
| [tex2Dgrad](http://preview.library.microsoft.com/en-us/library/bb509679) | tex2Dgrad(s, t, ddx, ddy)        |                                   | 2D texture lookup with a gradient.       | 2<sup>1</sup>        |
| [tex2Dlod](http://preview.library.microsoft.com/en-us/library/bb509680) | tex2Dlod(s, t)                   |                                   | 2D texture lookup with LOD.              | 3                    |
| [tex2Dproj](http://preview.library.microsoft.com/en-us/library/bb509681) | tex2Dproj(s, t)                  |                                   | 2D texture lookup with projective divide. | 2<sup>1</sup>        |
| [tex3D(s, t)](http://preview.library.microsoft.com/en-us/library/bb509682) |                                  | 3D纹理查询。                           | 3D texture lookup.                       | 1<sup>1</sup>        |
| [tex3D(s, t, ddx, ddy)](http://preview.library.microsoft.com/en-us/library/ff471391) |                                  |                                   | 3D texture lookup.                       | 2<sup>1</sup>        |
| [tex3Dbias](http://preview.library.microsoft.com/en-us/library/bb509683) | tex3Dbias(s, t)                  |                                   | 3D texture lookup with bias.             | 2<sup>1</sup>        |
| [tex3Dgrad](http://preview.library.microsoft.com/en-us/library/bb509684) | tex3Dgrad(s, t, ddx, ddy)        |                                   | 3D texture lookup with a gradient.       | 2<sup>1</sup>        |
| [tex3Dlod](http://preview.library.microsoft.com/en-us/library/bb509685) | tex3Dlod(s, t)                   |                                   | 3D texture lookup with LOD.              | 3<sup>1</sup>        |
| [tex3Dproj](http://preview.library.microsoft.com/en-us/library/bb509686) | tex3Dproj(s, t)                  |                                   | 3D texture lookup with projective divide. | 2<sup>1</sup>        |
| [texCUBE(s, t)](http://preview.library.microsoft.com/en-us/library/bb509687) |                                  | 立方纹理查询。                           | Cube texture lookup.                     | 1<sup>1</sup>        |
| [texCUBE(s, t, ddx, ddy)](http://preview.library.microsoft.com/en-us/library/ff471392) |                                  |                                   | Cube texture lookup.                     | 2<sup>1</sup>        |
| [texCUBEbias](http://preview.library.microsoft.com/en-us/library/bb509688) | texCUBEbias(s, t)                |                                   | Cube texture lookup with bias.           | 2<sup>1</sup>        |
| [texCUBEgrad](http://preview.library.microsoft.com/en-us/library/bb509689) | texCUBEgrad(s, t, ddx, ddy)      |                                   | Cube texture lookup with a gradient.     | 2<sup>1</sup>        |
| [texCUBElod](http://preview.library.microsoft.com/en-us/library/bb509690) |                                  |                                   | Cube texture lookup with LOD.            | 3<sup>1</sup>        |
| [texCUBEproj](http://preview.library.microsoft.com/en-us/library/bb509691) | texCUBEproj(s, t)                |                                   | Cube texture lookup with projective divide. | 2<sup>1</sup>        |
| [transpose](http://preview.library.microsoft.com/en-us/library/bb509701) | transpose(m)                     | 返回输入矩阵的转置。                        | Returns the transpose of the matrix m.   | 1                    |
| [trunc](http://preview.library.microsoft.com/en-us/library/cc308065) | trunc(x)                         |                                   | Truncates floating-point value(s) to integer value(s) | 1                    |


参考链接

- [每天30分钟看Shader--(1)HLSL固有函数 【Intrinsic Functions (DirectX HLSL)】](http://www.cppblog.com/lai3d/archive/2008/10/23/64889.html)

