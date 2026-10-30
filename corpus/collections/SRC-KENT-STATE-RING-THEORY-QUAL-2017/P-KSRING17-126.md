---
schema: qual/card@1
id: P-KSRING17-126
kind: problem
title: The residue field of $R_P$ is the fraction field of $R/P$
classification:
  areas: [algebra]
  topics:
  - Localization
  - Residue Fields
  - Fields of Fractions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 126 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with identity and $P$ a prime ideal of $R$. Let $R_{P}$ be the ring of quotients of $R$ with respect to the set $R - P = \{s \in R \st s \notin P\}$. Show that $R_{P}/P_{P}$ is the field of fractions of the integral domain $R/P$.
:::

::: {.solution}

Set
$$
S
\coloneqq
R\setminus P.
$$
Since $P$ is prime,
$$
R/P
$$
is an integral domain.
Let
$$
K
\coloneqq
\operatorname{Frac}(R/P).
$$

::: pf

::: {.pf-step #s1-1}

For every
$$
s\in S,
$$
the class
$$
s+P
$$
is nonzero in
$$
R/P.
$$


::: pf-proof

The condition
$$
s\in S
$$
means
$$
s\notin P.
$$
Thus
$$
s+P
\ne
0+P.
$$

:::

:::

::: pf-step

Define
$$
\Phi:R_P\to K
$$
by
$$
\boxed{
\Phi\left(\frac as\right)
\coloneqq
\frac{a+P}{s+P}.
}
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
s+P
$$
is a nonzero element of the domain
$$
R/P.
$$
Hence it is a valid denominator in
$$
\operatorname{Frac}(R/P).
$$

:::

:::

::: pf-step

The map $\Phi$ is well-defined.


::: pf-proof

Suppose
$$
\frac as
=
\frac bt
$$
in
$$
R_P.
$$
Then there exists
$$
u\in S
$$
such that
$$
u(at-bs)=0.
$$
Passing to
$$
R/P,
$$
one obtains
$$
(u+P)
\bigl(
(a+P)(t+P)
-
(b+P)(s+P)
\bigr)
=
0.
$$
By step [](#s1-1){.pf-ref},
$$
u+P
\ne
0+P.
$$
Since
$$
R/P
$$
is an integral domain,
$$
(a+P)(t+P)
=
(b+P)(s+P).
$$
This is precisely the equality
$$
\frac{a+P}{s+P}
=
\frac{b+P}{t+P}
$$
in the fraction field.

:::

:::

::: pf-step

The map $\Phi$ preserves addition.


::: pf-proof

For
$$
\frac as,\frac bt
\in
R_P,
$$
$$
\begin{aligned}
\Phi\left(
\frac as+\frac bt
\right)
&=
\Phi\left(
\frac{at+bs}{st}
\right)\\
&=
\frac{at+bs+P}{st+P}\\
&=
\frac{a+P}{s+P}
+
\frac{b+P}{t+P}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

The map $\Phi$ preserves multiplication and identity.


::: pf-proof

One has
$$
\begin{aligned}
\Phi\left(
\frac as\frac bt
\right)
&=
\Phi\left(
\frac{ab}{st}
\right)\\
&=
\frac{ab+P}{st+P}\\
&=
\frac{a+P}{s+P}
\frac{b+P}{t+P}.
\end{aligned}
$$
Also
$$
\Phi(1)
=
\Phi\left(\frac11\right)
=
\frac{1+P}{1+P}
=
1.
$$
Thus $\Phi$ is a unital ring homomorphism.

:::

:::

::: {.pf-step #s1-6}

The map $\Phi$ is surjective.


::: pf-proof

Let
$$
\frac{a+P}{b+P}
\in
K
$$
be arbitrary.
Its denominator is nonzero, so
$$
b\notin P.
$$
Hence
$$
b\in S,
$$
and
$$
\frac ab
\in
R_P.
$$
By definition,
$$
\Phi\left(\frac ab\right)
=
\frac{a+P}{b+P}.
$$
Thus $\Phi$ is onto.

:::

:::

::: {.pf-step #s1-7}

If
$$
\frac as
\in
\ker\Phi,
$$
then
$$
a\in P.
$$


::: pf-proof

The condition
$$
\Phi\left(\frac as\right)=0
$$
means
$$
\frac{a+P}{s+P}=0
$$
in the field of fractions of
$$
R/P.
$$
Since
$$
s+P\ne0,
$$
a fraction is zero exactly when its numerator is zero.
Hence
$$
a+P=0+P,
$$
so
$$
a\in P.
$$

:::

:::

::: {.pf-step #s1-8}

Conversely, if
$$
a\in P,
\qquad
s\notin P,
$$
then
$$
\frac as
\in
\ker\Phi.
$$


::: pf-proof

If
$$
a\in P,
$$
then
$$
a+P=0+P.
$$
Therefore
$$
\Phi\left(\frac as\right)
=
\frac{0+P}{s+P}
=
0.
$$

:::

:::

::: {.pf-step #s1-9}

The kernel of $\Phi$ is
$$
\boxed{
\ker\Phi
=
P_P
=
\left\{
\frac as:
a\in P,\ s\notin P
\right\}.
}
$$


::: pf-proof

Step [](#s1-7){.pf-ref} gives
$$
\ker\Phi
\subseteq
P_P,
$$
and step [](#s1-8){.pf-ref} gives the reverse inclusion.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
R_P/P_P
\cong
\operatorname{Frac}(R/P).
}
$$


::: pf-proof

By steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}, $\Phi$ is a surjective ring homomorphism.
By step [](#s1-9){.pf-ref}, its kernel is
$$
P_P.
$$
The first isomorphism theorem gives
$$
R_P/P_P
\cong
K
=
\operatorname{Frac}(R/P).
$$

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
