---
schema: qual/card@1
id: P-ALGPAN11-05
kind: problem
title: Proper subgroup of $\ZZ$ containing three of $p$, $p+q$, $pq$, $p^q$, $q^p$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-05.png)
:::

::: {.solution}
The answer is $\boxed{\text{(E)}\;p,\ pq,\ p^q}$.

::: pf

::: pf-step

$J=p\mathbb Z$ is a proper subgroup of $\mathbb Z$ that contains $p$, $pq$, and $p^q$.

::: pf-proof

It is proper because $p>1$.
It contains $p$, $pq$, and $p^q$.

:::

:::

::: pf-step

The other two listed elements are not in $J$.

::: pf-proof

Because $p$ and $q$ are distinct primes, $p\nmid q$, hence $p\nmid q^p$.
Also
\[
p\mid(p+q)\iff p\mid q,
\]
which is false.
Therefore among
\[
\{p,p+q,pq,p^q,q^p\}
\]
exactly $p,pq,p^q$ lie in $J$.

:::

:::

:::

:::
