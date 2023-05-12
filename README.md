
# ارسال اس ان آی جدید از طریق تلگرام
در بروز رسانی که انجام شد این قابلیت به بات اضاقه شده که خودش روزانه uuid، key_pair و short_id رو تجدید میکنه و کانفیگ جدید رو تو بات میفرسته. همچنین این قابلیت اضافه شده که فقط به پیام های خودتون جواب بده و هیچ کس حتی با داشتن آدرس بات تون نتونه تغییری ایجاد کنه.

از طریق آموزش سگارو از لینک زیر اول پراکسی تون رو راه بندازید:

[آموزش سگارو](https://telegra.ph/How-run-Reality-protocol-with-Xray-or-Sing-box-Core-with-iSegaro-04-18)


## راه اندازی بات
اول فایل first.py رو میگیریم که آی پی سرورتون و توکن بات تلگرام رو به راحتی ست کنید بدون نیاز به استفاده از nano، اول ازتون آی پی سرور رو میخواد و بعد هم توکن بات تلگرام. دو تا دستور زیر رو اجرا کنید:
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
 پیامی که به بات تلگرام میفرستید هم به این شکل باشه
```bash
/replace sni
```
