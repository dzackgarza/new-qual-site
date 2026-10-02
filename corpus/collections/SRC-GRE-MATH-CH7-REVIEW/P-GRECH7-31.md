---
schema: qual/card@1
id: P-GRECH7-31
kind: problem
title: Which subset of $\mathbb{R}^3$ is compact
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 31 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Which of the following sets in $\mathbb{R}^3$ is compact?

(A) $\{x, y, z \mid |x + y + z| < 5\}$
(B) $\{x, y, z \mid x < 2 \ \& \ y < 2 \ \& \ z < 2\}$
(C) $\{x, y, z \mid 0 \le x \le 3, 0 \le y \le 3, 0 \le z \le 3\}$
(D) $\{x, y, z \mid x \ge 0, y \ge 0, z \ge 0\}$
(E) $\{x, y, z \mid 2 < x^2 + y^2 + z^2 < 8\}$
:::

::: {.solution}
<1>1. Choice (C) is closed and bounded in $\RR^3$.

::: {.proof}
Choice (C) is the box
$$
[0,3]^3.
$$
It is closed as a finite product of closed intervals, and it is bounded because every point $(x,y,z)$ in it satisfies
$$
\|(x,y,z)\|^2=x^2+y^2+z^2\le 27.
$$
:::

<1>2. Choices (B) and (D) are not bounded.

::: {.proof}
For every positive integer $n$, the point $(-n,0,0)$ lies in (B), so (B) is unbounded. Likewise $(n,0,0)$ lies in (D) for every positive integer $n$, so (D) is unbounded.
:::

<1>3. Choices (A) and (E) are not closed.

::: {.proof}
For (A), the points
$$
\left(5-\frac1n,0,0\right)
$$
belong to the set for $n\ge1$ and converge to $(5,0,0)$, which is not in the set because $|5|\not<5$.

For (E), the points
$$
\left(\sqrt{2+\frac1n},0,0\right)
$$
belong to the set for all sufficiently large $n$ and converge to $(\sqrt2,0,0)$, which is excluded because its squared norm is exactly $2$.
:::

<1>4. Therefore the compact set is
$$
\boxed{[0,3]^3},
$$
so the answer is (C).

::: {.proof}
By the Heine--Borel theorem, a subset of $\RR^3$ is compact exactly when it is closed and bounded. Step <1>1 proves these properties for (C), while steps <1>2 and <1>3 rule out the other choices.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required choice.
:::
:::
