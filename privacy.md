# Privacy Policy — Smart Block

_Last updated: 11 November 2026_

## Short version

Smart Block does not collect, transmit or sell any personal data. Everything
it keeps stays in your own browser.

## What the extension stores

- **Your settings**: which rules are on or off and whether blocking is
  paused. These are saved with the Chrome `storage.sync` API, so they live in
  your Chrome profile and Chrome itself syncs them between your signed-in
  devices.
- **Counters**: how many items each rule hid per day, for the "today" and
  "7 days" numbers in the popup. These are plain counts with no page
  addresses, video titles or search queries. They are saved with the Chrome
  `storage.local` API, stay on this device only, and days older than 60 days
  are deleted automatically.
- **Already-counted Shorts**: so that reloading a page does not count the
  same Short twice, the identifiers of Shorts already counted are kept in
  the tab's own session storage. They never leave the tab and are erased
  when the tab is closed.

Neither the settings nor the counters ever reach the author of this
extension or any third party.

## What the extension does on web pages

The extension runs only on youtube.com and Google Search pages. There it:

- hides page elements such as YouTube Shorts, the YouTube home feed, related
  videos and comments, and the "Top stories" block and the News tab in
  Google Search;
- redirects a few addresses inside the same sites, for example a YouTube
  Shorts link to the same video in the regular player, or news.google.com to
  google.com when that rule is switched on.

To do this it looks at the structure of the page in your browser. Nothing
about the pages, your searches, the videos you watch or your accounts is
recorded or sent anywhere.

The extension does not run on any other website.

## What the extension does not do

- No analytics, telemetry or crash reporting
- No cookies, no tracking, no advertising identifiers
- No network requests of any kind
- No remote code: all logic ships inside the extension package
- No account and no sign-in
- No access to your browsing history or passwords

## Removing your data

Uninstalling the extension removes the stored settings and counters.

## Changes to this policy

If the extension ever starts handling data differently, this page will be
updated before that version is released, and the date above will change.

## Contact

Questions about this policy: open an issue at
<https://github.com/ismoilovmk/smart-block/issues>.

---

# Политика конфиденциальности — Smart Block

_Обновлено: 11 ноября 2026_

## Коротко

Smart Block не собирает, не передаёт и не продаёт персональные данные. Всё,
что он хранит, остаётся в вашем браузере.

## Что хранит расширение

- **Настройки**: какие правила включены и стоит ли блокировка на паузе. Они
  сохраняются через `storage.sync` и лежат в вашем профиле Chrome. Между
  вашими устройствами их синхронизирует сам Chrome.
- **Счётчики**: сколько элементов скрыло каждое правило за день, для чисел
  «Сегодня» и «7 дней» в окне расширения. Это только количества, без адресов
  страниц, названий видео и поисковых запросов. Они сохраняются через
  `storage.local`, остаются только на этом устройстве, а дни старше 60 дней
  удаляются автоматически.
- **Уже посчитанные Shorts**: чтобы перезагрузка страницы не считала один и
  тот же Shorts дважды, идентификаторы посчитанных Shorts хранятся в
  сессионном хранилище самой вкладки. Они не покидают вкладку и стираются,
  когда она закрывается.

Ни настройки, ни счётчики не попадают к автору расширения или третьим лицам.

## Что расширение делает на страницах

Расширение работает только на youtube.com и страницах поиска Google. Там оно:

- скрывает элементы страницы: Shorts, ленту на главной, похожие видео и
  комментарии на YouTube, блок «Главные новости» и вкладку «Новости» в
  поиске Google;
- перенаправляет несколько адресов внутри тех же сайтов, например ссылку на
  Shorts на то же видео в обычном плеере или news.google.com на google.com,
  если это правило включено.

Для этого оно смотрит на структуру страницы в вашем браузере. Ничего о
страницах, ваших запросах, видео или аккаунтах не записывается и никуда не
отправляется.

На других сайтах расширение не работает.

## Чего расширение не делает

- Нет аналитики, телеметрии и отчётов об ошибках
- Нет cookies, отслеживания и рекламных идентификаторов
- Нет сетевых запросов
- Нет удалённого кода: вся логика находится внутри пакета расширения
- Нет аккаунта и входа
- Нет доступа к истории браузера и паролям

## Удаление данных

Удаление расширения удаляет сохранённые настройки и счётчики.

## Изменения политики

Если расширение начнёт работать с данными иначе, эта страница будет
обновлена до выхода такой версии, и дата вверху изменится.

## Контакты

Вопросы по политике: создайте issue на
<https://github.com/ismoilovmk/smart-block/issues>.
