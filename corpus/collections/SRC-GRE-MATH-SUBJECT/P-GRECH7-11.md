---
schema: qual/card@1
id: P-GRECH7-11
kind: problem
title: Iterations of Euclid's algorithm on $380$ and $72$
classification:
  areas: [prelim]
  topics:
  - Euclidean Algorithm
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

::: {.solution}

Interpreting the update lines in the displayed pseudocode as assignments, one loop iteration replaces $(a,b)$ by $(b,a\bmod b)$.

::: pf

::: {.pf-step #s1-1}

Starting from $(380,72)$, the successive pairs after each iteration are
$$
(72,20),\quad(20,12),\quad(12,8),\quad(8,4),\quad(4,0).
$$


::: pf-proof

The successive Euclidean divisions are
$$
380=5\cdot72+20,
$$
$$
72=3\cdot20+12,
$$
$$
20=1\cdot12+8,
$$
$$
12=1\cdot8+4,
$$
and
$$
8=2\cdot4+0.
$$
Thus each remainder produces exactly the next displayed value of $b$.

:::

:::

::: {.pf-step #s1-2}

The loop terminates after
$$
\boxed{5}
$$
iterations, so the answer is (C).


::: pf-proof

By step [](#s1-1){.pf-ref}, the value of $b$ becomes $0$ for the first time after the fifth update. The while-condition then fails, with $a=4$, so the algorithm terminates after five iterations.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested iteration count.

:::

:::

:::
