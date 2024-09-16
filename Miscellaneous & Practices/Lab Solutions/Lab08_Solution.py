def check_distance(relations, first_person, second_person):
    if first_person == second_person:
        return 0
    elif first_person not in relations:
        raise ValueError("Tidak ada hubungan.")
    return 10 * (relations[first_person][1]) + check_distance(relations, relations[first_person][0], second_person)

inp = input("Masukkan data hubungan:\n")
relations = {}
while inp != "SELESAI":
    first_person, second_person, distance_raw = inp.strip().split(" ")
    distance = float(distance_raw)
    relations[first_person] = (second_person, distance)
    inp = input()
first_person = input("Masukkan nama awal: ").strip()
second_person = input("Masukkan nama tujuan: ").strip()

try:
    total_distance = int(check_distance(relations, first_person, second_person))
    print(f"Jarak total: {total_distance:d}")
    if distance <= 100:
        print(f"{first_person} dan {second_person} kenalan dekat.")
    elif distance <= 1000:
        print(f"{first_person} dan {second_person} mungkin saling kenal.")
    else:
        print(f"{first_person} dan {second_person} tidak saling kenal.")
except ValueError:
    print(f"Tidak ada hubungan antara {first_person} dan {second_person}.")
