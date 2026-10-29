---
schema: qual/card@1
id: P-VN6VF
kind: problem
title: Example of a UFD that is not a Euclidean domain
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Factorization
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Give an example of a UFD that is not a Euclidean domain.
:::

::: {.solution}
Let $k$ be a field. We show that $k[x,y]$ is a $\boxed{\text{UFD that is not Euclidean}}$.

::: pf

::: pf-step

$k[x,y]$ is a UFD.

::: pf-proof

$k[x]$ is a PID and hence a UFD. By Gauss's lemma, a polynomial ring over a UFD is again a UFD, so $k[x,y]=k[x][y]$ is a UFD.

:::

:::

::: {.pf-step #notpid}

The ideal $(x,y)$ of $k[x,y]$ is not principal.

::: pf-proof

If $(x,y)=(f)$, then $f$ divides both $x$ and $y$. Since $x$ and $y$ are non-associate irreducibles, they have no common nonunit divisor, so $f$ is a unit and $(x,y)=k[x,y]$. This contradicts $1\notin(x,y)$, since every element of $(x,y)$ has zero constant term.

:::

:::

::: pf-qed

Every Euclidean domain is a PID, and by step [](#notpid){.pf-ref} $k[x,y]$ is not a PID.

:::

:::

:::
