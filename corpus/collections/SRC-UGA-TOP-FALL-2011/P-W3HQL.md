---
schema: qual/card@1
id: P-W3HQL
kind: problem
title: The genera $g$ for which there is a covering $\Sigma_5\to\Sigma_g$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
For any natural number $g$ let $\Sigma_g$ denote the (compact, orientable) surface of genus $g$.

Determine, with proof, all valued of $g$ with the property that there exists a covering space $\pi : \Sigma_5 \to \Sigma_g$ .

> Hint: How does the Euler characteristic behave for covering spaces?
:::

::: {.solution}
<1>1. If $\Sigma_5\to\Sigma_g$ is $d$-sheeted, $\chi(\Sigma_5)=d\chi(\Sigma_g)$.
Proof: covering.

<1>2. $\chi(\Sigma_g)=2-2g$, so $-8=d(2-2g)$.
Proof: <1>1.

<1>3. Hence $d=4/(g-1)$.
Proof: <1>2.

<1>4. $d$ integer $\ge1$, so $g-1\mid4$, so $g=2,3,5$.
Proof: divisors of $4$ are $1,2,4$.

<1>5. Each occurs ($g=5,d=1$ identity; $g=3,d=2$; $g=2,d=4$ via covering constructions).
Proof: existence.

<1>6. Q.E.D.
Proof: <1>4.
:::
