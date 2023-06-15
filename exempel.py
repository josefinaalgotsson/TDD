from datetime import datetime

string_input_with_date = None

past = datetime.strptime(string_input_with_date, "%Y-%m-%d")

present = datetime.now()
print(type(present))

print(past.date() < present.date())