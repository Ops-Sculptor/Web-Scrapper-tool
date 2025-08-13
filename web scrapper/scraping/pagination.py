from urllib.parse import urljoin

def find_pagination_links(soup, base_url):
    links = []
    selectors = ['.pagination a[href]', 'a[rel="next"]']
    for selector in selectors:
        for link in soup.select(selector):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href)
                if full_url not in links:
                    links.append(full_url)
    return links
