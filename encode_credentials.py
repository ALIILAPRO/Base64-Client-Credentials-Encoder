import base64

def get_encoded_credentials():
	while True:
		try:
			# Prompt the user to enter their client ID and secret
			client_id = input("Enter your client ID: ").strip()
			if not client_id:
				raise ValueError("Client ID cannot be empty.")

			client_secret = input("Enter your client secret: ").strip()
			if not client_secret:
				raise ValueError("Client secret cannot be empty.")

			# Concatenate the client ID and secret with a colon separator
			credentials = f"{client_id}:{client_secret}"

			# Encode as ASCII and then Base64
			encoded_credentials = base64.b64encode(credentials.encode("ascii")).decode("ascii")

			return encoded_credentials
		except ValueError as ve:
			print(f"Invalid input: {ve}\nPlease try again.\n")
		except Exception as e:
			print(f"Error: {e}\nPlease try again.\n")

# Call the function to get the encoded credentials
encoded_credentials = get_encoded_credentials()

print(f"The encoded credentials are: {encoded_credentials}")
