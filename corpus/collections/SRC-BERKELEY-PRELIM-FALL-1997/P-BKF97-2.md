---
schema: qual/card@1
id: P-BKF97-2
kind: problem
title: A derivative changing sign has a zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the endpoint derivative signs to exclude both endpoints from being
    minima, then applied the extreme-value and Fermat theorems to an interior
    minimum.
---

::: {.problem}
Let $f$ be a real-valued function differentiable on an open interval containing $[a,b]$.
Prove that if
\[
f'(a)<0
\qquad\text{and}\qquad
f'(b)>0,
\]
then there is a point $c\in(a,b)$ such that $f'(c)=0$.
:::

::: {.solution}
<1>1. The point $a$ is not a minimum of $f$ on $[a,b]$.

::: {.proof}
Since
$$
f'(a)<0,
$$
the difference quotient
$$
\frac{f(a+h)-f(a)}{h}
$$
is negative for all sufficiently small positive $h$. For such $h$,
$$
f(a+h)<f(a).
$$
Thus $a$ cannot minimize $f$ on $[a,b]$.
:::

<1>2. The point $b$ is not a minimum of $f$ on $[a,b]$.

::: {.proof}
Since
$$
f'(b)>0,
$$
the difference quotient
$$
\frac{f(b+h)-f(b)}{h}
$$
is positive for all sufficiently small negative $h$. Because $h<0$, this
implies
$$
f(b+h)-f(b)<0,
$$
so
$$
f(b+h)<f(b).
$$
Thus $b$ cannot minimize $f$ on $[a,b]$.
:::

<1>3. The function $f$ attains its minimum on $[a,b]$ at some point
$$
c\in(a,b).
$$

::: {.proof}
Differentiability on an open interval containing $[a,b]$ implies
continuity on $[a,b]$. By the extreme-value theorem, $f$ attains a minimum
at some point of $[a,b]$. Steps <1>1 and <1>2 exclude the two endpoints, so
the minimizing point lies in $(a,b)$.
:::

<1>4. One has
$$
\boxed{f'(c)=0}.
$$

::: {.proof}
The point $c$ from step <1>3 is an interior local minimum, and $f$ is
differentiable there. Fermat's theorem therefore gives $f'(c)=0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required point.
:::
:::
