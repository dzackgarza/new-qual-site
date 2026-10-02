---
schema: qual/card@1
id: P-GRECH7-01
kind: problem
title: Interval containing a zero of $4x^3-4x^2-33x+45$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 1 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
For which of the following intervals does $P(x) = 4x^3 - 4x^2 - 33x + 45$ have a zero?

(A) $[-2, -1]$
(B) $[-1, 0]$
(C) $[0, 1]$
(D) $[2, 3]$
(E) $[3, 4]$
:::

::: {.solution}
<1>1. The polynomial factors as
$$
P(x)=(x+3)(2x-3)(2x-5).
$$

::: {.proof}
First,
$$
(2x-3)(2x-5)=4x^2-16x+15.
$$
Multiplying by $x+3$ gives
$$
(x+3)(4x^2-16x+15)
=4x^3-4x^2-33x+45
=P(x).
$$
:::

<1>2. The real zeros of $P$ are
$$
-3,\qquad \frac32,\qquad \frac52.
$$

::: {.proof}
By step <1>1, $P(x)=0$ exactly when one of the three linear factors vanishes.
:::

<1>3. Among the listed intervals, exactly $[2,3]$ contains a zero of $P$.

::: {.proof}
The zero $-3$ lies to the left of every listed interval. The zero $3/2$ lies strictly between $1$ and $2$, hence in none of the listed intervals. The zero $5/2$ satisfies
$$
2<\frac52<3,
$$
so it lies in $[2,3]$. None of the other listed intervals contains any of the three zeros from step <1>2.
:::

<1>4. Therefore the required interval is
$$
\boxed{[2,3]},
$$
so the answer is (D).

::: {.proof}
This is exactly the interval identified in step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required choice.
:::
:::
