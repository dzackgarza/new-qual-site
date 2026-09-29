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

::: pf

::: {.pf-step #s1}

One has
$$
I_n-f(1)
=
(n+1)\int_0^1x^n\bigl(f(x)-f(1)\bigr)\,dx.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

For every $\varepsilon>0$, there exist $0<\delta<1$ and $M<\infty$ such that
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

::: pf-proof

Continuity of $f$ at $1$ gives the first assertion for some $\delta>0$, which may be decreased to lie in $(0,1)$. Continuity on the compact interval $[0,1]$ makes $f(x)-f(1)$ bounded there, giving the second assertion.

:::

:::

::: {.pf-step #s3}

With $\delta$ and $M$ as in step [](#s2){.pf-ref},
$$
\abs{I_n-f(1)}
\leq
M(1-\delta)^{n+1}+\varepsilon
$$
for every $n$.

::: pf-proof

By step [](#s1){.pf-ref}, split the integral at $1-\delta$:
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

:::

::: {.pf-step #s4}

One has
$$
\lim_{n\to\infty}I_n=f(1).
$$

::: pf-proof

Because $0<1-\delta<1$,
$$
M(1-\delta)^{n+1}\longrightarrow0.
$$
Thus step [](#s3){.pf-ref} gives
$$
\limsup_{n\to\infty}\abs{I_n-f(1)}
\leq\varepsilon.
$$
Since $\varepsilon>0$ was arbitrary, the limsup is $0$, and therefore $I_n\to f(1)$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required limit.

:::

:::

:::
