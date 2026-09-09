---
schema: qual/card@1
id: P-O6M2P
kind: problem
title: Degree of a splitting field divides the factorial of the polynomial degree
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Permutations
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent discussion explicitly identifying the statement as Hungerford's splitting-fields exercise and against a graduate algebra exam guide reproducing the proof.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that if $f\in K[x]$ has degree $n$ and $F$ is a splitting field of $f$ over $K$, then $[F:K]$ divides $n!$.
:::

::: solution
We argue by strong induction on $n=\deg f$.

<1>1. The claim holds for $n\le1$.
::: proof
If $n=0$ or $1$, the polynomial already splits over $K$, so $F=K$ and
$[F:K]=1$, which divides $n!$.
:::

Assume $n\ge2$ and that the assertion holds for every polynomial of degree
strictly smaller than $n$ over every field.

<1>2. If $f$ is irreducible over $K$, then $[F:K]$ divides $n!$.
::: proof
Choose a root $\alpha\in F$. Irreducibility gives
\[
[K(\alpha):K]=n.
\]
Over $K(\alpha)$ one may write
\[
f(x)=(x-\alpha)g(x),
\qquad
\deg g=n-1.
\]
The field $F$ is a splitting field of $g$ over $K(\alpha)$: adjoining the roots
of $g$ to $K(\alpha)$ adjoins all roots of $f$.

By the induction hypothesis,
\[
[F:K(\alpha)]\mid(n-1)!.
\]
The tower law therefore gives
\[
[F:K]
=[F:K(\alpha)]\,[K(\alpha):K]
=n[F:K(\alpha)]
\mid n(n-1)!=n!.
\]
:::

<1>3. If $f$ is reducible over $K$, then $[F:K]$ divides $n!$.
::: proof
Write
\[
f(x)=g(x)h(x)
\]
with
\[
r=\deg g>0,
\qquad
s=\deg h>0,
\qquad
r+s=n.
\]
Let $E\subseteq F$ be the subfield generated over $K$ by all roots of $g$.
Then $E$ is a splitting field of $g$ over $K$, so by induction
\[
[E:K]\mid r!.
\]

Over $E$, the field $F$ is obtained by adjoining the roots of $h$, hence is a
splitting field of $h$ over $E$. Again by induction,
\[
[F:E]\mid s!.
\]
Thus
\[
[F:K]=[F:E][E:K]\mid r!s!.
\]
Finally,
\[
\frac{n!}{r!s!}=\binom{n}{r}\in\ZZ,
\]
so $r!s!\mid n!$. Hence $[F:K]\mid n!$.
:::

<1>4. Therefore the assertion holds for every degree $n$.
::: proof
Every polynomial is either irreducible or reducible. The two cases are covered
by <1>2 and <1>3, completing the strong induction.
:::
:::
