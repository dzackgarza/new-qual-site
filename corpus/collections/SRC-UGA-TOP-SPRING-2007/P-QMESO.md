---
schema: qual/card@1
id: P-QMESO
kind: problem
title: $H_n(X)\cong H_n(A)\oplus G_n$ when $A$ is a retract of $X$
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 8 of the official UGA Spring 2007 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used functoriality of singular homology: for the inclusion i:A->X and a
    retraction r:X->A, r_* i_*=id. Thus r_* is a split surjection with section
    i_*, and H_n(X)=im(i_*) direct-sum ker(r_*). Taking G_n=ker(r_*) gives the
    required decomposition. Compare Hatcher, Algebraic Topology, Proposition
    2.9 and the functoriality identities immediately following it.
---

::: problem
Prove that if $A$ is a retract of the topological space $X$, then for all nonnegative integers $n$ there is a group $G_n$ such that $H_{n} (X) \cong H_{n} (A) \oplus G_n$.

> Here $H_{n}$ denotes the $n$th singular homology group with integer coefficients.
:::

::: {.solution}
Let
\[
i:A\hookrightarrow X
\]
be the inclusion and let
\[
r:X\longrightarrow A
\]
be a retraction, so that
\[
r\circ i=\operatorname{id}_A.
\]
Fix $n\ge0$.

<1>1. The induced homomorphisms satisfy
\[
r_*\circ i_*=\operatorname{id}_{H_n(A)}.
\]
::: {.proof}
Singular homology is functorial.
Therefore
\[
r_*\circ i_*=(r\circ i)_*=(\operatorname{id}_A)_*
=\operatorname{id}_{H_n(A)}.
\]
:::

<1>2. The map
\[
i_*:H_n(A)\longrightarrow H_n(X)
\]
is injective, and
\[
r_*:H_n(X)\longrightarrow H_n(A)
\]
is surjective.
::: {.proof}
If $i_*(a)=0$, then by <1>1
\[
a=r_*i_*(a)=0,
\]
so $i_*$ is injective.

For every $a\in H_n(A)$,
\[
r_*(i_*(a))=a
\]
by <1>1, so $r_*$ is surjective.
:::

<1>3. Every $x\in H_n(X)$ has a decomposition
\[
x=i_*r_*(x)+\bigl(x-i_*r_*(x)\bigr)
\]
with
\[
i_*r_*(x)\in\operatorname{im}i_*,
\qquad
x-i_*r_*(x)\in\ker r_*.
\]
::: {.proof}
The first membership is immediate.
For the second, <1>1 gives
\[
r_*\bigl(x-i_*r_*(x)\bigr)
=r_*(x)-r_*i_*r_*(x)
=r_*(x)-r_*(x)
=0.
\]
:::

<1>4. The intersection
\[
\operatorname{im}i_*\cap\ker r_*
\]
is trivial.
::: {.proof}
Let $y$ lie in the intersection.
Write
\[
y=i_*(a)
\]
for some $a\in H_n(A)$.
Since $y\in\ker r_*$,
\[
0=r_*(y)=r_*i_*(a)=a
\]
by <1>1. Hence $y=i_*(0)=0$.
:::

<1>5. Hence
\[
H_n(X)=\operatorname{im}i_*\oplus\ker r_*
\cong H_n(A)\oplus\ker r_*.
\]
::: {.proof}
By <1>3 the two displayed subgroups generate $H_n(X)$, and by <1>4 their intersection is zero.
Thus the sum is direct.
By <1>2, $i_*$ identifies $H_n(A)$ isomorphically with $\operatorname{im}i_*$.
:::

Taking
\[
\boxed{G_n=\ker\bigl(r_*:H_n(X)\to H_n(A)\bigr)}
\]
gives
\[
\boxed{H_n(X)\cong H_n(A)\oplus G_n}
\]
for every $n\ge0$.
:::
