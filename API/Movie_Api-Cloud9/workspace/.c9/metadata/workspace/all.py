{"filter":false,"title":"all.py","tooltip":"/all.py","undoManager":{"mark":29,"position":29,"stack":[[{"start":{"row":0,"column":0},"end":{"row":37,"column":12},"action":"insert","lines":["import requests","import json","import os ","from pprint import pprint as pp","import csv","","date = [\"20181111\",\"20181118\",\"20181125\",\"20181202\",\"20181209\",\"20181216\",\"20181223\",\"20181230\",\"20190106\",\"20190113\"]","movie_key = os.getenv('MOVIE_TOKEN')","movies = [ ]","url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'","","for d in date:","    params = {","        'key': movie_key,","        'targetDt':d,","        'weekGb':\"0\"","    }","    res = requests.get(url, params=params)","    movies.append(res.json().get('boxOfficeResult').get('weeklyBoxOfficeList'))","    ","","movie_d = {}","for i in range(len(movies)):","  for m in movies[i]:","      movie_d[m.get('movieCd')] = [m.get('movieCd'),m.get('movieNm'),m.get('audiAcc'),date[i]]","","movie_l = list(movie_d.values())","# print(len(movie_l))","","with open('boxoffice.csv','w') as f1:","  boxoffice = csv.writer(f1)","  boxoffice.writerow(['movieCd', 'movieNm', 'audiAcc', 'recordDt'])","  for li in movie_l:","    boxoffice.writerow(li)","    ","f = open('boxoffice.csv','r')","print(len(f.read()))","f.close()   "],"id":1}],[{"start":{"row":37,"column":12},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":39,"column":0},"end":{"row":78,"column":14},"action":"insert","lines":["","","# --------영화 상세 ----------------","movie_c = list(movie_d.keys())","","url_base = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'","movieinfo = [ ]","for c in movie_c:","    params = {","        'key': movie_key,","        'movieCd' : c","    }","    res = requests.get(url_base, params=params)","    movieinfo.append(res.json().get('movieInfoResult').get('movieInfo'))","    ","info_d = []","for m in movieinfo:","  li = [m.get('movieCd'),m.get('movieNm'),m.get('movieNmEn'),m.get('movieNmOg'),","        m.get('openDt')[:4],m.get('openDt')[4:6],m.get('showTm'),'/'.join([g.get('genreNm') for g in m.get('genres')]),","        m.get('directors')[0].get('peopleNm'),m.get('audits')[0].get('watchGradeNm')]","  actors = m.get('actors')","  if len(actors) < 3:","    li.extend([actors[i].get('peopleNm') for i in range(len(actors))])","    li.extend([''*(3-len(actors))])","  else:","    li.extend([actors[i].get('peopleNm') for i in range(3)])","  info_d.append(li)","  ","with open('movie.csv','w') as f2:","  fields = ()","  boxoffice = csv.writer(f2)","  boxoffice.writerow(['movieCd','movieNm','movieNmEn','movieNmOg','openY','openM','showTm',","                      'genre','director','watchGrade','actor1','actor2','actor3'])","  for li in info_d:","    boxoffice.writerow(li)","    ","with open('movie.csv',newline='') as f:","  reader = csv.reader(f)","  for row in reader:","    print(row)"],"id":3}],[{"start":{"row":78,"column":14},"end":{"row":79,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":79,"column":0},"end":{"row":79,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":10},"action":"remove","lines":["------"],"id":5},{"start":{"row":41,"column":4},"end":{"row":41,"column":10},"action":"insert","lines":["------"]}],[{"start":{"row":41,"column":10},"end":{"row":41,"column":16},"action":"insert","lines":["------"],"id":6}],[{"start":{"row":41,"column":16},"end":{"row":41,"column":22},"action":"insert","lines":["------"],"id":7}],[{"start":{"row":41,"column":22},"end":{"row":41,"column":28},"action":"insert","lines":["------"],"id":8}],[{"start":{"row":41,"column":28},"end":{"row":41,"column":34},"action":"insert","lines":["------"],"id":9}],[{"start":{"row":41,"column":47},"end":{"row":41,"column":53},"action":"insert","lines":["------"],"id":10}],[{"start":{"row":41,"column":53},"end":{"row":41,"column":59},"action":"insert","lines":["------"],"id":11}],[{"start":{"row":41,"column":59},"end":{"row":41,"column":65},"action":"insert","lines":["------"],"id":12}],[{"start":{"row":41,"column":65},"end":{"row":41,"column":71},"action":"insert","lines":["------"],"id":13}],[{"start":{"row":79,"column":0},"end":{"row":79,"column":4},"action":"remove","lines":["    "],"id":14}],[{"start":{"row":79,"column":0},"end":{"row":116,"column":25},"action":"insert","lines":["","# ------------------------------------네이버 api --------------------------------------","movie_nc = {}","for info in movieinfo:","    movie_nc[info.get('movieNm')] = info.get('movieCd')","# print(movie_nc)","","header = {","    'X-Naver-Client-Id' : naver_id,","    'X-Naver-Client-Secret' : naver_pw","}","","url_base = 'https://openapi.naver.com/v1/search/movie.json?'","nmovie = []","for name in movie_nc:","  url_sub = \"query={}\".format(name)","  res = requests.get(url_base + url_sub, headers = header)","  nmovie.append(res.json().get('items'))"," ","movie_l = list(movie_nc.values())","movie_data = []","for i in range(len(nmovie)):","  m = nmovie[i][0]","  movie_data.append([movie_l[i],m.get('image'),m.get('link'),m.get('userRating')])","  ","with open('movie_naver.csv','w') as f1:","  mnaver = csv.writer(f1)","  mnaver.writerow(['movieCd', 'movieInk', 'movieImg', 'userRat'])","  for li in movie_data:","      mnaver.writerow(li)","f = open('movie_naver.csv','r')","# print(f.read())","f.close()","","for img in movie_data:","    with open(\"images/{}.jpg\".format(img[0]),'wb') as f3:","        imgdata = requests.get(img[1]).content","        f3.write(imgdata)"],"id":15}],[{"start":{"row":80,"column":84},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":81,"column":0},"end":{"row":82,"column":38},"action":"insert","lines":["naver_id = os.getenv('NAVER_MOVIE_ID')","naver_pw = os.getenv('NAVER_MOVIE_PW')"],"id":18}],[{"start":{"row":114,"column":0},"end":{"row":115,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":115,"column":0},"end":{"row":115,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":115,"column":1},"end":{"row":115,"column":2},"action":"insert","lines":[" "],"id":20},{"start":{"row":115,"column":2},"end":{"row":115,"column":3},"action":"insert","lines":["-"]},{"start":{"row":115,"column":3},"end":{"row":115,"column":4},"action":"insert","lines":["-"]},{"start":{"row":115,"column":4},"end":{"row":115,"column":5},"action":"insert","lines":["-"]},{"start":{"row":115,"column":5},"end":{"row":115,"column":6},"action":"insert","lines":["-"]},{"start":{"row":115,"column":6},"end":{"row":115,"column":7},"action":"insert","lines":["-"]},{"start":{"row":115,"column":7},"end":{"row":115,"column":8},"action":"insert","lines":["-"]},{"start":{"row":115,"column":8},"end":{"row":115,"column":9},"action":"insert","lines":["-"]},{"start":{"row":115,"column":9},"end":{"row":115,"column":10},"action":"insert","lines":["-"]},{"start":{"row":115,"column":10},"end":{"row":115,"column":11},"action":"insert","lines":["-"]},{"start":{"row":115,"column":11},"end":{"row":115,"column":12},"action":"insert","lines":["-"]},{"start":{"row":115,"column":12},"end":{"row":115,"column":13},"action":"insert","lines":["-"]},{"start":{"row":115,"column":13},"end":{"row":115,"column":14},"action":"insert","lines":["-"]},{"start":{"row":115,"column":14},"end":{"row":115,"column":15},"action":"insert","lines":["-"]},{"start":{"row":115,"column":15},"end":{"row":115,"column":16},"action":"insert","lines":["-"]},{"start":{"row":115,"column":16},"end":{"row":115,"column":17},"action":"insert","lines":["-"]},{"start":{"row":115,"column":17},"end":{"row":115,"column":18},"action":"insert","lines":["-"]},{"start":{"row":115,"column":18},"end":{"row":115,"column":19},"action":"insert","lines":["-"]},{"start":{"row":115,"column":19},"end":{"row":115,"column":20},"action":"insert","lines":["-"]},{"start":{"row":115,"column":20},"end":{"row":115,"column":21},"action":"insert","lines":["-"]},{"start":{"row":115,"column":21},"end":{"row":115,"column":22},"action":"insert","lines":["-"]},{"start":{"row":115,"column":22},"end":{"row":115,"column":23},"action":"insert","lines":["-"]},{"start":{"row":115,"column":23},"end":{"row":115,"column":24},"action":"insert","lines":["-"]},{"start":{"row":115,"column":24},"end":{"row":115,"column":25},"action":"insert","lines":["-"]},{"start":{"row":115,"column":25},"end":{"row":115,"column":26},"action":"insert","lines":["-"]},{"start":{"row":115,"column":26},"end":{"row":115,"column":27},"action":"insert","lines":["-"]},{"start":{"row":115,"column":27},"end":{"row":115,"column":28},"action":"insert","lines":["-"]},{"start":{"row":115,"column":28},"end":{"row":115,"column":29},"action":"insert","lines":["-"]}],[{"start":{"row":115,"column":29},"end":{"row":115,"column":30},"action":"insert","lines":["-"],"id":21},{"start":{"row":115,"column":30},"end":{"row":115,"column":31},"action":"insert","lines":["-"]},{"start":{"row":115,"column":31},"end":{"row":115,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":115,"column":31},"end":{"row":115,"column":32},"action":"remove","lines":["d"],"id":22}],[{"start":{"row":115,"column":31},"end":{"row":115,"column":32},"action":"insert","lines":[" "],"id":23}],[{"start":{"row":115,"column":32},"end":{"row":115,"column":33},"action":"insert","lines":["이"],"id":27}],[{"start":{"row":115,"column":33},"end":{"row":115,"column":34},"action":"insert","lines":["미"],"id":30}],[{"start":{"row":115,"column":34},"end":{"row":115,"column":35},"action":"insert","lines":["지"],"id":31}],[{"start":{"row":115,"column":35},"end":{"row":115,"column":36},"action":"insert","lines":[" "],"id":32}],[{"start":{"row":115,"column":36},"end":{"row":115,"column":37},"action":"insert","lines":["저"],"id":36}],[{"start":{"row":115,"column":37},"end":{"row":115,"column":38},"action":"insert","lines":["장"],"id":38}],[{"start":{"row":115,"column":38},"end":{"row":115,"column":39},"action":"insert","lines":[" "],"id":39}],[{"start":{"row":115,"column":39},"end":{"row":115,"column":40},"action":"insert","lines":["-"],"id":40},{"start":{"row":115,"column":40},"end":{"row":115,"column":41},"action":"insert","lines":["-"]},{"start":{"row":115,"column":41},"end":{"row":115,"column":42},"action":"insert","lines":["-"]},{"start":{"row":115,"column":42},"end":{"row":115,"column":43},"action":"insert","lines":["-"]},{"start":{"row":115,"column":43},"end":{"row":115,"column":44},"action":"insert","lines":["-"]},{"start":{"row":115,"column":44},"end":{"row":115,"column":45},"action":"insert","lines":["-"]},{"start":{"row":115,"column":45},"end":{"row":115,"column":46},"action":"insert","lines":["-"]},{"start":{"row":115,"column":46},"end":{"row":115,"column":47},"action":"insert","lines":["-"]},{"start":{"row":115,"column":47},"end":{"row":115,"column":48},"action":"insert","lines":["-"]},{"start":{"row":115,"column":48},"end":{"row":115,"column":49},"action":"insert","lines":["-"]},{"start":{"row":115,"column":49},"end":{"row":115,"column":50},"action":"insert","lines":["-"]},{"start":{"row":115,"column":50},"end":{"row":115,"column":51},"action":"insert","lines":["-"]},{"start":{"row":115,"column":51},"end":{"row":115,"column":52},"action":"insert","lines":["-"]},{"start":{"row":115,"column":52},"end":{"row":115,"column":53},"action":"insert","lines":["-"]},{"start":{"row":115,"column":53},"end":{"row":115,"column":54},"action":"insert","lines":["-"]},{"start":{"row":115,"column":54},"end":{"row":115,"column":55},"action":"insert","lines":["-"]},{"start":{"row":115,"column":55},"end":{"row":115,"column":56},"action":"insert","lines":["-"]},{"start":{"row":115,"column":56},"end":{"row":115,"column":57},"action":"insert","lines":["-"]},{"start":{"row":115,"column":57},"end":{"row":115,"column":58},"action":"insert","lines":["-"]},{"start":{"row":115,"column":58},"end":{"row":115,"column":59},"action":"insert","lines":["-"]},{"start":{"row":115,"column":59},"end":{"row":115,"column":60},"action":"insert","lines":["-"]},{"start":{"row":115,"column":60},"end":{"row":115,"column":61},"action":"insert","lines":["-"]},{"start":{"row":115,"column":61},"end":{"row":115,"column":62},"action":"insert","lines":["-"]},{"start":{"row":115,"column":62},"end":{"row":115,"column":63},"action":"insert","lines":["-"]},{"start":{"row":115,"column":63},"end":{"row":115,"column":64},"action":"insert","lines":["-"]},{"start":{"row":115,"column":64},"end":{"row":115,"column":65},"action":"insert","lines":["-"]},{"start":{"row":115,"column":65},"end":{"row":115,"column":66},"action":"insert","lines":["-"]},{"start":{"row":115,"column":66},"end":{"row":115,"column":67},"action":"insert","lines":["-"]},{"start":{"row":115,"column":67},"end":{"row":115,"column":68},"action":"insert","lines":["-"]},{"start":{"row":115,"column":68},"end":{"row":115,"column":69},"action":"insert","lines":["-"]},{"start":{"row":115,"column":69},"end":{"row":115,"column":70},"action":"insert","lines":["-"]}]]},"ace":{"folds":[],"scrolltop":1200,"scrollleft":0,"selection":{"start":{"row":115,"column":70},"end":{"row":115,"column":70},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":87,"state":"start","mode":"ace/mode/python"}},"timestamp":1548377619066,"hash":"e24d3005564bb0d9100708ecb10419e9d53761e8"}