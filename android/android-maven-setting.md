# Android Maven Setting

## 国内仓库配置
```
allprojects {
    repositories {
        //---------------------------必备镜像仓库和仓库地址---------------------------------
        maven { url ' https://maven.aliyun.com/repository/jcenter' }
        maven { url ' https://maven.aliyun.com/repository/central' }
        maven { url ' https://maven.aliyun.com/repository/public' }
        maven { url ' https://maven.aliyun.com/repository/google' }
        maven { url ' https://maven.aliyun.com/repository/gradle-plugin' }
        maven { url 'http://maven.aliyun.com/nexus/content/repositories/releases/' }

        google()
        jcenter()
        mavenCentral()
        maven { url "https://jitpack.io" }
        // 无效网址，导致编译卡住，一定要注释掉，可恨可恨（根据场景自行决定是否注释）
        // maven { url 'https://maven.google.com' }
        //---------------------------必备镜像仓库和仓库地址--------------------------------
    }
}
```