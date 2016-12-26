# AppStringsTranslator
Automatically translate iOS App language into multi-language, depends on Baidu translate. 依赖百度翻译，自动把 App 语言文件翻译成多国语言。

## Usage

1. Modify `AppStringsTranslator.py`, fill your own Baidu `AppKey/SecretKey`, See [this](http://api.fanyi.baidu.com/api/trans/product/desktop?req=developer).
2. Run script from terminal.
3. Input strings file name.
4. Input from language.
5. Input to language list, split by space.
6. Wait and done.

``` bash
>> LSiMac:AppStringsTranslator $ python AppStringsTranslator.py
>> Enter a fileName: Localizable.strings
>> Supports languages:
['auto', 'zh', 'en', 'yue', 'wyw', 'jp', 'kor', 'fra', 'spa', 'th', 'ara', 'ru', 'pt', 'de', 'it', 'el', 'nl', 'pl', 'bul', 'est', 'dan', 'fin', 'cs', 'rom', 'slo', 'swe', 'hu', 'cht', 'vie']
>> Enter from language: zh
>> Enter to language list, split by space: cht en jp kor
>> Start
Translating cht to fileName: Localizable_cht.strings
Finished translating to cht
Translating en to fileName: Localizable_en.strings
Finished translating to en
Translating jp to fileName: Localizable_jp.strings
Finished translating to jp
Translating kor to fileName: Localizable_kor.strings
Finished translating to kor
All done!

```

## Feature

- Translate all values in `xx.strings`.
- Keep original keys, comments and empty lines.
- Generate new strings file `xx_toLang.strings` in the same directory.

## Supports languages

``` bash
语言简写               名称
auto                自动检测
zh                  中文
en                  英语
yue                 粤语
wyw                 文言文
jp                  日语
kor                 韩语
fra                 法语
spa                 西班牙语
th                  泰语
ara                 阿拉伯语
ru                  俄语
pt                  葡萄牙语
de                  德语
it                  意大利语
el                  希腊语
nl                  荷兰语
pl                  波兰语
bul                 保加利亚语
est                 爱沙尼亚语
dan                 丹麦语
fin                 芬兰语
cs                  捷克语
rom                 罗马尼亚语
slo                 斯洛文尼亚语
swe                 瑞典语
hu                  匈牙利语
cht                 繁体中文
vie                 越南语
```

## Q & A

Q: Why do not use Google translate? 
A: In China, Google's services are not stable.  
 

## Reference

1. [Baidu Translate API](http://api.fanyi.baidu.com/api/trans/product/apidoc)