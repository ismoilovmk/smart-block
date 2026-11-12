"""Builds the static site. Run:  python build.py [path-to-PRIVACY.md]

Output: landing pages (index.html, ru/index.html), privacy pages, the
how-to guides from guides.py, sitemap.xml and robots.txt.

The privacy pages are generated from the extension's PRIVACY.md so the
policy has one source of text. Without the argument the existing
privacy.md copy in this folder is used.

Set STORE_URL once the extension is public: every install button on the
site switches from "in review" to a real link."""
import html
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))  # so `python -I build.py` finds guides.py

from guides import GUIDES, UPDATED  # noqa: E402
BASE = 'https://ismoilovmk.github.io/smart-block/'
ISSUES = 'https://github.com/ismoilovmk/smart-block/issues'
STORE_URL = None

EN = dict(
    lang='en', path='', other_lang='ru', other_href='ru/', other='Русский', root='',
    title='Smart Block — remove YouTube Shorts and recommendations',
    meta='A free Chrome extension that removes YouTube Shorts, recommendations and the home feed, '
         'and the Top stories block in Google Search. Search and subscriptions keep working.',
    privacy='Privacy',
    h1='YouTube without <s>Shorts</s>.<br>Google without the <s>news block</s>.',
    lead='Smart Block is a Chrome extension that removes the feeds and leaves the rest working. '
         'You still search, watch and read. You just stop scrolling.',
    cta_soon='Chrome Web Store: in review', cta='Add to Chrome — free',
    note_soon='Free. No account. The install link will appear here once the store approves the first version.',
    note='Free. No account. Nothing leaves your browser.',
    what='What goes, what stays', gone='Removed', stay='Still works',
    gone_items=['YouTube Shorts, everywhere', 'The YouTube home feed', 'Related videos and end screens',
                'Comments, if you want', '“Top stories” in Google Search', 'The Google News tab, if you want'],
    stay_items=['YouTube search', 'Subscriptions', 'Playlists and history', 'The video you came for',
                'Normal Google results', 'Images, Maps, everything else'],
    how='How it works',
    how_items=[
        'Every rule has its own switch, so you turn off only what pulls you in.',
        'Changes apply at once, without reloading the page.',
        'YouTube’s own “hide Shorts” button brings them back after 30 days. '
        'Here they stay gone while the extension is on.',
        'Need the feed for a moment? Pause for 15, 30 or 60 minutes, or until tomorrow. It switches back on by itself.',
        'A Short someone sends you still opens, as a normal video with no feed to swipe.',
    ],
    priv_h='Nothing leaves your browser',
    priv_p='No analytics, no tracking, no network requests, no account. The extension runs only on '
           'youtube.com and Google Search. The <a href="privacy.html">privacy policy</a> is one short page.',
    guides_h='Guides', home='Home', get='Get Smart Block',
    footer='Smart Block is an independent project, not affiliated with YouTube or Google. · '
           f'<a href="privacy.html">Privacy</a> · <a href="{ISSUES}">Report a problem</a>',
)

RU = dict(
    lang='ru', path='ru/', other_lang='en', other_href='../', other='English', root='../',
    title='Smart Block — убрать Shorts и рекомендации YouTube',
    meta='Бесплатное расширение для Chrome: убирает шортсы, рекомендации и ленту YouTube и блок '
         '«Главные новости» в поиске Google. Поиск и подписки работают как обычно.',
    privacy='Конфиденциальность',
    h1='YouTube без <s>Shorts</s>.<br>Google без <s>блока новостей</s>.',
    lead='Smart Block — расширение для Chrome, которое убирает ленты и оставляет всё остальное рабочим. '
         'Вы по-прежнему ищете, смотрите и читаете. Просто перестаёте листать.',
    cta_soon='Chrome Web Store: на проверке', cta='Установить в Chrome — бесплатно',
    note_soon='Бесплатно. Без аккаунта. Ссылка на установку появится здесь, когда стор одобрит первую версию.',
    note='Бесплатно. Без аккаунта. Ничего не покидает ваш браузер.',
    what='Что уходит и что остаётся', gone='Убрано', stay='Работает как раньше',
    gone_items=['Шортсы YouTube, везде', 'Лента на главной YouTube', 'Похожие видео и подсказки в конце',
                'Комментарии, если хотите', '«Главные новости» в поиске Google', 'Вкладка «Новости» в Google, если хотите'],
    stay_items=['Поиск по YouTube', 'Подписки', 'Плейлисты и история', 'Видео, за которым вы пришли',
                'Обычные результаты Google', 'Картинки, Карты и всё остальное'],
    how='Как это работает',
    how_items=[
        'У каждого правила свой переключатель: отключайте только то, что затягивает именно вас.',
        'Изменения применяются сразу, без перезагрузки страницы.',
        'Встроенная кнопка YouTube «скрыть Shorts» возвращает их через 30 дней. '
        'Здесь они остаются убранными, пока расширение включено.',
        'Нужна лента на минуту? Поставьте паузу на 15, 30 или 60 минут либо до завтра. Потом всё включится само.',
        'Shorts, который вам прислали, всё равно откроется: как обычное видео, без ленты.',
    ],
    priv_h='Ничего не покидает ваш браузер',
    priv_p='Нет аналитики, отслеживания, сетевых запросов и аккаунта. Расширение работает только на '
           'youtube.com и в поиске Google. <a href="privacy.html">Политика конфиденциальности</a> '
           'занимает одну короткую страницу.',
    guides_h='Инструкции', home='Главная', get='Установить Smart Block',
    footer='Smart Block — независимый проект, не связанный с YouTube или Google. · '
           f'<a href="privacy.html">Конфиденциальность</a> · <a href="{ISSUES}">Сообщить о проблеме</a>',
)

SITE = {'en': EN, 'ru': RU}


def items(xs):
    return ''.join(f'<li>{x}</li>' for x in xs)


def cta(t):
    if STORE_URL:
        return f'<a class="cta" href="{STORE_URL}">{t["cta"]}</a>\n<p class="note">{t["note"]}</p>'
    return f'<span class="cta soon">{t["cta_soon"]}</span>\n<p class="note">{t["note_soon"]}</p>'


def shell(lang, title, root, nav, body, footer, path, meta='', alternates=None):
    """One HTML page. `path` is the page's address relative to the site root;
    `alternates` maps a language to the same page in that language."""
    head = [f'<link rel="canonical" href="{BASE}{path}">']
    if meta:
        head.insert(0, f'<meta name="description" content="{html.escape(meta, quote=True)}">')
    for alt_lang, alt_path in (alternates or {}).items():
        head.append(f'<link rel="alternate" hreflang="{alt_lang}" href="{BASE}{alt_path}">')
    extra = '\n'.join(head)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title, quote=False)}</title>
{extra}
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


def local(slug, lang):
    """A guide's address as seen from a page of the same language."""
    return slug[len(SITE[lang]['path']):]


def landing(t):
    nav = (f'<a href="privacy.html">{t["privacy"]}</a>'
           f'<a href="{t["other_href"]}" lang="{t["other_lang"]}">{t["other"]}</a>')
    guide_links = items(f'<a href="{local(g["slug"], t["lang"])}">{g["h1"]}</a>'
                        for g in GUIDES if g['lang'] == t['lang'])
    body = f'''<main>
<h1>{t["h1"]}</h1>
<p class="lead">{t["lead"]}</p>
{cta(t)}

<h2>{t["what"]}</h2>
<div class="cols">
  <div class="box gone"><h3>{t["gone"]}</h3><ul>{items(t["gone_items"])}</ul></div>
  <div class="box stay"><h3>{t["stay"]}</h3><ul>{items(t["stay_items"])}</ul></div>
</div>

<h2>{t["how"]}</h2>
<ul class="plain">{items(t["how_items"])}</ul>

<h2>{t["priv_h"]}</h2>
<p>{t["priv_p"]}</p>

<h2>{t["guides_h"]}</h2>
<ul class="plain guides">{guide_links}</ul>
</main>'''
    alternates = {'en': EN['path'], 'ru': RU['path']}
    return shell(t['lang'], t['title'], t['root'], nav, body, t['footer'], t['path'], t['meta'], alternates)


def block(kind, content):
    if kind == 'h2':
        return f'<h2>{content}</h2>'
    if kind == 'p':
        return f'<p>{content}</p>'
    if kind == 'note':
        return f'<p class="callout">{content}</p>'
    if kind in ('ol', 'ul'):
        return f'<{kind} class="plain">{items(content)}</{kind}>'
    raise ValueError(f'unknown block {kind}')


def guide(g):
    t = SITE[g['lang']]
    nav = f'<a href="./">{t["home"]}</a>'
    alternates = None
    if g['pair']:
        other = SITE[t['other_lang']]
        href = t['other_href'] + local(g['pair'], other['lang'])
        nav += f'<a href="{href}" lang="{other["lang"]}">{t["other"]}</a>'
        alternates = {g['lang']: g['slug'], other['lang']: g['pair']}
    parts = '\n'.join(block(kind, content) for kind, content in g['body'])
    body = f'''<article class="guide">
<h1>{g["h1"]}</h1>
<p class="updated">{UPDATED[g["lang"]]}</p>
<p class="lead">{g["lead"]}</p>
{parts}
<div class="getit">
<h2>{t["get"]}</h2>
{cta(t)}
</div>
</article>'''
    return shell(g['lang'], g['title'], t['root'], nav, body, t['footer'], g['slug'], g['meta'], alternates)


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
    for chunk in re.split(r'\n\s*\n', text.strip()):
        lines = chunk.split('\n')
        if lines[0].startswith('# '):
            out.append(f'<h1>{inline(lines[0][2:])}</h1>')
        elif lines[0].startswith('## '):
            out.append(f'<h2>{inline(lines[0][3:])}</h2>')
        elif lines[0].startswith('- '):
            lis = [inline(join(i[2:].split('\n'))) for i in re.split(r'\n(?=- )', chunk)]
            out.append('<ul class="plain">' + items(lis) + '</ul>')
        else:
            out.append(f'<p>{inline(join(lines))}</p>')
    return '\n'.join(out)


def privacy_pages(source):
    text = source.read_text(encoding='utf-8')
    text = re.sub(r'https://github\.com/ismoilovmk/-?smart-block/issues', ISSUES, text)
    en_md, ru_md = text.split('\n---\n')
    alternates = {'en': 'privacy.html', 'ru': 'ru/privacy.html'}
    en_nav = '<a href="./">Home</a><a href="ru/privacy.html" lang="ru">Русский</a>'
    ru_nav = '<a href="./">Главная</a><a href="../privacy.html" lang="en">English</a>'
    en = shell('en', 'Privacy Policy — Smart Block', '', en_nav, f'<article>\n{markdown(en_md)}\n</article>',
               'Smart Block', 'privacy.html', alternates=alternates)
    ru = shell('ru', 'Политика конфиденциальности — Smart Block', '../', ru_nav,
               f'<article>\n{markdown(ru_md)}\n</article>', 'Smart Block', 'ru/privacy.html', alternates=alternates)
    return en, ru


def sitemap(paths):
    urls = '\n'.join(f'  <url><loc>{BASE}{p}</loc></url>' for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(exist_ok=True)
    target.write_text(text, encoding='utf-8')


def main():
    copy = ROOT / 'privacy.md'
    if len(sys.argv) > 1:
        shutil.copyfile(sys.argv[1], copy)
    pages = {'index.html': landing(EN), 'ru/index.html': landing(RU)}
    pages['privacy.html'], pages['ru/privacy.html'] = privacy_pages(copy)
    for g in GUIDES:
        pages[g['slug']] = guide(g)
    for path, text in pages.items():
        write(path, text)
    addresses = ['' if p == 'index.html' else p.replace('index.html', '') for p in pages]
    write('sitemap.xml', sitemap(addresses))
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
    print(f'built {len(pages)} pages, sitemap.xml, robots.txt')


if __name__ == '__main__':
    main()
