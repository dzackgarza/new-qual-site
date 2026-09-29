---
schema: qual/card@1
id: P-BKF15-3B
kind: problem
title: A plane section of the unit ball of $C[0,1]$ that is a circular disk
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
    Independently checked the retained Fall 2015 solution packet: the plane
    spanned by cos(2 pi t) and sin(2 pi t) has sup norm equal to the
    Euclidean norm of its coefficient pair.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked linear independence, the exact supremum over one full period,
    and identification of the section with the closed Euclidean unit disk.
---

::: {.problem}
The unit cube in the space $C [ 0 , 1 ]$ of continuous real-valued functions on the interval is defined as the subset

$$
\{ f \in C [ 0 , 1 ] \mid \| f \| : = \operatorname* { s u p } _ { 0 \leq t \leq 1 } | f ( t ) | \leq 1 \} .
$$

Prove that there exists a 2-dimensional linear subspace in $C [ 0 , 1 ]$ whose intersection with the unit cube is a circular disk.
:::

::: {.solution}
Let
$$
u(t)\coloneqq\cos(2\pi t),
\qquad
v(t)\coloneqq\sin(2\pi t),
$$
and let
$$
W\coloneqq\operatorname{span}_{\RR}\{u,v\}.
$$

::: pf

::: {.pf-step #s1}

The subspace $W$ has dimension $2$.

::: pf-proof

Suppose
$$
au+bv=0
$$
as a function on $[0,1]$. Evaluating at $t=0$ gives
$$
a=0.
$$
Then evaluating at $t=1/4$ gives
$$
b=0.
$$
Thus $u$ and $v$ are linearly independent.

:::

:::

::: {.pf-step #s2}

For every $a,b\in\RR$,
$$
\left\|
a\cos(2\pi t)+b\sin(2\pi t)
\right\|_\infty
=
\sqrt{a^2+b^2}.
$$

::: pf-proof

Put
$$
R\coloneqq\sqrt{a^2+b^2}.
$$
If $R=0$, the identity is immediate. Suppose $R>0$. Choose
$\phi\in\RR$ such that
$$
\cos\phi=\frac aR,
\qquad
\sin\phi=\frac bR.
$$
Then
$$
a\cos(2\pi t)+b\sin(2\pi t)
=
R\cos(2\pi t-\phi).
$$
Therefore the absolute value is at most $R$ for every $t$. Since
$2\pi t$ runs through a complete interval of length $2\pi$ as
$t$ runs from $0$ to $1$, there is some $t$ for which
$$
\cos(2\pi t-\phi)=\pm1.
$$
Hence the supremum of the absolute value is exactly $R$.

:::

:::

::: {.pf-step #s3}

The intersection of $W$ with the unit cube is
$$
\left\{
au+bv:
a^2+b^2\le1
\right\}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\|au+bv\|_\infty\le1
\iff
\sqrt{a^2+b^2}\le1
\iff
a^2+b^2\le1.
$$

:::

:::

::: {.pf-step #s4}

Under the linear coordinates
$$
\RR^2\longrightarrow W,
\qquad
(a,b)\longmapsto au+bv,
$$
the section in step [](#s3){.pf-ref} is the closed Euclidean unit disk.

::: pf-proof

Step [](#s1){.pf-ref} makes the displayed map a linear isomorphism, and step [](#s3){.pf-ref}
identifies the section with
$$
\{(a,b)\in\RR^2:a^2+b^2\le1\},
$$
which is the closed circular unit disk.

:::

:::

::: {.pf-step #s5}

Therefore there exists a $2$-dimensional linear subspace of
$C[0,1]$ whose intersection with the unit cube is a circular disk.

::: pf-proof

The subspace $W$ has dimension $2$ by step [](#s1){.pf-ref} and
has the required section by step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required existence statement.

:::

:::

:::
