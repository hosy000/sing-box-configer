
# ارسال اس ان آی جدید از طریق تلگرام
در بروز رسانی که انجام شد این قابلیت به بات اضاقه شده که خودش روزانه uuid، key_pair و short_id رو تجدید میکنه و کانفیگ جدید رو تو بات میفرسته. همچنین این قابلیت اضافه شده که فقط به پیام های خودتون جواب بده و هیچ کس حتی با داشتن آدرس بات تون نتونه تغییری ایجاد کنه.

#### از طریق آموزش سگارو از لینک زیر نحوه پیدا کردن SNI خوب و ساز و کار کلی کارکرد سیستم رو یاد بگیرید، من خودم از اونجا یاد گرفتم

[آموزش سگارو](https://telegra.ph/How-run-Reality-protocol-with-Xray-or-Sing-box-Core-with-iSegaro-04-18)

## راه اندازی پراکسی
توجه کنید که یه بخشی از کار رو اینجا انجام میدیم و بقیه ش رو باید از آموزش سگارو پیش برید!
اول با دستور زیر سینگ باکس رو دریافت کنید. نسخه ش رو هم میتونید ویراییش کنید قبل از اجرای دستور ولی در حال حاضر(1402/2) این جدیدترین نسخه س:
```bash
curl -Lo /root/sb https://github.com/SagerNet/sing-box/releases/download/v1.3-beta11/sing-box-1.3-beta11-linux-amd64.tar.gz && tar -xzf /root/sb && cp -f /root/sing-box-*/sing-box /root && rm -r /root/sb /root/sing-box-* && chown root:root /root/sing-box && chmod +x /root/sing-box
```
### راه اندازی بات
اول فایل first.py رو میگیریم که آی پی و پورت سرورتون و توکن بات تلگرام رو به راحتی ست کنید بدون نیاز به استفاده از nano، اول ازتون آی پی و بعد پورت سرور رو میخواد و بعدش هم توکن بات تلگرام. دو تا دستور زیر رو اجرا کنید:
```bash
curl -Lo /root/first.py https://raw.githubusercontent.com/hosy000/sing-box-configer/master/first.py
python first.py
```
بعد از اینکه تموم شد دستور زیر رو اجرا کنید که فایل first.py که دیگه بهش احتیاج نداریم حذف بشه:
```bash
rm first.py
```
حالا فایل های اصلی رو در جای درست شون بذاریم:
```bash
curl -Lo /root/configer.py https://raw.githubusercontent.com/hosy000/sing-box-configer/master/configer.py
curl -Lo /etc/systemd/system/configer.service https://raw.githubusercontent.com/hosy000/sing-box-configer/master/configer.service
curl -Lo /etc/systemd/system/sing-box.service https://raw.githubusercontent.com/iSegaro/Sing-Box/main/sing-box.service
```
واسه اجرای اسکریپت نیاز به پایتون و کتابخونه تلگرام داریم، با این دستور نصبش کنید:
```bash
pip install python-telegram-bot==13.5
```
حالا برای اینکه اسکریپت مون خودکار اجرا بشه حتی بعد ریستارت، دستورات زیر رو هم وارد کنید:

```bash
systemctl daemon-reload
systemctl enable configer.service
systemctl start configer.service
```
اسکریپت مون که اجرا شد خودش براتون کانفیگ اولیه رو ست میکنه و شما با ارسال دستور start/ در تلگرام به بات تون هم کانفیگ رو دریافت کنید هم آی دی شما بعنوان صاحب ست میشه و دیگه بات فقط به شما جواب میده. 

اگر بعد از اینکه پراکسی رو راه انداحتید کانفیگ تون تایم اوت داد اس ان آی  جدید براش بفرستید تو تلگرام و دوباره امتحان کنید. پیامی که به بات تلگرام میفرستید هم به این شکل باشه
```bash
/replace sni
```
با دستور status/ هم میتونید استاتوس سینگ باکس یا کانفیگر رو تو تلگرام دریافت کنید که ببینید سینگ باکس در چه وضعیتیه و اگه مشکلی هست از کجاست.
```bash
/status sing-box
/status configer.service
```

*با تشکر از همه کسایی که برای دسترسی آزاد به اینترنت زحمت میکشن از جمله سگارو عزیز و تیم IRCF*
