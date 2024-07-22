#FERRAMENTA CONSTRUIDA PELO SRJARE337
import socket
import sys
import time
from colorama import Fore, Style, init, Back

init(autoreset=True)

common_subdomains = [
    'www', 'mail', 'ftp', 'ns1', 'ns2', 'test', 'admin', 'webmail', 'blog', 'shop',
    'dev', 'api', 'm', 'docs', 'support', 'customer', 'forum', 'news', 'static', 'cdn',
    'store', 'secure', 'backup', 'app', 'int', 'data', 'management', 'beta', 'portal', 'my',
    'cloud', 'server', 'wiki', 'mx', 'vpn', 'service', 'status', 'tools', 'app1', 'media',
    'image', 'files', 'downloads', 'local', 'auth', 'admin1', 'office', 'sms', 'info',
    'mail1', 'archive', 'projects', 'events', 'survey', 'forms', 'shop1', 'search', 'resources',
    'monitor', 'tickets', 'newsletter', 'pay', 'uploads', 'chat', 'live', 'clients', 'team',
    'about', 'feedback', 'welcome', 'register', 'contact', 'calendar', 'forum1', 'payment',
    'support1', 'sso', 'api1', 'login', 'identity', 'inbox', 'forum2', 'conference', 'admin2',
    'data1', 'gateway', 'preview', 'platform', 'management1', 'wiki1', 'admin3', 'service1',
    'products', 'sales', 'company', 'careers', 'partners', 'events1', 'customer1', 'update',
    'site', 'stats', 'billing', 'help', 'staff', 'dev1', 'email', 'security', 'service2', 'web',
    'web1', 'mail2', 'ftp1', 'ns3', 'ns4', 'test1', 'admin4', 'webmail2', 'blog1', 'shop2',
    'dev2', 'api2', 'm1', 'docs1', 'support2', 'customer2', 'forum3', 'news1', 'static1', 'cdn1',
    'store1', 'secure1', 'backup1', 'app2', 'int1', 'data2', 'management2', 'beta1', 'portal1', 'my1',
    'cloud1', 'server1', 'wiki2', 'mx1', 'vpn1', 'service3', 'status1', 'tools1', 'app3', 'media1',
    'image1', 'files1', 'downloads1', 'local1', 'auth1', 'admin5', 'office1', 'sms1', 'info1',
    'mail3', 'archive1', 'projects1', 'events2', 'survey1', 'forms1', 'shop3', 'search1', 'resources1',
    'monitor1', 'tickets1', 'newsletter1', 'pay1', 'uploads1', 'chat1', 'live1', 'clients1', 'team1',
    'about1', 'feedback1', 'welcome1', 'register1', 'contact1', 'calendar1', 'forum4', 'payment1',
    'support2', 'sso1', 'api3', 'login1', 'identity1', 'inbox1', 'forum5', 'conference1', 'admin6',
    'data3', 'gateway1', 'preview1', 'platform1', 'management3', 'wiki3', 'admin7', 'service4',
    'products1', 'sales1', 'company1', 'careers1', 'partners1', 'events3', 'customer2', 'update1',
    'site1', 'stats1', 'billing1', 'help1', 'staff1', 'dev2', 'email1', 'security1', 'service5', 'web2',
    'web2', 'mail4', 'ftp2', 'ns5', 'ns6', 'test2', 'admin8', 'webmail3', 'blog2', 'shop4',
    'dev3', 'api4', 'm2', 'docs2', 'support3', 'customer3', 'forum6', 'news2', 'static2', 'cdn2',
    'store2', 'secure2', 'backup2', 'app4', 'int2', 'data4', 'management4', 'beta2', 'portal2', 'my2',
    'cloud2', 'server2', 'wiki4', 'mx2', 'vpn2', 'service6', 'status2', 'tools2', 'app5', 'media2',
    'image2', 'files2', 'downloads2', 'local2', 'auth2', 'admin9', 'office2', 'sms2', 'info2',
    'mail5', 'archive2', 'projects2', 'events4', 'survey2', 'forms2', 'shop5', 'search2', 'resources2',
    'monitor2', 'tickets2', 'newsletter2', 'pay2', 'uploads2', 'chat2', 'live2', 'clients2', 'team2',
    'about2', 'feedback2', 'welcome2', 'register2', 'contact2', 'calendar2', 'forum7', 'payment2',
    'support3', 'sso2', 'api5', 'login2', 'identity2', 'inbox2', 'forum8', 'conference2', 'admin10',
    'data5', 'gateway2', 'preview2', 'platform2', 'management5', 'wiki5', 'admin11', 'service7',
    'products2', 'sales2', 'company2', 'careers2', 'partners2', 'events5', 'customer3', 'update2',
    'site2', 'stats2', 'billing2', 'help2', 'staff2', 'dev3', 'email2', 'security2', 'service8', 'web3',
    'web3', 'mail6', 'ftp3', 'ns7', 'ns8', 'test3', 'admin12', 'webmail4', 'blog3', 'shop6',
    'dev4', 'api6', 'm3', 'docs3', 'support4', 'customer4', 'forum9', 'news3', 'static3', 'cdn3',
    'store3', 'secure3', 'backup3', 'app6', 'int3', 'data6', 'management6', 'beta3', 'portal3', 'my3',
    'cloud3', 'server3', 'wiki6', 'mx3', 'vpn3', 'service9', 'status3', 'tools3', 'app7', 'media3',
    'image3', 'files3', 'downloads3', 'local3', 'auth3', 'admin13', 'office3', 'sms3', 'info3',
    'mail7', 'archive3', 'projects3', 'events6', 'survey3', 'forms3', 'shop7', 'search3', 'resources3',
    'monitor3', 'tickets3', 'newsletter3', 'pay3', 'uploads3', 'chat3', 'live3', 'clients3', 'team3',
    'about3', 'feedback3', 'welcome3', 'register3', 'contact3', 'calendar3', 'forum10', 'payment3',
    'support4', 'sso3', 'api7', 'login3', 'identity3', 'inbox3', 'forum11', 'conference3', 'admin14',
    'data7', 'gateway3', 'preview3', 'platform3', 'management7', 'wiki7', 'admin15', 'service10',
    'products3', 'sales3', 'company3', 'careers3', 'partners3', 'events7', 'customer4', 'update3',
    'site3', 'stats3', 'billing3', 'help3', 'staff3', 'dev4', 'email3', 'security3', 'service11', 'web4'
]


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
