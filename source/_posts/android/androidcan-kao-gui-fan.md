---
title: Android Code Style
date: 2018-10-02 09:09:09
categories: Android
---
## Android參考規範

[https://google.github.io/styleguide/javaguide.html](https://google.github.io/styleguide/javaguide.html)

### 基本的命名法

Java編程比較常見的有下面三種命名方式

1.駝峰\(Camel\)命名法:又稱小駝峰命名法，除首單詞外，其余所有單詞的第一個字母大寫。

2.帕斯卡\(pascal\)命名法:又稱大駝峰命名法，所有單詞的第一個字母大寫

3.下劃線命名法:單詞與單詞間用下劃線做間隔

一般建議拿來做命名的單詞要比較精悍短小，這樣即使兩三個單詞一起拼裝成一個命名，也不至於顯得很冗長。當然有些單詞我們也可以直接寫成一些約定俗成的縮寫。諸如：msg\(message\)、init\(initial\)、img\(image\)等.....

個人認為，這些縮寫可參照業界常見的縮寫命名，也可以根據當前項目中的風格，進行團隊成員間的約定。這樣相對比較靈活，也方便團隊成員之間相互理解。

### 包命名

采用反域名命名規則，全部使用小寫字母，一般為3層

一級包名為com;

二級包名為xx（可以是公司或則個人的隨便）;

三級包名應用的英文名app\_name;

四級包名為模塊名或層級名;

如：www.ziines.com

正常-&gt;com.ziines.www

參考-&gt;com.ziines.android或com.ziines.it

如：framework.com.hk

正常-&gt;hk.nmg.framework

| 命名格式 | 作用 |
| :--- | :--- |
| com.xx.app\_name.activities\(或com.xx.app\_name.activity\) | 存放app所有的Activity |
| com.xx.app\_name.service | 存放app所有的Service |
| com.xx.app\_name.receiver | 存放app所有的BroadcastReceiver |
| com.xx.app\_name.provider | 存放app所有的ContentProvider |
| com.xx.app\_name.fragment | 存放app所有的Fragment |
| com.xx.app\_name.dialog | 存放app所有的Dialog |
| com.xx.app\_name.base | 存放app一些共有的基礎模塊，諸如BaseActivity、BaseContentProvider、BaseService，BaseFragment等 |
| com.xx.app\_name.utils | 存放app的工具類,諸如格式化日期的DateFormatUtils，處理字符串的StringUtils等 |
| com.xx.app\_name.bean\(或com.xx.app\_name.unity\) | 存放app自定義的實體類 |
| com.xx.app\_name.db\) | 存放app數據庫操作相關的類 |
| com.xx.app\_name.view\) | 存放app自定義的控件 |
| com.xx.app\_name.adapter\) | 存放app所有的適配器類 |

### 類命名

| 類 | 命名格式 | 示例 |
| :--- | :--- | :--- |
| Activity | XXX功能+Activity | 如主界面HomeActivity,啟動頁LauncherActivity |
| Service | XXX功能+Service | 如消息推送的Service，PushService或PushMessageService |
| BroadcastReceiver | XXX功能+Receiver | 如在線的消息廣播接受者，OnlineReceiver |
| ContentProvider | XXX功能+Provider | 如聯系人的內容提供者，ContactsProvider |
| Fragment | XXX功能+Fragment | 如顯示聯系人的Fragment，ContactsFragment |
| Dialog | XXX功能+Dialog | 如普通的選擇提示對話框，ChoiceDialog |
| Adapter | XXX功能+XX类型控件Adapter | 如聯系人列表，ContactsListAdapter |
| 基础功能类 | Base+XX父类名 | 如BaseActivity，BaseFragment |
| 工具类 | XXX功能+Utils | 如處理字符串的工具類，StringUtils |
| 管理类 | XXX功能+Manager | 如管理聯系人的類，ContactsManager |

### 接口命名

和類名基本一致。也可以在接口名前面再加一個大寫的I，表明這是一個接口Interface。

### 方法

動詞或動名詞，采用小駝峰命名法。

| 命名風格 | 含義 |
| :--- | :--- |
| initXX\(\) | 初始化，如初始化所有控件initView\(\) |
| isXX\(\) | 是否滿足某種要求，如是否為註冊用戶isRegister\(\) |
| processXX\(\) | 對數據做某些處理，可以以process作為前綴 |
| displayXX\(\) | 顯示提示信息，如displayXXDialog，displayToast，displayXXPopupWindow |
| saveXX\(\) | 保存XX數據 |
| resetXX\(\) | 重置XX數據 |
| addXX\(\)/insertXX\(\) | 添加XX數據 |
| deleteXX\(\)/removeXX\(\) | 刪除XX數據 |
| updateXX\(\) | 更新XX數據 |
| searchXX\(\)/findXX\(\)/queryXX\(\) | 查找XX數據 |
| draw\(\) | 控件裏面使用居多，例如繪制文本drawText |

### 變量

采采用小駝峰命名法。同樣比較簡單，但為了更好表明含義，我建議做一下的的區分

成員變量命名前面加m（member，表示成員變量之意），如，控件的寬高 mWidth，mHeight

靜態類變量前面加s（static，表示靜態變量之意），如，一個靜態的單例 sSingleInstance

### 常量

同樣較為簡單，全部大寫,采用下劃線命名法.如：MIN\_WIDTH,MAX\_SIZE

### 布局資源文件\(layout文件夾下\)

全部小寫，采用下劃線命名法

| 布局類型 | 命名風格 |
| :--- | :--- |
| Activity的xml布局 | activity\_+XX功能，如主頁面activity\_home |
| Fragment的xml布局 | fragment\_+XX功能，如聯繫人模塊fragment\_contacts |
| Dialog的xml布局 | dialog\_+XX功能，如選擇日期dialog\_select\_date |
| 抽取出來重用的xml布局（include） | include\_+XX功能，如底部tab欄include\_bottom\_tabs |
| ListView或者RecyclerView的item xml布局 | XX功能+\_list\_item，如聯繫人的contact\_info\_list\_item |
| GridView的item xml布局 | XX功能+\_grid\_item，如相冊的album\_grid\_item |

### 動畫資源文件\(anim文件夾下\)

全部小寫，采用下劃線命名法，加前綴區分.

| 動畫效果 | 命名風格 |
| :--- | :--- |
| 淡入/淡出 | fade\_in/fade\_out |
| 从某個方向淡入/淡出 | fade\_方向\_in\(out\),右边淡入淡出fade\_right\_in\(out\) |
| 从某個方向彈入/彈出 | push\_方向\_in\(out\),右边推入推出push\_right\_in\(out\) |
| 从某個方向滑入/滑出 | slide\_in\(out\)_from_方向,右边滑入滑出slide\_in\(out\)\_from\_right |

### strings和colors資源文件

小駝峰命名法,命名風格大致如下：

string命名格式：XX界面\_XX功能\_str,如 activity\_home\_welcome\_str

color命名格式：color\_16進制顏色值，如紅色 color\_ff0000

像string通常建議把同一個界面的所有string都放到一起，方便查找。而color的命名則省去我們頭疼的想這個顏色怎麽命名。

### selecor、drawable、layer-list資源文件

小駝峰命名法。命名風格通常都是XX\_selector、XX\_drawable、XX\_layer。

下面舉兩個比較常用的栗子：

按鈕按壓效果button\_selector，正常狀態命名為button\_normal\(XX\_normal\)，按壓狀態命名為button\_pressed\(XX\_pressed\)

選擇效果checkbox\_selector,未選中狀態命名為checkbox\_unchecked\(XX\_unchecked\),選中狀態為checkbox\_checked\(XX\_checked\)

### styles、dimens資源文件

style采用大駝峰命名法，主題可以命名為XXTheme,控件的風格可以命名為XXStyle

dimen采用小駝峰命名法，如所有Activity的titlebar的高度，activity\_title\_height\_dimen

### 控件id命名

| 控件 | java前綴縮寫 | xml |
| :--- | :--- | :--- |
| RelativeLayout | rly | rly |
| LinearLayout | lly | lly |
| FrameLayout | fly | fly |
| TextView | tv | tv |
| Button | btn | btn |
| ImageButton | imgBtn | img\_btn |
| ImageView | iv | iv |
| CheckBox | chk | chk |
| RadioButton | rb | rb |
| analogClock | anaClk | ana\_clk |
| DigtalClock | dgtClk | dgt\_clk |
| DatePicker | dtPk | dt\_pk |
| EditText | edt | edt |
| TimePicker | tmPk | tm\_pk |
| toggleButton | tglBtn | tgl\_btn |
| ProgressBar | proBar / progressBar | pro\_bar / progress\_bar |
| SeekBar | skBar / seekBar | sk\_bar / seek\_bar |
| AutoCompleteTextView | autoTv | auto\_tv |
| ZoomControl | zmCtl | zm\_ctl |
| VideoView | videoView | video\_view |
| WebView | webView | web\_view |
| Spinner | spn | spn |
| Chronometer | cmt | cmt |
| ScollView | scollView | scoll\_view |
| TextSwitch | txtSwitch | txt\_swt |
| ImageSwitch | imgSwt | img\_swt |
| ListView | lv | lv |
| GridView | gv | gv |
| ExpandableList | epdLt | epd\_lt |
| MapView | mapView | map\_view |

前言

這份文檔是Google Java編程風格規範的完整定義。當且僅當一個Java源文件符合此文檔中的規則， 我們才認為它符合Google的Java編程風格。

與其它的編程風格指南一樣，這裏所討論的不僅僅是編碼格式美不美觀的問題， 同時也討論一些約定及編碼標準。然而，這份文檔主要側重於我們所普遍遵循的規則， 對於那些不是明確強制要求的，我們盡量避免提供意見。

1.1 術語說明

在本文檔中，除非另有說明：

術語class可表示一個普通類，枚舉類，接口或是annotation類型\(@interface\)

術語comment只用來指代實現的註釋\(implementation comments\)，我們不使用“documentation comments”一詞，而是用Javadoc。

其他的術語說明會偶爾在後面的文檔出現。

1.2 指南說明

本文檔中的示例代碼並不作為規範。也就是說，雖然示例代碼是遵循Google編程風格，但並不意味著這是展現這些代碼的唯一方式。 示例中的格式選擇不應該被強制定為規則。

源文件基礎

2.1 文件名

源文件以其最頂層的類名來命名，大小寫敏感，文件擴展名為.java。

2.2 文件編碼：UTF-8

源文件編碼格式為UTF-8。

2.3 特殊字符

2.3.1 空白字符

除了行結束符序列，ASCII水平空格字符\(0x20，即空格\)是源文件中唯一允許出現的空白字符，這意味著：

所有其它字符串中的空白字符都要進行轉義。

制表符不用於縮進。

2.3.2 特殊轉義序列

對於具有特殊轉義序列的任何字符\(\b, \t, \n, \f, \r, ", '及\\)，我們使用它的轉義序列，而不是相應的八進制\(比如\012\)或Unicode\(比如\u000a\)轉義。

2.3.3 非ASCII字符

對於剩余的非ASCII字符，是使用實際的Unicode字符\(比如∞\)，還是使用等價的Unicode轉義符\(比如\u221e\)，取決於哪個能讓代碼更易於閱讀和理解。

Tip: 在使用Unicode轉義符或是一些實際的Unicode字符時，建議做些註釋給出解釋，這有助於別人閱讀和理解。

例如：

String unitAbbrev = "μs"; \| 贊，即使沒有註釋也非常清晰

String unitAbbrev = "\u03bcs"; // "μs" \| 允許，但沒有理由要這樣做

String unitAbbrev = "\u03bcs"; // Greek letter mu, "s" \| 允許，但這樣做顯得笨拙還容易出錯

String unitAbbrev = "\u03bcs"; \| 很糟，讀者根本看不出這是什麽

return '\ufeff' + content; // byte order mark \| Good，對於非打印字符，使用轉義，並在必要時寫上註釋

Tip: 永遠不要由於害怕某些程序可能無法正確處理非ASCII字符而讓你的代碼可讀性變差。當程序無法正確處理非ASCII字符時，它自然無法正確運行， 你就會去fix這些問題的了。\(言下之意就是大膽去用非ASCII字符，如果真的有需要的話\)

源文件結構

一個源文件包含\(按順序地\)：

許可證或版權信息\(如有需要\)

package語句

import語句

一個頂級類\(只有一個\)

以上每個部分之間用一個空行隔開。

3.1 許可證或版權信息

如果一個文件包含許可證或版權信息，那麽它應當被放在文件最前面。

3.2 package語句

package語句不換行，列限制\(4.4節\)並不適用於package語句。\(即package語句寫在一行裏\)

3.3 import語句

3.3.1 import不要使用通配符

即，不要出現類似這樣的import語句：import java.util.\*;

3.3.2 不要換行

import語句不換行，列限制\(4.4節\)並不適用於import語句。\(每個import語句獨立成行\)

3.3.3 順序和間距

import語句可分為以下幾組，按照這個順序，每組由一個空行分隔：

所有的靜態導入獨立成組

com.google imports\(僅當這個源文件是在com.google包下\)

第三方的包。每個頂級包為一組，字典序。例如：android, com, junit, org, sun

java imports

javax imports

組內不空行，按字典序排列。

3.4 類聲明

3.4.1 只有一個頂級類聲明

每個頂級類都在一個與它同名的源文件中\(當然，還包含.java後綴\)。

例外：package-info.java，該文件中可沒有package-info類。

3.4.2 類成員順序

類的成員順序對易學性有很大的影響，但這也不存在唯一的通用法則。不同的類對成員的排序可能是不同的。 最重要的一點，每個類應該以某種邏輯去排序它的成員，維護者應該要能解釋這種排序邏輯。比如， 新的方法不能總是習慣性地添加到類的結尾，因為這樣就是按時間順序而非某種邏輯來排序的。

3.4.2.1 重載：永不分離

當一個類有多個構造函數，或是多個同名方法，這些函數/方法應該按順序出現在一起，中間不要放進其它函數/方法。

格式

術語說明：塊狀結構\(block-like construct\)指的是一個類，方法或構造函數的主體。需要註意的是，數組初始化中的初始值可被選擇性地視為塊狀結構\(4.8.3.1節\)。

4.1 大括號

4.1.1 使用大括號\(即使是可選的\)

大括號與if, else, for, do, while語句一起使用，即使只有一條語句\(或是空\)，也應該把大括號寫上。

4.1.2 非空塊：K 

&

 R 風格

對於非空塊和塊狀結構，大括號遵循Kernighan和Ritchie風格 \(Egyptian brackets\):

左大括號前不換行

左大括號後換行

右大括號前換行

如果右大括號是一個語句、函數體或類的終止，則右大括號後換行; 否則不換行。例如，如果右大括號後面是else或逗號，則不換行。

示例：

return new MyClass\(\) {

@Override public void method\(\) {

if \(condition\(\)\) {

try {

something\(\);

} catch \(ProblemException e\) {

recover\(\);

}

}

}

};

4.8.1節給出了enum類的一些例外。

4.1.3 空塊：可以用簡潔版本

一個空的塊狀結構裏什麽也不包含，大括號可以簡潔地寫成{}，不需要換行。例外：如果它是一個多塊語句的一部分\(if/else 或 try/catch/finally\) ，即使大括號內沒內容，右大括號也要換行。

示例：

void doNothing\(\) {}

4.2 塊縮進：2個空格

每當開始一個新的塊，縮進增加2個空格，當塊結束時，縮進返回先前的縮進級別。縮進級別適用於代碼和註釋。\(見4.1.2節中的代碼示例\)

4.3 一行一個語句

每個語句後要換行。

4.4 列限制：80或100

一個項目可以選擇一行80個字符或100個字符的列限制，除了下述例外，任何一行如果超過這個字符數限制，必須自動換行。

例外：

不可能滿足列限制的行\(例如，Javadoc中的一個長URL，或是一個長的JSNI方法參考\)。

package和import語句\(見3.2節和3.3節\)。

註釋中那些可能被剪切並粘貼到shell中的命令行。

4.5 自動換行

術語說明：一般情況下，一行長代碼為了避免超出列限制\(80或100個字符\)而被分為多行，我們稱之為自動換行\(line-wrapping\)。

我們並沒有全面，確定性的準則來決定在每一種情況下如何自動換行。很多時候，對於同一段代碼會有好幾種有效的自動換行方式。

Tip: 提取方法或局部變量可以在不換行的情況下解決代碼過長的問題\(是合理縮短命名長度吧\)

4.5.1 從哪裏斷開

自動換行的基本準則是：更傾向於在更高的語法級別處斷開。

如果在非賦值運算符處斷開，那麽在該符號前斷開\(比如+，它將位於下一行\)。註意：這一點與Google其它語言的編程風格不同\(如C++和JavaScript\)。 這條規則也適用於以下“類運算符”符號：點分隔符\(.\)，類型界限中的

&

（

&lt;

T extends Foo 

&

 Bar

&gt;

\)，catch塊中的管道符號\(catch \(FooException \| BarException e\)

如果在賦值運算符處斷開，通常的做法是在該符號後斷開\(比如=，它與前面的內容留在同一行\)。這條規則也適用於foreach語句中的分號。

方法名或構造函數名與左括號留在同一行。

逗號\(,\)與其前面的內容留在同一行。

4.5.2 自動換行時縮進至少+4個空格

自動換行時，第一行後的每一行至少比第一行多縮進4個空格\(註意：制表符不用於縮進。見2.3.1節\)。

當存在連續自動換行時，縮進可能會多縮進不只4個空格\(語法元素存在多級時\)。一般而言，兩個連續行使用相同的縮進當且僅當它們開始於同級語法元素。

第4.6.3水平對齊一節中指出，不鼓勵使用可變數目的空格來對齊前面行的符號。

4.6 空白

4.6.1 垂直空白

以下情況需要使用一個空行：

類內連續的成員之間：字段，構造函數，方法，嵌套類，靜態初始化塊，實例初始化塊。

例外：兩個連續字段之間的空行是可選的，用於字段的空行主要用來對字段進行邏輯分組。

在函數體內，語句的邏輯分組間使用空行。

類內的第一個成員前或最後一個成員後的空行是可選的\(既不鼓勵也不反對這樣做，視個人喜好而定\)。

要滿足本文檔中其他節的空行要求\(比如3.3節：import語句\)

多個連續的空行是允許的，但沒有必要這樣做\(我們也不鼓勵這樣做\)。

4.6.2 水平空白

除了語言需求和其它規則，並且除了文字，註釋和Javadoc用到單個空格，單個ASCII空格也出現在以下幾個地方：

分隔任何保留字與緊隨其後的左括號\(\(\)\(如if, for catch等\)。

分隔任何保留字與其前面的右大括號\(}\)\(如else, catch\)。

在任何左大括號前\({\)，兩個例外：

@SomeAnnotation\({a, b}\)\(不使用空格\)。

String

\[\]\[\]

 x = foo;\(大括號間沒有空格，見下面的Note\)。

在任何二元或三元運算符的兩側。這也適用於以下“類運算符”符號：

類型界限中的

&

\(

&lt;

T extends Foo 

&

 Bar

&gt;

\)。

catch塊中的管道符號\(catch \(FooException \| BarException e\)。

foreach語句中的分號。

在, : ;及右括號\(\)\)後

如果在一條語句後做註釋，則雙斜杠\(//\)兩邊都要空格。這裏可以允許多個空格，但沒有必要。

類型和變量之間：List list。

數組初始化中，大括號內的空格是可選的，即new int\[\] {5, 6}和new int\[\] { 5, 6 }都是可以的。

Note：這個規則並不要求或禁止一行的開關或結尾需要額外的空格，只對內部空格做要求。

4.6.3 水平對齊：不做要求

術語說明：水平對齊指的是通過增加可變數量的空格來使某一行的字符與上一行的相應字符對齊。

這是允許的\(而且在不少地方可以看到這樣的代碼\)，但Google編程風格對此不做要求。即使對於已經使用水平對齊的代碼，我們也不需要去保持這種風格。

以下示例先展示未對齊的代碼，然後是對齊的代碼：

private int x; // this is fine

private Color color; // this too

private int x; // permitted, but future edits

private Color color; // may leave it unaligned

Tip：對齊可增加代碼可讀性，但它為日後的維護帶來問題。考慮未來某個時候，我們需要修改一堆對齊的代碼中的一行。 這可能導致原本很漂亮的對齊代碼變得錯位。很可能它會提示你調整周圍代碼的空白來使這一堆代碼重新水平對齊\(比如程序員想保持這種水平對齊的風格\)， 這就會讓你做許多的無用功，增加了reviewer的工作並且可能導致更多的合並沖突。

4.7 用小括號來限定組：推薦

除非作者和reviewer都認為去掉小括號也不會使代碼被誤解，或是去掉小括號能讓代碼更易於閱讀，否則我們不應該去掉小括號。 我們沒有理由假設讀者能記住整個Java運算符優先級表。

4.8 具體結構

4.8.1 枚舉類

枚舉常量間用逗號隔開，換行可選。

沒有方法和文檔的枚舉類可寫成數組初始化的格式：

private enum Suit { CLUBS, HEARTS, SPADES, DIAMONDS }

由於枚舉類也是一個類，因此所有適用於其它類的格式規則也適用於枚舉類。

4.8.2 變量聲明

4.8.2.1 每次只聲明一個變量

不要使用組合聲明，比如int a, b;。

4.8.2.2 需要時才聲明，並盡快進行初始化

不要在一個代碼塊的開頭把局部變量一次性都聲明了\(這是c語言的做法\)，而是在第一次需要使用它時才聲明。 局部變量在聲明時最好就進行初始化，或者聲明後盡快進行初始化。

4.8.3 數組

4.8.3.1 數組初始化：可寫成塊狀結構

數組初始化可以寫成塊狀結構，比如，下面的寫法都是OK的：

new int\[\] {

0, 1, 2, 3

}

new int\[\] {

0,

1,

2,

3

}

new int\[\] {

0, 1,

2, 3

}

new int\[\]{0, 1, 2, 3}

4.8.3.2 非C風格的數組聲明

中括號是類型的一部分：String\[\] args， 而非String args\[\]。

4.8.4 switch語句

術語說明：switch塊的大括號內是一個或多個語句組。每個語句組包含一個或多個switch標簽\(case FOO:或default:\)，後面跟著一條或多條語句。

4.8.4.1 縮進

與其它塊狀結構一致，switch塊中的內容縮進為2個空格。

每個switch標簽後新起一行，再縮進2個空格，寫下一條或多條語句。

4.8.4.2 Fall-through：註釋

在一個switch塊內，每個語句組要麽通過break, continue, return或拋出異常來終止，要麽通過一條註釋來說明程序將繼續執行到下一個語句組， 任何能表達這個意思的註釋都是OK的\(典型的是用// fall through\)。這個特殊的註釋並不需要在最後一個語句組\(一般是default\)中出現。示例：

switch \(input\) {

case 1:

case 2:

prepareOneOrTwo\(\);

// fall through

case 3:

handleOneTwoOrThree\(\);

break;

default:

handleLargeNumber\(input\);

}

4.8.4.3 default的情況要寫出來

每個switch語句都包含一個default語句組，即使它什麽代碼也不包含。

4.8.5 註解\(Annotations\)

註解緊跟在文檔塊後面，應用於類、方法和構造函數，一個註解獨占一行。這些換行不屬於自動換行\(第4.5節，自動換行\)，因此縮進級別不變。例如：

@Override

@Nullable

public String getNameIfPresent\(\) { ... }

例外：單個的註解可以和簽名的第一行出現在同一行。例如：

@Override public int hashCode\(\) { ... }

應用於字段的註解緊隨文檔塊出現，應用於字段的多個註解允許與字段出現在同一行。例如：

@Partial @Mock DataLoader loader;

參數和局部變量註解沒有特定規則。

4.8.6 註釋

4.8.6.1 塊註釋風格

塊註釋與其周圍的代碼在同一縮進級別。它們可以是/\* ... 

\*

/風格，也可以是// ...風格。對於多行的/

\*

 ... 

\*

/註釋，後續行必須從

\*

開始， 並且與前一行的\*對齊。以下示例註釋都是OK的。

/\*

\*

 This is // And so /\* Or you can

\*

 okay. // is this. \* even do this. \*/

 \*/

註釋不要封閉在由星號或其它字符繪制的框架裏。

Tip：在寫多行註釋時，如果你希望在必要時能重新換行\(即註釋像段落風格一樣\)，那麽使用/\* ... \*/。

4.8.7 Modifiers

類和成員的modifiers如果存在，則按Java語言規範中推薦的順序出現。

public protected private abstract static final transient volatile synchronized native strictfp

命名約定

5.1 對所有標識符都通用的規則

標識符只能使用ASCII字母和數字，因此每個有效的標識符名稱都能匹配正則表達式\w+。

在Google其它編程語言風格中使用的特殊前綴或後綴，如name

\_

, mName, s

\_

name和kName，在Java編程風格中都不再使用。

5.2 標識符類型的規則

5.2.1 包名

包名全部小寫，連續的單詞只是簡單地連接起來，不使用下劃線。

5.2.2 類名

類名都以UpperCamelCase風格編寫。

類名通常是名詞或名詞短語，接口名稱有時可能是形容詞或形容詞短語。現在還沒有特定的規則或行之有效的約定來命名註解類型。

測試類的命名以它要測試的類的名稱開始，以Test結束。例如，HashTest或HashIntegrationTest。

5.2.3 方法名

方法名都以lowerCamelCase風格編寫。

方法名通常是動詞或動詞短語。

下劃線可能出現在JUnit測試方法名稱中用以分隔名稱的邏輯組件。一個典型的模式是：test

&lt;

MethodUnderTest

&gt;

\_

&lt;

state

&gt;

，例如testPop

\_

emptyStack。 並不存在唯一正確的方式來命名測試方法。

5.2.4 常量名

常量名命名模式為CONSTANT\_CASE，全部字母大寫，用下劃線分隔單詞。那，到底什麽算是一個常量？

每個常量都是一個靜態final字段，但不是所有靜態final字段都是常量。在決定一個字段是否是一個常量時， 考慮它是否真的感覺像是一個常量。例如，如果任何一個該實例的觀測狀態是可變的，則它幾乎肯定不會是一個常量。 只是永遠不打算改變對象一般是不夠的，它要真的一直不變才能將它示為常量。

// Constants

static final int NUMBER = 5;

static final ImmutableList

&lt;

String

&gt;

 NAMES = ImmutableList.of\("Ed", "Ann"\);

static final Joiner COMMA\_JOINER = Joiner.on\(','\); // because Joiner is immutable

static final SomeMutableType\[\] EMPTY\_ARRAY = {};

enum SomeEnum { ENUM\_CONSTANT }

// Not constants

static String nonFinal = "non-final";

final String nonStatic = "non-static";

static final Set

&lt;

String

&gt;

 mutableCollection = new HashSet

&lt;

String

&gt;

\(\);

static final ImmutableSet

&lt;

SomeMutableType

&gt;

 mutableElements = ImmutableSet.of\(mutable\);

static final Logger logger = Logger.getLogger\(MyClass.getName\(\)\);

static final String\[\] nonEmptyArray = {"these", "can", "change"};

這些名字通常是名詞或名詞短語。

5.2.5 非常量字段名

非常量字段名以lowerCamelCase風格編寫。

這些名字通常是名詞或名詞短語。

5.2.6 參數名

參數名以lowerCamelCase風格編寫。

參數應該避免用單個字符命名。

5.2.7 局部變量名

局部變量名以lowerCamelCase風格編寫，比起其它類型的名稱，局部變量名可以有更為寬松的縮寫。

雖然縮寫更寬松，但還是要避免用單字符進行命名，除了臨時變量和循環變量。

即使局部變量是final和不可改變的，也不應該把它示為常量，自然也不能用常量的規則去命名它。

5.2.8 類型變量名

類型變量可用以下兩種風格之一進行命名：

單個的大寫字母，後面可以跟一個數字\(如：E, T, X, T2\)。

以類命名方式\(5.2.2節\)，後面加個大寫的T\(如：RequestT, FooBarT\)。

5.3 駝峰式命名法\(CamelCase\)

駝峰式命名法分大駝峰式命名法\(UpperCamelCase\)和小駝峰式命名法\(lowerCamelCase\)。 有時，我們有不只一種合理的方式將一個英語詞組轉換成駝峰形式，如縮略語或不尋常的結構\(例如”IPv6”或”iOS”\)。Google指定了以下的轉換方案。

名字從散文形式\(prose form\)開始:

把短語轉換為純ASCII碼，並且移除任何單引號。例如：”Müller’s algorithm”將變成”Muellers algorithm”。

把這個結果切分成單詞，在空格或其它標點符號\(通常是連字符\)處分割開。

推薦：如果某個單詞已經有了常用的駝峰表示形式，按它的組成將它分割開\(如”AdWords”將分割成”ad words”\)。 需要註意的是”iOS”並不是一個真正的駝峰表示形式，因此該推薦對它並不適用。

現在將所有字母都小寫\(包括縮寫\)，然後將單詞的第一個字母大寫：

每個單詞的第一個字母都大寫，來得到大駝峰式命名。

除了第一個單詞，每個單詞的第一個字母都大寫，來得到小駝峰式命名。

最後將所有的單詞連接起來得到一個標識符。

示例：

Prose form Correct Incorrect ------------------------------------------------------------------

"XML HTTP request" XmlHttpRequest XMLHTTPRequest

"new customer ID" newCustomerId newCustomerID

"inner stopwatch" innerStopwatch innerStopWatch

"supports IPv6 on iOS?" supportsIpv6OnIos supportsIPv6OnIOS

"YouTube importer" YouTubeImporter

YoutubeImporter\*

加星號處表示可以，但不推薦。

Note：在英語中，某些帶有連字符的單詞形式不唯一。例如：”nonempty”和”non-empty”都是正確的，因此方法名checkNonempty和checkNonEmpty也都是正確的。

編程實踐

6.1 @Override：能用則用

只要是合法的，就把@Override註解給用上。

6.2 捕獲的異常：不能忽視

除了下面的例子，對捕獲的異常不做響應是極少正確的。\(典型的響應方式是打印日誌，或者如果它被認為是不可能的，則把它當作一個AssertionError重新拋出。\)

如果它確實是不需要在catch塊中做任何響應，需要做註釋加以說明\(如下面的例子\)。

try {

int i = Integer.parseInt\(response\);

return handleNumericResponse\(i\);

} catch \(NumberFormatException ok\) {

// it's not numeric; that's fine, just continue

}

return handleTextResponse\(response\);

例外：在測試中，如果一個捕獲的異常被命名為expected，則它可以被不加註釋地忽略。下面是一種非常常見的情形，用以確保所測試的方法會拋出一個期望中的異常， 因此在這裏就沒有必要加註釋。

try {

emptyStack.pop\(\);

fail\(\);

} catch \(NoSuchElementException expected\) {

}

6.3 靜態成員：使用類進行調用

使用類名調用靜態的類成員，而不是具體某個對象或表達式。

Foo aFoo = ...;

Foo.aStaticMethod\(\); // good

aFoo.aStaticMethod\(\); // bad

somethingThatYieldsAFoo\(\).aStaticMethod\(\); // very bad

6.4 Finalizers: 禁用

極少會去重寫Object.finalize。

Tip：不要使用finalize。如果你非要使用它，請先仔細閱讀和理解Effective Java 第7條款：“Avoid Finalizers”，然後不要使用它。

Javadoc

7.1 格式

7.1.1 一般形式

Javadoc塊的基本格式如下所示：

/\*\*

\*

 Multiple lines of Javadoc text are written here,

\*

 wrapped normally...

 \*/

public int method\(String p1\) { ... }

或者是以下單行形式：

/\*\* An especially short bit of Javadoc. \*/

基本格式總是OK的。當整個Javadoc塊能容納於一行時\(且沒有Javadoc標記@XXX\)，可以使用單行形式。

7.1.2 段落

空行\(即，只包含最左側星號的行\)會出現在段落之間和Javadoc標記\(@XXX\)之前\(如果有的話\)。 除了第一個段落，每個段落第一個單詞前都有標簽

&lt;

p

&gt;

，並且它和第一個單詞間沒有空格。

7.1.3 Javadoc標記

標準的Javadoc標記按以下順序出現：@param, @return, @throws, @deprecated, 前面這4種標記如果出現，描述都不能為空。 當描述無法在一行中容納，連續行需要至少再縮進4個空格。

7.2 摘要片段

每個類或成員的Javadoc以一個簡短的摘要片段開始。這個片段是非常重要的，在某些情況下，它是唯一出現的文本，比如在類和方法索引中。

這只是一個小片段，可以是一個名詞短語或動詞短語，但不是一個完整的句子。它不會以A {@code Foo} is a...或This method returns...開頭, 它也不會是一個完整的祈使句，如Save the record...。然而，由於開頭大寫及被加了標點，它看起來就像是個完整的句子。

Tip：一個常見的錯誤是把簡單的Javadoc寫成/

\*\*

 @return the customer ID \*/，這是不正確的。它應該寫成/

\*\*

 Returns the customer ID. \*/。

7.3 哪裏需要使用Javadoc

至少在每個public類及它的每個public和protected成員處使用Javadoc，以下是一些例外：

7.3.1 例外：不言自明的方法

對於簡單明顯的方法如getFoo，Javadoc是可選的\(即，是可以不寫的\)。這種情況下除了寫“Returns the foo”，確實也沒有什麽值得寫了。

單元測試類中的測試方法可能是不言自明的最常見例子了，我們通常可以從這些方法的描述性命名中知道它是幹什麽的，因此不需要額外的文檔說明。

Tip：如果有一些相關信息是需要讀者了解的，那麽以上的例外不應作為忽視這些信息的理由。例如，對於方法名getCanonicalName， 就不應該忽視文檔說明，因為讀者很可能不知道詞語canonical name指的是什麽。

7.3.2 例外：重寫

如果一個方法重寫了超類中的方法，那麽Javadoc並非必需的。

7.3.3 可選的Javadoc

對於包外不可見的類和方法，如有需要，也是要使用Javadoc的。如果一個註釋是用來定義一個類，方法，字段的整體目的或行為， 那麽這個註釋應該寫成Javadoc，這樣更統一更友好。



