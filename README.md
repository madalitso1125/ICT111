# Student Grading System - ICT111 Lab 2[span_1](start_span)[span_1](end_span)
**Institution:** Mulungushi University[span_2](start_span)[span_2](end_span)  
**School:** School of Engineering and Technology[span_3](start_span)[span_3](end_span)  
**Department:** Computer Science and IT[span_4](start_span)[span_4](end_span)  
**Due Date:** 09-11-2026[span_5](start_span)[span_5](end_span)  

---

## 1. Input-Process-Output (IPO) Plan & Data Structure

### IPO Plan
* **Input:** 
  * Menu navigation option (`1`, `2`, `3`, or `4`)[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
  * Student details: Student Number (non-blank string), Name (non-blank string), and Mark (numeric value from `0` to `100`)[span_8](start_span)[span_8](end_span).
* **Process:**
  * Validate user inputs using `while` loops and `try-except` exception handling blocks to prevent crashes on non-numeric or out-of-range entries[span_9](start_span)[span_9](end_span).
  * Evaluate marks using `if/elif/else` selection logic to classify scores into grades (`A`, `B`, `C`, `D`, `F`) and decisions (`Excellent`, `Very good`, `Good`, `Pass`, `Fail`)[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).
  * Store each record as a dictionary inside a centralized Python list (`students`)[span_12](start_span)[span_12](end_span).
  * Iterate over records using `for` loops to display formatted reports and compute summary statistics (total students, class average, highest/lowest marks, and pass/fail counts)[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span).
* **Output:**
  * Success confirmations upon record insertion[span_15](start_span)[span_15](end_span).
  * Tabular list of student records[span_16](start_span)[span_16](end_span).
  * Statistical summary report.
  * Error warnings and clean program exit[span_17](start_span)[span_17](end_span).

### Data Structure Rationale: Why a List of Dictionaries?
A **list of dictionaries** is optimal for this application because:
1. **Dynamic Scaling (List):** A list allows us to append an arbitrary number of student records dynamically without requiring a pre-defined array size.
2. **Attribute Mapping (Dictionary):** Each student record contains heterogeneous attributes (`student_number`, `name`, `mark`, `grade`, `decision`)[span_18](start_span)[span_18](end_span). A dictionary maps descriptive string keys directly to these values, making data access readable and maintainable (e.g., `s['mark']` instead of relying on rigid numeric indices).

---

## 2. Test Cases and Verification

| Test ID | Input / Action | Expected Behavior | Observed Behavior | Status |
| :--- | :--- | :--- | :--- | :--- |
| **T1** | Add mark `79`, then `80` | `79` gets Grade B (Very good); `80` gets Grade A (Excellent). Both count as passes[span_19](start_span)[span_19](end_span). | Correct grades and pass decisions assigned[span_20](start_span)[span_20](end_span). | **Passed** |
| **T2** | Add mark `49`, then `50` | `49` gets Grade F (Fail); `50` gets Grade D (Pass)[span_21](start_span)[span_21](end_span). | Correct boundary classification observed[span_22](start_span)[span_22](end_span). | **Passed** |
| **T3** | Enter `-1`, `101`, or `"abc"` as mark | Reject invalid/out-of-range/non-numeric inputs; display error message; re-prompt without crashing[span_23](start_span)[span_23](end_span). | Handled gracefully via `try-except` and bounds checking[span_24](start_span)[span_24](end_span). | **Passed** |
| **T4** | Choose summary option before adding students | Prevent division by zero; display an informative message indicating no records exist[span_25](start_span)[span_25](end_span). | Handled safely with check `if not students:`[span_26](start_span)[span_26](end_span). | **Passed** |
| **T5** | Choose an invalid menu option (`5` or `"xyz"`) | Display a warning message and return cleanly to the main menu[span_27](start_span)[span_27](end_span). | Warning displayed and menu re-rendered[span_28](start_span)[span_28](end_span). | **Passed** |

---

## 3. Reflection Answers

1. **Why does the order of if/elif conditions matter at grade boundaries?**  
   Python evaluates `if/elif` chains sequentially from top to bottom and stops at the first condition that evaluates to `True`. Because our program checks lower bounds (e.g., `mark >= 80`, `mark >= 70`, `mark >= 60`), placing higher thresholds first ensures that a mark like `85` matches `mark >= 80` immediately. If the order were reversed and `mark >= 50` was evaluated first, a mark of `85` would satisfy `mark >= 50` and be incorrectly assigned a 'D' grade.

2. **What error could arise when calculating the average of an empty list?**  
   If no student records have been added, the total number of students is `0`. Attempting to divide the cumulative total marks by `0` (`total_marks / total_students`) results in a `ZeroDivisionError`, causing the program to crash. This is safely prevented by checking `if not students:` prior to computation.

3. **How would you adapt the program to handle two courses per student?**  
   To manage multiple courses, we could:
   * Nest a dictionary within each student record to map course codes to marks (e.g., `"courses": {"ICT111": 78, "MAT111": 85}`).
   * Update the input prompt to capture marks across both course identifiers.
   * Expand the statistics module to report individual course averages alongside overall cumulative performance.

---
