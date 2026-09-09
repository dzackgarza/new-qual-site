---
schema: qual/card@1
id: E-HAT-1.2-18
kind: problem
title: Suspension vs reduced suspension of convergent sequence; reduced suspension of contractible space need not be contractible
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Suspension
  - Mapping Cone
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 18 and Example 1.25; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Proved finite edge-crossing for loops in the unreduced suspension by uniform continuity, used finite retractions for freeness, and factored the Hawaiian-earring winding map through the mapping-cone quotient.
---

In this problem we use the notions of suspension, reduced suspension, cone, and mapping cone defined in Chapter 0. Let $X$ be the subspace of $\mathbb{R}$ consisting of the sequence $1, {^1/_2}, {^1/_3}, {^1/_4}, \cdots$ together with its limit point 0.

(a) For the suspension $SX$, show that $\pi_1(SX)$ is free on a countably infinite set of generators, and deduce that $\pi_1(SX)$ is countable.
In contrast to this, the reduced suspension $\Sigma X$, obtained from $SX$ by collapsing the segment $\{0\} \times I$ to a point, is the shrinking wedge of circles in Example 1.25, with an uncountable fundamental group.

(b) Let $C$ be the mapping cone of the quotient map $SX \to \Sigma X$.
Show that $\pi_1(C)$ is uncountable by constructing a homomorphism from $\pi_1(C)$ onto $\Pi_\infty \mathbb{Z} / \oplus_\infty \mathbb{Z}$.
Note that $C$ is the reduced suspension of the cone $CX$.
Thus the reduced suspension of a contractible space need not be contractible, unlike the unreduced suspension.

::: {.solution}
Write
\[
x_n=\frac1n\quad(n\ge1),
\qquad x_0=0.
\]
In $SX$, let $E_n$ be the suspension arc coming from $\{x_n\}\times I$, and let $S,N$ be the two suspension vertices.
Thus $SX$ is the union of the countably many arcs $E_n$, all with endpoints $S,N$, with $E_n$ accumulating onto $E_0$.

<1>1. Any loop in $SX$ crosses from $S$ to $N$, or from $N$ to $S$, only finitely many times.
::: {.proof}
The suspension coordinate defines a continuous function
\[
h:SX\to I,
\qquad
h(S)=0,\quad h(N)=1,\quad h([x,t])=t.
\]
For a loop $\gamma:I\to SX$, the composite $h\gamma:I\to I$ is uniformly continuous.
Choose $\delta>0$ such that
\[
|s-t|<\delta
\quad\Longrightarrow\quad
|h\gamma(s)-h\gamma(t)|<\frac12.
\]
Any subinterval on which $\gamma$ goes from $S$ to $N$ or from $N$ to $S$ has endpoints whose $h\gamma$-values differ by $1$, hence must have length at least $\delta$.
There can be only finitely many pairwise disjoint such subintervals in $I$.
:::

<1>2. Every loop in $SX$ is homotopic to a finite edge loop using only finitely many arcs $E_n$.
::: {.proof}
Away from $S$ and $N$ one has
\[
SX\setminus\{S,N\}\cong X\times(0,1).
\]
Since $X$ is totally disconnected, each path component of this complement is one open arc
\[
E_n\setminus\{S,N\}.
\]
Thus between successive visits to $S$ or $N$, the loop stays in a single $E_n$.

An excursion that leaves $S$ along one arc and returns to $S$ without reaching $N$ is homotopic rel endpoints to the constant path inside that interval arc; likewise for excursions based at $N$.
After deleting these inessential excursions, every remaining piece crosses between $S$ and $N$.
There are only finitely many such pieces by <1>1.
Hence the loop is homotopic to a finite concatenation of full traversals of finitely many $E_n$'s.
:::

<1>3. For $n\ge1$, let $a_n$ be the loop that travels from $S$ to $N$ along $E_n$ and returns from $N$ to $S$ along $E_0$.
Then the classes $[a_n]$ generate $\pi_1(SX)$.
::: {.proof}
By <1>2, every loop is a finite edge loop.
Insert or delete occurrences of $E_0\bar E_0$ between successive traversals to rewrite each full traversal of $E_n$ relative to the reference edge $E_0$.
The resulting loop is a finite word in the $a_n$ and their inverses.
:::

<1>4. The classes $[a_n]$ satisfy no nontrivial finite relation.
::: {.proof}
Fix $m$ and let
\[
K_m=E_0\cup E_1\cup\cdots\cup E_m.
\]
Define
\[
r_m:X\to\{x_0,x_1,\dots,x_m\}
\]
by fixing $x_0,x_1,\dots,x_m$ and sending every $x_n$ with $n>m$ to $x_0$.
This map is continuous: the only nonisolated point of $X$ is $x_0$, and the entire tail is sent to $x_0$.
Suspending $r_m$ gives a retraction
\[
R_m:SX\to K_m.
\]

The finite graph $K_m$ consists of $m+1$ parallel edges between $S$ and $N$, so
\[
\pi_1(K_m)\cong F(a_1,\dots,a_m).
\]
If a reduced word in $a_1,\dots,a_m$ were nullhomotopic in $SX$, applying $(R_m)_*$ would make the same reduced word trivial in this free group, which is impossible.
Thus there is no nontrivial finite relation among the $[a_n]$.
:::

<1>5. Therefore
\[
\boxed{
\pi_1(SX)\cong F(a_1,a_2,\dots),
}
\]
the free group on countably infinitely many generators; in particular, $\pi_1(SX)$ is countable.
::: {.proof}
Generation is <1>3 and freeness is <1>4.
A word in a countable alphabet has finite length, and the set of all finite words in a countable alphabet is countable.
:::

<1>6. Collapsing $E_0$ gives the reduced suspension $\Sigma X$, the shrinking wedge of circles, and there is a surjective winding homomorphism
\[
\rho:\pi_1(\Sigma X)\longrightarrow\prod_{n=1}^{\infty}\mathbb Z.
\]
::: {.proof}
After $E_0$ is collapsed, each $E_n\cup E_0$ becomes a circle $C_n$, and the diameters of these circles shrink to the common basepoint.
This is the shrinking wedge of circles of Example 1.25.
For each $n$, collapse all circles except $C_n$ to the basepoint to obtain a retraction
\[
s_n:\Sigma X\to C_n.
\]
The product of the induced winding-number homomorphisms is $\rho$.

Given any integer sequence $(k_n)$, traverse $C_n$ exactly $k_n$ times during a sequence of time intervals accumulating at $1$.
Since the circles shrink to the basepoint, the resulting infinite concatenation is continuous at the limiting time.
Its image under $\rho$ is $(k_n)$, so $\rho$ is surjective.
:::

<1>7. Let
\[
q:SX\to\Sigma X
\]
be the quotient map.
Then
\[
\rho\bigl(q_*(\pi_1(SX))\bigr)
=
\bigoplus_{n=1}^{\infty}\mathbb Z.
\]
::: {.proof}
By <1>5, $\pi_1(SX)$ is generated by the loops $a_n$.
The quotient $q$ sends $a_n$ to the standard loop once around $C_n$.
Therefore
\[
\rho(q_*[a_n])=e_n,
\]
the $n$th standard basis vector.
Every element of $\pi_1(SX)$ is a finite word, so its coordinate vector has finite support.
Conversely every finite-support integer sequence is a finite integral combination of the $e_n$ and is therefore obtained from a finite product of powers of the $a_n$.
:::

<1>8. If $C$ is the mapping cone of $q$, then
\[
\pi_1(C)
\cong
\pi_1(\Sigma X)/\left\langle\!\left\langle q_*(\pi_1(SX))\right\rangle\!\right\rangle .
\]
::: {.proof}
Write the mapping cone as
\[
C=\Sigma X\cup_q CSX.
\]
Use open neighborhoods of the two displayed pieces whose intersection deformation retracts onto $SX$.
The cone $CSX$ is contractible, while the other piece deformation retracts onto $\Sigma X$.
Van Kampen therefore quotients $\pi_1(\Sigma X)$ by the normal closure of the image of $\pi_1(SX)$ under $q_*$.
:::

<1>9. The homomorphism $\rho$ induces a surjection
\[
\boxed{
\overline\rho:\pi_1(C)	woheadrightarrow
\frac{\prod_{n=1}^{\infty}\mathbb Z}
{\bigoplus_{n=1}^{\infty}\mathbb Z}.
}
\]
::: {.proof}
Let
\[
p:\prod_{n=1}^{\infty}\mathbb Z
\to
\left(\prod_{n=1}^{\infty}\mathbb Z\right)
/\left(\bigoplus_{n=1}^{\infty}\mathbb Z\right)
\]
be the quotient map.
By <1>7,
\[
(p\rho)\,q_*=0.
\]
The target is abelian, so $p\rho$ kills the normal closure of $q_*(\pi_1(SX))$.
By <1>8 it therefore factors uniquely through $\pi_1(C)$.
The factor $\overline\rho$ is surjective because both $\rho$ and $p$ are surjective.
:::

<1>10. The group $\pi_1(C)$ is uncountable.
::: {.proof}
The product
\[
\prod_{n=1}^{\infty}\mathbb Z
\]
has cardinality $2^{\aleph_0}$, whereas the direct sum
\[
\bigoplus_{n=1}^{\infty}\mathbb Z
\]
is countable.
Thus the quotient in <1>9 is uncountable.
Since it is a quotient of $\pi_1(C)$, the group $\pi_1(C)$ must also be uncountable.
:::

<1>11. The space $C$ is the reduced suspension of the cone $CX$, so a reduced suspension of a contractible space need not be contractible.
::: {.proof}
Writing out the two quotient constructions shows that forming the mapping cone of
\[
SX\to\Sigma X
\]
amounts to taking the suspension of $CX$ and collapsing the suspension line over the cone point; this is precisely the reduced suspension $\Sigma(CX)$.
The cone $CX$ is contractible.
But <1>10 gives
\[
\pi_1(C)\ne0,
\]
so $C\cong\Sigma(CX)$ is not contractible.
:::
:::
