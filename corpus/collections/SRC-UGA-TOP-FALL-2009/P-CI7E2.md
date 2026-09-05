---
schema: qual/card@1
id: P-CI7E2
kind: problem
title: Closed subsets and quotients $X/A$ of a normal space are normal
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Quotient Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the definition and conclusion against problem 2 of the official UGA Fall 2009 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the unproved closed-surjection theorem by a direct saturated-neighborhood proof and verified the Hausdorff clause for both A and X/A.
---

::: problem
Let $A$ be a closed subset of a normal topological space $X$.
Show that both $A$ and the quotient $X/A$ are normal.
:::

::: {.solution}
<1>1. The closed subspace $A$ is Hausdorff.
::: {.proof}
The space $X$ is normal, so by the definition in the problem it is Hausdorff.
Every subspace of a Hausdorff space is Hausdorff.
Therefore $A$, with its subspace topology, is Hausdorff.
:::

<1>2. Any two disjoint closed subsets of $A$ have disjoint open neighborhoods in $A$.
::: {.proof}
Let $C,D\subseteq A$ be disjoint and closed in $A$.
Since $A$ is closed in $X$, both $C$ and $D$ are closed in $X$.
Normality of $X$ gives disjoint open subsets $U,V\subseteq X$ with
\[
C\subseteq U,
\qquad
D\subseteq V.
\]
Then
\[
U\cap A
\qquad\text{and}\qquad
V\cap A
\]
are disjoint open subsets of $A$ containing $C$ and $D$, respectively.
:::

<1>3. Hence $A$ is normal.
::: {.proof}
Step <1>1 verifies the Hausdorff requirement, and <1>2 verifies separation of arbitrary disjoint closed subsets of $A$.
These are exactly the two conditions in the definition of normality given in the problem.
:::

<1>4. Let
\[
q:X\longrightarrow X/A
\]
be the quotient map collapsing $A$ to one point.
Then $q$ is a closed map.
::: {.proof}
Let $C\subseteq X$ be closed.
If $C\cap A=\varnothing$, then no additional point is introduced when one saturates $C$ under the quotient relation, so
\[
q^{-1}(q(C))=C.
\]
If $C\cap A\ne\varnothing$, then $q(C)$ contains the collapsed point and its full inverse image contains all of $A$, so
\[
q^{-1}(q(C))=C\cup A.
\]
In either case $q^{-1}(q(C))$ is closed in $X$ because both $A$ and $C$ are closed.

For a quotient map, a subset $F\subseteq X/A$ is closed exactly when $q^{-1}(F)$ is closed: this follows from the defining open-set criterion by taking complements.
Therefore $q(C)$ is closed in $X/A$.
Thus $q$ is closed.
:::

<1>5. The quotient $X/A$ is a $T_1$ space.
::: {.proof}
Let $y\in X/A$ and choose $x\in X$ with $q(x)=y$.
Since $X$ is Hausdorff, the singleton $\{x\}$ is closed in $X$.
By <1>4, its image
\[
q(\{x\})=\{y\}
\]
is closed in $X/A$.
Hence every singleton in $X/A$ is closed, which is the $T_1$ property.
:::

<1>6. Any two disjoint closed subsets of $X/A$ have disjoint open neighborhoods.
::: {.proof}
Let $F,G\subseteq X/A$ be disjoint closed subsets.
Their inverse images
\[
q^{-1}(F),
\qquad
q^{-1}(G)
\]
are disjoint closed subsets of $X$.
By normality of $X$, choose disjoint open sets $U,V\subseteq X$ such that
\[
q^{-1}(F)\subseteq U,
\qquad
q^{-1}(G)\subseteq V.
\]

Define
\[
U'= (X/A)\setminus q(X\setminus U),
\qquad
V'= (X/A)\setminus q(X\setminus V).
\]
The complements $X\setminus U$ and $X\setminus V$ are closed, so <1>4 implies that their images are closed.
Hence $U'$ and $V'$ are open.

If $y\in F$, then the whole fiber
\[
q^{-1}(y)\subseteq q^{-1}(F)\subseteq U,
\]
so the fiber does not meet $X\setminus U$.
Thus $y\notin q(X\setminus U)$ and hence $y\in U'$.
Therefore $F\subseteq U'$; similarly $G\subseteq V'$.

Finally, if $y\in U'\cap V'$, then the nonempty fiber $q^{-1}(y)$ would be contained in both $U$ and $V$.
This is impossible because $U\cap V=\varnothing$.
Hence
\[
U'\cap V'=\varnothing.
\]
So $U'$ and $V'$ are the required disjoint open neighborhoods.
:::

<1>7. The quotient $X/A$ is Hausdorff.
::: {.proof}
Let $y,z\in X/A$ be distinct.
By <1>5, the singleton sets $\{y\}$ and $\{z\}$ are disjoint closed subsets.
Applying <1>6 to these two closed sets gives disjoint open neighborhoods of $y$ and $z$.
Thus $X/A$ is Hausdorff.
:::

<1>8. Therefore $X/A$ is normal.
::: {.proof}
Step <1>7 verifies the Hausdorff requirement, while <1>6 separates arbitrary disjoint closed subsets by disjoint open neighborhoods.
This is precisely normality in the definition given by the problem.
:::
:::
