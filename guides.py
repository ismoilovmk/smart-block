"""Text of the how-to guides. Each guide answers one search query honestly:
every method that works, including the ones that need no extension.

A guide is a dict: slug, lang, pair (slug of the same guide in the other
language, or None), title, meta, h1, lead, body. Body is a list of blocks:
('h2', text), ('p', text), ('ol', [items]), ('ul', [items]), ('note', text).
Text may contain inline HTML."""

UPDATED = {'en': 'Updated November 2026', 'ru': 'Обновлено в ноябре 2026'}

EN_SHORTS = dict(
    slug='remove-youtube-shorts.html', lang='en', pair='ru/ubrat-shorts-youtube.html',
    title='How to remove YouTube Shorts on PC (and keep them gone)',
    meta='Four ways to remove YouTube Shorts on a computer: the built-in button, a bookmark, content filters and a free Chrome extension. How long each one lasts.',
    h1='How to remove YouTube Shorts on a computer',
    lead='YouTube has no setting that turns Shorts off on desktop. There are four ways to get rid of them, '
         'and they differ in how much they hide and how long it lasts.',
    body=[
        ('h2', '1. The built-in “hide” button: about 30 days'),
        ('p', 'On the home page, find the Shorts shelf, open the menu in its corner and choose the option to hide it '
              '(shown as an “X” or “Not interested”).'),
        ('ul', ['Hides the shelf on the home page only.',
                'Shorts stay in search results, in subscriptions, on channel pages and in the left menu.',
                'The shelf comes back by itself after roughly a month.']),
        ('h2', '2. Open subscriptions instead of the home page'),
        ('p', 'Bookmark <code>youtube.com/feed/subscriptions</code> and use it as your way into YouTube. '
              'You skip the recommendation feed entirely. Shorts from channels you follow can still appear there, '
              'and nothing changes in search.'),
        ('h2', '3. Content filters in an ad blocker'),
        ('p', 'Ad blockers that accept custom filter lists can hide Shorts with community-made rules. '
              'This works well in Firefox with uBlock Origin. In Chrome it is harder now: the full uBlock Origin '
              'is no longer offered for Chrome, and its Lite version supports fewer custom rules. '
              'Filter lists also need updating whenever YouTube changes its layout.'),
        ('h2', '4. A browser extension made for this'),
        ('p', 'An extension hides Shorts everywhere at once and keeps them hidden for as long as it is switched on. '
              '<a href="./">Smart Block</a> is the one this site is about. It is free and removes:'),
        ('ul', ['Shorts shelves on the home page, in search and in subscriptions;',
                'the Shorts entry in the left menu and the Shorts tab on channels;',
                'the “Shorts” filter above search results;',
                'direct Shorts links, which go back to the home page instead.']),
        ('p', 'Everything else on YouTube keeps working. If you need Shorts for a moment, pause the extension '
              'for 15, 30 or 60 minutes and it switches back on by itself.'),
        ('note', 'Other extensions do this too. Unhook is the best known and covers YouTube only. '
                 'Pick whichever you trust; the important part is that it removes Shorts in every place, not just one shelf.'),
        ('h2', 'Which one should you use?'),
        ('ul', ['You only mind the shelf on the home page: the built-in button, repeated monthly.',
                'You want Shorts gone for good on your computer: an extension.',
                'You already run uBlock Origin in Firefox: a filter list is enough.']),
        ('p', 'On a phone the options are different. See '
              '<a href="remove-youtube-shorts-phone.html">how to remove YouTube Shorts on iPhone and Android</a>.'),
    ])

EN_RECS = dict(
    slug='remove-youtube-recommendations.html', lang='en', pair='ru/ubrat-rekomendacii-youtube.html',
    title='How to remove YouTube recommendations (home feed, sidebar, end screen)',
    meta='How to remove YouTube recommendations on the home page, next to the player and at the end of a video: history settings, autoplay, a free extension.',
    h1='How to remove YouTube recommendations',
    lead='Recommendations show up in three places: the home feed, the column next to the player, and the wall of '
         'suggestions when a video ends. Each has its own fix.',
    body=[
        ('h2', 'Home feed: turn off watch history'),
        ('ol', ['Open <code>myactivity.google.com</code> and go to “YouTube History”.',
                'Turn the history off. You can also delete what is already saved.',
                'Reload YouTube. With no history, the home page stays empty and shows a search box.']),
        ('p', 'The price: “continue watching” and your history list stop working too, on every device signed in to the account.'),
        ('h2', 'End of video: turn off autoplay'),
        ('p', 'The autoplay switch is in the player’s control bar. Turning it off stops the next video from starting, '
              'but the grid of suggestions at the end still appears.'),
        ('h2', 'Sidebar: no built-in switch'),
        ('p', 'YouTube offers no way to hide the related videos next to the player. You can make the player wider '
              '(theatre mode or full screen) to push them out of view.'),
        ('h2', 'All three at once: an extension'),
        ('p', '<a href="./">Smart Block</a> is a free Chrome extension with a separate switch for each place:'),
        ('ul', ['<strong>Home feed</strong>: replaced by a short note; search and subscriptions work as usual.',
                '<strong>Related videos</strong>: the column next to the player and the end-of-video suggestions.',
                '<strong>Comments</strong>, if they distract you as well.']),
        ('p', 'Your watch history keeps working, because nothing is changed in your account. The extension only hides '
              'parts of the page in your browser.'),
        ('note', 'Unhook is another well-known extension for the same job. Both are free.'),
        ('p', 'Also annoyed by Shorts? See <a href="remove-youtube-shorts.html">how to remove YouTube Shorts on PC</a>.'),
    ])

EN_NEWS = dict(
    slug='remove-top-stories-google.html', lang='en', pair=None,
    title='How to remove Top stories and news from Google Search results',
    meta='Google has no switch for Top stories. What works: the Web filter, the udm=14 trick, and a free Chrome extension that hides the news block.',
    h1='How to remove “Top stories” from Google Search',
    lead='You search for one thing and Google puts a row of headlines above the answer. There is no setting that '
         'turns the block off, but there are three ways around it.',
    body=[
        ('h2', '1. The “Web” filter'),
        ('p', 'Under the search box, open “More” and choose “Web”. Google then shows plain links only: '
              'no Top stories, no video carousel, no AI summary. You have to choose it again for every search.'),
        ('h2', '2. Make “Web” the default with udm=14'),
        ('p', 'The Web filter is the address parameter <code>udm=14</code>. In Chrome, open '
              '<code>chrome://settings/searchEngines</code>, add a search engine with the address below and make it the default:'),
        ('p', '<code>https://www.google.com/search?q=%s&amp;udm=14</code>'),
        ('p', 'Every search from the address bar now opens in Web mode. You lose the useful extras too: '
              'maps, the calculator, quick answers.'),
        ('h2', '3. Hide only the news'),
        ('p', '<a href="./">Smart Block</a> is a free Chrome extension that removes just the news parts and leaves '
              'the rest of the results page as it was:'),
        ('ul', ['the “Top stories” block in results;',
                'the News tab under the search box;',
                'news.google.com, which goes to the regular Google home page instead.']),
        ('note', 'Looking for the news feed on your phone’s home screen or in the Google app? That is Google Discover, '
                 'a different feature. It is switched off in the Google app settings, not in the browser.'),
    ])

EN_PHONE = dict(
    slug='remove-youtube-shorts-phone.html', lang='en', pair='ru/ubrat-shorts-na-telefone.html',
    title='How to remove YouTube Shorts on iPhone and Android',
    meta='What works for removing YouTube Shorts in the phone app: the Shorts time limit, the hide button, watching in a browser. And what does not.',
    h1='How to remove YouTube Shorts on a phone',
    lead='The YouTube app has no “off” switch for Shorts, and no extension can change the app. '
         'These are the options that exist today.',
    body=[
        ('h2', '1. Set a Shorts time limit'),
        ('p', 'The YouTube app has a daily limit for the Shorts feed. Open the app settings and look in the time '
              'management section for the Shorts limit, then set the smallest value offered. When the limit is reached, '
              'the feed stops and shows a reminder.'),
        ('p', 'The limit is easy to dismiss, so it works as a nudge rather than a lock. '
              'The names of the menu items change between app versions.'),
        ('h2', '2. Hide the Shorts shelf'),
        ('p', 'On the home tab, open the menu on the Shorts shelf and choose the option to hide it. '
              'As on desktop, it returns after about a month, and the Shorts button at the bottom stays.'),
        ('h2', '3. Watch in a browser instead of the app'),
        ('p', 'In a mobile browser YouTube can be filtered. Firefox for Android supports extensions, including '
              'content blockers with rules that hide Shorts. On iPhone, Safari supports content-blocker apps from the App Store. '
              'This takes some setting up, and you give up the app’s downloads and background play.'),
        ('h2', 'What does not work'),
        ('ul', ['Chrome extensions: Chrome on phones does not run them.',
                '“Not interested” on single videos: it tunes recommendations but does not remove Shorts.']),
        ('h2', 'On your computer'),
        ('p', 'On a computer Shorts can be removed completely. '
              '<a href="remove-youtube-shorts.html">Here is how</a>, including the free '
              '<a href="./">Smart Block</a> extension. Smart Block works in desktop Chrome only.'),
    ])

RU_SHORTS = dict(
    slug='ru/ubrat-shorts-youtube.html', lang='ru', pair='remove-youtube-shorts.html',
    title='Как убрать шортсы (Shorts) из YouTube на ПК навсегда',
    meta='Четыре способа убрать шортсы из YouTube на компьютере: встроенная кнопка, закладка, фильтры и бесплатное расширение Chrome. Надолго ли хватает.',
    h1='Как убрать шортсы из YouTube на компьютере',
    lead='В настройках YouTube на компьютере нет выключателя Shorts. Убрать шортсы можно четырьмя способами. '
         'Они отличаются тем, что именно скрывают и надолго ли.',
    body=[
        ('h2', '1. Встроенная кнопка «скрыть»: примерно на 30 дней'),
        ('p', 'На главной странице найдите полку Shorts, откройте меню в её углу и выберите «Скрыть» '
              '(крестик или «Не интересует»).'),
        ('ul', ['Скрывается только полка на главной.',
                'В поиске, в подписках, на страницах каналов и в меню слева шортсы остаются.',
                'Примерно через месяц полка возвращается сама.']),
        ('h2', '2. Открывать подписки вместо главной'),
        ('p', 'Добавьте в закладки <code>youtube.com/feed/subscriptions</code> и заходите на YouTube через неё. '
              'Ленты рекомендаций вы не увидите вовсе. Шортсы от каналов, на которые вы подписаны, там всё же появляются, '
              'а в поиске ничего не меняется.'),
        ('h2', '3. Фильтры в блокировщике рекламы'),
        ('p', 'Блокировщики, которые принимают свои списки фильтров, умеют скрывать Shorts по готовым правилам. '
              'Хорошо работает в Firefox с uBlock Origin. В Chrome сейчас сложнее: полной версии uBlock Origin для Chrome '
              'больше нет, а версия Lite поддерживает меньше своих правил. Кроме того, списки нужно обновлять, '
              'когда YouTube меняет вёрстку.'),
        ('h2', '4. Расширение, сделанное для этого'),
        ('p', 'Расширение убирает шортсы сразу везде и держит их скрытыми, пока включено. '
              '<a href="./">Smart Block</a>, которому посвящён этот сайт, бесплатный и убирает:'),
        ('ul', ['полки Shorts на главной, в поиске и в подписках;',
                'пункт Shorts в меню слева и вкладку Shorts на каналах;',
                'фильтр «Shorts» над результатами поиска;',
                'прямые ссылки на Shorts: вместо них открывается главная.']),
        ('p', 'Всё остальное на YouTube работает как обычно. Если шортсы понадобились на минуту, поставьте паузу '
              'на 15, 30 или 60 минут: потом расширение включится само.'),
        ('note', 'Это умеют и другие расширения. Самое известное — Unhook, оно работает только с YouTube. '
                 'Выбирайте то, которому доверяете. Главное, чтобы шортсы убирались везде, а не только одна полка.'),
        ('h2', 'Что выбрать'),
        ('ul', ['Мешает только полка на главной: встроенная кнопка, раз в месяц.',
                'Хотите убрать шортсы на компьютере насовсем: расширение.',
                'Уже пользуетесь uBlock Origin в Firefox: хватит списка фильтров.']),
        ('p', 'На телефоне способы другие: <a href="ubrat-shorts-na-telefone.html">как убрать шортсы на айфоне и андроиде</a>.'),
    ])

RU_RECS = dict(
    slug='ru/ubrat-rekomendacii-youtube.html', lang='ru', pair='remove-youtube-recommendations.html',
    title='Как убрать рекомендации в YouTube: главная, похожие видео, конец ролика',
    meta='Как убрать рекомендации в Ютубе на главной, рядом с плеером и в конце видео: история просмотров, автовоспроизведение, бесплатное расширение.',
    h1='Как убрать рекомендации в YouTube',
    lead='Рекомендации появляются в трёх местах: в ленте на главной, в колонке рядом с плеером и в сетке подсказок, '
         'когда видео закончилось. Для каждого места свой способ.',
    body=[
        ('h2', 'Лента на главной: отключить историю просмотров'),
        ('ol', ['Откройте <code>myactivity.google.com</code> и перейдите в «История YouTube».',
                'Отключите историю. Сохранённое можно заодно удалить.',
                'Обновите YouTube. Без истории главная остаётся пустой, со строкой поиска.']),
        ('p', 'Цена: перестают работать «продолжить просмотр» и список истории, причём на всех устройствах с этим аккаунтом.'),
        ('h2', 'Конец видео: отключить автовоспроизведение'),
        ('p', 'Переключатель автовоспроизведения находится на панели плеера. Следующее видео перестанет запускаться само, '
              'но сетка подсказок в конце останется.'),
        ('h2', 'Колонка справа: встроенного выключателя нет'),
        ('p', 'Скрыть похожие видео рядом с плеером в настройках YouTube нельзя. Можно растянуть плеер '
              '(режим кинотеатра или полный экран), и колонка уйдёт из поля зрения.'),
        ('h2', 'Всё сразу: расширение'),
        ('p', '<a href="./">Smart Block</a> — бесплатное расширение для Chrome с отдельным переключателем на каждое место:'),
        ('ul', ['<strong>Лента на главной</strong>: вместо неё короткая заметка, поиск и подписки работают как обычно.',
                '<strong>Похожие видео</strong>: колонка рядом с плеером и подсказки в конце ролика.',
                '<strong>Комментарии</strong>, если они тоже отвлекают.']),
        ('p', 'История просмотров при этом продолжает работать: в аккаунте ничего не меняется. '
              'Расширение только скрывает части страницы в вашем браузере.'),
        ('note', 'Для той же задачи есть известное расширение Unhook. Оба бесплатные.'),
        ('p', 'Мешают ещё и шортсы? Смотрите, <a href="ubrat-shorts-youtube.html">как убрать Shorts из YouTube на ПК</a>.'),
    ])

RU_PHONE = dict(
    slug='ru/ubrat-shorts-na-telefone.html', lang='ru', pair='remove-youtube-shorts-phone.html',
    title='Как убрать шортсы из YouTube на телефоне: айфон и андроид',
    meta='Что помогает убрать шортсы в приложении YouTube на телефоне: лимит времени, кнопка «скрыть», просмотр через браузер. И что не работает.',
    h1='Как убрать шортсы из YouTube на телефоне',
    lead='В приложении YouTube нет выключателя Shorts, и никакое расширение изменить приложение не может. '
         'Вот способы, которые есть сегодня.',
    body=[
        ('h2', '1. Поставить лимит времени на Shorts'),
        ('p', 'В приложении YouTube есть дневной лимит для ленты Shorts. Откройте настройки приложения, найдите в разделе '
              'управления временем лимит Shorts и выберите самое маленькое значение. Когда лимит исчерпан, '
              'лента останавливается и показывает напоминание.'),
        ('p', 'Лимит легко отклонить, так что это подсказка, а не замок. '
              'Названия пунктов меню меняются от версии к версии.'),
        ('h2', '2. Скрыть полку Shorts'),
        ('p', 'На главной вкладке откройте меню полки Shorts и выберите «Скрыть». Как и на компьютере, '
              'через месяц она вернётся, а кнопка Shorts внизу экрана останется.'),
        ('h2', '3. Смотреть через браузер, а не через приложение'),
        ('p', 'В мобильном браузере YouTube можно фильтровать. Firefox для Android поддерживает расширения, '
              'в том числе блокировщики с правилами против Shorts. На айфоне Safari поддерживает приложения-блокировщики '
              'из App Store. Это требует настройки, и вы теряете загрузки и фоновое воспроизведение приложения.'),
        ('h2', 'Что не работает'),
        ('ul', ['Расширения Chrome: на телефонах Chrome их не запускает.',
                '«Не интересует» на отдельных роликах: это подстраивает рекомендации, но шортсы не убирает.']),
        ('h2', 'На компьютере'),
        ('p', 'На компьютере шортсы убираются полностью. <a href="ubrat-shorts-youtube.html">Вот как это сделать</a>, '
              'в том числе бесплатным расширением <a href="./">Smart Block</a>. Оно работает только в Chrome на компьютере.'),
    ])

GUIDES = [EN_SHORTS, EN_RECS, EN_NEWS, EN_PHONE, RU_SHORTS, RU_RECS, RU_PHONE]
