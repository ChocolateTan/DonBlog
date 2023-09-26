# iOS 插件 LLDebugTool

```swift
import LLDebugTool

LLDebugTool.shared().startWorking { config in
              config.colorStyle = .homebrew
              config.configPrimaryColor(.white, backgroundColor: Environment.themeColor, statusBarStyle: .default)
              config.ignoredHosts = ["pubads.g.doubleclick.net","googleads.g.doubleclick.net","securepubads.g.doubleclick.net","graph.facebook.com","web.facebook.com"]
          }
```
> https://github.com/HDB-Li/LLDebugTool