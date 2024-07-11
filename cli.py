import argparse
import subprocess


def encrypt_file(input_file, output_file, recipient):
    try:
        subprocess.run(['gpg', '--output', output_file, '--encrypt', '--recipient', recipient, input_file], check=True)
        print(f"File '{input_file}' successfully encrypted to '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Error encrypting file: {e}")


def main():
    parser = argparse.ArgumentParser(description="Encrypt files using GPG Encryptor")
    parser.add_argument('input_file', help='The file to encrypt')
    parser.add_argument('output_file', help='The output encrypted file')
    parser.add_argument('email', help='The email containing the key')
    args = parser.parse_args()
    encrypt_file(args.input_file, args.output_file, args.recipient)


if __name__ == "__main__":
    main()
