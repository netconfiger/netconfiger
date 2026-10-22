#!/usr/bin/env python3
"""NetConfiger GitHub Pages static acceptance checks (offline, stdlib only)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import sys

ROOT=Path(__file__).resolve().parents[1]
NEEDED={"index.html","en.html","zh.html","assets/site.css","assets/site.js","README.md","DEPLOY.md",".nojekyll"}

class Page(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True);self.lang=None;self.links=[];self.ids=[];self.meta={};self.scripts=[];self.imgs=[];self.buttons=[];self.tags=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);self.tags.append(tag)
        if tag=="html":self.lang=a.get("lang")
        if tag in ("a","link"):self.links.append(a.get("href",""))
        if tag=="script":self.scripts.append(a.get("src",""))
        if tag=="img":self.imgs.append(a.get("src",""))
        if tag=="button":self.buttons.append(a)
        if a.get("id"):self.ids.append(a["id"])
        if tag=="meta" and a.get("name"):self.meta[a["name"]]=a.get("content")

def fail(m):raise AssertionError(m)

def local_exists(page,url):
    p=urlsplit(url)
    if p.scheme or p.netloc or url.startswith("//") or url.startswith("mailto:"):return
    if not p.path:
        if p.fragment and p.fragment not in page.ids:fail(f"{page.path.name}: missing #{p.fragment}")
        return
    target=(page.path.parent/p.path).resolve()
    if not target.is_relative_to(ROOT.resolve()):fail(f"external local file traversal: {url}")
    if not target.is_file():fail(f"{page.path.name}: missing {url}")

try:
    for r in NEEDED:
        if not (ROOT/r).is_file():fail(f"missing file: {r}")
    for file,lang,toggle in [('index.html','zh-CN','en.html'),('en.html','en','index.html')]:
        src=ROOT/file;html=src.read_text(encoding='utf-8');page=Page();page.path=src;page.feed(html)
        if page.lang!=lang:fail(f"{file} language should be {lang}")
        if page.meta.get('nc-build')!='gh-pages-v6-20261022':fail(f"{file} missing build marker")
        if toggle not in ''.join(page.links):fail(f"{file} missing language toggle")
        if './assets/site.css' not in page.links or './assets/site.js' not in page.scripts:fail(f"{file} missing shared resources")
        if not any('data-menu-button' in b for b in page.buttons):fail(f"{file} missing mobile menu")
        if 'main' not in page.ids or 'how' not in page.ids:fail(f"{file} missing main sections")
        if page.tags.count('h1')!=1:fail(f"{file} must have one h1")
        for u in page.links+page.scripts+page.imgs:local_exists(page,u)
        for fragment in ('#main','#how'):
            if fragment not in page.links:fail(f"{file} missing {fragment}")
    if 'url=./index.html' not in (ROOT/'zh.html').read_text(encoding='utf-8'):fail('legacy redirect missing')
    if 'https://netconfiger.com/zh/download' not in (ROOT/'index.html').read_text(encoding='utf-8'):fail('CN download link missing')
    if 'https://netconfiger.com/download' not in (ROOT/'en.html').read_text(encoding='utf-8'):fail('EN download link missing')
    print('PASS: V6 CN/EN HTML, paths, anchors, JS/CSS, mobile menu, legacy URL, download destinations')
except Exception as exc:
    print('FAIL:',exc,file=sys.stderr);sys.exit(1)
