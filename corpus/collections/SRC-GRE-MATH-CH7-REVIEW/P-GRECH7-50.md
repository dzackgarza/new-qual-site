---
schema: qual/card@1
id: P-GRECH7-50
kind: problem
title: Output sequence of the $3x+1$ algorithm from $17$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 50 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The shared algorithm lost its multiplication sign in both extractions; the solution computes 3a+1.
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

What is the sequence of outputs when the input value is 17?

(A) 17, 52, 28, 14, 7, 20, 10, 5, 16, 8, 4, 2, 1
(B) 52, 28, 14, 7, 20, 10, 5, 16, 8, 4, 2, 1
(C) 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
(D) 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
(E) The sequence does not end.
:::
