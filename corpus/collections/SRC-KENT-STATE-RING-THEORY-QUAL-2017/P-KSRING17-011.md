---
schema: qual/card@1
id: P-KSRING17-011
kind: problem
title: Boolean rings have characteristic 2 and are commutative
classification:
  areas: [algebra]
  topics:
  - Boolean Rings
  - Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 11 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that a non-zero ring $R$ in which $x^{2} = x$ for all $x \in R$ is of characteristic $2$ and is commutative.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\in R$,
$$
x=-x.
$$


::: pf-proof

The hypothesis applied to $x$ gives
$$
x^2=x.
$$
Applied to $-x$, it gives
$$
(-x)^2=-x.
$$
But
$$
(-x)^2=x^2=x.
$$
Therefore
$$
x=-x.
$$

:::

:::

::: {.pf-step #s1-2}

For every $x\in R$,
$$
2x=0.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives
$$
x=-x.
$$
Adding $x$ to both sides yields
$$
x+x=0.
$$
Thus
$$
2x=0
$$
for every $x\in R$.

:::

:::

::: {.pf-step #s1-3}

The ring $R$ has characteristic $2$.


::: pf-proof

Step [](#s1-2){.pf-ref} shows that
$$
2\cdot1_R=0.
$$
Hence the characteristic divides $2$. Since $R$ is nonzero,
$$
1_R\ne0,
$$
so the characteristic is not $1$. Therefore
$$
\boxed{\operatorname{char}R=2.}
$$

:::

:::

::: {.pf-step #s1-4}

For all $x,y\in R$,
$$
xy+yx=0.
$$


::: pf-proof

Apply the hypothesis to $x+y$:
$$
(x+y)^2=x+y.
$$
Expanding,
$$
x^2+xy+yx+y^2=x+y.
$$
Since
$$
x^2=x
\qquad\text{and}\qquad
y^2=y,
$$
subtraction gives
$$
xy+yx=0.
$$

:::

:::

::: {.pf-step #s1-5}

The ring $R$ is commutative.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
xy=-yx.
$$
But by step [](#s1-3){.pf-ref} the ring has characteristic $2$, so
$$
-yx=yx.
$$
Therefore
$$
xy=yx
$$
for all $x,y\in R$. Hence
$$
\boxed{R\text{ is commutative}.}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the characteristic assertion, and step [](#s1-5){.pf-ref} proves commutativity.

:::

:::

:::
