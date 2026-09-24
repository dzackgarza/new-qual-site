---
schema: qual/card@1
id: P-BKF10-3A
kind: problem
title: Bounded isolated singularities are removable
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Laurent-coefficient formula and the small-circle estimate
    forcing every negative coefficient to vanish.
---

::: {.problem}
Suppose that $f$ is bounded and analytic on a deleted neighborhood $0<\abs{z}<\varepsilon$ of the origin.
Let
$$
f(z)=\sum_{j=-\infty}^{\infty}c_jz^j
$$
be the Laurent expansion of $f$.
Show that if $j<0$, then $c_j=0$.
:::

::: {.solution}
<1>1. Choose $M>0$ such that
$$
\abs{f(z)}\le M
$$
for all $0<\abs{z}<\varepsilon$.

::: {.proof}
Such an $M$ exists by the boundedness hypothesis.
:::

<1>2. For every integer $j$ and every $0<r<\varepsilon$,
$$
c_j
=\frac1{2\pi i}
\int_{\abs{z}=r}z^{-j-1}f(z)\,dz.
$$

::: {.proof}
This is the Laurent coefficient formula applied on the circle
$\abs{z}=r$, which lies in the annulus of analyticity.
:::

<1>3. For every integer $j$ and every $0<r<\varepsilon$,
$$
\abs{c_j}\le M r^{-j}.
$$

::: {.proof}
By step <1>2 and the ML estimate,
$$
\begin{aligned}
\abs{c_j}
&\le\frac1{2\pi}
   \max_{\abs{z}=r}\abs{z^{-j-1}f(z)}\cdot 2\pi r\\
&\le\frac1{2\pi}r^{-j-1}M\cdot2\pi r\\
&=Mr^{-j}.
\end{aligned}
$$
:::

<1>4. If $j<0$, then $c_j=0$.

::: {.proof}
For fixed $j<0$, the exponent $-j$ is positive. Step <1>3 holds for
every $0<r<\varepsilon$, so letting $r\to0^+$ gives
$$
0\le\abs{c_j}\le Mr^{-j}\longrightarrow0.
$$
Therefore $\abs{c_j}=0$, hence $c_j=0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves that every negative Laurent coefficient vanishes.
:::
:::
