---
schema: qual/card@1
id: P-KSRING17-018
kind: problem
title: Surjectivity of $R\to R/A\times R/B$ and comaximal ideals
classification:
  areas: [algebra]
  topics:
  - Comaximal Ideals
  - Ring Homomorphisms
  - Chinese Remainder Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 18 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a ring with ideals A and B. Let $R / A \times R / B$ be the ring with coordinate-wise addition and multiplication.
Show the following.

(a) The map $R \to R / A \times R / B$ given by $r \mapsto ( r + A , r + B )$ is a ring homomorphism.

(b) The homomorphism in part (a) is surjective if and only if $A + B = R$
:::

::: {.solution}

Define
$$
\varphi:R\to R/A\times R/B
$$
by
$$
\varphi(r)
\coloneqq
(r+A,r+B).
$$

::: pf

::: {.pf-step #s1-1}

The map $\varphi$ preserves addition.


::: pf-proof

For
$$
r,s\in R,
$$
one has
$$
\begin{aligned}
\varphi(r+s)
&=
(r+s+A,r+s+B)\\
&=
(r+A,r+B)
+
(s+A,s+B)\\
&=
\varphi(r)+\varphi(s).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

The map $\varphi$ preserves multiplication and identity.


::: pf-proof

For
$$
r,s\in R,
$$
coordinatewise multiplication gives
$$
\begin{aligned}
\varphi(rs)
&=
(rs+A,rs+B)\\
&=
(r+A,r+B)
(s+A,s+B)\\
&=
\varphi(r)\varphi(s).
\end{aligned}
$$
Also,
$$
\varphi(1_R)
=
(1_R+A,1_R+B),
$$
which is the identity of
$$
R/A\times R/B.
$$
Hence $\varphi$ is a ring homomorphism.

:::

:::

::: {.pf-step #s1-3}

If $\varphi$ is surjective, then
$$
A+B=R.
$$


::: pf-proof

Assume $\varphi$ is surjective. Then the element
$$
(1+A,0+B)
$$
has a preimage
$$
r\in R.
$$
Thus
$$
r+A=1+A,
\qquad
r+B=0+B.
$$
The first equality means
$$
1-r\in A,
$$
while the second means
$$
r\in B.
$$
Therefore
$$
1
=
(1-r)+r
\in
A+B.
$$
Since an ideal containing $1$ is the whole ring,
$$
A+B=R.
$$

:::

:::

::: {.pf-step #s1-4}

Assume
$$
A+B=R.
$$
Then there exist
$$
a\in A,
\qquad
b\in B
$$
such that
$$
a+b=1.
$$


::: pf-proof

The equality
$$
A+B=R
$$
means in particular that
$$
1\in A+B.
$$
Thus
$$
1=a+b
$$
for some
$$
a\in A,
\qquad
b\in B.
$$

:::

:::

::: {.pf-step #s1-5}

Under the hypothesis of step [](#s1-4){.pf-ref}, the map $\varphi$ is surjective.


::: pf-proof

Let
$$
(r+A,s+B)
\in
R/A\times R/B
$$
be arbitrary. Choose $a,b$ as in step [](#s1-4){.pf-ref} and define
$$
x
\coloneqq
rb+sa.
$$

Modulo $A$, one has
$$
a\equiv0
\pmod A
$$
and
$$
b=1-a\equiv1\pmod A.
$$
Hence
$$
x
=
rb+sa
\equiv
r
\pmod A.
$$
Therefore
$$
x+A=r+A.
$$

Similarly, modulo $B$,
$$
b\equiv0,
\qquad
a=1-b\equiv1,
$$
so
$$
x
\equiv
s
\pmod B.
$$
Thus
$$
x+B=s+B.
$$
Consequently
$$
\varphi(x)
=
(r+A,s+B),
$$
and $\varphi$ is surjective.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\varphi\text{ is surjective}
\iff
A+B=R.
}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} proves the forward implication, and step [](#s1-5){.pf-ref} proves the converse.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
