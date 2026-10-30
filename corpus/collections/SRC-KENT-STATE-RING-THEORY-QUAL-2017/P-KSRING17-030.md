---
schema: qual/card@1
id: P-KSRING17-030
kind: problem
title: The center of a simple ring is zero or a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 30 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
A ring $R$ is called simple if $R^{2} \neq 0$ and $0$ and $R$ are its only ideals. Show that the center of a simple ring is $0$ or a field.
:::

::: {.solution}

Let
$$
Z(R)
\coloneqq
\{z\in R:zr=rz\text{ for every }r\in R\}.
$$
If
$$
Z(R)=0,
$$
there is nothing to prove. Assume henceforth that
$$
Z(R)\ne0.
$$

::: pf

::: {.pf-step #s1-1}

If
$$
0\ne z\in Z(R),
$$
then
$$
zR\ne0.
$$


::: pf-proof

Suppose
$$
zR=0.
$$
Since $z$ is central, also
$$
Rz=0.
$$
Consider the additive subgroup
$$
\ZZ z
\subseteq
R.
$$
For every
$$
r\in R
$$
and every
$$
k\in\ZZ,
$$
one has
$$
r(kz)=k(rz)=0
$$
and
$$
(kz)r=k(zr)=0.
$$
Thus
$$
\ZZ z
$$
is a nonzero two-sided ideal of $R$.

Because $R$ is simple,
$$
\ZZ z=R.
$$
But every product of two elements of $\ZZ z$ is zero, since $zR=0$. Hence
$$
R^2=0,
$$
contradicting the definition of a simple ring.

Therefore
$$
zR\ne0.
$$

:::

:::

::: {.pf-step #s1-2}

For every
$$
0\ne z\in Z(R),
$$
one has
$$
zR=R.
$$


::: pf-proof

Because $z$ is central,
$$
zR
$$
is a two-sided ideal:
for
$$
r,s\in R,
$$
one has
$$
s(zr)
=
z(sr)
\in
zR
$$
and
$$
(zr)s
=
z(rs)
\in
zR.
$$
By step [](#s1-1){.pf-ref} this ideal is nonzero. Since $R$ is simple,
$$
zR=R.
$$

:::

:::

::: {.pf-step #s1-3}

The ring $R$ has a multiplicative identity.


::: pf-proof

Choose
$$
0\ne z\in Z(R).
$$
By step [](#s1-2){.pf-ref},
$$
zR=R.
$$
In particular,
$$
z\in zR,
$$
so there exists
$$
e\in R
$$
such that
$$
ze=z.
$$
Because $z$ is central,
$$
ez=ze=z.
$$

Let
$$
r\in R.
$$
Again by
$$
zR=R,
$$
write
$$
r=zs
$$
for some
$$
s\in R.
$$
Then
$$
er
=
e(zs)
=
(ez)s
=
zs
=
r.
$$
Likewise,
$$
re
=
(zs)e
=
z(se)
=
(ze)s
=
zs
=
r,
$$
where centrality of $z$ is used to rearrange the factors.
Thus $e$ is a two-sided identity of $R$.

:::

:::

::: {.pf-step #s1-4}

Every nonzero element of $Z(R)$ is invertible in $R$.


::: pf-proof

Let
$$
0\ne c\in Z(R).
$$
By step [](#s1-2){.pf-ref},
$$
cR=R.
$$
Since $e$ is the identity from step [](#s1-3){.pf-ref}, there exists
$$
d\in R
$$
such that
$$
cd=e.
$$
Because $c$ is central,
$$
dc=cd=e.
$$
Hence $d$ is a two-sided inverse of $c$.

:::

:::

::: {.pf-step #s1-5}

The inverse of every nonzero central element is again central.


::: pf-proof

Let
$$
c\in Z(R)^\times
$$
and let
$$
d=c^{-1}.
$$
For any
$$
r\in R,
$$
one has
$$
\begin{aligned}
dr
&=
dr(cd)\\
&=
d(rc)d\\
&=
d(cr)d\\
&=
(dc)rd\\
&=
rd.
\end{aligned}
$$
Thus
$$
dr=rd
$$
for every $r$, so
$$
d\in Z(R).
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
Z(R)\text{ is either }0\text{ or a field}.
}
$$


::: pf-proof

Under the standing assumption
$$
Z(R)\ne0,
$$
step [](#s1-3){.pf-ref} supplies an identity
$$
e\in Z(R),
$$
because an identity commutes with every element. The center is a commutative subring of $R$, and steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} show that every nonzero element of the center has an inverse in the center. Hence
$$
Z(R)
$$
is a field.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required dichotomy.

:::

:::

:::
