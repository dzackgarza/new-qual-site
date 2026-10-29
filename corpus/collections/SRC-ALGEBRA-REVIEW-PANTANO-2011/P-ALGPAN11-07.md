---
schema: qual/card@1
id: P-ALGPAN11-07
kind: problem
title: Properties of the operation a star b equals ab plus a plus b
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
Let $*$ be the binary operation on the rational numbers given by $a*b=ab+a+b$.
Decide which of the following assertions are true: (I) $*$ is commutative; (II) there is a rational $*$-identity; (III) every rational number has a $*$-inverse.

![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-07.png)
:::

::: {.solution}
Assertions I and II are true, while III is false.

::: pf

::: {.pf-step #s1}

The operation is commutative.

::: pf-proof

Since multiplication and addition in $\QQ$ are commutative,
$$
a*b=ab+a+b=ba+b+a=b*a.
$$

:::

:::

::: {.pf-step #s2}

The $*$-identity is $0$.

::: pf-proof

For every $a\in\QQ$,
$$
a*0=a\cdot0+a+0=a,
$$
and by commutativity also $0*a=a$.

:::

:::

::: {.pf-step #s3}

Not every rational has a $*$-inverse.

::: pf-proof

The identity
$$
a*b=0
$$
is equivalent to
$$
(a+1)(b+1)=1.
$$
For $a\ne-1$ this gives $b=(a+1)^{-1}-1$, but for $a=-1$ one has
$$
(-1)*b=-1
$$
for every $b$.
Thus $-1$ has no inverse.

:::

:::

::: pf-step

Hence exactly I and II hold.

::: pf-proof

Step [](#s1){.pf-ref} proves I, step [](#s2){.pf-ref} proves II, and step [](#s3){.pf-ref} disproves III.

:::

:::

::: pf-qed

The preceding conclusion gives the requested truth values.

:::

:::

:::
