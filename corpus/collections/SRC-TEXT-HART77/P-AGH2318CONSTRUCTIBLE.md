---
schema: qual/card@1
id: P-AGH2318CONSTRUCTIBLE
kind: problem
title: Constructible subsets of a Zariski space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Spaces
  - Constructible Sets
  - Specialization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.18 statement and the preceding Zariski-space specialization results.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a Zariski topological space.
A constructible subset of $X$ is a subset which belongs to the smallest family $\mathcal{F}$ of subsets such that every open subset is in $\mathcal{F}$, a finite intersection of elements of $\mathcal{F}$ is in $\mathcal{F}$, and the complement of an element of $\mathcal{F}$ is in $\mathcal{F}$.

a. A subset of $X$ is locally closed if it is the intersection of an open subset with a closed subset.
Show that a subset of $X$ is constructible if and only if it can be written as a finite disjoint union of locally closed subsets.

b. Show that a constructible subset of an irreducible Zariski space $X$ is dense if and only if it contains the generic point.
Furthermore, in that case it contains a nonempty open subset.

c. A subset $S$ of $X$ is closed if and only if it is constructible and stable under specialization.
Similarly, a subset $T$ of $X$ is open if and only if it is constructible and stable under generization.

d. If $f: X \to Y$ is a continuous map of Zariski spaces, then the inverse image of any constructible subset of $Y$ is a constructible subset of $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #locally-closed-is-constructible}
Every locally closed subset of $X$ is constructible.

::: pf-proof
A locally closed subset has the form
\[
U\cap F
\]
with $U$ open and $F$ closed.  The open set $U$ belongs to the defining family of constructible sets, and
\[
F=X\setminus(X\setminus F)
\]
is constructible because $X\setminus F$ is open and constructible sets are closed under complements.  Hence $U\cap F$ is constructible.
:::

:::

::: {.pf-step #finite-union-locally-closed-constructible}
Every finite union of locally closed subsets is constructible.

::: pf-proof
Constructible sets are closed under finite unions because
\[
A\cup B=X\setminus\bigl((X\setminus A)\cap(X\setminus B)\bigr).
\]
Apply step [](#locally-closed-is-constructible){.pf-ref} to the finitely many locally closed subsets.
:::

:::

::: {.pf-step #constructible-is-finite-disjoint-union}
Every constructible subset is a finite disjoint union of locally closed subsets.

::: pf-proof
Any given constructible set is obtained from finitely many open subsets
\[
U_1,\ldots,U_n
\]
by finitely many intersections and complements.  Consider the $2^n$ Boolean atoms
\[
A_\epsilon
=
\bigcap_{i=1}^n E_i,
\]
where each $E_i$ is either $U_i$ or $X\setminus U_i$.

The atoms are pairwise disjoint and partition $X$.  Each atom can be written as
\[
\left(\bigcap_{\epsilon_i=1}U_i\right)
\cap
\left(\bigcap_{\epsilon_i=0}(X\setminus U_i)\right),
\]
an intersection of an open subset with a closed subset, hence is locally closed.

Every Boolean expression in the $U_i$ is a union of those atoms on which the expression is true.  Since there are only finitely many atoms, the constructible set is a finite disjoint union of locally closed subsets.
:::

:::

::: {.pf-step #constructible-iff-finite-disjoint-union}
Thus a subset of $X$ is constructible if and only if it is a finite disjoint union of locally closed subsets.

::: pf-proof
Step [](#finite-union-locally-closed-constructible){.pf-ref} proves one direction and step [](#constructible-is-finite-disjoint-union){.pf-ref} proves the other.
:::

:::

::: {.pf-step #dense-constructible-contains-generic-point}
Let $X$ be irreducible with generic point $\eta$, and let $C\subseteq X$ be constructible and dense.  Then
\[
\boxed{\eta\in C.}
\]

::: pf-proof
By step [](#constructible-iff-finite-disjoint-union){.pf-ref}, write
\[
C=C_1\amalg\cdots\amalg C_r,
\qquad
C_i=U_i\cap F_i
\]
with $U_i$ open and $F_i$ closed.

Since $C$ is dense,
\[
X=\overline C
=
\overline{C_1}\cup\cdots\cup\overline{C_r}.
\]
The space $X$ is irreducible, so one of these finitely many closed subsets equals $X$.  Say
\[
\overline{C_i}=X.
\]
But $C_i\subseteq F_i$ and $F_i$ is closed, so
\[
X=\overline{C_i}\subseteq F_i,
\]
hence $F_i=X$.  Therefore
\[
C_i=U_i
\]
is a nonempty open subset of $X$.

By Hartshorne II.3.17(d), the generic point $\eta$ belongs to every nonempty open subset of an irreducible Zariski space.  Thus
\[
\eta\in U_i=C_i\subseteq C.
\]
:::

:::

::: {.pf-step #contains-generic-point-implies-dense}
Conversely, if a subset $C\subseteq X$ contains the generic point $\eta$, then it is dense.

::: pf-proof
Since
\[
\overline{\{\eta\}}=X
\]
and $\eta\in C$,
\[
X=\overline{\{\eta\}}\subseteq\overline C.
\]
Hence $\overline C=X$.
:::

:::

::: {.pf-step #dense-iff-contains-generic-point}
A constructible subset of an irreducible Zariski space is dense if and only if it contains the generic point; when dense, it contains a nonempty open subset.

::: pf-proof
The equivalence is steps [](#dense-constructible-contains-generic-point){.pf-ref} and [](#contains-generic-point-implies-dense){.pf-ref}.  In the proof of step [](#dense-constructible-contains-generic-point){.pf-ref}, density produced a locally closed piece $C_i$ for which the closed factor was all of $X$, so
\[
C_i=U_i
\]
was a nonempty open subset contained in $C$.
:::

:::

::: {.pf-step #closed-is-constructible-and-spec-stable}
Every closed subset of $X$ is constructible and stable under specialization.

::: pf-proof
A closed subset is the complement of an open set, hence constructible.  Hartshorne II.3.17(e) proves that closed subsets are stable under specialization.
:::

:::

::: {.pf-step #s-contains-component-generic-points}
Let $S\subseteq X$ be constructible and stable under specialization, and put
\[
Z=\overline S.
\]
Then $S$ contains the generic point of every irreducible component of $Z$.

::: pf-proof
Because $Z$ is a closed subset of the noetherian space $X$, it has finitely many irreducible components
\[
Z=Z_1\cup\cdots\cup Z_r.
\]
Let $\eta_i$ be the generic point of $Z_i$.

Remove the other components:
\[
O_i
=
Z_i\setminus\bigcup_{j\ne i}Z_j.
\]
This is a nonempty open subset of the irreducible space $Z_i$, and it contains $\eta_i$.

Since $S$ is dense in $Z$, the intersection
\[
S\cap O_i
\]
is dense in $O_i$.  It is constructible in the open subspace $O_i$.  The space $O_i$ is an irreducible Zariski space: it is an open subspace of a noetherian space, and its irreducible closed subsets acquire generic points by taking closures in $Z_i$.

Applying step [](#dense-iff-contains-generic-point){.pf-ref} to $S\cap O_i$ gives
\[
\eta_i\in S\cap O_i\subseteq S.
\]
:::

:::

::: {.pf-step #s-equals-closure-is-closed}
The subset $S$ from step [](#s-contains-component-generic-points){.pf-ref} equals its closure $Z$ and hence is closed.

::: pf-proof
By step [](#s-contains-component-generic-points){.pf-ref}, $S$ contains every generic point $\eta_i$ of an irreducible component $Z_i$.  Since $S$ is stable under specialization, it contains every specialization of $\eta_i$, i.e. all of
\[
\overline{\{\eta_i\}}=Z_i.
\]
Therefore
\[
Z=\bigcup_iZ_i\subseteq S.
\]
The reverse inclusion $S\subseteq Z$ is automatic, so $S=Z$ is closed.
:::

:::

::: {.pf-step #closed-iff-constructible-spec-stable}
Hence
\[
\boxed{
S\text{ is closed}
\iff
S\text{ is constructible and stable under specialization}.}
\]

::: pf-proof
Step [](#closed-is-constructible-and-spec-stable){.pf-ref} proves one direction and steps [](#s-contains-component-generic-points){.pf-ref} and [](#s-equals-closure-is-closed){.pf-ref} prove the converse.
:::

:::

::: {.pf-step #open-iff-constructible-gen-stable}
A subset $T\subseteq X$ is open if and only if it is constructible and stable under generization.

::: pf-proof
The complement of a constructible set is constructible.  Moreover $T$ is stable under generization exactly when its complement
\[
X\setminus T
\]
is stable under specialization.

Thus step [](#closed-iff-constructible-spec-stable){.pf-ref} applied to $X\setminus T$ gives
\[
T\text{ open}
\iff
X\setminus T\text{ closed}
\iff
T\text{ constructible and generization-stable}.
\]
:::

:::

::: {.pf-step #preimage-of-constructible-is-constructible}
If $f:X\to Y$ is continuous, the inverse image of every constructible subset of $Y$ is constructible in $X$.

::: pf-proof
Let
\[
\mathcal G
=
\{C\subseteq Y:f^{-1}(C)\text{ is constructible in }X\}.
\]
For every open $U\subseteq Y$, continuity makes $f^{-1}(U)$ open, hence constructible, so $U\in\mathcal G$.

The family $\mathcal G$ is closed under complements because
\[
f^{-1}(Y\setminus C)=X\setminus f^{-1}(C),
\]
and under finite intersections because inverse images commute with intersections.  Therefore $\mathcal G$ contains the smallest family generated from open subsets under complements and finite intersections, namely all constructible subsets of $Y$.
:::

:::

::: pf-qed
Step [](#constructible-iff-finite-disjoint-union){.pf-ref} proves part (a), step [](#dense-iff-contains-generic-point){.pf-ref} proves part (b), steps [](#closed-iff-constructible-spec-stable){.pf-ref} and [](#open-iff-constructible-gen-stable){.pf-ref} prove part (c), and step [](#preimage-of-constructible-is-constructible){.pf-ref} proves part (d).
:::

:::

:::
