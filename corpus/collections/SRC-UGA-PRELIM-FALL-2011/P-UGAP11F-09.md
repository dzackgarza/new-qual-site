---
schema: qual/card@1
id: P-UGAP11F-09
kind: problem
title: Basis of the quotient of $\RR^3$ by equality of coordinate sums
classification:
  areas: [prelim]
  topics:
  - Vector Spaces
  - Bases
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Define an equivalence relation on $\RR^3$ by
$$
(x,y,z)\sim(x',y',z')
\quad\Longleftrightarrow\quad
x+y+z=x'+y'+z'.
$$
Find a basis for the vector space
$$
V=\RR^3/\!\sim
$$
and prove that it is a basis.
:::

::: {.solution}

Let
$$
\sigma:\RR^3\longrightarrow\RR,
\qquad
\sigma(x,y,z)=x+y+z.
$$

::: pf

::: {.pf-step #s1-1}

Two vectors are equivalent exactly when their difference lies in
$$
\ker\sigma.
$$


::: pf-proof

By definition,
$$
(x,y,z)\sim(x',y',z')
$$
if and only if
$$
x+y+z=x'+y'+z'.
$$
This is equivalent to
$$
\sigma\bigl((x,y,z)-(x',y',z')\bigr)=0,
$$
i.e. the difference lies in
$$
\ker\sigma.
$$
Thus the equivalence classes are precisely the cosets of
$$
\ker\sigma.
$$

:::

:::

::: pf-step

The quotient vector space $V$ is naturally isomorphic to $\RR$.


::: pf-proof

The map $\sigma$ is linear and surjective, since
$$
\sigma(t,0,0)=t
$$
for every $t\in\RR$.

By step [](#s1-1){.pf-ref},
$$
V
\cong
\RR^3/\ker\sigma.
$$
The first isomorphism theorem therefore gives
$$
V
\cong
\operatorname{im}\sigma
=
\RR.
$$

:::

:::

::: {.pf-step #s1-3}

Let
$$
e_1=(1,0,0).
$$
Then
$$
\boxed{\{[e_1]\}}
$$
spans $V$.


::: pf-proof

Take any class
$$
[(x,y,z)]\in V
$$
and set
$$
s=x+y+z.
$$
The vector
$$
se_1=(s,0,0)
$$
has coordinate sum $s$, the same as $(x,y,z)$. Hence
$$
(x,y,z)\sim se_1.
$$
Therefore
$$
[(x,y,z)]
=
[se_1]
=
s[e_1].
$$
So every vector in $V$ is a scalar multiple of $[e_1]$.

:::

:::

::: {.pf-step #s1-4}

The vector $[e_1]$ is nonzero and hence linearly independent.


::: pf-proof

If
$$
c[e_1]=0
$$
in $V$, then
$$
[ce_1]=[(0,0,0)].
$$
By the definition of the equivalence relation, the coordinate sums must agree:
$$
c=0.
$$
Thus the only scalar relation on $[e_1]$ is the trivial one.

:::

:::

::: {.pf-step #s1-5}

Consequently,
$$
\boxed{
\{[(1,0,0)]\}
}
$$
is a basis of $V$.


::: pf-proof

Step [](#s1-3){.pf-ref} proves spanning and step [](#s1-4){.pf-ref} proves linear independence.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested basis and proof.

:::

:::

:::
