import json

profile = {
    "name": "Vasu G N",
    "city": "Bangalore",
    "skills": ["Python", "Node.js", "FastAPI"]
}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

with open("profile.json", "r") as file:
    data = json.load(file)

print("Second skill:", data["skills"][1])

data["course"] = "Agentic AI"

with open("profile.json", "w") as file:
    json.dump(data, file, indent=4)

print("Final Dictionary:")
print(data)