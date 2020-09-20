# AutoSignInXMU
部署于GitHub Action 的XMU疫情打卡自动化⏰
本项目参考项目：[华大疫情自动打卡](https://github.com/Saujyun/AutoAction)，不过后者还有邮件提示和其他的签到项目，而且本校的打卡时间是从早上7点开始，所以设置为7：05分打卡，如果需要修改时间请修改main.yml的schedule选项。

### 如何部署

1. 一个GitHub账户。

   直接猛戳fork按钮将工程拷贝一份到你的仓库🔝

2. 配置你的账号和密码。

   在仓库的setting中的secrets里面添加你的“统一身份认证”的账号XMU_USER密码XMU_PASSWORD。❗：变量名必须是这两个对应的。

3. 打开**Action**查看工作流：

   selenium针对静态网页，随时可能失效。如果出现问题查看log信息，欢迎提Issue/Pull request😁。

   要是不需要每天填报了，那进入setting->action->选择Disable Actions for this repository。该仓库的工作流将不再运行。

