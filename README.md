# DevSetup
# LangInstaller 🚀  All-in-one installer for dev environment: programming languages, IDEs and code editors. Python, VS Code, Android Studio, Node.js, Postman and more.
from urllib.request import urlretrieve
import os
import flet as ft
#Это место временого хранения ссылок
#https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe
#https://cache.ruby-lang.org/pub/ruby/3.4/ruby-3.4.6.tar.gz
#https://cran.r-project.org/src/base/R-4
#https://cran.r-project.org/src/base/R-4/R-4.5.1.tar.xz
#https://www.cpan.org/src/5.0/perl-5.42.0.tar.gz


# Создаём папку SR_Downloads на рабочем столе
download_folder = os.path.join(os.path.expanduser("~"), "Desktop", "SR_Downloads")
os.makedirs(download_folder, exist_ok=True)  # Создаём папку, если её нет

# Скачиваем прямо в эту папку
file_path = os.path.join(download_folder, "python.zip")

#Programming_language

def install_python(): 
    file_path = os.path.join(download_folder, "python.zip")
    urlretrieve("https://www.python.org/ftp/python/3.13.7/python-3.13.7-embed-amd64.zip",file_path)

def install_cpp():
    file_path = os.path.join(download_folder, "cpp.exe")
    urlretrieve("https://aka.ms/vs/17/release/vc_redist.x86.exe",file_path)

def install_js():
    file_path = os.path.join(download_folder, "JS.msi")
    urlretrieve("https://nodejs.org/dist/v22.20.0/node-v22.20.0-x64.msi",file_path)

def install_java():
    file_path = os.path.join(download_folder, "Java.exe")
    urlretrieve("https://javadl.oracle.com/webapps/download/AutoDL?BundleId=252322_68ce765258164726922591683c51982c",file_path)

def install_cs():
    file_path = os.path.join(download_folder, "CS.exe")
    urlretrieve("https://builds.dotnet.microsoft.com/dotnet/Sdk/9.0.305/dotnet-sdk-9.0.305-win-x64.exe",file_path)

def install_go():
    file_path = os.path.join(download_folder, "Go.msi")
    urlretrieve("https://go.dev/dl/go1.25.1.windows-amd64.msi",file_path)

def install_rust():
    file_path = os.path.join(download_folder, "rust.exe")
    urlretrieve("https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe",file_path)

def install_php():
    file_path = os.path.join(download_folder, "PHP.zip")
    urlretrieve("https://downloads.php.net/~windows/releases/archives/php-8.4.13-src.zip",file_path)

def install_ruby():
    file_path = os.path.join(download_folder, "Ruby.tar.gz")
    urlretrieve("https://cache.ruby-lang.org/pub/ruby/3.4/ruby-3.4.6.tar.gz",file_path)

def install_swift():
    file_path = os.path.join(download_folder, "Swift.exe")
    urlretrieve("https://download.swift.org/swift-6.2-release/windows10/swift-6.2-RELEASE/swift-6.2-RELEASE-windows10.exe",file_path)

def install_sql():
    file_path = os.path.join(download_folder, "SQL.zip")
    urlretrieve("https://www.oracle.com/webapps/redirect/signon?nexturl=https://download.oracle.com/otn/mysql/ee/mysql-enterprise-9.4.0_winx64_bundle.zip",file_path)

def install_perl():
    file_path = os.path.join(download_folder, "Perl.tar.gz")
    urlretrieve("https://www.cpan.org/src/5.0/perl-5.42.0.tar.gz",file_path)

def install_lua():
    file_path = os.path.join(download_folder, "Lua.tar.gz")
    urlretrieve("https://www.lua.org/ftp/lua-5.4.8.tar.gz",file_path)




#IDEшки тут
def install_android_studio():
    file_path = os.path.join(download_folder, "Android_Studio.exe")
    urlretrieve("https://redirector.gvt1.com/edgedl/android/studio/install/2025.1.3.7/android-studio-2025.1.3.7-windows.exe",file_path)

def install_vscode():
    file_path = os.path.join(download_folder, "VSCode.zip")
    urlretrieve("https://github.com/microsoft/vscode/archive/refs/heads/main.zip",file_path)

def install_postman():
    file_path = os.path.join(download_folder, "Postman.exe")
    urlretrieve("https://dl.pstmn.io/download/latest/win64",file_path)

def install_jetbrains_toolbox():
    file_path = os.path.join(download_folder, "JetBrains_Toolbox.exe")
    urlretrieve("https://download.jetbrains.com/toolbox/jetbrains-toolbox-2.3.3.20970.exe", file_path)


#Редакторы кода
def install_notepadpp():
    file_path = os.path.join(download_folder, "Notepadpp.zip")
    urlretrieve("https://github.com/notepad-plus-plus/notepad-plus-plus/archive/refs/heads/master.zip",file_path)

def install_sublime_text():
    file_path = os.path.join(download_folder, "SublimeText.exe")
    urlretrieve("https://download.sublimetext.com/sublime_text_build_4184_x64_setup.exe", file_path)

def install_atom():
    file_path = os.path.join(download_folder, "Atom.exe")
    urlretrieve("https://github.com/atom/atom/releases/download/v1.63.1/AtomSetup-x64.exe", file_path)
