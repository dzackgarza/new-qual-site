---
schema: qual/card@1
id: P-AMD-2GG7VEF2
kind: problem
title: $\pi_1(S^n)=1$ for $n\geq 2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Fourteen steps asserted their claim with no justification and each now carries one: the two poles as
    distinct points of the sphere, the complements as open sets, the two stereographic homeomorphisms with
    their inverse formulas, the convexity of $\RR^n$ with the straight-line contraction, the image of the
    opposite pole under stereographic projection, the identification $U \cap V \cong \RR^n \setminus
    \{0\}$, the deformation retraction onto $S^{n-1}$, the path-connectedness of $S^{n-1}$ for $n \ge 2$,
    the choice of basepoint in $U \cap V$, the three hypotheses of Seifert--van Kampen, the form of the
    theorem that gives the amalgamated product, and the triviality of the two factors from contractibility.
    Checked while writing: the intersection is path-connected only because $n \ge 2$, which is where
    $S^{n-1}$ first has positive dimension, and the triviality of the amalgam over a nontrivial subgroup
    still gives the trivial group because both factors are trivial. The sources are cited by statement,
    Seifert--van Kampen for the cover by two open path-connected sets; no page reference is on the card or
    in its events. The statement is unchanged. The collection retains the UCSD 290 problem sheets and no
    solutions, so the argument is the card's own.
---

::: {.problem}
Show $\pi_1(S^n) = 1$ for $n\geq 2$.
:::

::: {.solution}
::: pf

::: pf-step
$U = S^n \setminus \{S\}$ and $V = S^n \setminus \{N\}$, for the poles $N$ and $S$, are open and cover $S^n$.

::: pf-proof

::: pf-step
Let $N = (0, \dots, 0, 1) \in S^n \subset \RR^{n+1}$ (North pole) and $S = (0, \dots, 0, -1) \in S^n$ (South pole).

::: pf-proof
Both points have norm $1$ in $\RR^{n+1}$ and they differ in the last coordinate, so they are distinct points of $S^n$; the first is the north pole and the second the south pole.
:::

:::

::: pf-step
Define $U = S^n \setminus \{S\}$ and $V = S^n \setminus \{N\}$.

::: pf-proof
The formulas pick out the complements of the two poles inside $S^n$; the complements are nonempty, since $S^n$ has more than two points for $n \ge 1$.
:::

:::

::: pf-step
Since $\{S\}$ and $\{N\}$ are closed singletons in $S^n$, $U$ and $V$ are open in $S^n$.

::: pf-proof
A singleton in a metric space is closed, and the complement of a closed subset is open; so $U$ and $V$ are open in the subspace topology of $S^n$.
:::

:::

::: pf-step
$U \cup V = S^n$ because $N \neq S$, so no point in $S^n$ is equal to both $N$ and $S$.

::: pf-proof
Every point of $S^n$ is either not equal to $S$ (so it lies in $U$) or not equal to $N$ (so it lies in $V$); since $N \neq S$, the two sets cover $S^n$.
:::

:::

:::

:::

::: {.pf-step #s2}
$U$ and $V$ are contractible, hence simply connected.

::: pf-proof

::: pf-step
Stereographic projection from $S$ is a homeomorphism $U \to \RR^n$.

::: pf-proof
Stereographic projection from $S$ sends $p \ne S$ to the point where the line through $S$ and $p$ meets the equatorial hyperplane, given by $p \mapsto \frac{1}{1+p_{n+1}}(p_1,\dots,p_n)$; that formula is continuous and has the continuous inverse $y \mapsto \frac{1}{\norm{y}^2+1}(2y, \norm{y}^2 - 1)$, so it is a homeomorphism $U \to \RR^n$.
:::

:::

::: pf-step
Stereographic projection from $N$ is a homeomorphism $V \to \RR^n$.

::: pf-proof
The same construction with the pole $N$ in place of $S$ gives a continuous map $V \to \RR^n$ with continuous inverse $y \mapsto \frac{1}{\norm{y}^2+1}(2y, 1 - \norm{y}^2)$, so it too is a homeomorphism.
:::

:::

::: pf-step
$\RR^n$ is convex, hence contractible to the origin via straight-line homotopy $H(x, t) = (1-t)x$.

::: pf-proof
For $x, y \in \RR^n$ and $t \in [0,1]$ the combination $(1-t)x + ty$ again lies in $\RR^n$, which is convexity; the straight-line homotopy $H(x,t) = (1-t)x$ is continuous, fixes the origin for every $t$, and sends everything to $0$ at $t = 1$.
:::

:::

::: pf-step
Therefore, $U \simeq * \implies \pi_1(U, x_0) = 1$ and $V \simeq * \implies \pi_1(V, x_0) = 1$ for any basepoint $x_0 \in U \cap V$.

::: pf-proof
A homeomorphism preserves contractibility, and a contractible space is simply connected, so $\pi_1(U, x_0) = \pi_1(V, x_0) = 1$.
:::

:::

:::

:::

::: pf-step
The intersection $U \cap V = S^n \setminus \{N, S\}$ is path-connected for $n \geq 2$.

::: pf-proof

::: {.pf-step #s3-1}
Under stereographic projection $\phi \colon U \to \RR^n$, the pole $N$ maps to $0 \in \RR^n$.

::: pf-proof
The line through $S$ and the opposite pole $N$ is the last coordinate axis, which meets the equatorial hyperplane in the origin; so stereographic projection from $S$ carries $N$ to $0$.
:::

:::

::: {.pf-step #s3-2}
Thus $U \cap V = U \setminus \{N\} \cong \RR^n \setminus \{0\}$.

::: pf-proof
Removing the pole $N$ from $U$ corresponds under the homeomorphism $\phi$ to removing $\phi(N) = 0$ from $\RR^n$, and a homeomorphism restricts to a homeomorphism of the complements.
:::

:::

::: {.pf-step #s3-3}
$\RR^n \setminus \{0\}$ deformation retracts to $S^{n-1}$ via $x \mapsto \frac{x}{\norm{x}}$.

::: pf-proof
The map $r(x) = x/\norm{x}$ is continuous on $\RR^n \setminus \{0\}$ and fixes the unit sphere pointwise; the homotopy $H(x,t) = (1-t)x + t\,x/\norm{x}$ is continuous on the product, starts at the identity, ends in $S^{n-1}$ and fixes $S^{n-1}$ throughout.
:::

:::

::: {.pf-step #s3-4}
For $n \geq 2$, the sphere $S^{n-1}$ has dimension $n-1 \geq 1$, which is path-connected.

::: pf-proof
The sphere $S^m$ is path-connected for $m \ge 1$: two points that are not antipodal are joined by the normalized straight segment, and antipodal points by either half of a great circle. Here $m = n - 1 \ge 1$.
:::

:::

::: pf-step
Therefore, $\RR^n \setminus \{0\}$ is path-connected, which implies $U \cap V$ is path-connected.

::: pf-proof
By steps [](#s3-1){.pf-ref} and [](#s3-2){.pf-ref}, $U \cap V \cong \RR^n \setminus \{0\}$; by steps [](#s3-3){.pf-ref} and [](#s3-4){.pf-ref}, $\RR^n \setminus \{0\}$ deformation retracts to the path-connected sphere $S^{n-1}$ for $n \ge 2$, so $U \cap V$ is nonempty and path-connected.
:::

:::

:::

:::

::: pf-step
$\pi_1(S^n, x_0) = 1$.

::: pf-proof

::: pf-step
Let $x_0 \in U \cap V$ be the basepoint.

::: pf-proof
The intersection $U \cap V$ is nonempty because $S^n$ has points other than the two poles when $n \ge 1$, so a basepoint can be chosen in it; that choice is fixed for the rest of the argument.
:::

:::

::: pf-step
The hypotheses of the Seifert-van Kampen theorem are satisfied: $U, V$ are open, $U \cup V = S^n$, and $U \cap V$ is path-connected.

::: pf-proof
$U$ and $V$ are open by the first part, they cover $S^n$, their intersection is path-connected by the previous part, and $x_0$ lies in that intersection; these are exactly the hypotheses the theorem requires of the cover.
:::

:::

::: {.pf-step #s4-3}
The theorem gives an isomorphism: $$\pi_1(S^n, x_0) \cong \pi_1(U, x_0) *_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0).$$

::: pf-proof
Seifert--van Kampen, in the form for a cover by two open path-connected sets with path-connected intersection, says that the fundamental group of the union is the amalgamated free product of the two fundamental groups over the fundamental group of the intersection, all based at $x_0$.
:::

:::

::: pf-step
By step [](#s2){.pf-ref}, $\pi_1(U, x_0) = 1$ and $\pi_1(V, x_0) = 1$.

::: pf-proof
Step [](#s2){.pf-ref} shows $U$ and $V$ are contractible, and a contractible space has trivial fundamental group at every basepoint, so both groups are trivial.
:::

:::

::: pf-step
The amalgamated free product of two trivial groups is trivial: $1 *_{\pi_1(U \cap V, x_0)} 1 = 1$.

::: pf-proof
Substituting $\pi_1(U, x_0) = 1$ and $\pi_1(V, x_0) = 1$ from step [](#s2){.pf-ref} into the van Kampen isomorphism of step [](#s4-3){.pf-ref} gives $\pi_1(S^n, x_0) \cong 1 *_{\pi_1(U \cap V, x_0)} 1 = 1$.
:::

:::

:::

:::

:::
:::
