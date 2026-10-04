# Case Study: Google Calendar Application using Greedy Strategy

## 1. Introduction
Calendar applications manage meetings, appointments, lectures, interviews, and other activities. Some activities overlap, so the system may need to select the maximum number of non-overlapping activities.

## 2. Problem Statement
Given activities with start and finish times, select the maximum number of non-overlapping activities.

| Activity | Start | Finish |
|---|---:|---:|
| A | 9:00 | 10:00 |
| B | 9:30 | 11:00 |
| C | 10:00 | 11:30 |
| D | 11:00 | 12:00 |
| E | 11:30 | 12:30 |
| F | 12:00 | 1:00 |

## 3. Objective
- Select maximum non-overlapping activities.
- Avoid event conflicts.
- Efficiently manage available time.
- Apply Greedy strategy.

## 4. Greedy Strategy
For the Activity Selection Problem, always select the activity that **finishes earliest**. This leaves maximum remaining time for future activities.

## 5. Algorithm
```text
ACTIVITY_SELECTION(activities)
1. Sort activities by finish time.
2. Select the first activity.
3. Set its finish time as last_finish.
4. For each remaining activity:
   If start_time >= last_finish:
       Select it.
       Update last_finish.
5. Return selected activities.
```

## 6. Example
Selected activities:
- A → 9:00–10:00
- C → 10:00–11:30
- E → 11:30–12:30

Maximum non-overlapping activities = **3**

## 7. Python Implementation
See `activity_selection.py`.

## 8. Output
```text
Selected Activities:
('A', 9, 10)
('C', 10, 11.5)
('E', 11.5, 12.5)

Total Activities Selected: 3
```

## 9. Complexity Analysis
Sorting: **O(n log n)**  
Selection: **O(n)**  
Overall Time Complexity: **O(n log n)**  
Space Complexity: **O(n)**

## 10. Real-World Applications
- Meeting scheduling
- Interview scheduling
- Classroom scheduling
- Appointment management
- Conference room allocation
- Event scheduling

## 11. Conclusion
The Greedy Strategy efficiently selects the maximum number of non-overlapping activities by choosing the activity with the earliest finishing time. This makes it suitable for calendar scheduling applications.
