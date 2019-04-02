---
title: Android音频开发
category: Android
---
## Android音频开发

### Android音频简介

更加详尽的参考：

 [http://www.jianshu.com/p/2cb75a71009f](http://www.jianshu.com/p/2cb75a71009f)

 [http://blog.csdn.net/cjh\_android/article/details/51341004](http://blog.csdn.net/cjh_android/article/details/51341004)

 其他下载网站：[https://www.xiph.org/downloads/](https://www.xiph.org/downloads/)

#### **AudioRecord**

主要是实现边录边播（AudioRecord+AudioTrack）以及对音频的实时处理（如会说话的汤姆猫、语音）

优点：语音的实时处理，可以用代码实现各种音频的封装

缺点：输出是PCM语音数据，如果保存成音频文件，是不能够被播放器播放的，所以必须先写代码实现数据编码以及压缩

示例：

使用AudioRecord类录音，并实现WAV格式封装。录音20s，输出的音频文件大概为3.5M左右（已写测试代码）

#### **MediaRecorder**

已经集成了录音、编码、压缩等，支持少量的录音音频格式，大概有.aac（API = 16） .amr .3gp

优点：大部分以及集成，直接调用相关接口即可，代码量小

缺点：无法实时处理音频；输出的音频格式不是很多，例如没有输出mp3格式文件

示例：

使用MediaRecorder类录音，输出amr格式文件。录音20s，输出的音频文件大概为33K（已写测试代码）

#### **音频格式比较**

WAV格式：录音质量高，但是压缩率小，文件大

AAC格式：相对于mp3，AAC格式的音质更佳，文件更小；有损压缩；一般苹果或者Android SDK4.1.2（API 16）及以上版本支持播放

AMR格式：压缩比比较大，但相对其他的压缩格式质量比较差，多用于人声，通话录音

至于常用的mp3格式，使用MediaRecorder没有该视频格式输出。一些人的做法是使用AudioRecord录音，然后编码成wav格式，再转换成mp3格式

---

### Android关于MediaRecorder开发

采用频率（the sampling rate）：模拟信息转成数字信号的采样率。

采样位数：8位 或者 16位 去存储每一次的采样结果。

声道数：单声道，立体声道。

比特率（Bit rate ）/位率：声音中的比特率是指将模拟声音信号转换成数字声音信号后，单位时间内的二进制数据量，是间接衡量音频质量的一个指标。

比特率\(bps\) = 采样频率（HZ）采样位数（Bit）声道数

```java
setAudioEncodingBitRate

MediaRecorder recorder = new MediaRecorder();
recorder.setAudioSource(MediaRecorder.AudioSource.MIC);
if (Build.VERSION.SDK_INT >= 10) {
    recorder.setAudioSamplingRate(44100);
    recorder.setAudioEncodingBitRate(96000);
    recorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4);
    recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AAC);
} else {
    // older version of Android, use crappy sounding voice codec
    recorder.setAudioSamplingRate(8000);
    recorder.setAudioEncodingBitRate(12200);
    recorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
    recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);
}
recorder.setOutputFile(file.getAbsolutePath());
try {
    recorder.prepare();
} catch (IOException e) {
    throw new RuntimeException(e);
}
```

setAudioEncodingBitRate

这个方法，声音会变得奇怪，类似回音之类，这个参数会影响输出文件的效果，尽量按照bit rate设置。

setAudioSamplingRate

一般参数为44100 16000 11025，这个影响文件采集效果，直接影响录音质量和文件大小。

---

### Android关于AudioRecorder开发

> 参考：[http://www.cnblogs.com/tyjsjl/p/3695122.html](http://www.cnblogs.com/tyjsjl/p/3695122.html)

---

### 使用FFmpeg

> 项目地址：[https://github.com/WritingMinds/ffmpeg-android-java](https://github.com/WritingMinds/ffmpeg-android-java)

---

### MediaRecorder和AudioRecorder获取分贝

在使用AudioRecorder的时候读取流计算分贝必须要用short\[\]类型计算

> [http://blog.csdn.net/sno\_guo/article/details/42428587](http://blog.csdn.net/sno_guo/article/details/42428587)



