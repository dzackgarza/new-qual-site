---
schema: qual/card@1
id: P-CASP08C
kind: problem
title: "Uniform limit of injective analytic functions on the upper half-plane is injective"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The prose said the translated functions "converge locally uniformly" without saying why (the constants f_j(a) need their own convergence, and the compact set must be enlarged to include a), and it said "the first alternative is impossible" without deriving that from the identity theorem. Both are now steps. Also stated: the punctured upper half-plane is connected and open, which Hurwitz needs, and that each g_j is nonzero because f_j is injective. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair.
---

::: {.problem}
Suppose that $f_j \to f$ in $H(\{\operatorname{Im} z > 0\})$, with each $f_j$ one-to-one.
If $f$ is not constant, show that $f$ is one-to-one.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, and it is Hurwitz's theorem applied to the translate that kills one point.

Let $\Omega=\{\operatorname{Im}z>0\}$ and let $f_j\to f$ mean locally uniformly on $\Omega$.

::: pf

::: {.pf-step #setup}
Fix distinct $a,b\in\Omega$, and put $g_j=f_j-f_j(a)$ and $g=f-f(a)$ on $\Omega\setminus\{a\}$.

::: pf-proof
$\Omega\setminus\{a\}$ is open and connected, being the upper half-plane with one point removed. Each $g_j$ and $g$ is holomorphic there, since $f_j$ and $f$ are holomorphic on $\Omega\supseteq\Omega\setminus\{a\}$ and $f_j(a)$, $f(a)$ are constants.
:::

:::

::: {.pf-step #convergence}
$g_j\to g$ locally uniformly on $\Omega\setminus\{a\}$, and $f_j(a)\to f(a)$.

::: pf-proof
On a compact $K\subseteq\Omega\setminus\{a\}$, $\sup_K\abs{g_j-g}\le\sup_K\abs{f_j-f}+\abs{f_j(a)-f(a)}$. The first term tends to $0$ by local uniform convergence of $f_j$ to $f$ on the compact set $K\cup\{a\}$, and the second tends to $0$ because $f_j\to f$ pointwise; so $g_j\to g$ uniformly on $K$.
:::

:::

::: {.pf-step #zerofree}
For every $j$, $g_j$ has no zero on $\Omega\setminus\{a\}$.

::: pf-proof
If $g_j(z)=0$ with $z\in\Omega\setminus\{a\}$, then $f_j(z)=f_j(a)$ with $z\ne a$, contradicting injectivity of $f_j$.
:::

:::

::: {.pf-step #hurwitz}
Either $g$ is identically zero on $\Omega\setminus\{a\}$, or $g$ has no zero there.

::: pf-proof
The $g_j$ are holomorphic on the region $\Omega\setminus\{a\}$ and converge locally uniformly to $g$ by step [](#convergence){.pf-ref}; Hurwitz's theorem then says that either $g\equiv0$ or $g$ is nowhere zero. (Each $g_j$ is nonzero by step [](#zerofree){.pf-ref}, so the hypothesis "$g_j$ never vanishes" needed for the second alternative is met.)
:::

:::

::: {.pf-step #nonconstant}
$g$ is not identically zero.

::: pf-proof
If $g\equiv0$ on $\Omega\setminus\{a\}$ then $f=f(a)$ on the nonempty open set $\Omega\setminus\{a\}$, hence $f$ is constant on the region $\Omega$ by the identity theorem, contradicting the hypothesis that $f$ is not constant.
:::

:::

::: {.pf-step}
$f$ is one-to-one.

::: pf-proof
For arbitrary distinct $a,b\in\Omega$, steps [](#hurwitz){.pf-ref} and [](#nonconstant){.pf-ref} put $g$ in the second alternative, so $0\ne g(b)=f(b)-f(a)$; that is $f(a)\ne f(b)$.
:::

:::

:::
:::
