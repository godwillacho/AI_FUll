from google import genai

client = genai.Client(
    api_key = 'AIzaSyABO2mgElYUv1Ytd6O4BneOZCtoNsHCSkk'
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)