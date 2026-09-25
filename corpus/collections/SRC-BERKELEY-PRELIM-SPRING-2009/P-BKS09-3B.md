---
schema: qual/card@1
id: P-BKS09-3B
kind: problem
title: Counting roots of $z^4-5z^3+z-2$ in a disk
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the disk radius |z| < 1 (OCR read 12) against s09solutions.pdf page 4 problem 3B.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the strict Rouche inequality on the unit circle and multiplicity count.
---

::: {.problem}
How many roots of the equation $z^4 - 5z^3 + z - 2 = 0$ lie in the disk $|z| < 1$?
:::

::: {.solution}
Set
$$
F(z)\coloneqq z^4-5z^3+z-2
$$
and
$$
G(z)\coloneqq-5z^3.
$$

<1>1. On the unit circle,
$$
\abs{F(z)-G(z)}<\abs{G(z)}.
$$

::: {.proof}
If $\abs z=1$, then
$$
\begin{aligned}
\abs{F(z)-G(z)}
&=
\abs{z^4+z-2}\\
&\leq
\abs z^4+\abs z+2\\
&=
4
<
5
=
\abs{-5z^3}
=
\abs{G(z)}.
\end{aligned}
$$
:::

<1>2. The polynomials $F$ and $G$ have the same number of zeros in
$\abs z<1$, counted with multiplicity.

::: {.proof}
Both functions are holomorphic on and inside the unit circle, and step <1>1
is the strict inequality required by Rouché's theorem. The conclusion follows
directly from that theorem.
:::

<1>3. The equation has
$$
\boxed{3}
$$
roots in the disk $\abs z<1$, counted with multiplicity.

::: {.proof}
The polynomial
$$
G(z)=-5z^3
$$
has exactly one zero, $z=0$, of multiplicity $3$. Step <1>2 transfers this
count to $F$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested number of roots.
:::
:::
