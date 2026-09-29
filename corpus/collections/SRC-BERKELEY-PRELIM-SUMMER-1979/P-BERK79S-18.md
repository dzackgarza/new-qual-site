---
schema: qual/card@1
id: P-BERK79S-18
kind: problem
title: Linear independence of $x,Tx,T^2x$ when $T^3x=Tx+x$ over $\QQ$
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
    The relations give (T^3-T-I)x=0. The polynomial p(t)=t^3-t-1 is
    irreducible over Q because a reducible cubic over Q has a rational root,
    while the only possible rational roots ±1 are not roots. Any linear
    dependence among x,Tx,T^2x would give a nonzero polynomial q of degree
    at most two with q(T)x=0. Coprimality of p and q then gives a Bezout
    identity forcing x=0, contradicting the hypothesis.
---

::: {.problem}
Let $E$ be a three-dimensional vector space over $\mathbb Q$.
Suppose $T:E\to E$ is linear and
\[
Tx=y,
\qquad
Ty=z,
\qquad
Tz=x+y
\]
for some $x,y,z\in E$ with $x\ne0$.
Prove that $x,y,z$ are linearly independent.
:::

::: {.solution}
Define
$$
p(t)=t^3-t-1\in\QQ[t].
$$

::: pf

::: {.pf-step #s1}

The vector $x$ satisfies
$$
p(T)x=0.
$$

::: pf-proof

Using the given relations,
$$
\begin{aligned}
T^3x
&=
T(T^2x)\\
&=
Tz\\
&=
x+y\\
&=
x+Tx.
\end{aligned}
$$
Hence
$$
(T^3-T-I)x=0,
$$
which is exactly $p(T)x=0$.

:::

:::

::: {.pf-step #s2}

The polynomial
$$
p(t)=t^3-t-1
$$
is irreducible over $\QQ$.

::: pf-proof

A reducible cubic over a field has a linear factor and therefore a root in
that field. By the rational root theorem, any rational root of the monic
integer polynomial $p$ must be an integer divisor of $1$, hence must be
$1$ or $-1$. But
$$
p(1)=-1
\qquad\text{and}\qquad
p(-1)=-1.
$$
Thus $p$ has no rational root and is irreducible over $\QQ$.

:::

:::

::: {.pf-step #s3}

Suppose, toward a contradiction, that $x,y,z$ are linearly
dependent. Then there is a nonzero polynomial
$$
q(t)=a+bt+ct^2\in\QQ[t]
$$
of degree at most $2$ such that
$$
q(T)x=0.
$$

::: pf-proof

Linear dependence gives rational numbers $a,b,c$, not all zero, with
$$
ax+by+cz=0.
$$
Since
$$
y=Tx
\qquad\text{and}\qquad
z=T^2x,
$$
this relation becomes
$$
(aI+bT+cT^2)x=0.
$$
This is $q(T)x=0$ for the displayed nonzero polynomial $q$.

:::

:::

::: {.pf-step #s4}

The polynomials $p$ and $q$ from steps [](#s2){.pf-ref} and [](#s3){.pf-ref} are relatively
prime in $\QQ[t]$.

::: pf-proof

The polynomial $p$ is irreducible of degree $3$ by step [](#s2){.pf-ref}, while
$q\neq0$ has degree at most $2$. Thus $p$ cannot divide $q$. Since every
nonunit divisor of the irreducible polynomial $p$ is associated to $p$
itself, the greatest common divisor of $p$ and $q$ is $1$ up to a unit.

:::

:::

::: {.pf-step #s5}

There are polynomials $r,s\in\QQ[t]$ such that
$$
r(t)p(t)+s(t)q(t)=1.
$$

::: pf-proof

The polynomial ring $\QQ[t]$ is a Euclidean domain. By Bezout's identity
and step [](#s4){.pf-ref}, relatively prime polynomials $p$ and $q$ admit the displayed
linear combination.

:::

:::

::: {.pf-step #s6}

The dependence assumption in step [](#s3){.pf-ref} forces
$$
x=0.
$$

::: pf-proof

Substitute the operator $T$ into the identity from step [](#s5){.pf-ref} and apply it
to $x$:
$$
\begin{aligned}
x
&=
\bigl(r(T)p(T)+s(T)q(T)\bigr)x\\
&=
r(T)p(T)x+s(T)q(T)x.
\end{aligned}
$$
Step [](#s1){.pf-ref} gives $p(T)x=0$, and step [](#s3){.pf-ref} gives $q(T)x=0$. Therefore the
right-hand side is zero, so $x=0$.

:::

:::

::: {.pf-step #s7}

The vectors $x,y,z$ are linearly independent:
$$
\boxed{
x,\ y,\ z\text{ are linearly independent over }\QQ.
}
$$

::: pf-proof

Step [](#s6){.pf-ref} contradicts the hypothesis $x\neq0$. Hence the dependence
assumption in step [](#s3){.pf-ref} is false.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::
