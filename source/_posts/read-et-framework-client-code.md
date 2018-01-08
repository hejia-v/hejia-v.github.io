---
title: ET框架客户端源码阅读
tags:
    - unity
    - game
date: 2018-01-05 21:24:35
updated: 2018-01-05 21:24:35
categories:
    - unity
    - game
---


[ET](https://github.com/egametang/ET)是一个unity的前后端框架，包含客户端和服务端两部分。采用的是组件式设计，前后端都由C#实现，并且前后端共享了部分代码，可以很方便的进行全栈开发。客户端方面的功能也比较齐全，基本包含了手游开发中使用频率比较高的各个功能。前后端都非常完整地实现了热更新，热更新机制采用的是[ILRuntime](https://github.com/Ourpalm/ILRuntime)，即把要热更新的C#代码当做脚本来进行热更，终于可以不用使用讨厌鬼lua了ヽ(￣▽￣)ﾉ。如果手头没有代码积累，ET框架是一个非常不错的选择。这个框架很对我胃口，业余抽空先看了一下客户端部分，感觉设计得挺精妙的，这里梳理一下，方便理解，以免使用该框架时没有头绪。另外也感慨一下，C#确实好用，语法很甜，使用起来，舒适度和Python差不多，同时又是强类型的，效率也不错，开发起来简直是一种享受。

<!--more-->

## 修复工程文件的bug
客户端的Hotfix工程可能存在找不到UnityEngine库的bug。这时需要修改一下ET/Unity/Hotfix/Unity.Hotfix.csproj文件。对照Unity.csproj的库引用部分的配置，修改Unity.Hotfix.csproj工程的引用配置。
例如将Unity.Hotfix.csproj的
```xml
<Reference Include="UnityEngine, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null">
    <HintPath>C:\Apps\Unity\Editor\Data\Managed\UnityEngine.dll</HintPath>
</Reference>
<Reference Include="UnityEngine.UI, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
    <HintPath>C:\Apps\Unity\Editor\Data\UnityExtensions\Unity\GUISystem\UnityEngine.UI.dll</HintPath>
</Reference>
```
改成
```xml
<Reference Include="UnityEngine">
    <HintPath>D:/Program Files/Unity/Editor/Data/Managed/UnityEngine/UnityEngine.dll</HintPath>
</Reference>
<Reference Include="UnityEngine.CoreModule">
    <HintPath>D:/Program Files/Unity/Editor/Data/Managed/UnityEngine/UnityEngine.CoreModule.dll</HintPath>
</Reference>
<Reference Include="UnityEngine.UI">
    <HintPath>D:/Program Files/Unity/Editor/Data/UnityExtensions/Unity/GUISystem/UnityEngine.UI.dll</HintPath>
</Reference>
```

## 阅读ET客户端源码

记录一下自己的阅读过程，以便将来阅读陌生项目时，有经验可供参考，并改进阅读方法。
1. 查看项目的文档。
2. 查看项目结构，文件及文件夹布局，凭经验粗略判断了一下核心文件，翻了一下主要文件的代码。
3. 运行了几次程序，看一下有哪些功能，了解一下程序长什么样。
4. 开始调试源码，跟随程序的运行，一步一步的跟，对程序的运行流程有一个初步的印象。由于是C#编写的，并且ide使用的是vs2017，在调试信息中经常可以看到相关连的类或结构的名字，甚至是代码文件的路径，**复制变量的值**，借助于vs2017的**转到文件**、**转到符号**等功能，可以迅速定位到相关位置。
5. 开始详细阅读主流程代码，关键点做下记录，以备将来查阅。

## 客户端demo
ET框架的客户端demo只有一个Init.unity场景，里面的内容如下图
![1](http://ozy76jm8o.bkt.clouddn.com/blog/images/read-et-framework-client-code-1.png)
Init.cs就挂在名为Global的GameObject上，Init.cs是游戏逻辑的入口。

启动服务器后，同时开2个客户端时，屏幕中会出现2个小人，开始时是重叠在一起的，右键可以移动小人，观察帧同步的效果。在实际测试中发现，运动出现不同步的频率还是有点高的，实际使用时需要优化。

## 主要的类
这里列出了一些比较重要的类以及方法的说明，相当于一个大纲，方便快速理解框架结构。这里整理出的内容仅供参考，因为代码在不断变更，相关的类的功能也在变化。

### DllHelper
路径：Scripts/helper/DllHelper.cs

    static class DllHelper
        + static void/Assembly LoadHotfixAssembly
            ILRuntime模式
                将Hotfix.dll和Hotfix.pdb读取到byte数组, 使用Init.Instance.AppDomain.LoadAssembly载入
            普通模式
                将Hotfix.dll和Hotfix.mdb读取到byte数组, 使用Assembly.Load加载成Assembly对象并返回
        + static Type[] GetMonoTypes()
                List<Type> types = new List<Type>();
                foreach (Assembly assembly in ObjectEvents.Instance.GetAll())
                {
                    types.AddRange(assembly.GetTypes());
                }
                return types.ToArray();
        + static Type[] GetHotfixTypes()
            ILRuntime模式
                return appDomain.LoadedTypes.Values.Select(x => x.ReflectionType).ToArray();
            普通模式
                return ObjectEvents.Instance.HotfixAssembly.GetTypes()

### ObjectEvents
路径：Scripts/base/object/ObjectEvents.cs

    interface IObjectEvent
        + Type Type()
        + void Set(object value)

    abstract class ObjectEvent<T> : IObjectEvent
        - T value
        + T Get()
        + Set(object v)  设置value
        + Type Type()

    sealed class ObjectEvents
        - static ObjectEvents instance  单例
        - Assembly hotfixAssembly
        - Dictionary<string, Assembly> assemblies
        - Dictionary<Type, IObjectEvent> disposerEvents
        - EQueue<Disposer> updates, updates2, starts, loaders, loaders2, lateUpdates, lateUpdates2
        + void LoadHotfixDll()
            ILRuntime模式
                DllHelper.LoadHotfixAssembly载入Hotfix.dll
            普通模式
                hotfixAssembly引用DllHelper.LoadHotfixAssembly()返回的Assembly对象
            this.Load();
        + void Add(string name, Assembly assembly)
            assemblies[name] = assembly;
            遍历assemblies里的assembly的所有type, 如果具有ObjectEventAttribute特性, 且继承了IObjectEvent,
            就创建type的实例objectEvent, 并添加进disposerEvents，即disposerEvents[objectEvent.Type()] = objectEvent;
        + Assembly Get(string name)
            return this.assemblies[name];
        + Assembly[] GetAll()
            return this.assemblies.Values.ToArray();
        + void Add(Disposer disposer)
            通过disposer的type从disposerEvents中获取objectEvent，
            如果是ILoad, 就添加进loaders
            如果是IUpdate, 就添加进updates
            如果是IStart, 就添加进starts
        + void Awake(Disposer disposer)  有泛型版本，用于扩展传到disposer的参数个数，但逻辑是一致的
            Add(disposer)
            通过disposer的type从disposerEvents中获取objectEvent，
            IAwake iAwake = objectEvent as IAwake;
            objectEvent.Set(disposer);
            iAwake.Awake();
            objectEvent相当于是一个包装器, disposer是具体做这件事的对象，objectEvent调用disposer的Awake,
            继承接口的是objectEvent, disposer对objectEvent是已知的, disposer不用继承任何IAwake之类的接口，简化disposer的继承
        + void Load()
            从loaders弹出一个disposer，通过disposer的type从disposerEvents中获取objectEvent，再将disposer添加到loaders2，
            ILoad iLoad = objectEvent as ILoad;
            objectEvent.Set(disposer);
            iLoad.Load(); --> 通过objectEvent调用disposer里的方法，
            重复以上操作直到loaders里的弹完为止
            loaders和loaders2对调
        + void Start()
            从starts里弹出disposer
            通过objectEvent调用disposer里的Start方法
            流程和Load()差不多，只是从starts里弹出disposer没有被回收。
        + void Update()
            类似Load()
        + void LateUpdate()
            类似Load()

### Disposer
路径：Scripts/base/object/Disposer.cs

    abstract class Object: ISupportInitialize
        + virtual void BeginInit()
        + virtual void EndInit()

    [BsonKnownTypes(typeof(Component))]
    abstract class Disposer : Object, IDisposable
        - long Id
        - bool IsFromPool
        + Disposer()
        + Disposer(long id)
        + virtual void Dispose()

### Component
路径：Scripts/Base/Object/Component.cs

    [BsonIgnoreExtraElements]
    abstract partial class Component: Disposer
        - Entity Parent
        + Component()
        + T GetParent<T>() where T : Entity
        + override void Dispose()

路径：Scripts/Base/Object/ComponentAttribute.cs

    [BsonKnownTypes(typeof(AConfigComponent))]
    [BsonKnownTypes(typeof(Entity))]
    partial class Component

### ComponentFactory
路径：Scripts/Base/Object/ComponentFactory.cs

    static class ComponentFactory
        + Create 一组泛型函数，
            从对象池里创建组件，并通过ObjectEvents.Instance.Awake(disposer);来Awake组件
            这是一组泛型函数，支持传入多个参数给组件的Awake函数

### EventComponent
路径：Scripts/component/EventComponent.cs

    interface IEvent
        + Run：一组泛型函数，支持最多6个参数，无返回值

    interface IEventMethod
        + Run：一组泛型函数，支持最多4个参数，无返回值

    class IEventMonoMethod : IEventMethod
        - object obj
        + IEventMonoMethod(object obj)
            初始化时引用一个IEvent对象obj，
        + Run：一组泛型函数，支持最多4个参数，无返回值，让obj执行IEvent的run方法

    class IEventILMethod : IEventMethod
        - ILRuntime.Runtime.Enviorment.AppDomain appDomain
        - ILTypeInstance instance
        - IMethod method  --> ILRuntime貌似只能通过这种方式执行函数
        - object[] param
        + IEventILMethod(Type type, string methodName)
            使用AppDomain获取将要调用的方法，同时appDomain.Instantiate(type.FullName)创建一个实例并赋值给instance，
            并从type获取到method
            注：
            创建IEventMonoMethod和IEventILMethod的地方，在EventComponent的Load方法里，
            在Load里是直接通过类(继承了IEvent)来创建实例的，只不过IEventMonoMethod是在构造函数外面创建IEvent实例，
            IEventILMethod是在构造函数里面创建IEvent实例，感觉都在构造函数里面创建IEvent实例比较好，这样统一一些，不会那么奇怪
        + Run：一组泛型函数，支持最多4个参数，无返回值
            让obj执行IEvent的run方法，内部是通过appdomain Invoke方法，实现方法的调用

    class EventComponentEvent : ObjectEvent<EventComponent>, IAwake, ILoad
        + void Awake()
            调用EventComponent的Awake函数
        + void Load()
            调用EventComponent的Load函数

    class EventComponent : Component
        - EventComponent Instance 单例
        - Dictionary<EventIdType, List<IEventMethod>> allEvents
        + Awake
            Instance = this;
            this.Load();
        + Load
            新建allEvents

            通过DllHelper.GetMonoTypes获取types列表，遍历types，获取有EventAttribute特性的type，
            从type获取到的EventAttribute为aEventAttribute，创建该type的实例obj，然后添加到allEvents，
            即allEvents[(EventIdType)aEventAttribute.Type].Add(new IEventMonoMethod(obj));
            感觉有点问题，要是type没继承IEvent，无法静态检查出来，运行时就gg了  ￣ω￣=

            通过DllHelper.GetHotfixTypes获取types列表，重复上面的过程，
            不同之处在于，在ILRuntime模式下，创建IEventILMethod而不是IEventMonoMethod
        + Run(EventIdType type, ...)：一组泛型函数，支持最多3个参数，无返回值
            从allEvents根据EventIdType取出IEventMethod列表，然后执行列表里的IEventMethod对象的Run方法


> 因为各Component基本上都有对应的ComponentEvent，ComponentEvent的功能基本上就是调用Component的Awake,Start,Update等方法，少数ComponentEvent可能有一些额外的功能。以下部分，如果XXXComponentEvent没有特殊功能，就略过不表了。

### UIComponent
路径：Scripts/Other/UIFactoryAttribute.cs

    [AttributeUsage(AttributeTargets.Class)]
    class UIFactoryAttribute: Attribute
        - int Type  --> 枚举值
        + UIFactoryAttribute(int type)

路径：Scripts/component/UIComponent.cs

    class class UIComponent: Component
        - GameObject Root  --> ui的根节点
        - Dictionary<UIType, IUIFactory> UiTypes
        - Dictionary<UIType, UI> uis
        + void Awake()
            this.Root = GameObject.Find("Global/UI/");
            this.Load();
        + void Load()
            清空UiTypes，
            遍历DllHelper.GetMonoTypes()获取到的types列表，获取有UIFactoryAttribute特性的type，创建type的实例factory，
            添加到UiTypes，即this.UiTypes.Add((UIType)attribute.Type, factory);
            attribute为从type获取的UIFactoryAttribute特性
        + UI Create(UIType type)
            从UiTypes中取出type类型的factory，创建出UI类型实体ui，并将ui添加到uis列表中。
            // 设置canvas
            string cavasName = ui.GameObject.GetComponent<CanvasConfig>().CanvasName;
            ui.GameObject.transform.SetParent(this.Root.Get<GameObject>(cavasName).transform, false);
        + void Dispose()
            遍历uis并Dispose，清空uis和UiTypes
        + void Add(UIType type, UI ui)
        + void Remove(UIType type)
        + void RemoveAll()
        + UI Get(UIType type)
        + List<UIType> GetUITypeList()

### IUIFactory
路径：Scripts/Other/IUIFactory.cs

    interface IUIFactory
        + UI Create(Scene scene, UIType type, GameObject parent);
        + void Remove(UIType type);

### UILoadingFactory
路径：Scripts/UI/UILoading/Factory/UILoadingFactory.cs

    class UILoadingFactory : IUIFactory
        + UI Create(Scene scene, UIType type, GameObject gameObject)
            这里只创建了加载界面，
            资源在Resources/KV.prefab
            从UnityEngine.Resources.Load('KV').Get<GameObject>("UILoading");取出界面
            UnityEngine.Object.Instantiate 实例化界面得到对象go
            设置go的层
            使用go创建UI类型的实体ui
            给ui添加UILoadingComponent组件
        + void Remove(UIType type)
            空

### UILoadingComponent
路径：Scripts/UI/UILoading/Component/UILoadingComponent.cs

    UILoadingComponentEvent : ObjectEvent<UILoadingComponent>, IAwake, IStart
        + void Awake()
            获取界面的Text控件的引用，赋值给UILoadingComponent的text
        + async void Start()
            在一个while循环中，不断更新UILoadingComponent的text，更新下载进度的文字显示，直到下载完成为止。

    class UILoadingComponent : Component
        - Text text

### UI
路径：Scripts/Entity/UI.cs

    class UIEvent : ObjectEvent<UI>, IAwake<Scene, UI, GameObject>
        + void Awake(Scene scene, UI parent, GameObject gameObject)

    sealed class UI: Entity
        - Scene Scene
        - string Name  --> this.GameObject.name
        - GameObject GameObject
        - Dictionary<string, UI> children
        + void Awake(Scene scene, UI parent, GameObject gameObject)
            清空children
            设置Scene和GameObject
            gameObject.transform.SetParent(parent.GameObject.transform, false)
        + void Dispose()
            遍历children进行Dispose
            UnityEngine.Object.Destroy(GameObject);
            清空children
        + void Add(UI ui)
        + void Remove(string name)
        + UI Get(string name)

### ResourcesComponent
路径：Scripts/component/ResourcesComponent.cs


### Opcode
enum Opcode
    一组网络协议号

### MessageAttribute

粗略观察了一下，有MessageAttribute的type基本上都是协议包的结构体

    class MessageAttribute: Attribute
        - Opcode Opcode

### OpcodeTypeComponent

    class OpcodeTypeComponent : Component
        - DoubleMap<Opcode, Type> opcodeTypes
        + void Awake()
            遍历DllHelper.GetMonoTypes()，取出有MessageAttribute的type,添加到opcodeTypes

### GlobalConfigComponent

    class GlobalConfigComponent : Component
        - GlobalConfigComponent Instance 单例
        - GlobalProto GlobalProto
        + void Awake()
            资源在Assets/Res/Config/GlobalProto.txt
            ConfigHelper.GetGlobal() 从Resources/KV.prefab取名为GlobalProto的文本，然后反序列化到GlobalProto中
            GlobalProto.txt就是一个json文件，主要存储热更新地址和服务器地址，

### NetOuterComponent

    class NetOuterComponent : NetworkComponent
        + void Awake()
            this.Awake(NetworkProtocol.TCP);
            this.MessagePacker = new ProtobufPacker(); 将数据压成包，压包器，采用Protobuf
            this.MessageDispatcher = new ClientDispatcher();
        + new void Update()

### ClientDispatcher
路径：Scripts/Base/Message/ClientDispatcher.cs

    interface IMessageDispatcher
        + void Dispatch(Session session, Opcode opcode, int offset, byte[] messageBytes, AMessage message)

    class ClientDispatcher: IMessageDispatcher
        + void Dispatch(Session session, Opcode opcode, int offset, byte[] messageBytes, AMessage message)
            根据message类型判断消息类型，
            message如果是FrameMessage，那就是帧同步消息，
                Game.Scene.GetComponent<ClientFrameComponent>().Add(session, frameMessage);
            message如果是AMessage或ARequest，那就是普通消息或者是Rpc请求消息，
                由MessageDispatherComponent处理

### Session
路径：Scripts/Entity/Session.cs

    sealed class Session : Entity
        - static uint RpcId
        - NetworkComponent network
        - AChannel channel
        - Dictionary<uint, Action<object>> requestCallback
        - List<byte[]> byteses
        + void Awake(NetworkComponent net, AChannel c)
            设置network和channel，清空requestCallback
        + void Start()
            this.StartRecv();
        + override void Dispose()
        + async void StartRecv()
            一个while循环使之不断运转。
            packet = await this.channel.Recv(); 接收包，收包的任一环节出现异常，都会导致循环停止。
            先取出opcode,在调用RunDecompressedBytes，处理协议消息。完了之后进入下一轮循环，等待接受消息。
        + void RunDecompressedBytes(ushort opcode, byte[] messageBytes, int offset, int count)
            根据opcode从OpcodeTypeComponent中取出对应的协议结构体，然后将messageBytes反序列化到协议结构体中。
            然后把协议消息发送出去，这里有判断rpc的逻辑。
        + void CallWithAction(ARequest request, Action<AResponse> action)
            rpc调用
        + Task<AResponse> Call(ARequest request, bool isHotfix)
            Rpc调用,发送一个消息,等待返回一个消息
        + Task<AResponse> Call(ARequest request, bool isHotfix, CancellationToken cancellationToken)
            Rpc调用
        + Task<Response> Call<Response>(ARequest request) where Response : AResponse
            Rpc调用,发送一个消息,等待返回一个消息
        + Task<Response> Call<Response>(ARequest request, CancellationToken cancellationToken)
            Rpc调用
        + void Send(AMessage message)
            发送消息
        + void Reply<Response>(Response message) where Response : AResponse
            发送消息
        + void SendMessage(object message)
            将协议消息发往服务器

### AChannel
路径：Scripts/Base/Network/AChannel.cs

    enum PacketFlags

    enum ChannelType

    abstract class AChannel: IDisposable
        - long Id
        - ChannelType ChannelType
        - AService service
        - IPEndPoint RemoteAddress
        + abstract void Send(byte[] buffer)
        + abstract void Send(List<byte[]> buffers);
        + abstract Task<Packet> Recv();
        + virtual void Dispose()

### MessageDispatherComponent

类似EventComponent模块，分有热更版本

    interface IMessageMethod
        + void Run(Session session, AMessage a);

    class IMessageMonoMethod : IMessageMethod
        + void Run(Session session, AMessage a)

    class IMessageILMethod : IMessageMethod
        + void Run(Session session, AMessage a)

    class MessageDispatherComponent : Component
        - Dictionary<Opcode, List<IMessageMethod>> handlers
        + void Awake()
            this.Load();
        + void Load()
            从DllHelper.GetMonoTypes()和DllHelper.GetHotfixTypes()获取types,
            从中选择出带有MessageHandlerAttribute的type，添加到handlers中
        + void Handle(Session session, MessageInfo messageInfo)
            从handlers中找出与messageInfo.Opcode对应的IMessageMethod，运行它的Run方法

### ClientFrameComponent

    class FrameMessage : AActorMessage
        - int Frame
        - List<AFrameMessage> Messages

    struct SessionFrameMessage
        - Session Session
        - FrameMessage FrameMessage

    class ClientFrameComponent: Component
        - int Frame
        - EQueue<SessionFrameMessage> Queue
        - int count = 1
        - int waitTime
        - const int maxWaitTime = 40
        + void Start()
            UpdateAsync();
        + void Add(Session session, FrameMessage frameMessage)
            添加到Queue
        + async void UpdateAsync()
            一个while循环使之不断运转。每隔一段时间调用一次this.UpdateFrame();
            如果队列中消息多于4个，则加速跑帧
        + void UpdateFrame()
            从Queue出队一个SessionFrameMessage，
            将SessionFrameMessage.FrameMessage.Messages里的消息通过MessageDispatherComponent都发送出去

### NetworkComponent

这个是和服务器公用的组件

    abstract class NetworkComponent : Component
        - AService Service
        - AppType AppType
        - Dictionary<long, Session> sessions
        - IMessagePacker MessagePacker
        - IMessageDispatcher MessageDispatcher
        + void Awake(NetworkProtocol protocol)
            根据protocol类型创建Service，有TService和KService两种
        + void Awake(NetworkProtocol protocol, IPEndPoint ipEndPoint)
            根据protocol类型创建Service，有TService和KService两种，
            将ipEndPoint传给Service的构造函数，并this.StartAccept();
        + async void StartAccept()
            在while循环中，不断的执行await this.Accept();
        + virtual async Task<Session> Accept()
            具体功能需要调一下
        + virtual void Remove(long id)
            移除Session
        + Session Get(long id)
            获取Session
        + virtual Session Create(IPEndPoint ipEndPoint)
            创建一个新Session
        + public void Update()
            this.Service.Update();
        + override void Dispose()

网络方面还有TService，KService，Channel等，涉及到的东西比较多，具体的功能和流程需要在使用的时候弄清楚。

