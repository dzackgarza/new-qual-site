---
schema: qual/card@1
id: P-AZOFF-I01
kind: problem
title: Analytic self-maps of the disk with unimodular boundary values are finite Blaschke products
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Schwarz lemma and reflection principle, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Boundary modulus one and continuity force all zeros into a compact
    subdisk, hence there are finitely many. Dividing by the finite Blaschke
    product with those zeros gives a zero-free analytic function with
    boundary modulus one; applying the maximum modulus principle to it and
    its reciprocal makes it a unimodular constant. The three requested
    conclusions follow from this factorization.
---

::: {.problem}
[Fall 2012, Problem $\# 7 ]$ Write $\mathbb { D } : = \{ z \in \mathbb { C } : | z | < 1 \}$ for the open unit disk.
Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic, and admits a continuous extension $\widetilde { f } : \overline { { \mathbb { D } } } \to \overline { { \mathbb { D } } }$ such that $| f ( z ) | = 1$ whenever $| z | = 1$ .

a) Prove that $f$ is a rational function.

b) Suppose that $z = 0$ is the unique zero of $f$. Prove that $f(z) = \lambda z^n$ for some $\lambda \in \mathbb { C }$ of absolute value 1 and some natural number $n$ .

c) More generally, suppose that $a _ { 1 } , \dots , a _ { n } \in \mathbb { D }$ are the zeros of $f$, listed with multiplicity.
Prove that

$$
f ( z ) = \lambda \prod _ { j = 1 } ^ { n } { \frac { z - a _ { j } } { 1 - { \overline { { a } } } _ { j } z } } , \quad | \lambda | = 1 .
$$
:::

::: {.solution}
Let
$$
\DD=\{z\in\CC:\abs{z}<1\}.
$$

<1>1. The function $f$ has only finitely many zeros in $\DD$.

::: {.proof}
The continuous extension $\widetilde f$ satisfies
$$
\abs{\widetilde f(\zeta)}=1
$$
for every $\zeta$ on the unit circle. By continuity, for every such
$\zeta$ there is a neighborhood $U_\zeta$ in $\overline\DD$ on which
$$
\abs{\widetilde f}>\frac12.
$$
The unit circle is compact, so finitely many of the $U_\zeta$ cover it.
Consequently there is an $r<1$ such that
$$
\abs{f(z)}>\frac12
$$
whenever $r<\abs{z}<1$.

Thus every zero of $f$ lies in the compact disk
$$
\{z:\abs{z}\leq r\}\subset\DD.
$$
Since $f$ is not identically zero, its zeros are isolated. An infinite set
of zeros in this compact disk would have an accumulation point in $\DD$,
contradicting the identity theorem. Hence the zero set is finite.
:::

<1>2. List the zeros of $f$, with multiplicity, as
$$
a_1,\ldots,a_n
$$
and define
$$
B(z)=\prod_{j=1}^n
\frac{z-a_j}{1-\overline{a_j}z}.
$$
Then $B$ is analytic on a neighborhood of $\overline\DD$, has exactly the
same zeros in $\DD$ as $f$ with the same multiplicities, and
$$
\abs{B(\zeta)}=1
$$
for every $\abs{\zeta}=1$.

::: {.proof}
For each $j$, one has $\abs{a_j}<1$, so the denominator
$$
1-\overline{a_j}z
$$
does not vanish on $\overline\DD$. Hence every factor, and therefore $B$,
is analytic on a neighborhood of $\overline\DD$.

Its numerator shows that the factor indexed by $j$ has a simple zero at
$a_j$; listing the $a_j$ with multiplicity therefore makes the zero
multiplicities of $B$ agree with those of $f$.

If $\abs{\zeta}=1$, then
$$
\abs{\zeta-a_j}
=
\abs{\zeta}\,
\abs{1-\overline{\zeta}a_j}
=
\abs{1-\overline{a_j}\zeta}.
$$
Thus every factor has modulus one on the unit circle, and so does $B$.
:::

<1>3. The quotient
$$
h(z)=\frac{f(z)}{B(z)}
$$
extends to a zero-free analytic function on $\DD$, continuous on
$\overline\DD$, and satisfies
$$
\abs{h(\zeta)}=1
$$
for every $\abs{\zeta}=1$. Consequently
$$
h\equiv\lambda
$$
for some $\lambda\in\CC$ with $\abs{\lambda}=1$.

::: {.proof}
By step <1>2, $f$ and $B$ have the same zeros with the same multiplicities,
so every apparent singularity of $f/B$ at an $a_j$ is removable. After
removing them, $h$ is analytic and zero-free on $\DD$. It is continuous on
$\overline\DD$ because both $f$ and $B$ are continuous there and $B$ is
nonzero on the unit circle.

For $\abs{\zeta}=1$, the boundary hypotheses on $f$ and step <1>2 give
$$
\abs{h(\zeta)}
=
\frac{\abs{f(\zeta)}}{\abs{B(\zeta)}}
=
1.
$$
The maximum modulus principle applied on the disk gives
$$
\abs{h(z)}\leq1
$$
for $z\in\DD$. Since $h$ has no zeros, $1/h$ is analytic on $\DD$ and
continuous on $\overline\DD$, with boundary modulus one as well. Applying
the same argument to $1/h$ gives
$$
\abs{h(z)}\geq1.
$$
Therefore $\abs{h(z)}=1$ throughout $\DD$. By the open mapping theorem,
$h$ is constant. Write $h\equiv\lambda$; its boundary modulus gives
$\abs{\lambda}=1$.
:::

<1>4. Part (a): $f$ is a rational function.

::: {.proof}
By step <1>3,
$$
f(z)
=
\lambda B(z)
=
\lambda
\prod_{j=1}^n
\frac{z-a_j}{1-\overline{a_j}z}.
$$
The right-hand side is rational.
:::

<1>5. Part (b): if $0$ is the unique zero of $f$, then
$$
\boxed{
f(z)=\lambda z^n
}
$$
for some $n\in\NN$ and some $\lambda\in\CC$ with
$\abs{\lambda}=1$.

::: {.proof}
Let $n$ be the multiplicity of the zero at $0$. Then the zero list in step
<1>2 is
$$
a_1=\cdots=a_n=0.
$$
Hence
$$
B(z)
=
\prod_{j=1}^n\frac{z}{1}
=
z^n.
$$
Step <1>3 therefore gives
$$
f(z)=\lambda z^n,
\qquad
\abs{\lambda}=1.
$$
:::

<1>6. Part (c): in general,
$$
\boxed{
f(z)=\lambda
\prod_{j=1}^n
\frac{z-a_j}{1-\overline{a_j}z},
\qquad
\abs{\lambda}=1.
}
$$

::: {.proof}
This is exactly the identity $f=\lambda B$ established in step <1>3,
with $B$ defined in step <1>2.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>4--<1>6 prove parts (a)--(c), respectively.
:::
:::
