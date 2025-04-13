import streamlit as st
import requests

def country_name(country):
	url = f"https://restcountries.com/v3.1/name/{country}"
	response = requests.get(url)

	if response.status_code == 200:
		data = response.json()
		country_data = data[0]
		name = country_data["name"]["country"]
		captial = country_data["capital"][0]
		population = country_data["population"]
		area = country_data["area"]
		currency = country_data["currencies"]
		region = country_data["region"]
		return name , captial , population , area , currency ,region
	else:
		return None

def main():
	st.title("country information")
	countrys_name = input("country_name")
	if countrys_name:
		country_info = country_name(countrys_name)
		if country_info:
			name, capital , population , area ,currency , region = country_info
			st.subheader("country info")
			st.write(f"country name{name}")
			st.write(f"captial{captial}")
			st.write(f"captial{population}")
			st.write(f"captial{area}")
			st.write(f"captial{currency}")
			st.write(f"captial{region}")
		else:
			st.write("not found")

if __name__ == "__main__":
	main()
			
			
