subject_dict = {}
with open("subjects.txt", "r", encoding="utf-8") as f:
    for line in f:

        subject, lectures, practicals, labs = line.strip().split(",")
        total_classes = sum(int(x) if x else 0 for x in [lectures, practicals, labs])
        total_classes = 0
        if lectures.strip():
            total_classes += int(lectures)
        if practicals.strip():
            total_classes += int(practicals)
        if labs.strip():
            total_classes += int(labs)
        subject_dict[subject] = total_classes
print(subject_dict)

# Этот код не работает, если для какого-нибудь вида ничего нет (то есть вообще никакая цифра не указана).
# Если стоит 0 - работает.