---
schema: qual/card@1
id: P-HCAO5
kind: problem
title: A root over an extension gives a linear factor
classification:
  areas:
  - algebra
  topics:
  - Polynomial Roots
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $F$ be a field, let $E/F$ be a field extension, and let $p(x) \in F[x]$.
If $a \in E$ and $p(a)=0$, show that
\[
p(x)=(x-a)q(x)
\]
for some $q(x) \in E[x]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There are $q(x)\in E[x]$ and $c\in E$ with $p(x)=(x-a)q(x)+c$.

::: pf-proof

Since $F\subseteq E$, we have $p(x)\in F[x]\subseteq E[x]$. The polynomial
$x-a\in E[x]$ is monic of degree $1$, so division with remainder in $E[x]$
gives $p(x)=(x-a)q(x)+r(x)$ with $r=0$ or $\deg r<1$; in either case $r$ is a
constant $c\in E$.

:::

:::

::: {.pf-step #s2}

$c=0$.

::: pf-proof

Applying the evaluation homomorphism $E[x]\to E$, $x\mapsto a$, to step
[](#s1){.pf-ref} gives $0=p(a)=(a-a)q(a)+c=c$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $p(x)=(x-a)q(x)$ with $q(x)\in E[x]$.

:::

:::

:::
