from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# ANSI escape codes untuk warna
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def print_colored(text, color):
    print(f"{color}{text}{Color.RESET}")

def spam_report(phone_number, message="This number is spamming"):
    print_colored(f"Memulai proses pelaporan untuk nomor: {phone_number}", Color.CYAN)

    try:
        # Inisialisasi WebDriver
        driver = webdriver.Chrome()
        print_colored("WebDriver berhasil diinisialisasi...", Color.GREEN)

        # Buka WhatsApp Web
        driver.get("https://web.whatsapp.com/")
        print_colored("Membuka WhatsApp Web. Harap scan QR Code...", Color.YELLOW)
        time.sleep(15)  # Beri waktu untuk scan QR code

        # Cari kontak
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(phone_number)
        time.sleep(2)

        # Pilih kontak
        try:
            contact = driver.find_element(By.XPATH, f'//span[@title="{phone_number}"]')
            contact.click()
            time.sleep(2)
        except Exception as e:
            print_colored(f"Kontak {phone_number} tidak ditemukan.", Color.RED)
            driver.quit()
            return

        # Buka menu opsi (tiga titik vertikal)
        options_menu = driver.find_element(By.XPATH, '//div[@title="Opsi lainnya"]')
        options_menu.click()
        time.sleep(1)

        # Pilih "Laporkan"
        report_button = driver.find_element(By.XPATH, '//div[text()="Laporkan"]')
        report_button.click()
        time.sleep(1)

        # Centang blokir dan kirim laporan
        block_checkbox = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
        block_checkbox.click()
        time.sleep(1)

        send_report_button = driver.find_element(By.XPATH, '//div[@aria-label="Laporkan"]')
        send_report_button.click()
        time.sleep(5)

        print_colored(f"Berhasil melaporkan {phone_number}!", Color.GREEN)

    except Exception as e:
        print_colored(f"Gagal melaporkan {phone_number}: {e}", Color.RED)

    finally:
        driver.quit()
        print_colored("WebDriver ditutup.", Color.CYAN)

# Ambil nomor telepon dari argumen command line
if len(sys.argv) > 1:
    phone_number = sys.argv[1]
    spam_report(phone_number)
else:
    print_colored("Usage: python spam_report.py <nomor_telepon>", Color.YELLOW)
    print_colored("Contoh: python spam_report.py +6281234567890", Color.YELLOW)