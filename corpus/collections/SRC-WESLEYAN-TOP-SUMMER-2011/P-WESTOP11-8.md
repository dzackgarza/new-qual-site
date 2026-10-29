---
schema: qual/card@1
id: P-WESTOP11-8
kind: problem
title: Boundary inclusion for a punctured genus-$2$ surface and obstruction to a retraction
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $X$ be the closed orientable genus-$2$ surface with the interior of a small disk removed, and let $A$ be the boundary circle of that disk.

Calculate the homomorphisms induced by the inclusion
$$
A\hookrightarrow X
$$
on the fundamental group and on homology. Use these maps to prove that $A$ is not a retract of $X$.
:::

::: {.solution}

Choose a basepoint
$$
x_0\in A
$$
and let
$$
i:A\hookrightarrow X
$$
be the inclusion.

::: pf

::: {.pf-step #s1-1}

The surface $X$ deformation retracts onto a wedge of four circles.


::: pf-proof

A compact connected orientable surface of genus $2$ with one boundary
component has a spine consisting of the standard four curves
$$
a_1,b_1,a_2,b_2.
$$
Collapsing the complementary disk onto this spine gives
$$
X\simeq
S^1\vee S^1\vee S^1\vee S^1.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\pi_1(X,x_0)
\cong
F(a_1,b_1,a_2,b_2),
$$
the free group on four generators.


::: pf-proof

The fundamental group of a wedge of four circles is the free group on the
four circle generators, and deformation retraction preserves fundamental
groups.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\pi_1(A,x_0)
\cong
\ZZ.
$$
If
$$
c
$$
denotes the positively oriented generator of the boundary circle, then,
up to replacing $c$ by its inverse according to orientation convention,
$$
\boxed{
i_*(c)
=
[a_1,b_1][a_2,b_2].
}
$$


::: pf-proof

The standard polygonal presentation of the closed genus-$2$ surface has
attaching word
$$
[a_1,b_1][a_2,b_2].
$$
For the closed surface this word is killed by the $2$-cell.
Removing the interior of a disk removes that relation and turns the attaching
circle into the boundary component.
Thus the boundary generator is represented by the product of commutators.

:::

:::

::: {.pf-step #s1-4}

The induced homomorphism
$$
i_*:
\pi_1(A,x_0)
\to
\pi_1(X,x_0)
$$
is injective.


::: pf-proof

By step [](#s1-3){.pf-ref}, the generator of
$$
\pi_1(A)\cong\ZZ
$$
maps to
$$
w
\coloneqq
[a_1,b_1][a_2,b_2].
$$
This is a nontrivial reduced word in the free group $F_4$.
Since free groups are torsion-free,
$$
w^n=1
$$
implies
$$
n=0.
$$
Hence the homomorphism
$$
\ZZ\to F_4,
\qquad
n\mapsto w^n,
$$
is injective.

:::

:::

::: {.pf-step #s1-5}

The homology groups are
$$
H_0(A)\cong\ZZ,
\qquad
H_1(A)\cong\ZZ,
\qquad
H_j(A)=0\quad(j\ge2),
$$
and
$$
H_0(X)\cong\ZZ,
\qquad
H_1(X)\cong\ZZ^4,
\qquad
H_j(X)=0\quad(j\ge2).
$$


::: pf-proof

The groups for
$$
A\cong S^1
$$
are standard.
By step [](#s1-1){.pf-ref},
$$
X\simeq\bigvee^4S^1,
$$
whose cellular homology has one copy of $\ZZ$ in degree $0$, four
copies in degree $1$, and zero in higher degrees.

:::

:::

::: {.pf-step #s1-6}

On degree-$0$ homology,
$$
i_*:
H_0(A)
\to
H_0(X)
$$
is an isomorphism.


::: pf-proof

Both spaces are path-connected, and inclusion sends the unique path
component of $A$ into the unique path component of $X$.
Thus the induced map on
$$
H_0\cong\ZZ
$$
is the identity under the standard identifications.

:::

:::

::: {.pf-step #s1-7}

On degree-$1$ homology,
$$
\boxed{
i_*:
H_1(A)
\to
H_1(X)
\text{ is the zero homomorphism}.
}
$$


::: pf-proof

For a path-connected space,
$$
H_1(Y;\ZZ)
\cong
\pi_1(Y)^{\mathrm{ab}}.
$$
By step [](#s1-3){.pf-ref}, the boundary generator maps in the fundamental group to
$$
[a_1,b_1][a_2,b_2].
$$
Every commutator vanishes under abelianization, so this element maps to
zero in
$$
F_4^{\mathrm{ab}}
\cong
\ZZ^4.
$$
Thus the generator of
$$
H_1(A)\cong\ZZ
$$
maps to zero.

:::

:::

::: {.pf-step #s1-8}

In every degree
$$
j\ge2,
$$
the induced map
$$
i_*:H_j(A)\to H_j(X)
$$
is the zero map between zero groups.


::: pf-proof

This is immediate from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The boundary circle $A$ is not a retract of $X$.


::: pf-proof

Suppose there were a retraction
$$
r:X\to A.
$$
Then
$$
r\circ i
=
\operatorname{id}_A.
$$
Applying degree-$1$ homology gives
$$
r_*\circ i_*
=
\operatorname{id}_{H_1(A)}.
$$
But step [](#s1-7){.pf-ref} gives
$$
i_*=0,
$$
so
$$
r_*\circ i_*
=
0.
$$
Since
$$
H_1(A)\cong\ZZ\ne0,
$$
its identity map is nonzero, a contradiction.

:::

:::

::: {.pf-step #s1-10}

The same obstruction is visible directly on fundamental groups.


::: pf-proof

If a retraction existed, then
$$
r_*\circ i_*
=
\operatorname{id}_{\pi_1(A)}.
$$
But
$$
\pi_1(A)\cong\ZZ
$$
is abelian, so every homomorphism
$$
r_*:F_4\to\ZZ
$$
kills commutators.
Hence by step [](#s1-3){.pf-ref},
$$
r_*i_*(c)
=
r_*\bigl([a_1,b_1][a_2,b_2]\bigr)
=
0,
$$
whereas the identity on
$$
\ZZ
$$
would send $c$ to the nonzero generator $c$.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} compute the map on fundamental groups,
steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} compute the maps on homology,
and steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} prove that $A$ is not a retract of $X$.

:::

:::

:::
