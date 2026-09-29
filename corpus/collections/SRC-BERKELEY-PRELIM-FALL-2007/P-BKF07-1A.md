---
schema: qual/card@1
id: P-BKF07-1A
kind: problem
title: Subrings of the Gaussian integers
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained quotient-group classification and
    verified multiplicative closure and uniqueness of the listed subrings.
---

::: {.problem}
Let
\[
\mathbb Z[i]=\{a+bi:a,b\in\mathbb Z\}.
\]
List all subrings of \(\mathbb Z[i]\), with each subring appearing exactly once.
:::

::: {.solution}

For every integer $n\ge1$, define
$$
R_n=\ZZ+n\ZZ i
=
\{a+nbi:a,b\in\ZZ\}.
$$

::: pf

::: {.pf-step #Rn-are-subrings}
The sets
$$
\ZZ,\qquad R_1,\qquad R_2,\qquad\ldots
$$
are subrings of $\ZZ[i]$.

::: pf-proof
The set $\ZZ$ is a subring. Fix $n\ge1$. Clearly $0,1\in R_n$, and
$R_n$ is closed under additive inverses and addition. If
$$
x=a+nbi,
\qquad
y=c+ndi
$$
belong to $R_n$, then
$$
xy
=
(ac-n^2bd)+n(ad+bc)i
\in
R_n.
$$
Thus $R_n$ is also a subring.
:::

:::

::: {.pf-step #subring-contains-Z}
Every subring $R\subseteq\ZZ[i]$ contains $\ZZ$.

::: pf-proof
Under the convention for rings and subrings used here, $R$ contains
the same identity $1$. Hence it contains every integer multiple of
$1$, so
$$
\ZZ\subseteq R.
$$
:::

:::

::: {.pf-step #subgroups-bijection}
Additive subgroups of $\ZZ[i]$ containing $\ZZ$ are in
bijection with subgroups of
$$
\ZZ[i]/\ZZ\cong\ZZ.
$$

::: pf-proof
The correspondence theorem for groups sends an additive subgroup
$H$ with
$$
\ZZ\subseteq H\subseteq\ZZ[i]
$$
to $H/\ZZ$. The quotient is isomorphic to $\ZZ$ via
$$
(a+bi)+\ZZ\longmapsto b.
$$
:::

:::

::: {.pf-step #inverse-images}
The inverse images of the subgroups of $\ZZ$ under the map in
step [](#subgroups-bijection){.pf-ref} are precisely
$$
\ZZ
$$
and
$$
R_n=\ZZ+n\ZZ i
\qquad(n\ge1).
$$

::: pf-proof
Every subgroup of the additive group $\ZZ$ is either $\{0\}$ or
$n\ZZ$ for a unique integer $n\ge1$. The inverse image of $\{0\}$ is
$\ZZ$. The inverse image of $n\ZZ$ consists exactly of the Gaussian
integers whose imaginary coefficient is divisible by $n$, namely
$R_n$.
:::

:::

::: {.pf-step #classification}
Every subring of $\ZZ[i]$ is exactly one member of the list in
step [](#Rn-are-subrings){.pf-ref}.

::: pf-proof
Let $R$ be a subring. By step [](#subring-contains-Z){.pf-ref}, it is an additive subgroup
containing $\ZZ$. Steps [](#subgroups-bijection){.pf-ref} and [](#inverse-images){.pf-ref} therefore show that
$$
R=\ZZ
$$
or
$$
R=R_n
$$
for some $n\ge1$.

The list has no repetitions: $\ZZ$ has only elements with imaginary
coefficient $0$, while $R_n$ contains $ni$; and if $R_m=R_n$, then
their imaginary-coordinate subgroups satisfy
$$
m\ZZ=n\ZZ,
$$
which forces $m=n$ for positive $m,n$.
:::

:::

::: {.pf-step #final-list}
Thus the complete classification is
$$
\boxed{
\ZZ,\quad
\ZZ+i\ZZ,\quad
\ZZ+2i\ZZ,\quad
\ZZ+3i\ZZ,\quad\ldots
}.
$$

::: pf-proof
Step [](#Rn-are-subrings){.pf-ref} shows that every listed set is a subring, and step [](#classification){.pf-ref}
shows that every subring occurs exactly once.
:::

:::

::: pf-qed
Step [](#final-list){.pf-ref} answers the problem.
:::

:::

:::
