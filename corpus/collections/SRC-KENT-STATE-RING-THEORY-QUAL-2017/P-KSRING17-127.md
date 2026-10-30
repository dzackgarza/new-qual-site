---
schema: qual/card@1
id: P-KSRING17-127
kind: problem
title: A domain is the intersection of its localizations at maximal ideals
classification:
  areas: [algebra]
  topics:
  - Localization
  - Integral Domains
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 127 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $D$ be an integral domain and $F$ its field of fractions. Denote by $\mathcal{M}$ the set of all maximal ideals of $D$. For $M \in \mathcal{M}$, let $D_{M} = \{\frac{a}{s} \st a, s \in D,\ s \notin M\} \subset F$. Show that $\bigcap_{M \in \mathcal{M}} D_{M} = D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
D
\subseteq
D_M
$$
for every maximal ideal
$$
M
$$
of $D$.


::: pf-proof

Let
$$
d\in D.
$$
Since
$$
1\notin M,
$$
the fraction
$$
\frac d1
$$
belongs to
$$
D_M.
$$
Under the natural embedding
$$
D\subseteq F,
$$
this fraction is just $d$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
D
\subseteq
\bigcap_{M\in\mathcal M}D_M.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} holds for every maximal ideal $M$.

:::

:::

::: pf-step

Let
$$
x
\in
\bigcap_{M\in\mathcal M}D_M.
$$
Define
$$
I_x
\coloneqq
\{d\in D:dx\in D\}.
$$
Then $I_x$ is an ideal of $D$.


::: pf-proof

If
$$
d,e\in I_x,
$$
then
$$
dx,ex\in D,
$$
so
$$
(d-e)x
=
dx-ex
\in
D.
$$
Thus
$$
d-e\in I_x.
$$

If
$$
r\in D
$$
and
$$
d\in I_x,
$$
then
$$
(rd)x
=
r(dx)
\in
D.
$$
Hence
$$
rd\in I_x.
$$
Thus $I_x$ is an ideal.

:::

:::

::: pf-step

The ideal $I_x$ is nonzero.


::: pf-proof

Write
$$
x=\frac ab
$$
in the fraction field with
$$
a,b\in D,
\qquad
b\ne0.
$$
Then
$$
bx=a\in D.
$$
Hence
$$
b\in I_x.
$$
Since
$$
b\ne0,
$$
the ideal $I_x$ is nonzero.

:::

:::

::: {.pf-step #s1-5}

One has
$$
x\in D
\iff
I_x=D.
$$


::: pf-proof

If
$$
x\in D,
$$
then for every
$$
d\in D,
$$
$$
dx\in D.
$$
Hence
$$
I_x=D.
$$

Conversely, if
$$
I_x=D,
$$
then
$$
1\in I_x.
$$
By definition,
$$
1\cdot x=x\in D.
$$

:::

:::

::: {.pf-step #s1-6}

Suppose, for contradiction, that
$$
x\notin D.
$$
Then
$$
I_x
$$
is a proper ideal.


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
x\notin D
$$
implies
$$
I_x\ne D.
$$

:::

:::

::: {.pf-step #s1-7}

There exists a maximal ideal
$$
M
$$
such that
$$
I_x\subseteq M.
$$


::: pf-proof

Every proper ideal in a commutative ring with identity is contained in a maximal ideal.
Apply this to the proper ideal from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Since
$$
x\in D_M,
$$
there exist
$$
c,s\in D
$$
with
$$
s\notin M
$$
such that
$$
x=\frac cs.
$$


::: pf-proof

This is the definition of the localization
$$
D_M.
$$

:::

:::

::: {.pf-step #s1-9}

The denominator $s$ from step [](#s1-8){.pf-ref} belongs to $I_x$.


::: pf-proof

From
$$
x=\frac cs,
$$
one has
$$
sx=c.
$$
Since
$$
c\in D,
$$
the definition of
$$
I_x
$$
gives
$$
s\in I_x.
$$

:::

:::

::: {.pf-step #s1-10}

This contradicts
$$
s\notin M.
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
I_x\subseteq M.
$$
Step [](#s1-9){.pf-ref} gives
$$
s\in I_x.
$$
Therefore
$$
s\in M,
$$
contradicting step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Hence
$$
x\in D.
$$


::: pf-proof

The assumption
$$
x\notin D
$$
leads to the contradiction in step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\bigcap_{M\in\mathcal M}D_M
\subseteq
D.
$$


::: pf-proof

The element
$$
x
$$
was arbitrary in the intersection, and step [](#s1-11){.pf-ref} shows it belongs to $D$.

:::

:::

::: {.pf-step #s1-13}

Combining both inclusions,
$$
\boxed{
\bigcap_{M\in\mathcal M}D_M
=
D.
}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives
$$
D
\subseteq
\bigcap_M D_M,
$$
and step [](#s1-12){.pf-ref} gives the reverse inclusion.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required identity.

:::

:::

:::
