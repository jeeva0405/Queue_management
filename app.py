from model import predict_waiting_time

patients = int(input("Enter patients ahead: "))
avg_time = int(input("Enter avg time: "))

waiting_time = predict_waiting_time(patients, avg_time)

print(f"Estimated waiting time: {waiting_time} minutes")

if waiting_time < 20:
    print("Best time to visit ✅")
else:
    print("Try another slot ❌")