---
schema: qual/card@1
id: P-CAFA16G
kind: problem
title: "Analytic continuation of the logarithm along a path is always a branch of the logarithm"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The source
      is a course examination, so there is no retained solution set behind the card and the problem
      statement is the source. Each step re-read: the initial germ satisfies e^{f_0} = z; along a
      link of the continuation chain the two functions agree on a nonempty open set inside the
      connected domain, so the identity theorem extends e^{f_t} = z to the whole domain; and the
      chain has finitely many links, so the identity propagates to every t. The card states the chain
      formulation it uses, since the phrase analytic continuation along a path presupposes one. Not
      claimed: anything about the monodromy of the logarithm around a loop, which is the reason the
      continuation depends on the path for paths that wind.
---

::: {.problem}
Let $\gamma: [0, 1] \to \CC$ be a path such that $\gamma(0) = 1$ and $\gamma(t) \neq 0$ for every $t \in [0, 1]$.
Assume that $(f_t, D_t)_{0 \leq t \leq 1}$ is an analytic continuation of $f_0(z) = \log z$ along $\gamma$.
Prove that $f_t$ is a branch of the logarithm for every $t \in [0, 1]$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #start}
$e^{f_{0}(z)}=z$ for $z$ in the initial domain.

::: pf-proof
$f_{0}(z)=\log z$ is a branch of the logarithm on its domain, so exponentiation inverts it there.
:::

:::

::: {.pf-step #overlap}
If $e^{f_{s}(z)}=z$ on $D_{s}$ and $f_{s}=f_{t}$ on a nonempty open subset of $D_{s}\cap D_{t}$, then $e^{f_{t}(z)}=z$ on all of $D_{t}$.

:::: pf-proof

::: {.pf-step #onsubset}
$e^{f_{t}(z)}=z$ on that open subset.

::: pf-proof
There $f_{t}=f_{s}$, so $e^{f_{t}}=e^{f_{s}}=z$ by the hypothesis of the step.
:::

:::

::: {.pf-step #identity}
$e^{f_{t}(z)}=z$ on $D_{t}$.

::: pf-proof
Both $e^{f_{t}}$ and the identity function are holomorphic on the domain $D_{t}$, which is connected and open, and they agree on a nonempty open subset; by the identity theorem they agree everywhere on $D_{t}$.
:::

:::

:::

:::

::: {.pf-step #propagate}
$e^{f_{t}(z)}=z$ for every $t\in[0,1]$ and every $z\in D_{t}$.

::: pf-proof
An analytic continuation along a path is given by a chain of function elements: a partition $0=t_{0}<t_{1}<\dots<t_{n}=1$, domains $D_{i}$ with $\gamma([t_{i},t_{i+1}])\subseteq D_{i}$, and functions $f_{i}$ holomorphic on $D_{i}$ with $f_{i}=f_{i+1}$ on a nonempty open subset of $D_{i}\cap D_{i+1}$. Starting from step [](#start){.pf-ref} and applying step [](#overlap){.pf-ref} once for each link of the chain gives the identity on each $D_{i}$, hence at every $t$ of the subdivision, and for $t$ between subdivision points the element is the one carried by the corresponding $D_{i}$.
:::

:::

::: {.pf-step #branch}
Each $f_{t}$ is a branch of the logarithm.

::: pf-proof
Step [](#propagate){.pf-ref} gives $e^{f_{t}(z)}=z$ for $z\in D_{t}$, and $f_{t}$ is holomorphic on the domain $D_{t}$ by definition of an analytic continuation. A holomorphic function on a domain whose exponential is the identity there is a branch of the logarithm, so
$$
\boxed{e^{f_{t}(z)}=z\text{ on }D_{t}\text{ for every }t\in[0,1].}
$$
In particular $0\notin D_{t}$ for every $t$, since $z=e^{f_{t}(z)}$ is never zero.
:::

:::

:::
:::
