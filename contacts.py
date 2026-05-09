contacts = [{"name": "Gabriel", "phone": "123-456-7890"},
            {"name": "Michael", "phone": "987-654-3210"},
            {"name": "jake", "phone": "555-555-5555"}
            ]
for x in range(0,3):
    print(f"{x+1}. {contacts[x]['name']} - {contacts[x]['phone']}")
