---
schema: qual/card@1
id: P-AGXVARIRRDECOMP
kind: problem
title: Unique decomposition of an affine algebraic set into irreducible components
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducible Components
  - Noetherian Spaces
  - Affine Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 2.6 and the corresponding clause of Exercises
    2.7 in the recorded source. The source defines "affine variety" to mean an
    irreducible Zariski-closed subset, then asks for the unique irreducible-
    component decomposition of an arbitrary Zariski-closed subset X' of A^n.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced "affine variety" by "Zariski-closed subset (affine algebraic
    set)". Under the source's own convention an affine variety is already
    irreducible, so the previous wording made the requested decomposition
    tautological and did not match the source exercise.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked Noetherianity from Hilbert basis theorem, existence by a minimal
    closed counterexample, and uniqueness by the finite-cover property of an
    irreducible subset. Cross-checked against the projective analogue
    P-AGH25NOETHERIAN.
---

::: {.problem}
Let $k$ be an algebraically closed field and let
$$
X\subseteq\AA^n_k
$$
be Zariski closed. Show that there is a unique finite decomposition
$$
X=X_1\union\cdots\union X_r
$$
into irreducible Zariski-closed subsets such that no $X_i$ is contained in a
different $X_j$. These subsets are the irreducible components of $X$.
:::

::: {.solution}
Uniqueness means uniqueness of the collection of components, without an
ordering. The empty set has the empty decomposition.

<1>1. The affine space $\AA^n_k$ is a Noetherian topological space.

::: {.proof}
Let
$$
Y_1\supseteq Y_2\supseteq\cdots
$$
be a descending chain of Zariski-closed subsets of $\AA^n_k$. Their vanishing
ideals form an ascending chain
$$
I(Y_1)\subseteq I(Y_2)\subseteq\cdots
$$
in
$$
k[x_1,\ldots,x_n].
$$
By the Hilbert basis theorem, this polynomial ring is Noetherian, so the chain
of ideals stabilizes. Since
$$
V(I(Y_i))=Y_i
$$
for every closed $Y_i$, the original chain of closed subsets also stabilizes.
Thus $\AA^n_k$ is Noetherian.
:::

<1>2. Every Zariski-closed subset of $\AA^n_k$ is a finite union of
irreducible Zariski-closed subsets.

::: {.proof}
Suppose otherwise. Among the closed subsets that admit no such finite
decomposition, choose one minimal under inclusion; this is possible by the
descending chain condition from step <1>1. Call it $Y$.

The set $Y$ is nonempty, because the empty set is the empty finite union. It
is not irreducible, because otherwise $Y$ itself would be a one-term
decomposition. Hence
$$
Y=A\union B
$$
for proper closed subsets
$$
A,B\subsetneq Y.
$$
By minimality of $Y$, both $A$ and $B$ are finite unions of irreducible
closed subsets. Combining those two finite decompositions gives one for $Y$,
a contradiction.

Therefore every closed subset admits a finite irreducible decomposition.
:::

<1>3. Every finite irreducible decomposition can be reduced to one in which
no member is contained in another.

::: {.proof}
Starting from a finite decomposition
$$
X=Y_1\union\cdots\union Y_s,
$$
delete any repeated member and any member $Y_i$ contained in another member
$Y_j$. Such a deletion does not change the union. Since there are only
finitely many members, this process terminates and leaves a finite
decomposition in which no distinct member contains another.
:::

<1>4. If an irreducible subset $T$ is contained in a finite union of closed
sets
$$
C_1\union\cdots\union C_s,
$$
then
$$
T\subseteq C_j
$$
for some $j$.

::: {.proof}
Inside the irreducible space $T$,
$$
T=(T\intersect C_1)\union\cdots\union(T\intersect C_s)
$$
is a finite union of closed subsets. For $s=2$, irreducibility says that one
of the two closed subsets is all of $T$. Induction on $s$ gives the same
conclusion for any finite number of closed subsets.
:::

<1>5. A decomposition satisfying the noncontainment condition is unique.

::: {.proof}
Suppose
$$
X=X_1\union\cdots\union X_r
=
Y_1\union\cdots\union Y_s
$$
are two finite decompositions into irreducible closed subsets, with no member
of either decomposition contained in a distinct member of the same
decomposition.

Fix $i$. Since
$$
X_i\subseteq Y_1\union\cdots\union Y_s,
$$
step <1>4 gives
$$
X_i\subseteq Y_j
$$
for some $j$. Applying step <1>4 to
$$
Y_j\subseteq X_1\union\cdots\union X_r
$$
gives
$$
Y_j\subseteq X_h
$$
for some $h$. Thus
$$
X_i\subseteq X_h.
$$
The noncontainment condition in the first decomposition forces $h=i$, so
$$
X_i=Y_j.
$$

Hence every $X_i$ occurs among the $Y_j$. By symmetry every $Y_j$ occurs
among the $X_i$. The two decompositions therefore have exactly the same
members.
:::

<1>6. The members of this unique decomposition are exactly the maximal
irreducible closed subsets of $X$.

::: {.proof}
Let $X_i$ be a member and suppose
$$
X_i\subseteq Z\subseteq X
$$
with $Z$ irreducible and closed. Since
$$
Z\subseteq X_1\union\cdots\union X_r,
$$
step <1>4 gives
$$
Z\subseteq X_j
$$
for some $j$. Then
$$
X_i\subseteq X_j,
$$
so the noncontainment condition gives $j=i$, and hence $Z=X_i$. Thus every
$X_i$ is maximal irreducible.

Conversely, step <1>4 shows that every irreducible closed subset of $X$ is
contained in some $X_i$, so every maximal irreducible closed subset is one of
the $X_i$.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove existence of a finite decomposition with the required
noncontainment property, step <1>5 proves uniqueness, and step <1>6 identifies
the members as the irreducible components.
:::
:::
