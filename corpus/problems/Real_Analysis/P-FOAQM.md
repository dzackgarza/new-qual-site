---
schema: qual/card@1
id: P-FOAQM
kind: problem
title: Riemann integrability of $g$ when $|g(x)-g(y)|\le|f(x)-f(y)|$ for integrable
  $f$
classification:
  areas:
  - real-analysis
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
For a bounded function $h$ and a partition $P$ of $[0,1]$ into intervals $I_1,\ldots,I_n$, write
$$
U(h,P) - L(h,P) = \sum_{k=1}^n \qty{\sup_{I_k} h - \inf_{I_k} h}\,\mu(I_k).
$$

::: pf

::: pf-step
$g$ is bounded.

::: pf-proof
A Riemann integrable function is bounded, say $\abs f\leq M$. Then $\abs{g(x)} \leq \abs{g(0)} + \abs{f(x)-f(0)} \leq \abs{g(0)} + 2M$.
:::

:::

::: {.pf-step #oscillation}
For every interval $I\subseteq[0,1]$, $\sup_I g - \inf_I g \leq \sup_I f - \inf_I f$.

::: pf-proof
For a bounded function $h$, $\sup_I h - \inf_I h = \sup_{x,y\in I}\abs{h(x)-h(y)}$. The hypothesis gives $\abs{g(x)-g(y)}\leq\abs{f(x)-f(y)}$ for all $x,y\in I$; take the supremum.
:::

:::

::: pf-step
$g$ is Riemann integrable.

::: pf-proof
Fix $\varepsilon>0$. Since $f$ is integrable, Riemann's criterion gives a partition $P$ with $U(f,P)-L(f,P)<\varepsilon$.
By step [](#oscillation){.pf-ref} applied to each interval of $P$, $U(g,P)-L(g,P)\leq U(f,P)-L(f,P)<\varepsilon$.
By Riemann's criterion, $g$ is integrable.
:::

:::

:::

:::
