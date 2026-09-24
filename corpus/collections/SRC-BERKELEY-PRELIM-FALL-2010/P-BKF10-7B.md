---
schema: qual/card@1
id: P-BKF10-7B
kind: problem
title: The derivative bound $\lvert f'(0)\rvert\le1$ in Schwarz's lemma
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the removable extension of f(z)/z, maximum modulus on every
    smaller disk, and the limiting radius argument.
---

::: {.problem}
If $f$ is analytic from the unit disk into itself and $f(0)=0$, prove that
$$
\abs{f'(0)}\le1.
$$
Since this problem is part of the proof of Schwarz's lemma, quoting that lemma does not receive full credit.
:::

::: {.solution}
Let
$$
D\coloneqq\{z\in\CC:\abs{z}<1\}.
$$

<1>1. The function
$$
g(z)\coloneqq
\begin{cases}
\dfrac{f(z)}z,&z\ne0,\\[4pt]
f'(0),&z=0
\end{cases}
$$
is analytic on $D$.

::: {.proof}
Since $f(0)=0$ and $f$ is analytic,
$$
\lim_{z\to0}\frac{f(z)}z
=\lim_{z\to0}\frac{f(z)-f(0)}{z-0}
=f'(0).
$$
Thus $f(z)/z$ has a removable singularity at $0$, and the displayed
value $g(0)=f'(0)$ gives its analytic extension to all of $D$.
:::

<1>2. For every $0<r<1$,
$$
\abs{g(0)}\le\frac1r.
$$

::: {.proof}
On the circle $\abs{z}=r$, the hypothesis that $f(D)\subseteq D$ gives
$$
\abs{f(z)}<1.
$$
Therefore
$$
\abs{g(z)}=\frac{\abs{f(z)}}r\le\frac1r.
$$
By step <1>1, $g$ is analytic on a neighborhood of the closed disk
$\abs{z}\le r$. The maximum modulus principle therefore gives
$$
\abs{g(0)}
\le\max_{\abs{z}=r}\abs{g(z)}
\le\frac1r.
$$
:::

<1>3. One has
$$
\abs{f'(0)}\le1.
$$

::: {.proof}
By definition in step <1>1,
$$
\abs{f'(0)}=\abs{g(0)}.
$$
Step <1>2 gives $\abs{g(0)}\le1/r$ for every $0<r<1$. Letting
$r\to1^-$ yields
$$
\abs{f'(0)}\le1.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required derivative bound.
:::
:::
