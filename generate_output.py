import json
import csv

# JSON formatında çıktı oluşturma
def generate_json_output(certificates):
    with open('certificates.json', 'w') as f:
        json.dump(certificates, f, indent=4)

# CSV formatında çıktı oluşturma
def generate_csv_output(certificates):
    with open('certificates.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Certificate Name', 'Expiration Date'])
        for cert in certificates:
            writer.writerow([cert['name'], cert['expiration']])

# Ana çalıştırma fonksiyonu
def main():
    # Örnek sertifika verisi
    certificates = [
        {'name': 'cert1', 'expiration': '2025-01-01'},
        {'name': 'cert2', 'expiration': '2023-06-15'},
        {'name': 'cert3', 'expiration': '2024-09-30'}
    ]

    generate_json_output(certificates)
    generate_csv_output(certificates)

if __name__ == "__main__":
    main()
