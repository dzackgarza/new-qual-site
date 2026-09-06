---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-03
kind: problem
title: A diagonal in the countable-closed and finite-complement topologies
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Product Topology
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part One, question 3 of the Topology Ph.D. Qualifying Exam
    dated January 12, 2008 in assets/attachments/F07phdtop.pdf. The source itself
    defines the countable-closed topology and then asks about the finite-complement
    topology; the card intentionally retains that inconsistency.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Under the literal cofinite topology on X x X, Delta is infinite and hence not
    closed. If instead X carries either the cofinite or the defined cocountable
    topology and X x X has the product topology, every two nonempty opens of X
    intersect, so every basic neighborhood of an off-diagonal point meets Delta;
    again Delta is not closed.
---

::: {.problem}
A set is said to have the countable-closed topology if the closed sets are the countable sets together with the empty set.
If $X$ is a topological space with an uncountably infinite number of points is the diagonal $\Delta:=\{(x,x)\mid x\in X\}$ closed in the finite complement topology?
Justify your answer carefully.
:::

::: remark
The source first names the countable-closed topology and then asks about the finite-complement topology; both terms are retained as printed.
:::

::: {.solution}
The answer is no under each natural reading of the source's inconsistent wording.

<1>1. If “the finite complement topology” means the cofinite topology directly on the set $X\times X$, then $\Delta$ is not closed.
::: {.proof}
In the cofinite topology on an infinite set, the proper closed subsets are precisely the finite subsets.
Since $X$ is uncountable, the diagonal
\[
\Delta=\{(x,x):x\in X\}
\]
is in bijection with $X$ and is therefore uncountable, hence infinite.
It is also a proper subset of $X\times X$ because $X$ has at least two distinct points, so an off-diagonal pair belongs to its complement.
Thus $\Delta$ is neither finite nor all of $X\times X$, and hence is not closed in the cofinite topology on $X\times X$.
:::

<1>2. If $X$ carries the cofinite topology and $X\times X$ carries the product topology, then $\Delta$ is not closed.
::: {.proof}
Choose distinct points $a,b\in X$.
Suppose there were a basic product neighborhood
\[
(a,b)\in U\times V
\]
with
\[
(U\times V)\cap\Delta=\varnothing,
\]
where $U,V$ are nonempty cofinite open subsets of $X$.
The intersection $U\cap V$ is cofinite, hence nonempty because $X$ is infinite.
Choose $z\in U\cap V$.
Then
\[
(z,z)\in U\times V
\]
and also $(z,z)\in\Delta$, a contradiction.
Therefore every basic neighborhood of the off-diagonal point $(a,b)$ meets $\Delta$.
Hence
\[
(a,b)\in\overline\Delta\setminus\Delta,
\]
so $\Delta$ is not closed.
:::

<1>3. If the intended topology was instead the countable-closed topology defined in the first sentence, with the product topology on $X\times X$, then $\Delta$ is again not closed.
::: {.proof}
The open nonempty subsets of the countable-closed topology are the complements of countable subsets of $X$.
If $U,V$ are two such nonempty open sets, then
\[
X\setminus(U\cap V)
=(X\setminus U)\cup(X\setminus V)
\]
is countable.
Since $X$ is uncountable, $U\cap V$ is nonempty.

Now repeat the argument of <1>2: for any off-diagonal point $(a,b)$ and any basic product neighborhood $U\times V$ of it, choose $z\in U\cap V$.
Then $(z,z)\in(U\times V)\cap\Delta$.
Thus every off-diagonal point lies in $\overline\Delta$, so in particular $\Delta$ is not closed.
:::

<1>4. Thus the source ambiguity does not affect the conclusion: the diagonal is not closed.
::: {.proof}
The literal cofinite reading is <1>1; the cofinite product reading is <1>2; and the topology actually defined by the source is handled in <1>3. All three yield the same negative answer.
:::
:::
