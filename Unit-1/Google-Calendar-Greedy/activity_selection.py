def activity_selection(activities):
    activities.sort(key=lambda x: x[2])

    selected = []
    last_finish = 0

    for activity in activities:
        name, start, finish = activity

        if start >= last_finish:
            selected.append(activity)
            last_finish = finish

    return selected


activities = [
    ("A", 9, 10),
    ("B", 9.5, 11),
    ("C", 10, 11.5),
    ("D", 11, 12),
    ("E", 11.5, 12.5),
    ("F", 12, 13)
]

selected = activity_selection(activities)

print("Selected Activities:")
for activity in selected:
    print(activity)

print("\nTotal Activities Selected:", len(selected))
