import requests
import whois
import shodan
import os

# Load environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')

def github_recon():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    repos = requests.get('https://api.github.com/orgs/fuel-labs/repos', headers=headers).json()
    for repo in repos:
        print(f"Repository: {repo['name']} - {repo['html_url']}")

def whois_recon(domain):
    w = whois.whois(domain)
    print(f"WHOIS for {domain}:")
    print(w)

def shodan_recon(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    result = api.host(ip)
    print(f"Shodan information for IP {ip}:")
    print(result)

if __name__ == "__main__":
    github_recon()
    whois_recon("fuel.network")
    shodan_recon("8.8.8.8")
