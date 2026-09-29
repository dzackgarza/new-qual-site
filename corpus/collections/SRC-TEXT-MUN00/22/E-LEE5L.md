---
schema: qual/card@1
id: E-LEE5L
kind: problem
title: A quotient map that is neither open nor closed
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $\pi_1: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ be projection on the first coordinate.
Let $A$ be the subspace of $\mathbb{R} \times \mathbb{R}$ consisting of all points $x \times y$ for which either $x \geq 0$ or $y = 0$ (or both); let $q: A \to \mathbb{R}$ be obtained by restricting $\pi_1$.
Show that $q$ is a quotient map that is neither open nor closed.
:::

::: {.solution}
::: pf

::: {.pf-step #q-continuous-surjective}
$q$ is continuous and surjective.

::: pf-proof
$q$ is the restriction of the continuous projection $\pi_1$, and $q(x,0)=x$ with $(x,0)\in A$ for every $x\in\mathbb R$.
:::

:::

::: {.pf-step #q-quotient-map}
$q$ is a quotient map.

::: pf-proof
By step [](#q-continuous-surjective){.pf-ref} it suffices to show that $U\subseteq\mathbb R$ is open whenever $q^{-1}(U)$ is open in $A$.
Let $x_0\in U$.
Then $(x_0,0)\in q^{-1}(U)$, so there is an open box $B=(a,b)\times(-\varepsilon,\varepsilon)$ containing $(x_0,0)$ with $B\cap A\subseteq q^{-1}(U)$.
For $t\in(a,b)$, the point $(t,0)$ lies in $B\cap A$, so $t=q(t,0)\in U$.
Hence $x_0\in(a,b)\subseteq U$.
:::

:::

::: {.pf-step #q-not-open}
$q$ is not open.

::: pf-proof
The set $[0,\infty)\times(0,\infty)=A\cap(\mathbb R\times(0,\infty))$ is open in $A$, and its image $[0,\infty)$ is not open in $\mathbb R$.
:::

:::

::: {.pf-step #q-not-closed}
$q$ is not closed.

::: pf-proof
The set $C=\{(x,y):x>0,\ xy=1\}$ equals $\{(x,y):x\ge0,\ xy=1\}$, which is closed in $\mathbb R^2$; it lies in $A$, so it is closed in $A$.
Its image $q(C)=(0,\infty)$ is not closed in $\mathbb R$, since $0$ is a limit point of it.
:::

:::

::: pf-qed
Steps [](#q-quotient-map){.pf-ref}, [](#q-not-open){.pf-ref}, and [](#q-not-closed){.pf-ref}.
:::

:::

:::
