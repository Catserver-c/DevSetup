from urllib.request import urlretrieve
import os
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
    file_path = os.path.join(download_folder, "Lua.tsr.gz")
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

#Something (Я не знаю)
def install_git():
    file_path = os.path.join(download_folder, "git.exe")
    urlretrieve("https://github.com/git-for-windows/git/releases/download/v2.51.0.windows.2/Git-2.51.0.2-64-bit.exe",file_path)

install_postman()


