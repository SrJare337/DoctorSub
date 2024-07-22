#FERRAMENTA CONSTRUIDA PELO SRJARE337
import socket
import sys
import time
from colorama import Fore, Style, init, Back

init(autoreset=True)

common_subdomains = ['www', 'mail', 'ftp', 'admin', 'blog', 'support', 'help', 'shop', 'secure', 'test', 
    'dev', 'stage', 'cms', 'news', 'portal', 'app', 'api', 'files', 'images', 'store', 
    'account', 'billing', 'docs', 'login', 'register', 'dashboard', 'panel', 'management', 
    'data', 'resources', 'static', 'private', 'public', 'demo', 'webmail', 'media', 'content', 
    'backup', 'devops', 'sandbox', 'stats', 'tools', 'status', 'forum', 'chat', 'user', 
    'profile', 'signup', 'signin', 'my', 'pay', 'event', 'projects', 'services', 'system', 
    'jobs', 'hr', 'sales', 'contact', 'info', 'marketing', 'newsletter', 'offers', 'updates', 
    'partners', 'research', 'tutorials', 'learning', 'ecommerce', 'gateway', 'social', 'video', 
    'audio', 'conference', 'review', 'testimonials', 'careers', 'inbox', 'calendar', 'settings', 
    'archive', 'tickets', 'client', 'server', 'manage', 'checkout', 'payments', 'order', 
    'helpdesk', 'authentication', 'alert', 'push', 'qa', 'preview', 'monitor', 'control', 
    'custom', 'website', 'vps', 'b2b', 'b2c', 'health', 'records', 'learn', 'guide', 'assets', 
    'maps', 'survey', 'training', 'university', 'cloud', 'invoice', 'platform', 'customer', 
    'care', 'global', 'example', 'root', 'code', 'cache', 'discovery', 'worker', 'page', 
    'new', 'alias', 'privacy', 'partner', 'recruitment', 'promotions', 'verification', 'report', 
    'events', 'configuration', 'feedback', 'finance', 'education', 'subscriptions', 'link', 
    'apply', 'manager', 'meeting', 'restore', 'repository', 'beta', 'manual', 'knowledge', 
    'premium', 'access', 'search', 'purchase', 'products', 'payment', 'stream', 'cdn', 'wiki', 
    'guest', 'network', 'production', 'github', 'public', 'secured', 'consulting', 'site', 
    'exam', 'project', 'message', 'center', 'distribute', 'academy', 'system', 'workspace', 
    'support', 'console', 'details', 'users', 'office', 'documents', 'requests', 'management', 
    'backup', 'project', 'customer', 'details', 'site', 'reports', 'management', 'development', 
    'config', 'report', 'application', 'admin', 'ecommerce', 'log', 'test', 'service', 'tool', 
    'online', 'portal', 'app', 'service', 'website', 'partner', 'search', 'update', 'info', 
    'review', 'beta', 'manage', 'store', 'secure', 'knowledge', 'session', 'query', 'integration', 
    'manual', 'review', 'info', 'subscribe', 'dashboard', 'premium', 'track', 'feedback', 
    'support', 'data', 'update', 'files', 'track', 'user', 'reports', 'platform', 'online', 
    'consult', 'academy', 'services', 'tracking', 'server', 'portal', 'vps', 'checkout', 
    'update', 'order', 'notify', 'resource', 'server', 'client', 'forum', 'static', 'support', 
    'partner', 'log', 'training', 'files', 'checkout', 'guest', 'platform', 'enterprise', 
    'analytics', 'service', 'data', 'subscription', 'api', 'products', 'search', 'application', 
    'knowledge', 'docs', 'update', 'forum', 'access', 'services', 'projects', 'resource', 
    'manage', 'api', 'notifications', 'tracking', 'review', 'customer', 'settings', 'static', 
    'checkout', 'partner', 'workspace', 'service', 'track', 'site', 'public', 'log', 'knowledge', 
    'notifications', 'user', 'apply', 'academy', 'feedback', 'partner', 'client', 'review', 
    'resource', 'order', 'support', 'portal', 'site', 'details', 'feedback', 'public', 'customer', 
    'projects', 'service', 'review', 'cloud', 'mail', 'forum', 'manage', 'portal', 'store', 
    'platform', 'review', 'feedback', 'tracking', 'api', 'education', 'manage', 'data', 
    'platform', 'support', 'details', 'partner', 'tools', 'forum', 'docs', 'resources', 
    'store', 'subscription', 'consulting', 'product', 'archive', 'review', 'test', 'server', 
    'notifications', 'tracking', 'portal', 'review', 'update', 'system', 'content', 'management', 
    'user', 'support', 'details', 'tracking', 'review', 'data', 'tracking', 'cloud', 
    'platform', 'feedback', 'update', 'service', 'forum', 'public', 'online', 'tracking', 
    'academy', 'order', 'client', 'tracking', 'support', 'feedback', 'store', 'tools', 
    'site', 'archive', 'management', 'tools', 'vps', 'platform', 'service', 'cloud', 'checkout', 
    'public', 'user', 'track', 'update', 'data', 'tools', 'archive', 'support', 'tracking', 
    'service', 'partner', 'site', 'consulting', 'feedback', 'review', 'resources', 'tracking', 
    'service', 'forum', 'data', 'tracking', 'site', 'review', 'partner', 'tools', 'tracking', 
    'public', 'client', 'tools', 'forum', 'manage', 'online', 'service', 'track', 'user', 
    'feedback', 'update', 'tracking', 'academy', 'review', 'resource', 'knowledge', 'public', 
    'service', 'archive', 'feedback', 'project', 'client', 'store', 'tracking', 'update', 
    'platform', 'service', 'tools', 'knowledge', 'update', 'service', 'client', 'archive', 
    'review', 'tools', 'data', 'client', 'service', 'public', 'update', 'tracking', 'feedback', 
    'tracking', 'tracking', 'client', 'knowledge', 'service', 'partner', 'update', 'tracking', 
    'consulting', 'review', 'forum', 'knowledge', 'public', 'tools', 'service', 'cloud', 
    'public', 'feedback', 'tools', 'knowledge', 'feedback', 'store', 'client', 'tracking', 
    'data', 'tracking', 'service', 'forum', 'client', 'feedback', 'data', 'public', 'client', 
    'service', 'tracking', 'knowledge', 'consulting', 'tracking', 'feedback', 'public', 
    'data', 'tracking', 'forum', 'client', 'archive', 'tracking', 'feedback', 'tracking', 
    'store', 'review', 'client', 'tracking', 'tracking', 'feedback', 'client', 'service', 
    'knowledge', 'service', 'forum', 'update', 'data', 'tracking', 'tracking', 'feedback', 
    'archive', 'client', 'service', 'store', 'tracking', 'feedback', 'public', 'service', 
    'feedback', 'tools', 'client', 'tracking', 'service', 'tracking', 'feedback', 'store', 
    'archive', 'client', 'service', 'knowledge', 'public', 'feedback', 'tracking', 'update', 
    'tracking', 'tools', 'store', 'feedback', 'tracking', 'knowledge', 'service', 'tracking', 
    'public', 'feedback', 'client', 'service', 'update', 'tracking', 'forum', 'tools', 
    'feedback', 'store', 'archive', 'knowledge', 'tracking', 'client', 'service', 'forum', 
    'public', 'feedback', 'tracking', 'tools', 'client', 'service', 'knowledge', 'archive', 
    'service', 'tracking', 'feedback', 'public', 'store', 'tracking', 'knowledge', 'client', 
    'service', 'update', 'archive', 'feedback', 'tracking', 'public', 'tools', 'client', 
    'service', 'forum', 'feedback', 'archive', 'tracking', 'knowledge', 'store', 'public', 
    'update', 'client', 'service', 'feedback', 'tracking', 'forum', 'tools', 'archive', 
    'public', 'tracking', 'store', 'feedback', 'knowledge', 'service', 'update', 'client', 
    'forum', 'tracking', 'store', 'public', 'feedback',]


def styled_print(text, color=Fore.GREEN, delay=0.01, bold=False):
    style = color
    if bold:
        style += Style.BRIGHT

    sys.stdout.write(style)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def loading_animation():
    animation_frames = ['|', '/', '-', '\\']
    for _ in range(10):
        for frame in animation_frames:
            sys.stdout.write(f"\r{Fore.YELLOW}Carregando enumeração {frame}")
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write(f"\r{Fore.GREEN}Carregamento Completo! \n")
    print(Style.RESET_ALL)

def check_subdomain(domain, subdomain):
    try:
        full_domain = f"{subdomain}.{domain}"
        ip = socket.gethostbyname(full_domain)
        return ip
    except socket.error:
        return None

def enumerate_subdomains(domain):
    active_subdomains = []
    start_time = time.time()

    styled_print(f'\nIniciando a enumeração de subdomínios para {domain}...', Fore.LIGHTYELLOW_EX, bold=True)
    loading_animation()

    for subdomain in common_subdomains:
        ip = check_subdomain(domain, subdomain)
        if ip:
            active_subdomains.append((subdomain, ip))

    end_time = time.time()
    duration = end_time - start_time

    styled_print(f'\nSubdomínios ativos para {domain}:', Fore.LIGHTGREEN_EX, bold=True)
    for index, (subdomain, ip) in enumerate(active_subdomains, start=1):
        styled_print(f'{index}. {subdomain}.{domain} - {ip}', Fore.LIGHTGREEN_EX, delay=0.02, bold=True)

    styled_print(f'\nDuração da enumeração: {duration:.2f} segundos', Fore.CYAN, bold=True)

def print_credits():
    styled_print('\nFerramenta desenvolvida por SrJare337', Fore.RED, bold=True)
    styled_print('Versão: V1.1', Fore.RED, bold=True)

def print_intro():
    border_length = 60
    title = "🔥HACKER SUBDOMAIN ENUMERATOR🔥"
    credits = "Ferramenta desenvolvida por SrJare337"
    padding_title = (border_length - len(title) - 4) // 2
    padding_credits = (border_length - len(credits) - 4) // 2
    border = "=" * border_length
    middle_line_title = f" {' ' * padding_title}{title} {' ' * padding_title} "
    middle_line_credits = f" {' ' * padding_credits}{credits} {' ' * padding_credits} "

    print(Back.BLACK + Fore.GREEN + border)
    styled_print(middle_line_title, Fore.LIGHTCYAN_EX, bold=True)
    styled_print(middle_line_credits, Fore.LIGHTCYAN_EX, bold=True)
    print(Fore.GREEN + border)

if __name__ == "__main__":
    print_intro()
    domain = input(Fore.CYAN + "Digite o domínio para verificar (exemplo.com): " + Style.RESET_ALL).strip()

    enumerate_subdomains(domain)
    print_credits()
