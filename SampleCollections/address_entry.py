full_name = ({
    "first name": 'Abbey',
    "last name": 'Jude'
})

address = "123 Penny Lane" 
city = "Liverpool"
state = "Meresyside"
zip_code = "L"

honorific = {"honorific": "Mrs."}
full_name.update(honorific)

mailing_address = f"""
    {full_name['honorific']} {full_name['first name']} {full_name['last name']}
    {address}
    {city}, {state} {zip_code}"""

print(mailing_address)