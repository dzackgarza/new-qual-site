---
schema: qual/card@1
id: P-JHUFA05ANG
kind: problem
title: Zeros of $z^9+z^5-8z^3-z+2$ between two circles
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared the polynomial and the annular counting region with September 2005 problem 7 on PDF page 43; corrected the title to name the requested annulus."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked strict bounds on both circles, subtraction of the two multiplicity counts and exclusion of boundary zeros."
---

::: {.problem}
7. How many zeros does the polynomial

$$
z ^ { 9 } + z ^ { 5 } - 8 z ^ { 3 } - z + 2
$$

have between the circles $\{ | z | = 1 \}$ and $\{ | z | = 2 \}$ . Justify your answer.
:::

::: solution
There are $\boxed{6}$ zeros between the circles, counted
with multiplicity. Let $p(z)=z^9+z^5-8z^3-z+2$.

<1>1. The unit disk contains three zeros.

::: proof
On $|z|=1$,
$$
|z^9+z^5-z+2|\leq1+1+1+2=5<8=|-8z^3|.
$$
Rouché's theorem gives the same number of zeros for
$p$ and $-8z^3$ in this disk, namely three counted
with multiplicity [@SS03]. The strict inequality also
gives $|p(z)|\geq3$ on the circle, so there are no
boundary zeros.
:::

<1>2. The radius-two disk contains nine zeros, leaving six in the annulus.

::: proof
On $|z|=2$,
$$
|z^5-8z^3-z+2|\leq32+64+2+2=100<512=|z^9|.
$$
Rouché's theorem now compares $p$ with $z^9$, giving
nine zeros in $|z|<2$, with multiplicity [@SS03].
Again the strict inequality excludes zeros on the
boundary. Subtracting the three inside $|z|<1$ gives
$9-3=6$ in $1<|z|<2$. Since neither circle contains
a zero, including the boundary circles would not
change this answer.
:::
:::
