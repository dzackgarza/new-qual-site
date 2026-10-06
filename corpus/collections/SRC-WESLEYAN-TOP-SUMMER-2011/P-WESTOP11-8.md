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
\[
A\hookrightarrow X
\]
on the fundamental group and on homology. Use these maps to prove that $A$ is not a retract of $X$.
:::

::: {.solution}
Choose a basepoint
\[
x_0\in A
\]
and let
\[
i:A\hookrightarrow X
\]
be the inclusion.

<1>1. The surface $X$ deformation retracts onto a wedge of four circles.

::: {.proof}
A compact connected orientable surface of genus $2$ with one boundary
component has a spine consisting of the standard four curves
\[
a_1,b_1,a_2,b_2.
\]
Collapsing the complementary disk onto this spine gives
\[
X\simeq
S^1\vee S^1\vee S^1\vee S^1.
\]
:::

<1>2. Therefore
\[
\pi_1(X,x_0)
\cong
F(a_1,b_1,a_2,b_2),
\]
the free group on four generators.

::: {.proof}
The fundamental group of a wedge of four circles is the free group on the
four circle generators, and deformation retraction preserves fundamental
groups.
:::

<1>3. One has
\[
\pi_1(A,x_0)
\cong
\mathbb Z.
\]
If
\[
c
\]
denotes the positively oriented generator of the boundary circle, then,
up to replacing $c$ by its inverse according to orientation convention,
\[
\boxed{
i_*(c)
=
[a_1,b_1][a_2,b_2].
}
\]

::: {.proof}
The standard polygonal presentation of the closed genus-$2$ surface has
attaching word
\[
[a_1,b_1][a_2,b_2].
\]
For the closed surface this word is killed by the $2$-cell.
Removing the interior of a disk removes that relation and turns the attaching
circle into the boundary component.
Thus the boundary generator is represented by the product of commutators.
:::

<1>4. The induced homomorphism
\[
i_*:
\pi_1(A,x_0)
\to
\pi_1(X,x_0)
\]
is injective.

::: {.proof}
By step <1>3, the generator of
\[
\pi_1(A)\cong\mathbb Z
\]
maps to
\[
w
\coloneqq
[a_1,b_1][a_2,b_2].
\]
This is a nontrivial reduced word in the free group $F_4$.
Since free groups are torsion-free,
\[
w^n=1
\]
implies
\[
n=0.
\]
Hence the homomorphism
\[
\mathbb Z\to F_4,
\qquad
n\mapsto w^n,
\]
is injective.
:::

<1>5. The homology groups are
\[
H_0(A)\cong\mathbb Z,
\qquad
H_1(A)\cong\mathbb Z,
\qquad
H_j(A)=0\quad(j\ge2),
\]
and
\[
H_0(X)\cong\mathbb Z,
\qquad
H_1(X)\cong\mathbb Z^4,
\qquad
H_j(X)=0\quad(j\ge2).
\]

::: {.proof}
The groups for
\[
A\cong S^1
\]
are standard.
By step <1>1,
\[
X\simeq\bigvee^4S^1,
\]
whose cellular homology has one copy of $\mathbb Z$ in degree $0$, four
copies in degree $1$, and zero in higher degrees.
:::

<1>6. On degree-$0$ homology,
\[
i_*:
H_0(A)
\to
H_0(X)
\]
is an isomorphism.

::: {.proof}
Both spaces are path-connected, and inclusion sends the unique path
component of $A$ into the unique path component of $X$.
Thus the induced map on
\[
H_0\cong\mathbb Z
\]
is the identity under the standard identifications.
:::

<1>7. On degree-$1$ homology,
\[
\boxed{
i_*:
H_1(A)
\to
H_1(X)
\text{ is the zero homomorphism}.
}
\]

::: {.proof}
For a path-connected space,
\[
H_1(Y;\mathbb Z)
\cong
\pi_1(Y)^{\mathrm{ab}}.
\]
By step <1>3, the boundary generator maps in the fundamental group to
\[
[a_1,b_1][a_2,b_2].
\]
Every commutator vanishes under abelianization, so this element maps to
zero in
\[
F_4^{\mathrm{ab}}
\cong
\mathbb Z^4.
\]
Thus the generator of
\[
H_1(A)\cong\mathbb Z
\]
maps to zero.
:::

<1>8. In every degree
\[
j\ge2,
\]
the induced map
\[
i_*:H_j(A)\to H_j(X)
\]
is the zero map between zero groups.

::: {.proof}
This is immediate from step <1>5.
:::

<1>9. The boundary circle $A$ is not a retract of $X$.

::: {.proof}
Suppose there were a retraction
\[
r:X\to A.
\]
Then
\[
r\circ i
=
\operatorname{id}_A.
\]
Applying degree-$1$ homology gives
\[
r_*\circ i_*
=
\operatorname{id}_{H_1(A)}.
\]
But step <1>7 gives
\[
i_*=0,
\]
so
\[
r_*\circ i_*
=
0.
\]
Since
\[
H_1(A)\cong\mathbb Z\ne0,
\]
its identity map is nonzero, a contradiction.
:::

<1>10. The same obstruction is visible directly on fundamental groups.

::: {.proof}
If a retraction existed, then
\[
r_*\circ i_*
=
\operatorname{id}_{\pi_1(A)}.
\]
But
\[
\pi_1(A)\cong\mathbb Z
\]
is abelian, so every homomorphism
\[
r_*:F_4\to\mathbb Z
\]
kills commutators.
Hence by step <1>3,
\[
r_*i_*(c)
=
r_*\bigl([a_1,b_1][a_2,b_2]\bigr)
=
0,
\]
whereas the identity on
\[
\mathbb Z
\]
would send $c$ to the nonzero generator $c$.
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>2--<1>4 compute the map on fundamental groups,
steps <1>5--<1>8 compute the maps on homology,
and steps <1>9--<1>10 prove that $A$ is not a retract of $X$.
:::
:::
