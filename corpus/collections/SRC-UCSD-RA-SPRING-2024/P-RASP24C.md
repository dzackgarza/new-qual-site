---
schema: qual/card@1
id: P-RASP24C
kind: problem
title: "Hölder space is a Banach space with compact unit ball"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Spring 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $0 < \alpha \leq 1$ and let $\Lambda_\alpha([0,1])$ denote the space of Hölder continuous functions of exponent $\alpha$ on $[0,1]$.
Specifically, $\Lambda_\alpha([0,1]) = \{f \in C([0,1]) : \norm{f}_{\Lambda_\alpha} < \infty\}$ where
$$
\norm{f}_{\Lambda_\alpha} = \abs{f(0)} + \sup_{x \neq y \in [0,1]} \frac{\abs{f(x) - f(y)}}{\abs{x - y}^\alpha}.
$$

(a) Show that $\norm{\cdot}_{\Lambda_\alpha}$ is a norm on $\Lambda_\alpha([0,1])$ and that with this norm $\Lambda_\alpha([0,1])$ is a Banach space.

(b) Let $B = \{f \in \Lambda_\alpha([0,1]) : \norm{f}_{\Lambda_\alpha} \leq 1\}$ be the closed unit ball.
Show that $B$ is compact with respect to the uniform norm.
:::

::: {.solution}
Write
$$
[f]_\alpha:=\sup_{x\ne y}
\frac{\abs{f(x)-f(y)}}{\abs{x-y}^\alpha},
\qquad
\norm{f}_{\Lambda_\alpha}=\abs{f(0)}+[f]_\alpha.
$$

::: pf

::: pf-step

Verify that $\norm{\cdot}_{\Lambda_\alpha}$ is a norm.

::: pf-proof

Nonnegativity and absolute homogeneity are immediate. If
$$
\norm{f}_{\Lambda_\alpha}=0,
$$
then $f(0)=0$ and $[f]_\alpha=0$, so $f(x)=f(y)$ for all $x,y$. Thus $f\equiv0$.

For the triangle inequality,
$$
\abs{f(0)+g(0)}\le \abs{f(0)}+\abs{g(0)}
$$
and
$$
[f+g]_\alpha\le [f]_\alpha+[g]_\alpha.
$$
Hence
$$
\norm{f+g}_{\Lambda_\alpha}
\le \norm{f}_{\Lambda_\alpha}+\norm{g}_{\Lambda_\alpha}.
$$

:::

:::

::: pf-step

Prove completeness.

::: pf-proof

Let $(f_n)$ be Cauchy in $\norm{\cdot}_{\Lambda_\alpha}$. For every $h\in\Lambda_\alpha([0,1])$ and $x\in[0,1]$,
$$
\abs{h(x)}\le \abs{h(0)}+[h]_\alpha \abs{x}^\alpha
\le \norm{h}_{\Lambda_\alpha}.
$$
Therefore
$$
\norm{h}_\infty\le \norm{h}_{\Lambda_\alpha},
$$
so $(f_n)$ is uniformly Cauchy. Since $C([0,1])$ is complete in the uniform norm, there is $f\in C([0,1])$ such that
$$
f_n\to f
$$
uniformly.

Fix $\varepsilon>0$. Choose $N$ such that for $m,n\ge N$,
$$
\norm{f_n-f_m}_{\Lambda_\alpha}<\varepsilon.
$$
Fix $n\ge N$ and let $m\to\infty$. Uniform convergence gives
$$
\abs{f_n(0)-f(0)}\le\varepsilon.
$$
Also, for every $x\ne y$,
$$
\frac{\abs{(f_n-f)(x)-(f_n-f)(y)}}{\abs{x-y}^\alpha}
=\lim_{m\to\infty}
\frac{\abs{(f_n-f_m)(x)-(f_n-f_m)(y)}}{\abs{x-y}^\alpha}
\le\varepsilon.
$$
Taking the supremum over $x\ne y$ gives
$$
[f_n-f]_\alpha\le\varepsilon.
$$
Thus
$$
\norm{f_n-f}_{\Lambda_\alpha}\le2\varepsilon
$$
for all $n\ge N$. In particular $f\in\Lambda_\alpha([0,1])$ and $f_n\to f$ in the Hölder norm. Hence $\Lambda_\alpha([0,1])$ is Banach.

:::

:::

::: pf-step

Establish the Arzelà--Ascoli hypotheses for the unit ball.

::: pf-proof

If $f\in B$, then
$$
\abs{f(0)}\le1,
\qquad
[f]_\alpha\le1.
$$
Hence for every $x\in[0,1]$,
$$
\abs{f(x)}\le \abs{f(0)}+[f]_\alpha \abs{x}^\alpha\le2.
$$
Thus $B$ is uniformly bounded. Moreover, for every $x,y\in[0,1]$,
$$
\abs{f(x)-f(y)}\le \abs{x-y}^\alpha
$$
uniformly for $f\in B$, so $B$ is equicontinuous.

By the Arzelà--Ascoli theorem, $B$ is relatively compact in the uniform norm.

:::

:::

::: pf-step

Show that $B$ is uniformly closed.

::: pf-proof

Suppose $f_n\in B$ and $f_n\to f$ uniformly. For each fixed $x\ne y$,
$$
\abs{f_n(0)}+
\frac{\abs{f_n(x)-f_n(y)}}{\abs{x-y}^\alpha}
\le1.
$$
Passing to the limit gives
$$
\abs{f(0)}+
\frac{\abs{f(x)-f(y)}}{\abs{x-y}^\alpha}
\le1.
$$
Taking the supremum over $x\ne y$ yields
$$
\abs{f(0)}+[f]_\alpha\le1.
$$
Therefore $f\in B$. Thus $B$ is closed in the uniform norm.

Since $B$ is both relatively compact and closed in $C([0,1])$, it is compact in the uniform norm.

:::

:::

:::

:::
