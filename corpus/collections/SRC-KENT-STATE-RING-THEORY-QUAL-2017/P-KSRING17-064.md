---
schema: qual/card@1
id: P-KSRING17-064
kind: problem
title: Integral domains are exactly the subrings of fields
classification:
  areas: [algebra]
  topics:
  - Integral Domains
  - Fields of Fractions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 64 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity.
Show that R is an integral domain if and only if R is a subring of a field.
:::

::: {.solution}

::: pf

::: pf-step

Assume first that $R$ is an integral domain.
Define
$$
F
\coloneqq
\operatorname{Frac}(R),
$$
the set of equivalence classes of pairs
$$
(a,b)
\in
R\times(R\setminus\{0\}),
$$
where
$$
(a,b)\sim(c,d)
\quad\Longleftrightarrow\quad
ad=bc.
$$


::: pf-proof

Because $R$ is an integral domain, the usual fraction relation is an equivalence relation, and the operations
$$
\frac ab+\frac cd
\coloneqq
\frac{ad+bc}{bd},
$$
and
$$
\frac ab\frac cd
\coloneqq
\frac{ac}{bd}
$$
are well-defined.
The denominator
$$
bd
$$
is nonzero because $R$ has no zero divisors.
This gives the usual fraction ring of $R$.

:::

:::

::: {.pf-step #s1-2}

The ring $F$ is a field.


::: pf-proof

The fraction
$$
\frac10
$$
is not permitted, so the zero element is represented by
$$
\frac01.
$$
Let
$$
\frac ab
\ne
0
$$
in $F$.
Then
$$
a\ne0.
$$
Hence
$$
\frac ba
$$
is a valid fraction and
$$
\frac ab\frac ba
=
\frac{ab}{ba}
=
1.
$$
Thus every nonzero element of $F$ is invertible.
Since $F$ is commutative with identity, it is a field.

:::

:::

::: {.pf-step #s1-3}

The map
$$
\iota:R\to F,
\qquad
\iota(r)
\coloneqq
\frac r1
$$
is an injective ring homomorphism.


::: pf-proof

For
$$
r,s\in R,
$$
one has
$$
\iota(r+s)
=
\frac{r+s}{1}
=
\frac r1+\frac s1
$$
and
$$
\iota(rs)
=
\frac{rs}{1}
=
\frac r1\frac s1.
$$
Also
$$
\iota(1_R)=1_F.
$$

If
$$
\iota(r)=\iota(s),
$$
then
$$
\frac r1
=
\frac s1,
$$
so
$$
r\cdot1=s\cdot1,
$$
hence
$$
r=s.
$$
Thus $\iota$ is injective.

:::

:::

::: {.pf-step #s1-4}

Therefore every integral domain is isomorphic to a subring of a field.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
F=\operatorname{Frac}(R)
$$
is a field, and by step [](#s1-3){.pf-ref},
$$
\iota:R\hookrightarrow F
$$
is an injective ring homomorphism.
Thus $R$ identifies with the subring
$$
\iota(R)\subseteq F.
$$

:::

:::

::: {.pf-step #s1-5}

Conversely, suppose $R$ is a subring of a field $K$.
Then $R$ has no nonzero zero divisors.


::: pf-proof

Let
$$
a,b\in R
$$
and suppose
$$
ab=0
$$
in $R$.
The same equality holds in the field $K$.
Since a field has no nonzero zero divisors,
$$
a=0
\quad\text{or}\quad
b=0.
$$
Thus $R$ has no nonzero zero divisors.

:::

:::

::: {.pf-step #s1-6}

Hence a nonzero subring of a field is an integral domain.


::: pf-proof

A subring of a field is commutative.
Under the standard unital-subring convention, it contains the same identity and is nonzero.
By step [](#s1-5){.pf-ref} it has no nonzero zero divisors.
Therefore it is an integral domain.

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{
R\text{ is an integral domain}
\iff
R\text{ is isomorphic to a subring of a field}.
}
$$


::: pf-proof

The forward implication is step [](#s1-4){.pf-ref}, and the converse is step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required equivalence.

:::

:::

:::
