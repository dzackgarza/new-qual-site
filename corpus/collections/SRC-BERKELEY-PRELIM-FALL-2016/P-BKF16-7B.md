---
schema: qual/card@1
id: P-BKF16-7B
kind: problem
title: An injective nonsurjective map and a surjective noninjective map summing to the identity
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: the space
    of real sequences converging to zero is stable under the difference and
    left-shift maps, whose sum is the identity.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked invariance of c_0, injectivity and nonsurjectivity of the
    difference map, surjectivity and noninjectivity of the shift, and the
    harmonic-series obstruction used for nonsurjectivity.
---

::: {.problem}
Find an example of a vector space V over the real numbers R and two linear maps $f , g : V \to V$ such that $f$ is injective but not surjective and g is surjective but not injective and such that $f + g$ is equal to the identity map $1 _ { V }$

Hint: construct V as a subspace of the space of sequences of real numbers, closed under the linear maps

$$
f ( a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . ) = ( a _ { 1 } - a _ { 2 } , a _ { 2 } - a _ { 3 } , . . . )
$$

and

$$
g ( a _ { 1 } , a _ { 2 } , a _ { 3 } , . . . ) = ( a _ { 2 } , a _ { 3 } , . . . ) .
$$
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
V
\coloneqq
\left\{
(a_1,a_2,\ldots)\in\mathbb R^{\mathbb N}
:
a_n\to0
\right\}.
$$
Define
$$
f(a_1,a_2,\ldots)
\coloneqq
(a_1-a_2,a_2-a_3,\ldots)
$$
and
$$
g(a_1,a_2,\ldots)
\coloneqq
(a_2,a_3,\ldots).
$$
Then $V$ is a real vector space and both $f$ and $g$ are linear
endomorphisms of $V$.

::: pf-proof

The space $V$ is closed under coordinatewise addition and scalar
multiplication. If $a_n\to0$, then also
$$
a_{n+1}\to0
$$
and
$$
a_n-a_{n+1}\to0.
$$
Hence both displayed formulas map $V$ into itself. Their coordinate
formulas are linear.

:::

:::

::: {.pf-step #s2}

One has
$$
\boxed{f+g=1_V}.
$$

::: pf-proof

For every
$$
a=(a_1,a_2,\ldots)\in V,
$$
the $n$th coordinate of $(f+g)(a)$ is
$$
(a_n-a_{n+1})+a_{n+1}=a_n.
$$
Thus $(f+g)(a)=a$ for every $a\in V$.

:::

:::

::: {.pf-step #s3}

The map $g$ is surjective.

::: pf-proof

Given
$$
b=(b_1,b_2,\ldots)\in V,
$$
put
$$
a=(0,b_1,b_2,\ldots).
$$
Since $b_n\to0$, also $a\in V$, and by construction
$$
g(a)=b.
$$

:::

:::

::: {.pf-step #s4}

The map $g$ is not injective.

::: pf-proof

The nonzero vector
$$
e_1=(1,0,0,\ldots)\in V
$$
satisfies
$$
g(e_1)=0.
$$
Hence $\ker g\ne0$.

:::

:::

::: {.pf-step #s5}

The map $f$ is injective.

::: pf-proof

Suppose
$$
f(a_1,a_2,\ldots)=0.
$$
Then
$$
a_n-a_{n+1}=0
$$
for every $n$, so the sequence is constant:
$$
a_1=a_2=\cdots.
$$
Because it belongs to $V$, its terms converge to $0$. Therefore every
term is $0$, and
$$
\ker f=0.
$$

:::

:::

::: {.pf-step #s6}

The map $f$ is not surjective.

::: pf-proof

The sequence
$$
b
\coloneqq
\left(-1,-\frac12,-\frac13,\ldots\right)
$$
belongs to $V$. Suppose for contradiction that
$$
f(a)=b
$$
for some
$$
a=(a_1,a_2,\ldots)\in V.
$$
Then for every $n\ge1$,
$$
a_n-a_{n+1}
=
-\frac1n,
$$
so
$$
a_{n+1}
=
a_n+\frac1n.
$$
Induction gives
$$
a_n
=
a_1+\sum_{j=1}^{n-1}\frac1j.
$$
The harmonic partial sums diverge to $+\infty$, so the right-hand side
cannot converge to $0$. This contradicts $a\in V$. Thus $b$ is not in
the image of $f$.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that $g$ is surjective but not injective. Steps
[](#s5){.pf-ref} and [](#s6){.pf-ref} show that $f$ is injective but not surjective. Step [](#s2){.pf-ref}
gives $f+g=1_V$, so the construction satisfies all requirements.

:::

:::

:::
