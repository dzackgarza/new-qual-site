---
schema: qual/card@1
id: P-BKF85-8
kind: problem
title: $(n+1)\int_0^1x^nf(x)\,dx\to f(1)$ for continuous $f$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md.
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$ be continuous.
Show that
\[
\lim_{n\to\infty}(n+1)\int_0^1 x^n f(x)\,dx=f(1).
\]
:::

::: {.solution}
For $n\geq0$, set
$$
I_n\coloneqq(n+1)\int_0^1x^nf(x)\,dx.
$$

<1>1. One has
$$
I_n-f(1)
=
(n+1)\int_0^1x^n\bigl(f(x)-f(1)\bigr)\,dx.
$$

::: {.proof}
Since
$$
(n+1)\int_0^1x^n\,dx=1,
$$
one may write
$$
f(1)
=
(n+1)\int_0^1x^nf(1)\,dx.
$$
Subtracting this from the definition of $I_n$ gives the identity.
:::

<1>2. For every $\varepsilon>0$, there exist $0<\delta<1$ and $M<\infty$ such that
$$
\abs{f(x)-f(1)}<\varepsilon
\qquad
\text{for }1-\delta\leq x\leq1,
$$
and
$$
\abs{f(x)-f(1)}\leq M
\qquad
\text{for }0\leq x\leq1.
$$

::: {.proof}
Continuity of $f$ at $1$ gives the first assertion for some $\delta>0$, which may be decreased to lie in $(0,1)$. Continuity on the compact interval $[0,1]$ makes $f(x)-f(1)$ bounded there, giving the second assertion.
:::

<1>3. With $\delta$ and $M$ as in step <1>2,
$$
\abs{I_n-f(1)}
\leq
M(1-\delta)^{n+1}+\varepsilon
$$
for every $n$.

::: {.proof}
By step <1>1, split the integral at $1-\delta$:
$$
\begin{aligned}
\abs{I_n-f(1)}
&\leq
(n+1)\int_0^{1-\delta}
x^n\abs{f(x)-f(1)}\,dx\\
&\quad+
(n+1)\int_{1-\delta}^1
x^n\abs{f(x)-f(1)}\,dx\\
&\leq
M(n+1)\int_0^{1-\delta}x^n\,dx
+\varepsilon(n+1)\int_{1-\delta}^1x^n\,dx\\
&\leq
M(1-\delta)^{n+1}+\varepsilon.
\end{aligned}
$$
:::

<1>4. One has
$$
\lim_{n\to\infty}I_n=f(1).
$$

::: {.proof}
Because $0<1-\delta<1$,
$$
M(1-\delta)^{n+1}\longrightarrow0.
$$
Thus step <1>3 gives
$$
\limsup_{n\to\infty}\abs{I_n-f(1)}
\leq\varepsilon.
$$
Since $\varepsilon>0$ was arbitrary, the limsup is $0$, and therefore $I_n\to f(1)$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required limit.
:::
:::
