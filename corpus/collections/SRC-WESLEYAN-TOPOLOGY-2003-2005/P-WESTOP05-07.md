---
schema: qual/card@1
id: P-WESTOP05-07
kind: problem
title: Fundamental group, first homology, and classification of an octagon quotient
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Take an octagon and identify its edges according to the cyclic word
$$
ab^{-1}cdc^{-1}bd^{-1}a.
$$
Find the fundamental group and first homology group of the resulting surface, and identify the surface in the standard classification.
:::

::: {.solution}

Label the octagon vertices cyclically by
$$
v_0,v_1,\dots,v_7,
$$
so the boundary edges are
$$
[v_0,v_1],\ [v_1,v_2],\dots,[v_7,v_0].
$$

The boundary word is
$$
a\,b^{-1}\,c\,d\,c^{-1}\,b\,d^{-1}\,a.
$$

## Vertex identifications

::: pf

::: {.pf-step #s1-1}

The two $a$-edges identify
$$
v_0\sim v_7
\qquad\text{and}\qquad
v_1\sim v_0.
$$


::: pf-proof

The first $a$-edge is oriented
$$
v_0\to v_1,
$$
and the final $a$-edge is oriented
$$
v_7\to v_0.
$$
Matching the arrows identifies starts with starts and ends with ends.

:::

:::

::: {.pf-step #s1-2}

The two $b$-edges identify
$$
v_2\sim v_5
\qquad\text{and}\qquad
v_1\sim v_6.
$$


::: pf-proof

The boundary edge $[v_1,v_2]$ is labeled $b^{-1}$, so its $b$-arrow
runs
$$
v_2\to v_1.
$$
The other $b$-edge runs
$$
v_5\to v_6.
$$
Match starts and ends.

:::

:::

::: {.pf-step #s1-3}

The two $c$-edges identify
$$
v_2\sim v_5
\qquad\text{and}\qquad
v_3\sim v_4.
$$


::: pf-proof

The $c$-edge $[v_2,v_3]$ is oriented
$$
v_2\to v_3,
$$
while the edge $[v_4,v_5]$ labeled $c^{-1}$ has $c$-orientation
$$
v_5\to v_4.
$$

:::

:::

::: {.pf-step #s1-4}

The two $d$-edges identify
$$
v_3\sim v_7
\qquad\text{and}\qquad
v_4\sim v_6.
$$


::: pf-proof

The $d$-edge $[v_3,v_4]$ is oriented
$$
v_3\to v_4,
$$
while the edge $[v_6,v_7]$ labeled $d^{-1}$ has $d$-orientation
$$
v_7\to v_6.
$$

:::

:::

::: {.pf-step #s1-5}

Hence there are exactly two vertex classes:
$$
\boxed{
A=\{v_0,v_1,v_3,v_4,v_6,v_7\}}
$$
and
$$
\boxed{
B=\{v_2,v_5\}}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} generate the displayed equivalence classes, and no listed
identification connects a vertex in $B$ to one in $A$.

:::

:::

::: pf-step

The quotient has
$$
\boxed{
V=2,\qquad E=4,\qquad F=1}.
$$


::: pf-proof

There are two vertex classes by step [](#s1-5){.pf-ref}, four paired edge classes
$a,b,c,d$, and one octagon interior.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\chi=V-E+F=2-4+1=-1}.
$$


::: pf-proof

Apply the cellular formula for Euler characteristic.

:::

:::

::: {.pf-step #s1-8}

The quotient surface is nonorientable.


::: pf-proof

The two occurrences of $a$ in the boundary word have the same orientation.
Thus the corresponding edge pair is glued with the boundary directions
matched rather than reversed. In the polygon classification of surfaces,
such a same-direction pair produces a crosscap, hence nonorientability.

:::

:::

::: pf-step

A closed connected nonorientable surface of genus $k$ has
$$
\chi=2-k.
$$


::: pf-proof

Its standard polygon has one vertex, $k$ edge classes, and one face, so
$$
\chi=1-k+1=2-k.
$$

:::

:::

::: {.pf-step #s1-10}

Since
$$
-1=2-k,
$$
one has
$$
\boxed{k=3}.
$$


::: pf-proof

Solve for $k$.

:::

:::

::: {.pf-step #s1-11}

Hence the quotient is
$$
\boxed{
N_3
=
\RP^2\#\RP^2\#\RP^2}.
$$


::: pf-proof

The quotient is closed and connected, is nonorientable by step [](#s1-8){.pf-ref}, and
has nonorientable genus $3$ by step [](#s1-10){.pf-ref}. Apply the classification of
closed surfaces.

:::

:::

::: pf-step

In the quotient $1$-skeleton, the $a$- and $d$-edges are loops
at $A$, while the $b$- and $c$-edges join $B$ to $A$.


::: pf-proof

From the vertex classes in step [](#s1-5){.pf-ref}:
the $a$-edge has endpoints in $A$, the $d$-edge has endpoints in $A$,
and representatives for $b,c$ have one endpoint in $B$ and the other in
$A$.

:::

:::

::: pf-step

Choose the $c$-edge as a maximal tree in the $1$-skeleton.


::: pf-proof

There are two vertices $A,B$, and the $c$-edge joins them. A single edge
joining the two vertices is a maximal tree.

:::

:::

::: pf-step

Collapsing this tree identifies $A$ and $B$ and does not change
the fundamental group.


::: pf-proof

Collapsing a maximal tree in a connected graph is a homotopy equivalence and
is the standard step in obtaining a presentation from a CW complex.

:::

:::

::: {.pf-step #s1-15}

After setting $c=1$, the $2$-cell attaching word becomes
$$
\boxed{
a\,b^{-1}\,d\,b\,d^{-1}\,a}.
$$


::: pf-proof

Start with
$$
a\,b^{-1}\,c\,d\,c^{-1}\,b\,d^{-1}\,a
$$
and replace $c,c^{-1}$ by the identity after the tree collapse.

:::

:::

::: pf-step

Thus
$$
\boxed{
\pi_1
\cong
\left\langle
a,b,d
\ \presentationbar\
a\,b^{-1}dbd^{-1}a=1
\right\rangle}.
$$


::: pf-proof

The collapsed $1$-skeleton is a wedge of three circles $a,b,d$, and the
single $2$-cell imposes the relation from step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

Cyclically conjugating the relator gives the equivalent presentation
$$
\boxed{
\pi_1
\cong
\left\langle
a,b,d
\ \presentationbar\
a^2[b^{-1},d]=1
\right\rangle}.
$$


::: pf-proof

The relator
$$
a\,b^{-1}dbd^{-1}a
$$
is cyclically conjugate to
$$
a^2b^{-1}dbd^{-1}
=
a^2[b^{-1},d].
$$
Replacing a relator by a conjugate does not change its normal closure.

:::

:::

::: pf-step

By the surface classification, this group is also isomorphic to the
standard nonorientable genus-$3$ surface group
$$
\boxed{
\left\langle
x,y,z
\ \presentationbar\
x^2y^2z^2=1
\right\rangle}.
$$


::: pf-proof

Step [](#s1-11){.pf-ref} identifies the underlying surface with
$$
N_3=\#^3\RP^2,
$$
whose standard polygon presentation has the displayed fundamental group.

:::

:::

::: pf-step

Abelianizing the presentation in step [](#s1-17){.pf-ref} kills the commutator
$$
[b^{-1},d].
$$


::: pf-proof

Every commutator is trivial in an abelian group.

:::

:::

::: pf-step

Hence the only remaining relation in the abelianization is
$$
\boxed{2a=0}.
$$


::: pf-proof

The relator
$$
a^2[b^{-1},d]
$$
becomes
$$
a^2
$$
after abelianization.

:::

:::

::: {.pf-step #s1-21}

Therefore
$$
\boxed{
H_1
\cong
\pi_1^{\mathrm{ab}}
\cong
\ZZ\langle b\rangle
\oplus
\ZZ\langle d\rangle
\oplus
\ZZ/2\langle a\rangle}.
$$


::: pf-proof

The generators $b,d$ remain free, while $a$ is subject only to
$2a=0$.

:::

:::

::: {.pf-step #s1-22}

Thus
$$
\boxed{
H_1
\cong
\ZZ^2\oplus\ZZ/2}.
$$


::: pf-proof

This is the group in step [](#s1-21){.pf-ref} written in standard form.

:::

:::

::: pf-qed

Step [](#s1-17){.pf-ref} gives a presentation of the fundamental group, step [](#s1-22){.pf-ref} gives
the first homology group, and step [](#s1-11){.pf-ref} identifies the surface as
$\#^3\RP^2$.

:::

:::

:::
