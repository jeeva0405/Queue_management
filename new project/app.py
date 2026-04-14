from model import predict_waiting_time

patients = int(input("Enter patients ahead: "))
avg_time = int(input("Enter avg time per patient: "))

waiting_time = predict_waiting_time(patients, avg_time)

print(f"Estimated waiting time: {waiting_time} minutes")

if waiting_time <= 30:
    print("Best time to visit ✅")
elif waiting_time <= 60:
    print("Moderate waiting time ⚠️")
else:
    print("Try another slot ❌")
