"""Builds the static site: index.html, ru/index.html, privacy.html,
ru/privacy.html. Run:  python build.py [path-to-PRIVACY.md]

The privacy pages are generated from the extension's PRIVACY.md so the
policy has one source of text. Without the argument the existing
privacy.md copy in this folder is used."""
import html
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).parent
ISSUES = 'https://github.com/ismoilovmk/smart-block/issues'

EN = dict(
    lang='en', other_lang='ru', other_href='ru/', other='Русский', root='',
    title='Smart Block — remove YouTube Shorts and recommendations',
    meta='A free Chrome extension that removes YouTube Shorts, recommendations and the home feed, '
         'and the Top stories block in Google Search. Search and subscriptions keep working.',
    privacy='Privacy',
    h1='YouTube without <s>Shorts</s>.<br>Google without the <s>news block</s>.',
    lead='Smart Block is a Chrome extension that removes the feeds and leaves the rest working. '
         'You still search, watch and read. You just stop scrolling.',
    cta='Chrome Web Store: in review',
    note='Free. No account. The install link will appear here once the store approves the first version.',
    what='What goes, what stays', gone='Removed', stay='Still works',
    gone_items=['YouTube Shorts, everywhere', 'The YouTube home feed', 'Related videos and end screens',
                'Comments, if you want', '“Top stories” in Google Search', 'The Google News tab'],
    stay_items=['YouTube search', 'Subscriptions', 'Playlists and history', 'The video you came for',
                'Normal Google results', 'Images, Maps, everything else'],
    how='How it works',
    how_items=[
        'Every rule has its own switch, so you turn off only what pulls you in.',
        'Changes apply at once, without reloading the page.',
        'YouTube’s own “hide Shorts” button brings them back after 30 days. '
        'Here they stay gone while the extension is on.',
        'Need the feed for a moment? Pause for 15, 30 or 60 minutes. It switches back on by itself.',
    ],
    priv_h='Nothing leaves your browser',
    priv_p='No analytics, no tracking, no network requests, no account. The extension runs only on '
           'youtube.com and Google Search. The <a href="privacy.html">privacy policy</a> is one short page.',
    footer='Smart Block is an independent project, not affiliated with YouTube or Google. · '
           f'<a href="privacy.html">Privacy</a> · <a href="{ISSUES}">Report a problem</a>',
)

RU = dict(
    lang='ru', other_lang='en', other_href='../', other='English', root='../',
    title='Smart Block — убрать Shorts и рекомендации YouTube',
    meta='Бесплатное расширение для Chrome: убирает шортсы, рекомендации и ленту YouTube и блок '
         '«Главные новости» в поиске Google. Поиск и подписки работают как обычно.',
    privacy='Конфиденциальность',
    h1='YouTube без <s>Shorts</s>.<br>Google без <s>блока новостей</s>.',
    lead='Smart Block — расширение для Chrome, которое убирает ленты и оставляет всё остальное рабочим. '
         'Вы по-прежнему ищете, смотрите и читаете. Просто перестаёте листать.',
    cta='Chrome Web Store: на проверке',
    note='Бесплатно. Без аккаунта. Ссылка на установку появится здесь, когда стор одобрит первую версию.',
    what='Что уходит и что остаётся', gone='Убрано', stay='Работает как раньше',
    gone_items=['Шортсы YouTube, везде', 'Лента на главной YouTube', 'Похожие видео и подсказки в конце',
                'Комментарии, если хотите', '«Главные новости» в поиске Google', 'Вкладка «Новости» в Google'],
    stay_items=['Поиск по YouTube', 'Подписки', 'Плейлисты и история', 'Видео, за которым вы пришли',
                'Обычные результаты Google', 'Картинки, Карты и всё остальное'],
    how='Как это работает',
    how_items=[
        'У каждого правила свой переключатель: отключайте только то, что затягивает именно вас.',
        'Изменения применяются сразу, без перезагрузки страницы.',
        'Встроенная кнопка YouTube «скрыть Shorts» возвращает их через 30 дней. '
        'Здесь они остаются убранными, пока расширение включено.',
        'Нужна лента на минуту? Поставьте паузу на 15, 30 или 60 минут. Потом всё включится само.',
    ],
    priv_h='Ничего не покидает ваш браузер',
    priv_p='Нет аналитики, отслеживания, сетевых запросов и аккаунта. Расширение работает только на '
           'youtube.com и в поиске Google. <a href="privacy.html">Политика конфиденциальности</a> '
           'занимает одну короткую страницу.',
    footer='Smart Block — независимый проект, не связанный с YouTube или Google. · '
           f'<a href="privacy.html">Конфиденциальность</a> · <a href="{ISSUES}">Сообщить о проблеме</a>',
)


def items(xs):
    return ''.join(f'<li>{x}</li>' for x in xs)


def shell(lang, title, root, nav, body, footer, meta=''):
    meta_tag = f'\n<meta name="description" content="{meta}">' if meta else ''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>{meta_tag}
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="name" href="./">Smart Block</a>
  <nav>{nav}</nav>
</header>
{body}
<footer>{footer}</footer>
</div>
</body>
</html>
'''


def landing(t):
    nav = (f'<a href="privacy.html">{t["privacy"]}</a>'
           f'<a href="{t["other_href"]}" lang="{t["other_lang"]}">{t["other"]}</a>')
    body = f'''<main>
<h1>{t["h1"]}</h1>
<p class="lead">{t["lead"]}</p>
<span class="cta soon">{t["cta"]}</span>
<p class="note">{t["note"]}</p>

<h2>{t["what"]}</h2>
<div class="cols">
  <div class="box gone"><h3>{t["gone"]}</h3><ul>{items(t["gone_items"])}</ul></div>
  <div class="box stay"><h3>{t["stay"]}</h3><ul>{items(t["stay_items"])}</ul></div>
</div>

<h2>{t["how"]}</h2>
<ul class="plain">{items(t["how_items"])}</ul>

<h2>{t["priv_h"]}</h2>
<p>{t["priv_p"]}</p>
</main>'''
    return shell(t['lang'], t['title'], t['root'], nav, body, t['footer'], t['meta'])


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'&lt;(https?://[^&]+)&gt;', r'<a href="\1">\1</a>', s)
    return re.sub(r'^_(.+)_$', r'<em>\1</em>', s)


def join(lines):
    return ' '.join(line.strip() for line in lines)


def markdown(text):
    out = []
    for block in re.split(r'\n\s*\n', text.strip()):
        lines = block.split('\n')
        if lines[0].startswith('# '):
            out.append(f'<h1>{inline(lines[0][2:])}</h1>')
        elif lines[0].startswith('## '):
            out.append(f'<h2>{inline(lines[0][3:])}</h2>')
        elif lines[0].startswith('- '):
            lis = [inline(join(i[2:].split('\n'))) for i in re.split(r'\n(?=- )', block)]
            out.append('<ul class="plain">' + items(lis) + '</ul>')
        else:
            out.append(f'<p>{inline(join(lines))}</p>')
    return '\n'.join(out)


def privacy_pages(source):
    text = source.read_text(encoding='utf-8')
    text = re.sub(r'https://github\.com/ismoilovmk/-?smart-block/issues', ISSUES, text)
    en_md, ru_md = text.split('\n---\n')
    en_nav = '<a href="./">Home</a><a href="ru/privacy.html" lang="ru">Русский</a>'
    ru_nav = '<a href="./">Главная</a><a href="../privacy.html" lang="en">English</a>'
    en = shell('en', 'Privacy Policy — Smart Block', '', en_nav, f'<article>\n{markdown(en_md)}\n</article>', 'Smart Block')
    ru = shell('ru', 'Политика конфиденциальности — Smart Block', '../', ru_nav,
               f'<article>\n{markdown(ru_md)}\n</article>', 'Smart Block')
    return en, ru


def main():
    copy = ROOT / 'privacy.md'
    if len(sys.argv) > 1:
        shutil.copyfile(sys.argv[1], copy)
    (ROOT / 'ru').mkdir(exist_ok=True)
    (ROOT / 'index.html').write_text(landing(EN), encoding='utf-8')
    (ROOT / 'ru' / 'index.html').write_text(landing(RU), encoding='utf-8')
    en, ru = privacy_pages(copy)
    (ROOT / 'privacy.html').write_text(en, encoding='utf-8')
    (ROOT / 'ru' / 'privacy.html').write_text(ru, encoding='utf-8')
    print('built 4 pages')


if __name__ == '__main__':
    main()
