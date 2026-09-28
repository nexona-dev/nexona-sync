import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# --- Shopify API Ayarları ---
SHOPIFY_STORE_URL = "https://your-store.myshopify.com"
SHOPIFY_API_KEY = "YOUR_SHOPIFY_API_KEY"
SHOPIFY_PASSWORD = "YOUR_SHOPIFY_PASSWORD"

# --- Google Sheets Ayarları ---
SHEET_NAME = "Shopify Product Sync"
CREDENTIALS_FILE = "google_credentials.json"

def get_shopify_products():
    """Shopify'dan tüm ürünleri çeker."""
    url = f"{SHOPIFY_STORE_URL}/admin/api/2024-01/products.json"
    response = requests.get(url, auth=(SHOPIFY_API_KEY, SHOPIFY_PASSWORD))
    if response.status_code == 200:
        return response.json().get("products", [])
    else:
        print(f"Shopify hatası: {response.status_code}")
        return []

def sync_to_google_sheets(products):
    """Ürünleri Google Sheets'e yazar."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1

    sheet.clear()
    sheet.append_row(["Product ID", "Title", "Price", "Stock", "Updated At"])

    for product in products:
        for variant in product.get("variants", []):
            sheet.append_row([
                product["id"],
                product["title"],
                variant.get("price", "N/A"),
                variant.get("inventory_quantity", "N/A"),
                time.strftime("%Y-%m-%d %H:%M:%S")
            ])
    print(f"{len(products)} ürün Google Sheets'e senkronize edildi.")

def main():
    print("Shopify ürün senkronizasyonu başladı...")
    products = get_shopify_products()
    if products:
        sync_to_google_sheets(products)
    else:
        print("Ürün bulunamadı veya API hatası.")

if __name__ == "__main__":
    main()
