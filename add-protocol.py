def process_ips(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            ips = file.readlines()

        with open(output_file, 'w') as file:
            for ip in ips:
                ip = ip.strip()
                file.write(f"socks5://{ip}\n")
                file.write(f"http://{ip}\n")
                file.write(f"https://{ip}\n")

    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage example
process_ips('ips.txt', 'new-ips.txt')
