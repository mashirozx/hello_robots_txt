import os
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# set header
opener = urllib.request.build_opener()
opener.addheaders = []
opener.addheaders.append(
    ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'))
opener.addheaders.append(
    ('Referer', 'https://space.bilibili.com/13972644/dynamic'))
urllib.request.install_opener(opener)

dl_path = '../custom/img/avatar_frame/'
html_source_file = './dl-bili-frame.html'
scss_file = '../custom/scss/avatar_variables.scss'

f = open(html_source_file, 'r', encoding="utf-8")
dl_html = f.read()
f.close()

soup = BeautifulSoup(dl_html, features='html.parser')

if os.path.exists(scss_file):
  historyList = [line.rstrip('\n') for line in open(scss_file, 'r', encoding="utf-8")]
else:
  historyList = []

i = 1
for li in soup.find_all('li'):
  for img in li.find_all('img'):
    if (img.get('data') == 'pendant'):
      name = li.find('p').getText()
      url = img.get('src')
      f_name = os.path.basename(urlparse(url).path)
      file = dl_path + f_name
      if not os.path.exists(file):
        urllib.request.urlretrieve(url, file)

        if i < 10:
          id = '00' + str(i)
        elif i < 100:
          id = '0' + str(i)
        else:
          id = str(i)
        scss_line = f'$bili_frame_{id}: "{f_name}"; // {name} @ {url}'
        historyList.append(scss_line)
        with open(scss_file, 'w+', encoding="utf-8") as db:
          for row in historyList:
            db.write(str(row) + '\n')

        print('SAVE TO DB: ' + f_name)
      else:
        print('SKIP      : ' + f_name)
  # end of for
  i += 1

data = [
    ['hanser', 'http://i0.hdslb.com/bfs/garb/item/c114c9e3cd0f97982c47817e54cd35d23e830755.png'],
    ['中国绊爱', 'http://i1.hdslb.com/bfs/garb/item/c70f8bf2df14434d17d565aa5b0ff5347507f91c.png'],
    ['大理寺日志', 'http://i2.hdslb.com/bfs/garb/item/0312f94397fa9de427b1dc0ecda22b0086fc7197.png'],
    ['天宝伏妖录', 'http://i2.hdslb.com/bfs/garb/item/2bd90561ac8ac4ee5c5d2ac755d5892f51c0bbf7.png'],
    ['BML2020暗黑版', 'http://i1.hdslb.com/bfs/garb/item/6de2948bdf4b19112b06f899c88063dea4643ad7.png'],
    ['BML麦克风', 'http://i0.hdslb.com/bfs/face/f405c0fa184dc113e3d36c5f14e2e0ba8ae68190.png'],
    ['笔耕不辍', 'http://i2.hdslb.com/bfs/face/7bb7473829aeb29fa2eb17ba903f2b8bb602e629.png'],
    ['洛天依8th生日纪念', 'http://i1.hdslb.com/bfs/garb/item/e98718ae0d09e48bc85df969820b88241bc06883.png'],
    ['百妖谱', 'http://i1.hdslb.com/bfs/garb/item/858ac4fa56e9d6d843929958803cdf24cb068990.png'],
    ['泠鸢yousa', 'http://i2.hdslb.com/bfs/garb/item/3e66e712b8e70c6b02393c54ad5fd8d993eb39f9.png'],
    ['乐正绫五周年生日', 'http://i1.hdslb.com/bfs/garb/item/e09e26e354d4a3733c641913cddd07f78fcb2679.png'],
    ['明日方舟', 'http://i0.hdslb.com/bfs/garb/item/0c8e7d627a35c378b757f39419889ef1fcc0ed9b.png'],
    ['碧蓝航线2020', 'http://i1.hdslb.com/bfs/garb/item/fe1267f786bf69f1471aff715f8d38ec0e486df5.png'],
    ['碧蓝航线2020（动态）', 'http://i1.hdslb.com/bfs/garb/item/0aa9fd33133ed3fd9f11c857cc6ca848d6804113.webp'],
    ['如果历史是一群喵', 'http://i0.hdslb.com/bfs/garb/item/cd3e9a6fa18db9ebdc128b0fef64cb32c5aab854.png'],
    ['百鬼幼儿园', 'http://i1.hdslb.com/bfs/garb/item/c503b48eafaa67720b5bd93e3eaac15168b9fc0f.png'],
    ['王者荣耀-安琪拉', 'http://i0.hdslb.com/bfs/garb/item/d7f020c3cf017042c1f61fc6278994de66fa8cfc.png'],
    ['bilibili秋', 'http://i2.hdslb.com/bfs/face/aa04bf5ba7157461de99ab4de2e6250b3498d304.png'],
    ['约战：精灵再临', 'http://i0.hdslb.com/bfs/garb/item/88973710baf6272bafe36b1ae77fbad5e2b688a4.png'],
    ['#EveOneCat', 'http://i0.hdslb.com/bfs/garb/item/3a6053f073f979a776e02e088dd7dd7694c5b1f3.png'],
    ['#EveOneCat（动态）', 'http://i0.hdslb.com/bfs/garb/item/6c7f2ccb92627b11101dfbb616524845cac8f216.webp']
]

for item in data:
  name = item[0]
  url = item[1]
  f_name = os.path.basename(urlparse(url).path)
  file = dl_path + f_name
  if not os.path.exists(file):
    urllib.request.urlretrieve(url, file)

    if i < 10:
      id = '00' + str(i)
    elif i < 100:
      id = '0' + str(i)
    else:
      id = str(i)
    i += 1
    scss_line = f'$bili_frame_{id}: "{f_name}"; // {name} @ {url}'
    historyList.append(scss_line)
    with open(scss_file, 'w+', encoding="utf-8") as db:
      for row in historyList:
        db.write(str(row) + '\n')

    print('SAVE TO DB: ' + f_name)
  else:
    print('SKIP      : ' + f_name)
  # end of for
  i += 1
