---
schema: qual/card@1
id: E-AHENA
kind: problem
title: Closed continuous surjections preserve normality
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 31 Exercise 6, printed p. 32
    (tmp/sources/munkres-solutions-anadeore.pdf), and "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017), Problem 31.6, printed p. 5
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), whose auxiliary Theorems 1-3 are the
    saturation lemma used here; checked against Munkres, Topology (2000), Section 31 Exercise 6,
    printed p. 199, and its printed hint. What was corrected: Orellana's proof writes
    P(W) <= Y - p(X - W) for a set she calls "P" and never defines, and then displays
    "Z = p(W) = p(W) <= p(U) = V", using p(U) where U is her open set and not the neighbourhood V;
    the card states the one identity that does the work, y in Y - p(X - U) iff p^{-1}(y) <= U,
    proves it, and derives closedness, containment and disjointness from it.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subsections suffice, and the
    18 leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: singletons of $Y$ are closed because $X$ is $T_1$ and $p$ is a closed
    surjection; the saturated open set $W_U=Y\setminus p(X\setminus U)$ is open and satisfies
    $p^{-1}(W_U)\subseteq U$, which is the exercise's hint; and for disjoint closed $A,B$ the sets
    $W_U,W_V$ built from separating $U,V$ contain $A,B$ and are disjoint because their preimages are.
    Checked against Munkres, Topology (2000), section 31 Exercise 7. Nothing in the statement was
    changed.

---

::: {.exercise}

Let $p: X \to Y$ be a closed continuous surjective map.
Show that if $X$ is normal, then so is $Y$.
[Hint: If $U$ is an open set containing $p^{-1}(\theset{y})$, show there is a neighborhood $W$ of $y$ such that $p^{-1}(W) \subset U$.]
:::

::: {.solution}
::: pf

::: pf-step
$T_1$ separation axiom on $Y$:

::: pf-proof

::: pf-step
For any $y \in Y$, surjectivity gives $x\in X$ with $p(x)=y$. Since $X$ is $T_1$, the singleton $\{x\}$ is closed in $X$. The map $p$ is closed, so $\{y\}=p(\{x\})$ is closed in $Y$.

::: pf-proof
A normal space is $T_1$, so the singleton $\{x\}$ is closed, and the image of a closed set under the closed map $p$ is closed.
:::

:::

::: pf-step
Hence $Y$ satisfies the $T_1$ axiom.

::: pf-proof
Every singleton of $Y$ is closed, which is the $T_1$ axiom.
:::

:::

:::

:::

::: {.pf-step #saturated-neighborhoods}
Pushing open saturated neighborhoods down via closed maps:

::: pf-proof

::: pf-step
For any open set $U \subseteq X$, define the saturated open set:
$$W_U = Y \setminus p(X \setminus U).$$

::: pf-proof
This is a definition: the set of points of $Y$ whose entire fibre lies in $U$.
:::

:::

::: pf-step
Since $X \setminus U$ is closed in $X$ and $p$ is a closed map, $p(X \setminus U)$ is closed in $Y$.

::: pf-proof
The image of a closed set under a closed map is closed.
:::

:::

::: pf-step
Therefore, $W_U$ is an open subset of $Y$.

::: pf-proof
$W_U$ is the complement of the closed set $p(X\setminus U)$.
:::

:::

::: pf-step
For any $y \in Y$, $y \in W_U \iff y \notin p(X \setminus U) \iff p^{-1}(\{y\}) \subseteq U$.

::: pf-proof
Unwinding the definition: $y$ is not the image of a point outside $U$ exactly when every point over $y$ lies in $U$.
:::

:::

::: pf-step
Thus $p^{-1}(W_U) \subseteq U$.

::: pf-proof
The equivalence of the preceding step holds for every point of $W_U$.
:::

:::

:::

:::

::: pf-step
Separation of disjoint closed sets in $Y$:

::: pf-proof

::: pf-step
Let $A$ and $B$ be disjoint closed subsets of $Y$.

::: pf-proof
These are arbitrary disjoint closed subsets, the data that normality of $Y$ quantifies over.
:::

:::

::: pf-step
By continuity of $p$, the preimages $p^{-1}(A)$ and $p^{-1}(B)$ are closed subsets of $X$.

::: pf-proof
Preimages of closed sets under a continuous map are closed.
:::

:::

::: pf-step
Since $A \cap B = \varnothing$, $p^{-1}(A) \cap p^{-1}(B) = p^{-1}(A \cap B) = \varnothing$.

::: pf-proof
A point cannot map into both $A$ and $B$.
:::

:::

::: pf-step
Since $X$ is normal, there exist disjoint open sets $U, V \subset X$ such that:
$$p^{-1}(A) \subseteq U \quad \text{and} \quad p^{-1}(B) \subseteq V.$$

::: pf-proof
Normality of $X$ separates the disjoint closed sets $p^{-1}(A)$ and $p^{-1}(B)$.
:::

:::

::: pf-step
Applying the construction from step [](#saturated-neighborhoods){.pf-ref}, let $W_U = Y \setminus p(X \setminus U)$ and $W_V = Y \setminus p(X \setminus V)$.

::: pf-proof
$W_U$ and $W_V$ are the saturated open sets just constructed from these $U$ and $V$.
:::

:::

::: pf-step
Both $W_U$ and $W_V$ are open in $Y$.

::: pf-proof
Each is the complement of the image of a closed set under the closed map $p$.
:::

:::

::: pf-step
For any $a \in A$, $p^{-1}(\{a\}) \subseteq p^{-1}(A) \subseteq U$, so $a \in W_U$; thus $A \subseteq W_U$.

::: pf-proof
The fibre over $a$ lies in $p^{-1}(A)\subseteq U$, which by the equivalence above puts $a$ in $W_U$.
:::

:::

::: pf-step
Symmetrically, $B \subseteq W_V$.

::: pf-proof
The same argument with the roles of $A$ and $B$ exchanged.
:::

:::

::: pf-step
**Disjointness:** $p^{-1}(W_U \cap W_V) = p^{-1}(W_U) \cap p^{-1}(W_V) \subseteq U \cap V = \varnothing$.

::: pf-proof
Preimages commute with intersections, and the two preimages lie in the disjoint sets $U$ and $V$.
:::

:::

::: pf-step
Since $p$ is surjective, the empty preimage implies $W_U \cap W_V = \varnothing$.

::: pf-proof
A surjective map hits every point, so a set with empty preimage is empty.
:::

:::

:::

:::

::: pf-step
$A$ and $B$ are separated by disjoint open sets $W_U$ and $W_V$, so $Y$ is normal.

::: pf-proof
Disjoint closed sets have disjoint open neighbourhoods, and $Y$ is $T_1$ by the first part.
:::

:::

:::

:::
