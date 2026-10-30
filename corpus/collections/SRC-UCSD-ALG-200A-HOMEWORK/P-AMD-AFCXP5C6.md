---
schema: qual/card@1
id: P-AMD-AFCXP5C6
kind: problem
title: $\QQ/\ZZ$ as torsion in $\RR/\ZZ$ and as the roots of unity
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Torsion
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against the source-audited UCSD Math 200A Homework 1 occurrence and independently against Dummit--Foote's standard Q/Z exercise as reproduced in graduate group-theory notes. The live UCSD provenance PDF endpoint timed out during this review.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used Euclidean division for unique representatives in [0,1), computed the exact order of 1/n+Z, characterized torsion in R/Z by nr in Z, and proved q+Z -> exp(2 pi i q) is a well-defined bijective homomorphism onto the roots of unity.
---

::: {.problem}
Show: $\QQ/\ZZ$ has, for each coset, exactly one representative in $[0, 1) \intersect \QQ$

- Show: Every element of $\QQ/\ZZ$ has finite order.

- Show: There are elements in $\QQ/\ZZ$ of arbitrarily large order.

- Show: $\QQ/\ZZ = T(\RR/\ZZ)$

- Show: $\QQ/\ZZ \cong T(\units{\CC})$, the group of roots of unity in $\units{\CC}$.

  Note $\QQ/\ZZ \cong \units{\CC}$ is false: every element of $\QQ/\ZZ$ has finite order by the bullet above, while $2 \in \units{\CC}$ has infinite order.
:::

::: {.solution}

::: pf

::: pf-step

Every coset in $\QQ/\ZZ$ has a representative in $[0,1)\cap\QQ$.

::: pf-proof

Let
$$
q=\frac mn\in\QQ,
\qquad
m\in\ZZ,
\quad n\in\ZZ_{>0}.
$$
By Euclidean division there are unique integers $a,r$ such that
$$
m=an+r,
\qquad
0\le r<n.
$$
Then
$$
q=a+\frac rn,
$$
so
$$
q+\ZZ=\frac rn+\ZZ,
$$
and
$$
0\le\frac rn<1.
$$
Thus the coset has a representative in $[0,1)\cap\QQ$.

:::

:::

::: pf-step

That representative is unique.

::: pf-proof

Suppose $r,s\in[0,1)\cap\QQ$ represent the same coset.
Then
$$
r-s\in\ZZ.
$$
But
$$
-1<r-s<1.
$$
The only integer in $(-1,1)$ is $0$, hence
$$
r=s.
$$

:::

:::

::: {.pf-step #s3}

Every element of $\QQ/\ZZ$ has finite order.

::: pf-proof

Let
$$
q=\frac mn\in\QQ,
\qquad n>0.
$$
Then in the additive quotient group,
$$
n(q+\ZZ)
=nq+\ZZ
=m+\ZZ
=\ZZ,
$$
the identity coset.
Thus $q+\ZZ$ has finite order dividing $n$.

:::

:::

::: pf-step

For each integer $n\ge1$, the element
$$
\frac1n+\ZZ
$$
has order exactly $n$.

::: pf-proof

By step [](#s3){.pf-ref} its order divides $n$.
If a positive integer $k$ satisfies
$$
k\left(\frac1n+\ZZ\right)=\ZZ,
$$
then
$$
\frac kn\in\ZZ,
$$
so $n\mid k$.
Therefore no positive $k<n$ annihilates the coset, and its order is exactly $n$.
Since $n$ is arbitrary, $\QQ/\ZZ$ has elements of arbitrarily large finite order.

:::

:::

::: pf-step

One has
$$
T(\RR/\ZZ)=\QQ/\ZZ.
$$

::: pf-proof

By step [](#s3){.pf-ref}, every element of $\QQ/\ZZ$ has finite order, so
$$
\QQ/\ZZ\subseteq T(\RR/\ZZ).
$$
Conversely, suppose
$$
r+\ZZ\in\RR/\ZZ
$$
has finite order.
Then for some integer $n\ge1$,
$$
n(r+\ZZ)=\ZZ.
$$
Thus
$$
nr\in\ZZ,
$$
so
$$
r=\frac{nr}{n}\in\QQ.
$$
Hence
$$
r+\ZZ\in\QQ/\ZZ.
$$
The two inclusions prove the equality.

Let
$$
\mu_\infty=\{z\in\CC^\times:z^n=1\text{ for some }n\ge1\}
=T(\CC^\times)
$$
be the multiplicative group of all roots of unity.

:::

:::

::: {.pf-step #s6}

The map
$$
\Phi:\QQ/\ZZ\longrightarrow\mu_\infty,
\qquad
\Phi(q+\ZZ)=e^{2\pi i q},
$$
is a well-defined homomorphism.

::: pf-proof

If
$$
q+\ZZ=q'+\ZZ,
$$
then $q-q'\in\ZZ$, and therefore
$$
e^{2\pi iq}=e^{2\pi iq'}e^{2\pi i(q-q')}=e^{2\pi iq'}.
$$
Thus $\Phi$ is well-defined.
Moreover,
$$
\begin{aligned}
\Phi((q+\ZZ)+(r+\ZZ))
&=e^{2\pi i(q+r)}\\
&=e^{2\pi iq}e^{2\pi ir}\\
&=\Phi(q+\ZZ)\Phi(r+\ZZ),
\end{aligned}
$$
so it is a homomorphism.
Finally, if $q=m/n$, then
$$
\Phi(q+\ZZ)^n=e^{2\pi im}=1,
$$
so its image lies in $\mu_\infty$.

:::

:::

::: {.pf-step #s7}

The map $\Phi$ is injective.

::: pf-proof

Its kernel consists of those $q+\ZZ$ for which
$$
e^{2\pi iq}=1.
$$
For real $q$, this holds exactly when $q\in\ZZ$.
Thus
$$
\ker\Phi=\ZZ,
$$
meaning that the only kernel coset in $\QQ/\ZZ$ is the identity coset.
Hence $\Phi$ is injective.

:::

:::

::: {.pf-step #s8}

The map $\Phi$ is surjective onto $\mu_\infty$.

::: pf-proof

Let $\zeta\in\mu_\infty$.
Choose $n\ge1$ such that
$$
\zeta^n=1.
$$
Then $\abs{\zeta}^n=1$, so $\abs{\zeta}=1$ and
$$
\zeta=e^{i\theta}
$$
for some real $\theta$.
The equation $\zeta^n=1$ gives
$$
e^{in\theta}=1,
$$
so
$$
n\theta=2\pi k
$$
for some $k\in\ZZ$.
Hence
$$
\zeta=e^{2\pi i k/n}
=\Phi\left(\frac kn+\ZZ\right).
$$
Thus every root of unity is in the image.

:::

:::

::: pf-step

Therefore
$$
\QQ/\ZZ\cong T(\CC^\times).
$$

::: pf-proof

By steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref}, $\Phi$ is a bijective homomorphism from $\QQ/\ZZ$ onto the roots-of-unity subgroup $\mu_\infty=T(\CC^\times)$.
Hence it is an isomorphism.

:::

:::

:::

:::
