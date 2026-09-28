---
schema: qual/card@1
id: P-GRECH7-11
kind: problem
title: Iterations of Euclid's algorithm on $380$ and $72$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 11 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
The steps below are used to compute Euclid's Algorithm to find the greatest common divisor of two integers. If the numbers $380$ and $72$ are input, how many iterations of the algorithm will it take to find the gcd?

```
input a;
input b;
while (b > 0) {
    int r == a mod b;
    a == b;
    b == r;
}
int gcd == a;
output gcd;
```

(A) $3$
(B) $4$
(C) $5$
(D) $6$
(E) $7$
:::
