# iOS swift 正则问题

## 中英文文字导致正则失败
是"𨥈" 这个字的 unicode 值超过了65535，应该需要更多的 bytes 来 represent。导致 string.count 和 nsstring.length 不同。
```swift
let testStr = "狂捐錢起過百間小學 失意感激黃𨥈瑩"

testStr.forEach({
    s in
    s.unicodeScalars.forEach({
        unicode in
        print("\(s) scalars: \(unicode.value)")
    })
})
```

```
狂 scalars: 29378
捐 scalars: 25424
錢 scalars: 37666
起 scalars: 36215
過 scalars: 36942
百 scalars: 30334
間 scalars: 38291
小 scalars: 23567
學 scalars: 23416
  scalars: 32
失 scalars: 22833
意 scalars: 24847
感 scalars: 24863
激 scalars: 28608
黃 scalars: 40643
𨥈 scalars: 166216
瑩 scalars: 29801
```