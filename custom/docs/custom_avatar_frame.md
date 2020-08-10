Add custom avatar frame for your Mastodon account

为你的 Mastodon 账号添加一个头像框

<details>
 <summary>English Manual</summary>

To add a custom avatar frame, just add your rules to $user_config in [avatar.scss](https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar.scss) as samples:

For user @mashiro@hello.2heng.xin, add congif below (one account can only add one line of configuration, you can modify your configuration at any time):
  - if you want a pair of cat ears:

      `"https://hello.2heng.xin/@mashiro": ("cat_ears"),`

  - if you want a bilibili avatar frame of Kyaru (from Re:Dive), add rules below:

      `"https://hello.2heng.xin/@mashiro": ("bili_frame", $bili_frame_012),`

You can previewview all the bilibili avatar frame and get the index key here:
<https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar_variables.scss>

If you want to get more avatar frame from bilibili.com, this link will help you :)
<http://api.bilibili.com/x/space/acc/info?mid=13972644>  
PS. To use this API, you need to login your Bilibili account in browser first.

***

</details>

<details>
 <summary>中文说明</summary>

这里是配置项的说明，如果你是第一次用 Github，请照这里的说明操作：https://hello.2heng.xin/@sakura/104662388067118300

需要添加头像框只需按以下例子向 [avatar.scss](https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar.scss) 文件中的 $user_config 添加规则即可:

对于 @mashiro@hello.2heng.xin, 添加如下规则（每个账号仅限填写一行记录，你可以随时在这里修改你的配置）:
  - 猫耳:

      `"https://hello.2heng.xin/@mashiro": ("cat_ears"),`

  - 公主连接凯露的头像框:

      `"https://hello.2heng.xin/@mashiro": ("bili_frame", $bili_frame_012),`

你可以在下面链接里查到哔哩哔哩头像框对应的代码索引（你需要获得头像框对应的 `$bili_frame_xxx` 变量名，用来放在上面的配置里），后续会考虑做成一个网页方便查找:
<https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar_variables.scss>

如果你想要获取更多 bilibili.com 的头像框, 这个接口会很有用 :)
<http://api.bilibili.com/x/space/acc/info?mid=13972644>  
PS. 使用前请在浏览器上登陆自己的b站账号（cookie认证）.

</details>
