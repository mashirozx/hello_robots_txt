Add custom avatar frame for your Mastodon account

为你的 Mastodon 账号添加一个头像框

*中文说明在后面*

To add a custom avatar frame, just add your rules to $user_config in [avatar.scss](https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar.scss) as samples:

1. for local user @username, add rules below:
  - if you want a pair of cat ears:

      `"username": ("cat_ears"),`

  - if you want a bilibili avatar frame of Kyaru (from Re:Dive), add rules below:

      `"username": ("bili_frame", $bili_frame_012),`

2. and for user from another instance @username@example.com, add rules like follow:

  - if you want a pair of cat ears:

      `"username@example.com": ("cat_ears"),`

  - if you want a bilibili avatar frame of Kyaru (from Re:Dive), add rules below:

      `"username@example.com": ("bili_frame", $bili_frame_012),`

You can previewview all the bilibili avatar frame and get the index key here:
<https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar_variables.scss>

If you want to get more avatar frame from bilibili.com, this link will help you :)
<http://api.bilibili.com/x/space/acc/info?mid=13972644>  
PS. To use this API, you need to login your Bilibili account in browser first.

***

你需要一个Github账号，按下面指示修改后向本仓库提交 pull request，如果你是小白不会 pull request，建议先阅读这篇我能找到的最浅显的 Github 使用教程：<https://www.jianshu.com/p/d2b95458ff63>，实在还是不会私信我吧（[@mashiro](https://hello.2heng.xin/@mashiro)）。

需要添加头像框只需按以下例子向 [avatar.scss](https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar.scss) 文件中的 $user_config 添加规则即可:

1. 对于本站用户 @username, 添加如下规则:
  - 猫耳:

      `"username": ("cat_ears"),`

  - 公主连接凯露的头像框:

      `"username": ("bili_frame", $bili_frame_012),`

2. 对于外站用户 @username@example.com, 添加如下规则:

  - 猫耳:

      `"username@example.com": ("cat_ears"),`

  - 公主连接凯露的头像框:

      `"username@example.com": ("bili_frame", $bili_frame_012),`

你可以在下面查到哔哩哔哩头像框对应的代码索引，后续会考虑做成一个网页方便查找的:
<https://github.com/mashirozx/hello_robots_txt/blob/master/custom/scss/avatar_variables.scss>

如果你想要获取更多 bilibili.com 的头像框, 这个接口会很有用 :)
<http://api.bilibili.com/x/space/acc/info?mid=13972644>  
PS. 使用前请在浏览器上登陆自己的b站账号.
