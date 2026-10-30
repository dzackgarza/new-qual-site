---
schema: qual/card@1
id: P-KSRING17-124
kind: problem
title: Localization at a maximal ideal has the same residue field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 124 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with identity and $M$ a maximal ideal of $R$. Let $R_{M}$ be the ring of quotients of $R$ with respect to the multiplicative set $R - M = \{s \in R \st s \notin M\}$. Show the following.

(a) $M_{M} = \{\frac{a}{s} \st a \in M,\ s \notin M\}$ is the unique maximal ideal of $R_{M}$.

(b) The fields $R/M$ and $R_{M}/M_{M}$ are isomorphic.
:::

::: {.solution}

Let
$$
S
\coloneqq
R\setminus M.
$$
Since $M$ is maximal in a commutative ring, it is prime.

::: pf

::: pf-step

The set
$$
M_M
\coloneqq
\left\{
\frac as:
a\in M,\ s\in S
\right\}
$$
is well-defined as a subset of $R_M$.


::: pf-proof

Suppose
$$
\frac as
=
\frac bt
$$
in
$$
R_M,
$$
with
$$
s,t\in S
$$
and
$$
a\in M.
$$
By equality in a localization, there exists
$$
u\in S
$$
such that
$$
u(at-bs)=0.
$$
Thus
$$
uat
=
ubs.
$$
Since
$$
a\in M,
$$
one has
$$
uat\in M.
$$
Hence
$$
ubs\in M.
$$
Because
$$
u,s\notin M
$$
and $M$ is prime,
$$
b\in M.
$$
Thus membership in $M_M$ does not depend on the chosen representative.

:::

:::

::: {.pf-step #s1-2}

The set $M_M$ is closed under subtraction.


::: pf-proof

Let
$$
\frac as,\frac bt
\in
M_M.
$$
Then
$$
a,b\in M,
\qquad
s,t\in S.
$$
One has
$$
\frac as-\frac bt
=
\frac{at-bs}{st}.
$$
Since $M$ is an ideal,
$$
at-bs
\in
M.
$$
Since $M$ is prime and
$$
s,t\notin M,
$$
one has
$$
st\notin M.
$$
Therefore the difference belongs to
$$
M_M.
$$

:::

:::

::: {.pf-step #s1-3}

The set $M_M$ absorbs multiplication by arbitrary elements of $R_M$.


::: pf-proof

Let
$$
\frac rs
\in
R_M
$$
and
$$
\frac at
\in
M_M.
$$
Then
$$
a\in M,
\qquad
s,t\in S.
$$
Their product is
$$
\frac{ra}{st}.
$$
Since
$$
ra\in M
$$
and
$$
st\in S,
$$
the product lies in
$$
M_M.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
M_M
\trianglelefteq
R_M.
}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives the additive-subgroup condition, and step [](#s1-3){.pf-ref} gives absorption under multiplication by arbitrary elements.

:::

:::

::: {.pf-step #s1-5}

If
$$
\frac as
\in
R_M
$$
with
$$
a\notin M,
$$
then
$$
\frac as
$$
is a unit.


::: pf-proof

Because
$$
a\notin M,
$$
one has
$$
a\in S.
$$
Thus
$$
\frac sa
\in
R_M.
$$
Moreover,
$$
\frac as\frac sa
=
1.
$$
Hence
$$
\frac as
$$
is invertible.

:::

:::

::: {.pf-step #s1-6}

If
$$
\frac as
\in
M_M,
$$
then
$$
\frac as
$$
is not a unit.


::: pf-proof

Suppose
$$
a\in M,
\qquad
s\in S,
$$
and
$$
\frac as
$$
were invertible.
Then there would exist
$$
\frac bt
\in
R_M
$$
such that
$$
\frac{ab}{st}
=
1.
$$
By equality in the localization, there exists
$$
u\in S
$$
with
$$
u(ab-st)=0.
$$
Thus
$$
uab
=
ust.
$$
The left-hand side lies in
$$
M
$$
because
$$
a\in M.
$$
Hence
$$
ust\in M.
$$
But
$$
u,s,t\notin M
$$
and $M$ is prime, so their product cannot lie in $M$.
Contradiction.
Therefore
$$
\frac as
$$
is not a unit.

:::

:::

::: pf-step

The nonunits of $R_M$ are exactly the elements of $M_M$.


::: pf-proof

Step [](#s1-5){.pf-ref} shows every element outside $M_M$ is a unit.
Step [](#s1-6){.pf-ref} shows every element of $M_M$ is a nonunit.
Thus
$$
\boxed{
M_M
=
R_M\setminus R_M^\times.
}
$$

:::

:::

::: {.pf-step #s1-8}

The ideal $M_M$ is the unique maximal ideal of $R_M$.


::: pf-proof

By step [](#s1-4){.pf-ref}, the set of nonunits is an ideal.
A commutative ring is local exactly when its nonunits form an ideal, and in that case this ideal is the unique maximal ideal.
Hence
$$
\boxed{
M_M
\text{ is the unique maximal ideal of }R_M.
}
$$

:::

:::

::: pf-step

Define
$$
\Phi:R_M\to R/M
$$
by
$$
\boxed{
\Phi\left(\frac as\right)
\coloneqq
(a+M)(s+M)^{-1}.
}
$$


::: pf-proof

Since
$$
s\notin M,
$$
the class
$$
s+M
$$
is nonzero in the field
$$
R/M,
$$
and hence invertible.
Thus the displayed formula makes sense.

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
R_M.
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
R/M
$$
gives
$$
(u+M)
\bigl(
(a+M)(t+M)
-
(b+M)(s+M)
\bigr)
=
0.
$$
Because
$$
u\notin M,
$$
the element
$$
u+M
$$
is nonzero in the field and therefore invertible.
Hence
$$
(a+M)(t+M)
=
(b+M)(s+M).
$$
Multiplying by the inverses of
$$
s+M
$$
and
$$
t+M
$$
gives
$$
(a+M)(s+M)^{-1}
=
(b+M)(t+M)^{-1}.
$$
Thus $\Phi$ is well-defined.

:::

:::

::: {.pf-step #s1-11}

The map $\Phi$ is a ring homomorphism.


::: pf-proof

For
$$
\frac as,\frac bt
\in
R_M,
$$
one has
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
(at+bs+M)(st+M)^{-1}\\
&=
(a+M)(s+M)^{-1}
+
(b+M)(t+M)^{-1}.
\end{aligned}
$$
The multiplicative verification is analogous:
$$
\Phi\left(
\frac{ab}{st}
\right)
=
\Phi\left(\frac as\right)
\Phi\left(\frac bt\right).
$$
Also
$$
\Phi(1)=1+M.
$$

:::

:::

::: {.pf-step #s1-12}

The map $\Phi$ is surjective.


::: pf-proof

Let
$$
r+M
\in
R/M.
$$
Then
$$
\Phi\left(\frac r1\right)
=
(r+M)(1+M)^{-1}
=
r+M.
$$
Thus every element is in the image.

:::

:::

::: {.pf-step #s1-13}

The kernel of $\Phi$ is exactly $M_M$.


::: pf-proof

One has
$$
\Phi\left(\frac as\right)=0+M
$$
if and only if
$$
(a+M)(s+M)^{-1}=0+M.
$$
Since
$$
s+M
$$
is invertible, this is equivalent to
$$
a+M=0+M,
$$
that is,
$$
a\in M.
$$
By definition, this is equivalent to
$$
\frac as\in M_M.
$$
Thus
$$
\ker\Phi=M_M.
$$

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{
R_M/M_M
\cong
R/M.
}
$$


::: pf-proof

By steps [](#s1-11){.pf-ref} through [](#s1-13){.pf-ref}, $\Phi$ is a surjective ring homomorphism with kernel
$$
M_M.
$$
The first isomorphism theorem gives
$$
R_M/M_M
\cong
R/M.
$$

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves part (a), and step [](#s1-14){.pf-ref} proves part (b).

:::

:::

:::
