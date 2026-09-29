---
schema: qual/card@1
id: P-BKS01-3
kind: problem
title: Local rings with trivial unit group
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    In a local ring, 1+x is a unit for every x in the maximal ideal.
    A trivial unit group therefore forces the maximal ideal to be zero,
    so the ring is a field. Its multiplicative group has one element,
    hence the field is F_2.
---

::: {.problem}
Find all commutative rings $R$ with identity such that $R$ has a unique maximal ideal and its group of units is trivial.
:::

::: {.solution}
Let $\mathfrak m$ be the unique maximal ideal of $R$.

::: pf

::: {.pf-step #s1}

For every $x\in\mathfrak m$, the element $1+x$ is a unit.

::: pf-proof

In a commutative ring with a unique maximal ideal, every nonunit lies in
that maximal ideal. If $1+x$ were not a unit, then
$$
1+x\in\mathfrak m.
$$
Since also $x\in\mathfrak m$, subtraction would give
$$
1=(1+x)-x\in\mathfrak m,
$$
contradicting that a maximal ideal is proper. Hence $1+x$ is a unit.

:::

:::

::: pf-step

The maximal ideal is zero:
$$
\mathfrak m=0.
$$

::: pf-proof

The unit group is trivial, so its only element is $1$. By step [](#s1){.pf-ref},
for every $x\in\mathfrak m$,
$$
1+x=1.
$$
Thus $x=0$, proving the claim.

:::

:::

::: {.pf-step #s3}

The ring $R$ is a field with exactly two elements.

::: pf-proof

Since the unique maximal ideal is $0$, every nonzero element lies
outside the maximal ideal and is therefore a unit. Hence $R$ is a
field. Its group of units is
$$
R^\times=R\sm\{0\},
$$
and by hypothesis this group has the single element $1$. Therefore
$$
R=\{0,1\},
$$
so $R\cong\FF_2$.

:::

:::

::: {.pf-step #s4}

The ring $\FF_2$ satisfies the hypotheses.

::: pf-proof

Its unique maximal ideal is $(0)$, and its only unit is $1$.

:::

:::

::: {.pf-step #s5}

Therefore the complete answer is
$$
\boxed{R\cong\FF_2}.
$$

::: pf-proof

Step [](#s3){.pf-ref} proves necessity, and step [](#s4){.pf-ref} proves sufficiency.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required classification.

:::

:::

:::
