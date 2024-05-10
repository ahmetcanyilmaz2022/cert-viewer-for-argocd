import subprocess
import json

# Komut çıktısını almak için kullanılan fonksiyon
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Kubernetes sertifikalarını çekme işlemi
def get_certificates():
    command = "kubectl get certificates --all-namespaces -o json"
    certificates = run_command(command)
    return json.loads(certificates)

# Ana çalıştırma fonksiyonu
def main():
    certificates = get_certificates()
    for cert in certificates['items']:
        cert_name = cert['metadata']['name']
        expiration_date = cert['spec']['expiration']
        print(f"Certificate Name: {cert_name}, Expiration Date: {expiration_date}")

if __name__ == "__main__":
    main()
