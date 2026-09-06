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

- Show: $\QQ/\ZZ \cong T(\CC\units)$, the group of roots of unity in $\CC\units$.

  Note $\QQ/\ZZ \cong \CC\units$ is false: every element of $\QQ/\ZZ$ has finite order by the bullet above, while $2 \in \CC\units$ has infinite order.
:::

::: {.solution}
<1>1. Every coset in $\mathbb Q/\mathbb Z$ has a representative in $[0,1)\cap\mathbb Q$.
::: {.proof}
Let
\[
q=\frac mn\in\mathbb Q,
\qquad
m\in\mathbb Z,
\quad n\in\mathbb Z_{>0}.
\]
By Euclidean division there are unique integers $a,r$ such that
\[
m=an+r,
\qquad
0\le r<n.
\]
Then
\[
q=a+\frac rn,
\]
so
\[
q+\mathbb Z=\frac rn+\mathbb Z,
\]
and
\[
0\le\frac rn<1.
\]
Thus the coset has a representative in $[0,1)\cap\mathbb Q$.
:::

<1>2. That representative is unique.
::: {.proof}
Suppose $r,s\in[0,1)\cap\mathbb Q$ represent the same coset.
Then
\[
r-s\in\mathbb Z.
\]
But
\[
-1<r-s<1.
\]
The only integer in $(-1,1)$ is $0$, hence
\[
r=s.
\]
:::

<1>3. Every element of $\mathbb Q/\mathbb Z$ has finite order.
::: {.proof}
Let
\[
q=\frac mn\in\mathbb Q,
\qquad n>0.
\]
Then in the additive quotient group,
\[
n(q+\mathbb Z)
=nq+\mathbb Z
=m+\mathbb Z
=\mathbb Z,
\]
the identity coset.
Thus $q+\mathbb Z$ has finite order dividing $n$.
:::

<1>4. For each integer $n\ge1$, the element
\[
\frac1n+\mathbb Z
\]
has order exactly $n$.
::: {.proof}
By <1>3 its order divides $n$.
If a positive integer $k$ satisfies
\[
k\left(\frac1n+\mathbb Z\right)=\mathbb Z,
\]
then
\[
\frac kn\in\mathbb Z,
\]
so $n\mid k$.
Therefore no positive $k<n$ annihilates the coset, and its order is exactly $n$.
Since $n$ is arbitrary, $\mathbb Q/\mathbb Z$ has elements of arbitrarily large finite order.
:::

<1>5. One has
\[
T(\mathbb R/\mathbb Z)=\mathbb Q/\mathbb Z.
\]
::: {.proof}
By <1>3, every element of $\mathbb Q/\mathbb Z$ has finite order, so
\[
\mathbb Q/\mathbb Z\subseteq T(\mathbb R/\mathbb Z).
\]
Conversely, suppose
\[
r+\mathbb Z\in\mathbb R/\mathbb Z
\]
has finite order.
Then for some integer $n\ge1$,
\[
n(r+\mathbb Z)=\mathbb Z.
\]
Thus
\[
nr\in\mathbb Z,
\]
so
\[
r=\frac{nr}{n}\in\mathbb Q.
\]
Hence
\[
r+\mathbb Z\in\mathbb Q/\mathbb Z.
\]
The two inclusions prove the equality.
:::

Let
\[
\mu_\infty=\{z\in\mathbb C^\times:z^n=1\text{ for some }n\ge1\}
=T(\mathbb C^\times)
\]
be the multiplicative group of all roots of unity.

<1>6. The map
\[
\Phi:\mathbb Q/\mathbb Z\longrightarrow\mu_\infty,
\qquad
\Phi(q+\mathbb Z)=e^{2\pi i q},
\]
is a well-defined homomorphism.
::: {.proof}
If
\[
q+\mathbb Z=q'+\mathbb Z,
\]
then $q-q'\in\mathbb Z$, and therefore
\[
e^{2\pi iq}=e^{2\pi iq'}e^{2\pi i(q-q')}=e^{2\pi iq'}.
\]
Thus $\Phi$ is well-defined.
Moreover,
\[
\begin{aligned}
\Phi((q+\mathbb Z)+(r+\mathbb Z))
&=e^{2\pi i(q+r)}\\
&=e^{2\pi iq}e^{2\pi ir}\\
&=\Phi(q+\mathbb Z)\Phi(r+\mathbb Z),
\end{aligned}
\]
so it is a homomorphism.
Finally, if $q=m/n$, then
\[
\Phi(q+\mathbb Z)^n=e^{2\pi im}=1,
\]
so its image lies in $\mu_\infty$.
:::

<1>7. The map $\Phi$ is injective.
::: {.proof}
Its kernel consists of those $q+\mathbb Z$ for which
\[
e^{2\pi iq}=1.
\]
For real $q$, this holds exactly when $q\in\mathbb Z$.
Thus
\[
\ker\Phi=\mathbb Z,
\]
meaning that the only kernel coset in $\mathbb Q/\mathbb Z$ is the identity coset.
Hence $\Phi$ is injective.
:::

<1>8. The map $\Phi$ is surjective onto $\mu_\infty$.
::: {.proof}
Let $\zeta\in\mu_\infty$.
Choose $n\ge1$ such that
\[
\zeta^n=1.
\]
Then $|\zeta|^n=1$, so $|\zeta|=1$ and
\[
\zeta=e^{i\theta}
\]
for some real $\theta$.
The equation $\zeta^n=1$ gives
\[
e^{in\theta}=1,
\]
so
\[
n\theta=2\pi k
\]
for some $k\in\mathbb Z$.
Hence
\[
\zeta=e^{2\pi i k/n}
=\Phi\left(\frac kn+\mathbb Z\right).
\]
Thus every root of unity is in the image.
:::

<1>9. Therefore
\[
\mathbb Q/\mathbb Z\cong T(\mathbb C^\times).
\]
::: {.proof}
By <1>6--<1>8, $\Phi$ is a bijective homomorphism from $\mathbb Q/\mathbb Z$ onto the roots-of-unity subgroup $\mu_\infty=T(\mathbb C^\times)$.
Hence it is an isomorphism.
:::
:::
