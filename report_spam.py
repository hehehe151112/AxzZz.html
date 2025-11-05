from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def spam_report(phone_number, message="This number is spamming"):
    try:
        # Inisialisasi WebDriver (pastikan chromedriver sudah terinstall)
        driver = webdriver.Chrome()

        # Buka WhatsApp Web
        driver.get("https://web.whatsapp.com/")
        print("Scan QR Code...")
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
            print(f"Kontak {phone_number} tidak ditemukan: {e}")
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

        print(f"Berhasil melaporkan {phone_number}")

    except Exception as e:
        print(f"Gagal melaporkan {phone_number}: {e}")

    finally:
        driver.quit()

# Daftar nomor yang akan dilaporkan
phone_numbers = ["+6281234567890", "+6289876543210"]  # Ganti dengan nomor target

# Looping untuk melaporkan setiap nomor
for number in phone_numbers:
    spam_report(number)
