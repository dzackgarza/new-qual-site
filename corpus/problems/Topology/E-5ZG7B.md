---
schema: qual/card@1
id: E-5ZG7B
kind: problem
title: $\RR/\QQ$ has the indiscrete topology
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Point-Set Topology
relations: []
review: draft
---

::: {.problem}
Show that $\RR/\QQ$ has the indiscrete topology.
:::

::: {.solution}
Let $\pi:\RR\to\RR/\QQ$ be the quotient map, and let $U\subseteq\RR/\QQ$ be a nonempty open set. We show $U=\RR/\QQ$.

::: pf

::: {.pf-step #saturated}

$V\coloneqq\inverseof{\pi}(U)$ is a nonempty open subset of $\RR$ with $V+q=V$ for every $q\in\QQ$.

::: pf-proof

$V$ is open because $\pi$ is continuous, and nonempty because $\pi$ is surjective. If $y\in V$ and $q\in\QQ$, then $\pi(y+q)=\pi(y)\in U$, so $y+q\in V$.

:::

:::

::: {.pf-step #all}

$V=\RR$.

::: pf-proof

By step [](#saturated){.pf-ref}, $V$ contains an interval $(a,b)$ with $a<b$, and hence every translate $(a+q,b+q)$ with $q\in\QQ$. Given $x\in\RR$, density of $\QQ$ gives $q\in\QQ$ with $x-b<q<x-a$, so $x\in(a+q,b+q)\subseteq V$.

:::

:::

::: pf-qed

By step [](#all){.pf-ref} and surjectivity of $\pi$, $U=\pi(V)=\RR/\QQ$. So the only open sets of $\RR/\QQ$ are $\varnothing$ and $\RR/\QQ$.

:::

:::

:::
