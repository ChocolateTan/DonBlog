# iOS 证书有效性
## iOS证书处理
拿到证书文件后使用 keychain 分别导出cert跟key的p12
* 1、openssl pkcs12 -clcerts -nokeys -out apns-pro-cert.pem -in cert.p12 
cert.p12、apns-pro-cert.pem 自己命名的可以改变，这句用来将keychain导出的cert.p12变成apns-pro-cert.pem

* 2、openssl pkcs12 -nocerts -out apns-pro-key.pem -in key.p12 
key.p12、apns-pro-key.pem 自己命名的可以改变，这句用来将keychain导出的key.p12变成apns-pro-key.pem

* 3、openssl rsa -in apns-pro-key.pem -out apns-pro-key-noenc.pem
apns-pro-key-noenc.pem 自己命名的可以改变，这句用来去除apns-pro-key.pem的密码

* 4、cat apns-pro-cert.pem apns-pro-key-noenc.pem > apns-pro.pem
apns-pro.pem 自己命名的可以改变，这句用来将1、3的结果合体

## 测试证书有效性
openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert apns-dev-cert.pem -key apns-dev-key.pem

openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert aps_dev.pem -key key.pem

