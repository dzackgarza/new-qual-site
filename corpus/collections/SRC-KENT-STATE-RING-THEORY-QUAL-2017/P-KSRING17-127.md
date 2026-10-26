---
schema: qual/card@1
id: P-KSRING17-127
kind: problem
title: A domain is the intersection of its localizations at maximal ideals
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 127 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be an integral domain and F its field of fractions.
Denote by M the set of all maximal ideals of D. For $M \in \mathcal { M }$ , let $\begin{array} { r } { D _ { M } = \{ \frac { a } { s } \ | \ a , s \in D , s \not \in M \} \subset F } \end{array}$ . Show that $\bigcap _ { M \in { \mathcal { M } } } D _ { M } = D$
:::

::: pf

::: pf-step

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

::: pf-step

Therefore
$$
D
\subseteq
\bigcap_{M\in\mathcal M}D_M.
$$


::: pf-proof

Step <1>1 holds for every maximal ideal $M$.

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

::: pf-step

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

::: pf-step

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

By step <1>5,
$$
x\notin D
$$
implies
$$
I_x\ne D.
$$

:::

:::

::: pf-step

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
Apply this to the proper ideal from step <1>6.

:::

:::

::: pf-step

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

::: pf-step

The denominator $s$ from step <1>8 belongs to $I_x$.


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

::: pf-step

This contradicts
$$
s\notin M.
$$


::: pf-proof

By step <1>7,
$$
I_x\subseteq M.
$$
Step <1>9 gives
$$
s\in I_x.
$$
Therefore
$$
s\in M,
$$
contradicting step <1>8.

:::

:::

::: pf-step

Hence
$$
x\in D.
$$


::: pf-proof

The assumption
$$
x\notin D
$$
leads to the contradiction in step <1>10.

:::

:::

::: pf-step

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
was arbitrary in the intersection, and step <1>11 shows it belongs to $D$.

:::

:::

::: pf-step

Combining both inclusions,
$$
\boxed{
\bigcap_{M\in\mathcal M}D_M
=
D.
}
$$


::: pf-proof

Step <1>2 gives
$$
D
\subseteq
\bigcap_M D_M,
$$
and step <1>12 gives the reverse inclusion.

:::

:::

::: pf-qed

Step <1>13 is the required identity.

:::

:::
