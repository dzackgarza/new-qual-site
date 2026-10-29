---
schema: qual/card@1
id: P-IZZ3T
kind: problem
title: Riemann integrability under $\abs{g(x)-g(y)}\le\abs{f(x)-f(y)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
---

::: {.problem}
Suppose $f, g: [0, 1] \to \RR$ where $f$ is Riemann integrable and for $x, y\in [0, 1]$,
$$
\abs{g(x) - g(y)} \leq \abs{f(x) - f(y)}
.$$

Prove that $g$ is Riemann integrable.
:::

::: {.solution}
For an interval $I\subseteq[0,1]$ let $\omega_f(I)=\sup_{x,y\in I}\abs{f(x)-f(y)}$ and $\omega_g(I)=\sup_{x,y\in I}\abs{g(x)-g(y)}$ be the oscillations, and write $\abs{I}$ for its length.

::: pf

::: {.pf-step #bounded}
$g$ is bounded.

::: pf-proof
A Riemann integrable function is bounded, so $\abs{f} \leq M$ for some $M$.
Fix $x_0\in[0,1]$; then $\abs{g(x)}\le \abs{g(x_0)}+\abs{f(x)-f(x_0)} \leq \abs{g(x_0)} + 2M$.
:::

:::

::: {.pf-step #oscillation}
$\omega_g(I)\le \omega_f(I)$ for every interval $I$.

::: pf-proof
This is the hypothesis, after taking suprema over $x, y \in I$.
:::

:::

::: pf-step
$g$ is Riemann integrable.

::: pf-proof
Let $\varepsilon>0$.
Since $f$ is Riemann integrable, there is a partition $P$ of $[0,1]$ with $U(f,P)-L(f,P)=\sum_{I\in P}\omega_f(I)\abs{I}<\varepsilon$.
By steps [](#bounded){.pf-ref} and [](#oscillation){.pf-ref}, the Darboux sums of $g$ are defined and
$$
U(g,P)-L(g,P) =\sum_{I\in P}\omega_g(I)\abs{I} \le\sum_{I\in P}\omega_f(I)\abs{I} <\varepsilon,
$$
so the Darboux criterion applies.
:::

:::

:::
:::
