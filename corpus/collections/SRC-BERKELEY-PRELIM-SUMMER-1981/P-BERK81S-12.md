---
schema: qual/card@1
id: P-BERK81S-12
kind: problem
title: No unital commutative ring has additive group $\mathbb Q/\mathbb Z$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The identity element would have finite additive order n because every
    element of Q/Z is torsion. Then n annihilates every ring element via
    nr=(n1_R)r=0, so the whole additive group would have exponent dividing
    n. But Q/Z contains an element of order n+1.
---

::: {.problem}
Show that no commutative ring with identity has additive group isomorphic to $\mathbb Q/\mathbb Z$.
:::

::: {.solution}
<1>1. Every element of the additive group $\QQ/\ZZ$ has finite order.

::: {.proof}
Let
$$
\frac ab+\ZZ
\in
\QQ/\ZZ,
$$
where $a\in\ZZ$ and $b\in\NN$ with $b>0$. Then
$$
b
\left(
\frac ab+\ZZ
\right)
=
a+\ZZ
=
0.
$$
Thus every element of $\QQ/\ZZ$ is torsion.
:::

<1>2. Suppose, toward a contradiction, that $R$ is a ring with identity
$1_R$ whose additive group is isomorphic to $\QQ/\ZZ$. Then there is an
integer $n\geq1$ such that
$$
n1_R=0.
$$

::: {.proof}
Under an additive-group isomorphism
$$
(R,+)\cong\QQ/\ZZ,
$$
the element $1_R$ corresponds to an element of $\QQ/\ZZ$. By step <1>1,
that element has finite additive order. Hence some positive integer $n$
satisfies the displayed equality.
:::

<1>3. Every element of $R$ is annihilated additively by $n$:
$$
nr=0
$$
for every $r\in R$.

::: {.proof}
For any $r\in R$, distributivity and the identity property give
$$
\begin{aligned}
nr
&=
(n1_R)r\\
&=
0r\\
&=
0.
\end{aligned}
$$
:::

<1>4. The additive group $\QQ/\ZZ$ is not annihilated by any positive
integer.

::: {.proof}
Fix $n\geq1$. Consider
$$
\frac1{n+1}+\ZZ
\in
\QQ/\ZZ.
$$
Its additive order is exactly $n+1$: multiplying by $n+1$ gives $0$, while
for $1\leq k<n+1$,
$$
\frac{k}{n+1}\notin\ZZ.
$$
In particular,
$$
n
\left(
\frac1{n+1}+\ZZ
\right)
\neq
0.
$$
Thus multiplication by $n$ does not annihilate all of $\QQ/\ZZ$.
:::

<1>5. No ring with identity can have additive group isomorphic to
$\QQ/\ZZ$.

::: {.proof}
Step <1>3 says that, under the supposition in step <1>2, multiplication by
$n$ annihilates the entire additive group of $R$. An additive-group
isomorphism would then imply that multiplication by $n$ annihilates
$\QQ/\ZZ$, contradicting step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the required nonexistence statement. In particular, no
commutative ring with identity has the stated additive group.
:::
:::
