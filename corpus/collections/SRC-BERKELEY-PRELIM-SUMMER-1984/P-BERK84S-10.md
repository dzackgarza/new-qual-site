---
schema: qual/card@1
id: P-BERK84S-10
kind: problem
title: Completeness of the Hölder space $C^{1/3}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 10 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the norm axioms, uniform control from the anchor f(0)=0, and passage of the Holder quotient bound to the uniform limit.
---

::: {.problem}
Let $C^{1/3}$ be the set of real valued functions $f$ on the closed interval $[0,1]$ such that

1. $f(0) = 0$;

2. $\norm{f}$ is finite, where by definition
$$
\norm{f} = \sup \left\{ \frac{\abs{f(x) - f(y)}}{\abs{x - y}^{1/3}} \st x \neq y \right\}.
$$

Verify that $\norm{\cdot}$ is a norm for the space $C^{1/3}$, and prove that $C^{1/3}$ is complete with respect to this norm.
:::

::: {.solution}
For $f\in C^{1/3}$, write
$$
\norm{f}_{1/3}
:=\sup_{x\ne y}
\frac{\abs{f(x)-f(y)}}{\abs{x-y}^{1/3}}.
$$

::: pf

::: pf-step

The functional $\norm{\cdot}_{1/3}$ is a norm on $C^{1/3}$.

::: pf-proof

Nonnegativity is immediate. If $\norm{f}_{1/3}=0$, then
$$
\abs{f(x)-f(y)}=0
$$
for all $x,y$, so $f$ is constant. Since $f(0)=0$, this constant is $0$, hence $f=0$.
Conversely $\norm{0}_{1/3}=0$.

For $a\in\RR$,
$$
\norm{af}_{1/3}
=\abs{a}\,\norm{f}_{1/3}.
$$
Finally, for $x\ne y$,
$$
\frac{\abs{(f+g)(x)-(f+g)(y)}}{\abs{x-y}^{1/3}}
\le
\frac{\abs{f(x)-f(y)}}{\abs{x-y}^{1/3}}
+
\frac{\abs{g(x)-g(y)}}{\abs{x-y}^{1/3}}.
$$
Taking the supremum gives
$$
\norm{f+g}_{1/3}\le \norm{f}_{1/3}+\norm{g}_{1/3}.
$$
Thus all norm axioms hold.

:::

:::

::: {.pf-step #s2}

The Hölder norm controls the uniform norm.

::: pf-proof

Since $f(0)=0$, for every $x\in[0,1]$,
$$
\abs{f(x)}=\abs{f(x)-f(0)}
\le \norm{f}_{1/3}\abs{x}^{1/3}
\le \norm{f}_{1/3}.
$$
Hence
$$
\norm{f}_\infty\le \norm{f}_{1/3}.
$$

:::

:::

::: pf-step

Every Cauchy sequence in $\norm{\cdot}_{1/3}$ converges uniformly to a function $f$ with $f(0)=0$.

::: pf-proof

Let $(f_n)$ be Cauchy in $\norm{\cdot}_{1/3}$. By step [](#s2){.pf-ref},
$$
\norm{f_n-f_m}_\infty
\le \norm{f_n-f_m}_{1/3},
$$
so $(f_n)$ is uniformly Cauchy. Since $\RR$ is complete, there is a function $f:[0,1]\to\RR$ such that $f_n\to f$ uniformly. Because each $f_n(0)=0$,
$$
f(0)=\lim_{n\to\infty}f_n(0)=0.
$$

:::

:::

::: pf-step

In fact $f_n\to f$ in the Hölder norm.

::: pf-proof

Fix $\varepsilon>0$. Since $(f_n)$ is Cauchy, choose $N$ so that
$$
\norm{f_n-f_m}_{1/3}<\varepsilon
\qquad(m,n\ge N).
$$
Fix $n\ge N$ and $x\ne y$. Then for every $m\ge N$,
$$
\abs{(f_n-f_m)(x)-(f_n-f_m)(y)}
\le \varepsilon \abs{x-y}^{1/3}.
$$
Letting $m\to\infty$ and using pointwise convergence $f_m\to f$ gives
$$
\abs{(f_n-f)(x)-(f_n-f)(y)}
\le \varepsilon \abs{x-y}^{1/3}.
$$
Therefore
$$
\norm{f_n-f}_{1/3}\le\varepsilon
\qquad(n\ge N).
$$
Thus $f_n\to f$ in the given norm. In particular,
$$
\norm{f}_{1/3}
\le \norm{f-f_N}_{1/3}+\norm{f_N}_{1/3}<\infty,
$$
so $f\in C^{1/3}$.

Hence $C^{1/3}$ is complete.

:::

:::

:::

:::
