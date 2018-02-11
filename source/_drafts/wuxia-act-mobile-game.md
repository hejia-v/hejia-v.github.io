---
title: 武侠动作手游初稿(个人向)
date: 2018-02-09 21:18:33
updated: 2018-02-09 21:18:33
tags: game
categories: game
---

假日里闲来无事，回顾了一下自己掌握的知识，根据自己已有的技术储备，整理了一下开发一款武侠动作手游的方方面面。我并非专业策划，写下这篇文章，依据的是之前的开发经验和阅历，以及体验过的一些游戏，难免会有一些不合理之处，这些还恳请小伙伴们多多指教。本文并非策划文档，也不详谈技术，大致相当于一个大纲，对游戏的开发做一个总览，需要做些什么，目前能做到什么样的程度，心里先有一个底。

<!--more-->

## 题材和类型
选择武侠这题材，一方面自己喜欢武侠，并且我对武侠可以说是相当的熟悉了，从小到大看过的武侠小说数不胜数，容易驾驭，比较稳，同时，能够获取到的参考和素材也相当的多；另一方面，个人认为武侠这个题材的市场还是比较广的，这从国内游戏的题材分布可以看出。

选择偏动作的游戏类型，个人认为，一个优秀的即时战斗系统才可以比较好的表现出武侠里的刀光剑影、快意恩仇；自己也比较喜欢偏动作的游戏，开发3d Act一直是自己的夙愿和执念，嘿嘿。

## 世界观
先定下世界观，然后确定大致的编年史，然后定下故事线。

目前我初步是这么设定的，游戏发生在一个架空的时代，时间点在唐朝之后，大概是五代时期。当然既然架空了，和历史肯定是不太一样的，这样设定的原因，一方面是对五代历史了解的人不多，方便胡乱瞎编，另一方面，五代之后的宋朝是武侠小说非常集中的时代，可以方便剧情的后续扩展。

故事的起点是一次陨石坠落事件，陨石坠落事件带来了一种非常奇特的物质，在后续的剧情里，这种物质被发现是可以再生的。它的作用有这么几种：1. 赋予武侠中的内力更多的属性，这个可以参考《沧海》里的周流六劲，或者是一些超能力战斗漫画里的设定。 2. 充当游戏世界里的动力能源，甚至可以让它取代蒸汽机的作用。 3. 让游戏世界变得更加奇幻，但又说得通。

文案方面，个人比较喜欢流畅一些的文笔，例如马舸的文风：
> 二人沿山道下行，走了多时，来到一处涧桥边。那老僧眼望仙山幽美，恍如幻境，忽停步一叹，语含失望道：“我来此山，本欲一会当世‘真人’，可惜张全一修为虽高，却只能算半个‘真人’。”尚瑞生心中诧异，问道：“难道老师还当不得‘真人’二字？”那老僧摇了摇头，举目望天道：“果‘真人’者，无虚妄，无偶像，傲立天地，看破生死，蔑笑神佛。知‘因果’之无稽，洞人智之有穷。不悲不狂，永爱人生之风景；大真大痴，唯珍一世之运命。此才是人的生涯，可惜这人我看不到了！你有这样的后人，虽死亦如永生，连老衲也要羡慕了。”（《幻真缘》）


温婉一点的可以这样：
> 想到这一节，我心中已经雪亮，梁凉早就算好这一扑，我刚才岳阳楼吃饭喝茶动武，都是惯用右手，若用左手一定慢了一点而且不灵活，所以刚才故意站在左边，让右侧的我只能出左手，已是先赢了七分，更何况我生性喜洁，随随便便扑在地上，心里有所犹豫，出手自然又慢了些许，这也不能算他作弊，倒是我吃了哑巴亏。（《横吹洞萧》）

不过具体的实施还是得看情况。


## 技术选型
客户端引擎使用Unity，开发方便，资源丰富，易于扩展，跨平台容易，好处是显而易见的。将来web端如果真崛起了，那时用的应该是webassembly之类的技术，显然Unity是可以支持的。

游戏服务器采用C#语言，前后端都使用ET框架，分布式和组件式的设计十分适合本类型游戏。自己也已经实现了在C#中嵌入CPython，对于需要使用Python做算法的模块，可以直接用C#封装成组件并挂载到游戏服务器上。

游戏服务器的web控制台，支付服务器，辅助服务器，分析工具，各种脚本，全部使用Python编写，毕竟在小型项目里，Python的开发效率无与伦比。

如果存在性能压力比较大的地方，就使用C/C++实现，再导出到C#或Python中。

## 开发规划
开发分三个阶段吧：原型 -> 初版 -> 版本迭代

原型：
这是项目的开荒阶段，也是最艰苦的阶段。在我看来，要完成以下几点：
- 定下渲染技术，确定基本的画面基调，准备好场景和角色需要用到的范例材质和着色器。
- 制作好至少一个通用角色，基本上要包含80%的角色特性，头发，布料，绑定，物理等都要弄好。
- 制作好敌兵的各式基本AI行为。
- 制作好基本的技能系统和战斗系统，需要支持pvp的1v1和pve。
- 前后端同步进行，ET框架比较好的一点在于，某种程度上是开箱即用，全栈开发，前后端无缝结合。

由于只是技术验证，模型和动作等使用网上流传的资源就可以了。先做出一个可玩的原型，边玩边体验边调整，逐步迭代，C#是强类型语言，重构起来也是十分轻松愉快的。原型阶段尤为重要，毕竟即时制战斗，口说无凭，只有体验了，才可以定下接下来的调整方向。这个没做好，后续的无从谈起。

虽说这类游戏的demo、源码一大把，其实含金量大多数都不咋地，要做出自己的特色不那么容易，想做成自己心目中的完美效果更难，还是要有一定的妥协的，看自己的权衡和取舍吧。

初版：
这是第一个上线的版本。在原型的基础上，丰富各项游戏功能，达到一个比较高的完成度。这时也要避免同质化的问题，找到自己的定位和特色。

版本迭代：
初版的表现不错的话，那么就要开始不断更新版本了。至少我自己就挺喜欢这类游戏的，成绩不好肯定有原因，完成度不高？画面不好？体验不好？表现力不行？战斗不爽快？数值不合理？难度不合理？卡顿？粘度太差？出现新游戏了？。。。总之，抱着做ip的心，万一成了呢，这个世界观，我觉得不错的。

## 画面风格
画面采用卡通风格，使用 cel(赛璐璐) 渲染技术。目前市场上的崩坏3、桃源乡等二次元手游采用的都是这种风格，如图：
![cel-rendering-3](/images/act/cel-rendering-3.png)
![cel-rendering-4](/images/act/cel-rendering-4.png)
![cel-rendering-2](/images/act/cel-rendering-2.png)

采用这种画面风格，一方面这种画面确实好看，另一方面，避免同质化，避开和大厂的竞争。

我已经研究过一段时间这种渲染技术，花了不少精力收集这方面的资料：公开的技术分享，技术博客，shader源码，paper，youtube视频，工程文件等。

总体来说，实现这种卡通渲染不算难，网上的工程一大把，但这种非真实渲染技术太过tricky，画面好坏的评判主要依据的是人的主观，需要根据具体的项目进行针对性开发。

毕竟画面是游戏的脸面，在我对画面的需求中，想要线条更光滑一点，而不是常见到多边形状，勾线更细腻一点，线条更多一点，高光和阴影的层数更多一点，层次感更强一点，漫画风的感官更强烈一点，指不定还得加上后期(post process)，同时还得兼顾到手机的性能消耗。要达成这些，还需要花时间来研究。

至于画风这方面，使用真人比例，《刀剑异闻录》这部漫画比较对我的胃口，原画方面可以试试在[米大师](https://www.mihuashi.com)约稿。

其实如果不是非得要按自己的想法来，现在已经有这么几个现存的方案：
1. Asset Store的[RealToon (PC/MAC & Mobile)](https://assetstore.unity.com/packages/vfx/shaders/realtoon-pc-mac-mobile-65518)，效果如下：
    ![cel-rendering-1](/images/act/cel-rendering-1.png)

2. [Pencil+ 4 for unity](https://www.psoft.co.jp/jp/product/pencil/unity/)，这个是pencil+的unity版，价格小贵，购买起来还比较麻烦，实际的性能消耗也不清楚，好像国内还没有谁在用。
    ![UnityChang_Line](/images/act/UnityChang_Line.png)

3. Unity Chan Toon Shader，这个手头已有源码，效果如下：
    ![cel-rendering-5](/images/act/cel-rendering-5.png)

总之，做的时候，看看同类产品到了什么样的水平，既不能掉队，也最好不要在细节上死磕。


## 用户界面
用户界面主体上使用简约风格，可以参考国外单机游戏。

下面这个是刺客信条ios版，可以看看：
http://www.bilibili.com/video/av19424264/
下面这个的角色控制做得比较不错
http://www.bilibili.com/video/av19424408/


主界面按钮太多时，可以做一个一级按钮和一个快速按钮，按下一级按钮时呼出环形菜单，然后点击里面的按钮，进行相应操作，快速按钮自动切换成上一次点击的二级按钮，方便再次点击上次点击的按钮。

提示系统需要做好一点，刺客信条ios版做得就比较好，根据当前的状态和环境，自动弹出提示和按钮。我甚至觉得吃药等类似操作的按钮都可以做成根据状态自动显示和隐藏。

角色的标记，卡片的流光，技能按钮的cd，红蓝球/条等细节效果，基本上都找得到实现，无需太多担心。

场景的切换需要有Camera Fade效果，UI界面需要有进场和退场的效果。UI界面在实现时会大量使用行为树，将各种效果做成行为节点，这样不用写一行代码，只需连接行为节点和修改节点参数，就可以轻松的调整UI了，极大的提升效率，如下图：
![ui-1](/images/act/ui-1.png)

技能按钮暂时先参考手游通行的摆放方式，跟随战斗系统的开发，不断调整，看是使用双摇杆还是多级按钮啥的。

本游戏的定位不是mmo，至少在初版不是，没有大世界，进入游戏后，玩家在一个屋子里，可以在屋子里活动，屋子里的一些物件，例如炉子，门，窗子等代表一些玩法的入口，与这些入口交互后，可进入相应的玩法。

手头收集有一些UI界面，可以参考参考：
![ui-2](/images/act/ui-2.gif)
![ui-3](/images/act/ui-3.png)
![ui-4](/images/act/ui-4.png)
![ui-5](/images/act/ui-5.png)
![ui-6](/images/act/ui-6.png)
![ui-7](/images/act/ui-7.png)
![ui-8](/images/act/ui-8.png)
![ui-9](/images/act/ui-9.png)
![ui-10](/images/act/ui-10.png)
![ui-11](/images/act/ui-11.png)
![ui-12](/images/act/ui-12.png)
![ui-13](/images/act/ui-13.png)

## 捏脸系统
avatar。gif   unity\GAC
对这些公共统筹这组合，并加入自己的思考
    unity\Unity5Tree
截图！！！todo  摄像机摆一下

The-Custom-Character-Kit-v1.2

有参考的实现，尽管不怎么地，但总好过自己从头摸索
天刀 太白的 绑定 很值得一看 特别是头部的 那个
Unity5Tree ========================================================

## 城建
地图，不是事

避免与楚留香等重型mmo重叠，
战斗初版抄天刀，双摇杆，晶体管指令，迭代中往act靠，安全一些

第一版就一个主城，故事读发生在这里，妖猫传唐城挺不错，手上部分模型亮出来
## 酒馆

## 剧情副本

## 战斗系统
combat那个要手机截图
unity\TouchKit  触摸管理可以用用


状态同步的基础上，加上帧同步的技术，有点类似当年做的战斗本地化，c/s同一种语言，可以代码共享，并且框架一致，因此做起来还是比较靠谱的。应该是可行的。
http://blog.csdn.net/chrisfxs/article/details/73655934
http://bbs.gameres.com/thread_335685_1_1.html
## 导表

下图只起一个示范作用，胡乱填的，具体内容与本游戏无关
道具导表
![table-1](/images/act/table-1.png)
装备导表
![table-2](/images/act/table-2.png)
新手指引导表
![table-3](/images/act/table-3.png)

## 常用模块


乐趣在于战斗

语音转换文字，打本，不上传音频

并不算mmo, 有部分mmo功能，没有大世界
https://www.zybuluo.com/mdeditor#385343
这里简单列一下，可能还不止
将领界面
道具界面
改名界面
角色信息
成就系统
声望系统
任务系统
联盟界面
军团界面
帮会
阵营
道具合成与分解
建筑: 太学院、兵营、校场铁匠铺等
一些界面的链接，任务、将领等
家园系统

自由度比较高的玩法
围攻，  不过这是后话了

## 日程表
每天的活动，每天不一样，获取不同的材料

## 小活动
打地鼠
英雄之路
守卫剑阁
连连看
作为一个调味剂吧
## 聊天
游戏内发红包？

可否与微信互通
可否微创新
## 助手系统
新手引导
UI再设计的时候就要考虑引导层，强制式的，触发式，
帮助系统，聊天机器人，有开源实现，
个人助手类的，单独的开一个python server，自己已经实现了C# python互通，作为一个组件，就算单独作为进程，io也要消耗性能
助手的智力，需要月卡可以提升？，部分功能需要月卡开启

做一个人形助手，在特定的情况下，提示活动，啥的，可以互动
## 机器学习
利用神经网络提升表现力
适时的利用神经网络
结合物理系统，提升表现力
这个需要观察，
受击反映，动作流畅，平滑等
nn-horses
unity\NeuralHorses
如下便是神经网络具体效果的例子

没有nn之前，传统ai为主
少量的ai可以考虑神经网络，当然根据具体情况判断，是否真的有用，有没有简单的替代方案，缩减工期

## 资源规划

## 服务器控制台
参考kbe, 慢慢完善吧，Django
敏捷开发

## 调试
gm
包括调试log等

## 渠道接入
手绘icon，个人偏好
图片范例，icon，作用，用户画像

u8 sdk

python server
## 特色点
同质化太严重，从画面上找突破口？这是一个方向
## 竞争力
剧情，cel,特色打斗
---


楚留香没细完，但估计很接近pc mmo了

kbe功能更完善，更多的mmo逻辑，但比较复杂，大型项目中python不如有C#，但可以参考里面的同步策略
使用状态同步，dota2就是的，高时实是可以做的，但帧同步里的一些思想可以借用，比如实现pk录像回放等


进阶功能：帮战等,势力,,


中型，特色，

agent基本行为列出来


技术选型
服务器，3d体素，支持轻功

产品定位


偏动作，

不谈实现细节，只列出实现的大致方向，具体开发模式和方法

核心是主城和战斗，附带一点场景破坏，小幅度随机地图
技术细节就不多说了，网上很多技术分享，也需要在实际开发时，实际调整

引导(触发条件)，道具装备部分，execel->unity data->unity gui/graph->并且可以回馈覆写excel,有版本管理嘛，svn管理，放在unity外面
client/server公用数据代码，直接在unity的gui中调数据，连服务器的填表工具都省了
附上导表截图,不尽详细,实际上的参数没这么简单，但数据结构上是这样的，示例而已，根据实际情况细调

nvn没想好，重点1v1排位和pve

老式mmo赤壁里酒馆的作用，扭蛋

战斗时，幻境，鬼泣5那种

港片的打斗
特色就是1v1和cel，需要加强效果并突出



战斗部分，带上ai的图


剑，刀，锁链，镖
初版时，故事的时间线比较早期
太过奇幻的技能，以后再考虑吧


音效，暂时就拿来主义吧
音乐，按时长计价吧，看情况
act,看情况，实在做不好，再。。。，难点在于找动作素材
model:手头已有，先调试好，尾声时，wb做几个,作为模板，使用一程序生成的功能，毕竟blender的script那么方便，生成

Raven-- 3d server可参考这个，网格导航，目标的侦测和攻击,虽说战斗系统不同，但大多数还是相通的，毕竟大部分ai逻辑还是在server,部分ai计算由client分担，分布式，但并不是计算当前图的ai，这个需要考虑，安全性，
项目后期，server控制台，web, 直接把这些节点图投放到web上


========================================
手机 屏幕投射到pc



城建直接copy设计就可以，不需要啥美术素养，并且可以程序化生成，参考mc，参考garden，贴图都省了，或者进行贴图简化，参考一下彩漫，，极大的降低了成本

如果是2d原画，米大师，3d的话，其实手上积累了一些高精度游戏模型，也琢磨过，再找吧，就一个主城，很多是可以程序化的，,建筑参考mc，植被模型随手拈来，幡子等小物件需要绘图，需求量不会太大，五个英雄角色吧，玩家是自定义的。并且是赛璐璐cel风格，精度要求不会太高，
动作的话，需要考虑一下，-------1. 网上提取的，动作库，blender好写py脚本，转到blender，可以画故事稿(截图)，调试。3. youtube绑定教程数不胜数，自己就绑过，也有自动脚本  2. 其他游戏zuzhen抓取，并key 2. 根据一些影片，序列帧，武术示范图谱，用脚本导到blender, 手key
2d特效 手头有一点，原型阶段可以自己先用着，也可以找美术
剑无声 的采访  桃源乡
行为树主导的开发, 观察一下就知道，根据我之前的开发经验，所谓的剧情副本，就是用编辑器编辑出来的，ai行为是节点，连节点图就行，切换一下地图，换一下敌人，换一下台词，基本上就是一个剧情了，拖游戏时长。做复杂点，就参考一下 武侠小说中的阵法，斗阵，印象比较深刻的是萧逸的无忧公主中，几个阵法比较不错，糅合真实空间和心理幻想空间，比较出彩，可以做成多人剧情副本
3d主力软件 blender

提一下意见嘛

技术验证 阶段

酒馆，交到的友，在主城大逃杀玩法中用到
1v1 全天开放
nvn 黄金时间段开放


把 代码 还原回来
c
重型mm接近pc的剧情演出
bh3都没有
独立的小游戏，动作库
轻型动作手游，和楚留香的差异在哪，貌似只有cel渲染
楚留香，基本上就是手机版的天刀了
担忧，已有同类游戏，貌似只有画风这条，但这条到底有多大作用，真不清楚
我是这么认为，有大店，也有小店，不能说完全不能做，文案古艳一点，来一段


原型版本战斗的 要点列出来，技术指标，第一个可玩版本，其他的技能衔接等延后再说，更复杂的

gm命令
支持服务器，客服端，条件编译，

机核网采访 剑无生
东离剑游记 剑术 特效 白光，武戏不错
东离剑游纪 生死一剑
霹雳 可以找到一些灵感




全局实时光照

资源规划
初期其实对资源的需求不大，

音效
音乐
原画
模型，先看看模型库里有没有合适的，贴图外包，数量不会太多，一般在项目尾声换皮
特效-》和shader，自己搞定，教程太多了，就算是找外包，也未必如自己意，2d贴图其实素材也很多实在复杂的纹理不好可以找外包，，如果没有素材，就做外包吧
要不了啥专业训练

九yin也有人玩呢，jiuyin 如何发家的
当年coc有那么多，有些过得也挺致润的

既然喜欢，那就去做吧






天刀技能/战斗系统设
崩坏3
忍龙
鬼泣
剑网3明教绳索轻功
技能、战斗设计，节点树，slot
武侠剑术动作、湘潭的那个


* [SnpM/LockstepFramework: Framework for lockstep RTS, TD, and MOBA games. Under development.](https://github.com/SnpM/LockstepFramework)
* [尼尔机械纪元 特效 制作 - Google 搜索](https://www.google.co.jp/search?q=%E5%B0%BC%E5%B0%94%E6%9C%BA%E6%A2%B0%E7%BA%AA%E5%85%83+%E7%89%B9%E6%95%88+%E5%88%B6%E4%BD%9C&ei=fYVxWpD7C4eq0QTG1r4o&start=60&sa=N&biw=1425&bih=552)
* [《王者荣耀》技术总监复盘回炉历程：没跨过这三座大山，就是另一款MOBA霸占市场了-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/30902)
* [经验：《王者荣耀》技术总监分享背后技术_18183产业频道](http://chanye.18183.com/201709/942254.html)
* [Meet PlatinumGames’ NieR:Automata team! Part 2 | PlatinumGames Official Blog](https://www.platinumgames.com/official-blog/article/9018)
* [ninja gaiden mechanism - Google 搜索](https://www.google.co.jp/search?q=ninja+gaiden+mechanism&ei=xuRyWqCXE4Ty8QWJ0ovACA&start=20&sa=N&biw=1425&bih=552)
* [云风的 BLOG: 浅谈《守望先锋》中的 ECS 构架](https://blog.codingnow.com/2017/06/overwatch_ecs.html)
* [云风的 BLOG: 游戏动作感设计初探](https://blog.codingnow.com/2009/09/action_game.html)
* [动作手游实时PVP帧同步方案（客户端） - CSDN博客](http://blog.csdn.net/qq_27880427/article/details/52692772)
* [(8 条消息)为什么现在没有忍者龙剑传这样的硬派ACT了？ - 知乎](https://www.zhihu.com/question/66071494)
* [忍龙2的动作设计和战斗体验至今没有任何一个游戏比得过吧？【ps4吧】_百度贴吧](https://tieba.baidu.com/p/4943159195?red_tag=1903705776)
* [实例综述：动作游戏的战斗系统设计-GameRes游资网](http://bbs.gameres.com/thread_466339.html)
* [【视频】这个游戏的战斗系统或许可以媲美忍龙 ，难度也是很高【忍者龙剑传吧】_百度贴吧](https://tieba.baidu.com/p/5085824495?red_tag=1714894227)
* [(8 条消息)忍者龙剑传，战神，鬼泣的打击手感有何不同？ - 知乎](https://www.zhihu.com/question/23261204)
* [忍龙战斗系统详细解读_忍龙热门攻略_40407网页游戏](https://www.40407.com/news/201301/202231.html)
* [帧同步中，如何网络不好，具体该如何平滑位移-GAD腾讯游戏开发者平台](http://gad.qq.com/question/detail/32699)
* [MMO技能系统的同步机制分析-GameRes游资网](http://www.gameres.com/729629.html)
* [(8 条消息)MOBA类游戏是如何解决网络延迟同步的？ - 知乎](https://www.zhihu.com/question/36258781)
* [(8 条消息)大型多人在线游戏的开发中，如何做到每个玩家动作的实时同步的？ - 知乎](https://www.zhihu.com/question/27765214/answer/175391133)
* [(8 条消息)MMORPG的战斗在副本中使用帧同步方式的可行性，及是否有先例？ - 知乎](https://www.zhihu.com/question/57896810/answer/214952099)
* [游戏网络同步——MMO位置同步 - lovemysea的专栏 - CSDN博客](http://blog.csdn.net/lovemysea/article/details/72825693)
* [MMO技能系统的同步机制分析 - Bill Yuan - 博客园](https://www.cnblogs.com/sevenyuan/p/6678317.html)
* [实时pvp（皇室战争）网络同步研究 - CSDN博客](http://blog.csdn.net/langresser_king/article/details/51330543)
* [Blender Documentation Contents — Blender 2.79.0 855d2955c49 - API documentation](https://docs.blender.org/api/2.79/)
* [素描的诀窍 (豆瓣)](https://book.douban.com/subject/1154707/)
* [千人千面如何炼成 技术讲解捏脸系统设计原理-新浪天涯明月刀专区](http://games.sina.com.cn/o/z/wuxia/2015-10-15/fxivsch3599438.shtml)
* [uhlik/bpy: blender python scripts](https://github.com/uhlik/bpy)
* [剑三（95版本）和天刀的战斗数值体系架构-GameRes游资网](http://www.gameres.com/674240.html)
* [天涯明月刀 技术 战斗系统_百度搜索](https://www.baidu.com/s?wd=%E5%A4%A9%E6%B6%AF%E6%98%8E%E6%9C%88%E5%88%80%20%E6%8A%80%E6%9C%AF%20%E6%88%98%E6%96%97%E7%B3%BB%E7%BB%9F&pn=40&oq=%E5%A4%A9%E6%B6%AF%E6%98%8E%E6%9C%88%E5%88%80%20%E6%8A%80%E6%9C%AF%20%E6%88%98%E6%96%97%E7%B3%BB%E7%BB%9F&ie=utf-8&rsv_idx=1&rsv_pq=b91a102100005961&rsv_t=f991BKmg5J9LA2p%2BZ6AeCQVG4SOMVQUP3AcD0kfREJrK5sG2AVLk8u%2BkFu8&rsv_page=1)
* [鬼泣 技术 战斗系统_百度搜索](https://www.baidu.com/s?wd=%E9%AC%BC%E6%B3%A3%20%E6%8A%80%E6%9C%AF%20%E6%88%98%E6%96%97%E7%B3%BB%E7%BB%9F&pn=30&oq=%E9%AC%BC%E6%B3%A3%20%E6%8A%80%E6%9C%AF%20%E6%88%98%E6%96%97%E7%B3%BB%E7%BB%9F&ie=utf-8&rsv_pq=91116ec70001f0dc&rsv_t=544eTrjKSBo5BOWeoJok%2Bp6J9HPvzismB4bGfCglyBsMr5EYi8x32RZrlmU&rsv_page=1)
* [忍龙 战斗系统 反推_百度搜索](https://www.baidu.com/s?ie=UTF-8&wd=%E5%BF%8D%E9%BE%99%20%E6%88%98%E6%96%97%E7%B3%BB%E7%BB%9F%20%E5%8F%8D%E6%8E%A8)
* [反推技术贴：鬼泣等冷兵器动作游戏打击感设计思路探寻-GameRes游资网](http://www.gameres.com/456213.html)
* [【玩家思维】ARPG的战斗系统博弈设计-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/21832)
* [6-24 晨星计划笔记-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/28964)
* [搜索页面](http://gad.qq.com/search/index?word=%E6%88%98%E6%96%97%E7%B3%BB%E7%BB%9F)
* [动作游戏战斗系统设计综述-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/13063)
* [从《暗黑》3 开始：动作游戏战斗系统浅析-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/10518)
* [尽管搞砸了地图，但《异度神剑2》却做出了一套比音游还爽快的战斗系统-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/38201)
* [动作游戏的设计语法，强烈推荐游戏动画师们好好看看-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/11915#)
* [论打击感的本质（1）——力的理论及应用-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/30811#)
* [《天涯明月刀》服务器端3D引擎设计与开发-GAD腾讯游戏开发者平台](http://gad.qq.com/article/detail/10014#)


游戏技能设计
http://blog.csdn.net/mooke/article/details/9771545
https://www.zhihu.com/question/29545727
http://www.gameres.com/472405.html
https://www.cnblogs.com/sundayofit/p/7995474.html
https://wenku.baidu.com/view/2d6596134693daef5ff73daa.html
http://bbs.gameres.com/forum.php?mod=viewthread&tid=485662
https://www.zhihu.com/question/37954118
http://bbs.gameres.com/thread_485421.html
http://www.360doc.com/content/16/0902/18/16163490_587830473.shtml
https://www.cnblogs.com/GameDeveloper/archive/2013/01/21/2869257.html
https://www.cnblogs.com/gcczhongduan/p/4669824.html
http://gamerboom.com/archives/86733
http://www.sohu.com/a/112852986_483399
http://blog.csdn.net/blizmax6/article/details/6682677
http://gamerboom.com/archives/59080
http://bbs.3dmgame.com/thread-4402456-1-1.html
http://bbs.csdn.net/topics/390806898
http://tieba.baidu.com/p/4871080830
https://zhuanlan.zhihu.com/p/26104183
http://blog.sina.com.cn/s/blog_4ab4aa810100h13g.html
https://max.book118.com/html/2017/0321/96288909.shtm
http://gad.qq.com/article/detail/23887
http://developer.51cto.com/art/201507/486052.htm
http://www.anyv.net/index.php/article-685076
https://www.zhihu.com/question/35087902
http://www.360doc.com/content/16/0902/18/16163490_587830473.shtml
http://gad.qq.com/article/detail/33829
http://gad.qq.com/article/detail/34805
