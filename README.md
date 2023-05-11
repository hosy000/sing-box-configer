
# ارسال اس ان آی جدید از طریق تلگرام

از طریق آموزش سگارو از لینک  اول پراکسی تون رو راه بندازید:

[آموزش سگارو](https://telegra.ph/How-run-Reality-protocol-with-Xray-or-Sing-box-Core-with-iSegaro-04-18)


## راه اندازی

اول فایل ها رو در جای درست شون بذاریم:
```bash
curl -Lo /root/configer.py https://raw.githubusercontent.com/hosy000/sing-box-configer/master/configer.py
```
```bash
curl -Lo /etc/systemd/system/configer.service https://raw.githubusercontent.com/hosy000/sing-box-configer/master/configer.service
```
با دستور زیر فایل اسکریپت رو باز کنید و چیزایی که سگارو گفته بود رو به همون روش تغییر بدید و آخرای کد هم اونجا که نوشته telegram_bot_token_from_BotFather به جای این توکنی که BotFather بهتون داده رو اونجا قرار بدید:

```bash
nano configer.py
```
واسه اجرای اسکریپت نیاز به پایتون و کتابخونه تلگرام داریم، با این دستور نصبش کنید:
```bash
pip install python-telegram-bot==13.5
```
حالا برای اینکه اسکریپت مون خودکار اجرا بشه بعد ریستارت هم دستورات زیر رو هم وارد کنید:

```bash
systemctl daemon-reload
systemctl enable configer.service
systemctl start configer.service
```
 پیامی که به بات تلگرام میفرستید هم به این شکل باشه
```bash
/replace sni
```
