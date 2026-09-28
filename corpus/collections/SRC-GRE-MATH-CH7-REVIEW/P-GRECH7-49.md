---
schema: qual/card@1
id: P-GRECH7-49
kind: problem
title: Recurrence describing the $3x+1$ algorithm
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 49 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The shared algorithm lost its multiplication sign in both extractions; the solution computes 3a+1.
---

::: {.problem}
Use the algorithm for the "$3x+1$" problem:

```
input (a)
while a > 1
    begin
        if (a mod 2 = 0)
            a := a / 2
        else a := 3 * a + 1
        output (a)
    end
```

Which of the following correctly represents the algorithm described above?

(A) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_{n-1} \text{ odd} \\ 3a_{n-1} + 1 \text{ for } a_{n-1} \text{ even} \end{cases}$
(B) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_{n-1} \text{ even} \\ 3a_{n-1} + 1 \text{ for } a_{n-1} \text{ odd} \end{cases}$
(C) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_{n-1} \text{ even} \\ \frac{1}{2}(3a_{n-1} + 1) \text{ for } a_{n-1} \text{ odd} \end{cases}$
(D) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_n \text{ even} \\ 3a_{n-1} + 1 \text{ for } a_n \text{ odd} \end{cases}$
(E) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_n \text{ odd} \\ 3a_{n-1} + 1 \text{ for } a_n \text{ even} \end{cases}$
:::
