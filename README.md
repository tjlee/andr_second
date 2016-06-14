# andr_second
Задача№2

Есть лог-файл времени запросов к страницам аггрегатора интернет-магазинов следующего формата:
комментарии один запрос на одной строке, разделители полей - запятые, поля: время запроса, код ответа сервера, время загрузки 
при помощи Curl, время загрузки браузером, URL, тип ответа (INFO или WARN) 
Необходимо определить следующее: 
1) среднее время загрузки страницы через Curl и через браузер 
2) выделить из лога 5% запросов с максимальным временем загрузки 
3) выделить из лога запросы с максимальным разбросом между временем загрузки Curl и браузером 
4) выделить из лога 10 самых быстро загружаемых страниц магазинов (www.somesite/shop/....) П
ример лог-файла приведен ниже, реальный файл имеет несколько миллионов записей.
В качестве ответа принимаются любые скрипты, вычисляющие указанные значения 
Logfile created on 2011-10-11 15:58:37 +0400 by logger.rb/25413 
11/10/2011 15:58:33, 200, 0.563, 4.186122, http://www.somesite.ru/user/mike, INFO 
11/10/2011 15:58:37, 200, 0.677, 2.759748, http://www.somesite.ru/shop/Electronics, INFO
11/10/2011 15:58:41, 301, 0.188, 3.66476, http://www.somesite.ru/user/john/request_750361, INFO
11/10/2011 15:58:45, 200, 0.360, 0.989319, http://www.somesite.ru/shoplist/4014, INFO
11/10/2011 16:01:53, 200, 0.784, 3.873538, http://www.somesite.ru, INFO
11/10/2011 16:01:53, 200, 0.784, 3.873538, http://www.somesite.ru, WARN
11/10/2011 16:04:54, 200, 1.757, 3.681106, http://www.somesite.ru, INFO
11/10/2011 16:04:54, 200, 1.757, 3.681106, http://www.somesite.ru, WARN
11/10/2011 16:06:44, 200, 3.745, 3.588299, http://www.somesite.ru, INFO
11/10/2011 16:06:44, 200, 3.745, 3.588299, http://www.somesite.ru, WARN
11/10/2011 16:06:52, 200, 1.469, 3.270595, http://www.somesite.ru/user/helen, INFO
11/10/2011 16:06:52, 200, 1.469, 3.270595, http://www.somesite.ru/user/helen, WARN
11/10/2011 16:06:57, 200, 1.229, 4.498426, http://www.somesite.ru/shop/Photo, INFO
11/10/2011 16:06:57, 200, 1.229, 4.498426, http://www.somesite.ru/shop/Photo, WARN
11/10/2011 16:07:02, 301, 0.179, 5.39399, http://www.somesite.ru/user/jim/request_1761131, INFO
11/10/2011 16:07:02, 301, 0.179, 5.39399, http://www.somesite.ru/user/jim/request_1761131, WARN
11/10/2011 16:07:08, 200, 1.832, 1.046474, http://www.somesite.ru/shoplist/2004, INFO
11/10/2011 16:07:08, 200, 1.832, 1.046474, http://www.somesite.ru/shoplist/2004, WARN
11/10/2011 16:09:38, 200, 0.675, 3.503416, http://www.somesite.ru, INFO
11/10/2011 16:09:42, 200, 0.577, 3.6698, http://www.somesite.ru/user/bart, INFO
11/10/2011 16:09:47, 200, 0.473, 2.522292, http://www.somesite.ru/shop/DVD, INFO
11/10/2011 16:09:50, 301, 0.139, 3.5027, http://www.somesite.ru/user/leela/request_1342010, INFO
11/10/2011 16:09:53, 200, 0.301, 1.337687, http://www.somesite.ru/shoplist/4012, INFO
11/10/2011 16:12:39, 200, 1.032, 3.384388, http://www.somesite.ru, INFO
11/10/2011 16:12:43, 200, 0.619, 3.363121, http://www.somesite.ru/user/prof, INFO
11/10/2011 16:12:47, 200, 0.661, 2.378967, http://www.somesite.ru/shop/DVD, INFO
11/10/2011 16:12:50, 301, 0.157, 3.01223, http://www.somesite.ru/user/ghost/request_0249576, INFO
11/10/2011 16:12:54, 200, 0.365, 1.324937, http://www.somesite.ru/shoplist/4025, INFO
11/10/2011 16:15:41, 200, 1.008, 5.508995, http://www.somesite.ru, INFO
11/10/2011 16:15:48, 200, 2.556, 3.342224, http://www.somesite.ru/user/bounty, INFO
11/10/2011 16:15:54, 200, 1.266, 2.425955, http://www.somesite.ru/shop/Food, INFO
11/10/2011 16:15:57, 301, 0.161, 3.745915, http://www.somesite.ru/user/kate/request_0233815, INFO
11/10/2011 16:16:01, 404, 1.067, 2.230022, http://www.somesite.ru/shoplist/2107, INFO
11/10/2011 16:16:43, 200, 1.893, 4.720332, http://www.somesite.ru, INFO
11/10/2011 16:16:50, 200, 1.076, 3.547179, http://www.somesite.ru/user/dave, INFO
11/10/2011 16:16:54, 200, 1.113, 2.395444, http://www.somesite.ru/shop/Luxury, INFO
11/10/2011 16:16:58, 301, 0.155, 3.334468, http://www.somesite.ru/user/sarah/request_1005955, INFO
11/10/2011 16:17:02, 200, 0.383, 1.324922, http://www.somesite.ru/shoplist/2020, INFO
12/10/2011 13:42:29, 200, 1.058, 4.077444, http://www.somesite.ru, INFO
12/10/2011 13:42:34, 200, 0.577, 3.529785, http://www.somesite.ru/user/greg, INFO
12/10/2011 13:42:38, 200, 0.633, 2.549162, http://www.somesite.ru/shop/Cars, INFO
12/10/2011 13:42:42, 301, 0.149, 3.113283, http://www.somesite.ru/user/whatfor/request_2294691, INFO
12/10/2011 13:42:45, 200, 0.373, 1.372535, http://www.somesite.ru/shoplist/2103, INFO
12/10/2011 13:45:27, 200, 1.649, 3.788733, http://www.somesite.ru, INFO
12/10/2011 13:45:33, 200, 0.979, 4.29754, http://www.somesite.ru/user/sheyla, INFO
12/10/2011 13:45:38, 200, 1.061, 2.480179, http://www.somesite.ru/shop/Computers, INFO
12/10/2011 13:45:42, 301, 0.156, 3.08493, http://www.somesite.ru/user/targ/request_746359, INFO
12/10/2011 13:45:45, 200, 0.389, 0.926507, http://www.somesite.ru/shoplist/4016, INFO
12/10/2011 13:48:27, 200, 0.789, 4.546018, http://www.somesite.ru, INFO
12/10/2011 13:48:33, 200, 0.553, 4.266922, http://www.somesite.ru/user/progressor, INFO
12/10/2011 13:48:38, 200, 0.561, 2.461738, http://www.somesite.ru/shop/Cars, INFO
12/10/2011 13:48:41, 301, 0.149, 3.466122, http://www.somesite.ru/user/robot/request_797839, INFO
12/10/2011 13:48:44, 200, 0.444, 1.141595, http://www.somesite.ru/shoplist/4010, INFO
12/10/2011 13:51:27, 200, 1.683, 3.567614, http://www.somesite.ru, INFO
12/10/2011 13:51:33, 200, 0.900, 3.569849, http://www.somesite.ru/user/wizard, INFO
12/10/2011 13:51:37, 200, 1.139, 2.57537, http://www.somesite.ru/shop/Food, INFO
12/10/2011 13:51:41, 301, 0.145, 3.155322, http://www.somesite.ru/user/don/request_1101212, INFO
12/10/2011 13:51:44, 200, 0.375, 1.177174, http://www.somesite.ru/shoplist/4019, INFO
12/10/2011 14:09:42, 200, 0.720, 3.701964, http://www.somesite.ru, INFO
12/10/2011 14:09:47, 200, 0.562, 3.208066, http://www.somesite.ru/user/heyla, INFO
12/10/2011 14:09:51, 200, 0.531, 2.329227, http://www.somesite.ru/shop/Photo, INFO
12/10/2011 14:09:54, 301, 0.144, 2.836007, http://www.somesite.ru/user/brian/request_1021641, INFO
