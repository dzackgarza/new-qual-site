---
schema: qual/card@1
id: P-AGXGATHDIMCOVER
kind: problem
title: Dimension from an open cover, and dimension of subsets of an irreducible variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Krull Dimension
  - Open Covers
  - Irreducibility
relations: []
review: draft
---

::: problem
Let $X$ be a topological space, and show

a. If $\ts{U_i}_{i\in I}$ is an open cover of $X$, then $\dim X = \sup_{i\in I} \dim U_i$.

b. If $X$ is an irreducible affine variety and $U\subset X$ is a nonempty open subset, then $\dim X = \dim U$.
  Does this hold for any irreducible topological space?
:::

::: solution
> Strictly for notational convenience, we treat $\ts{U_i}$ as if it were a countable open cover.

**Part a**:
First note that if $U \subseteq V$, then $\dim U \leq \dim V$.
If this were not the case, one could find a chain $\ts{I_j}$ of closed irreducible subsets of $V$ of length $n>\dim U$.
But then $I'_j \da I_j \intersect U$ would again be closed and irreducible, yielding a chain of length $n$ in $U$.
Thus $\dim X\geq \dim U_i$, and it remains true that $\dim X \geq \sup \dim U_i$, so it suffices to show that $\dim X \leq \sup \dim U_i$.

Set $s \da \sup_i \dim U_i$ and $n\da \dim X$; we want to show $s\geq n$.
Let $\ts{I_j}_{j\leq n}$ be a maximal chain of length $n$ of closed irreducible subsets of $X$, so
\[
\emptyset \subsetneq I_0 \subsetneq I_1 \subsetneq \cdots \subsetneq I_n \subseteq X
.\]

Since $I_0\subset X$ and $\ts{U_i}$ covers $X$, we can find some $U_{0}\in \ts{U_i}$ such that $I_0\intersect U_0$ is nonempty, since otherwise there would be a point in $I_0 \intersect \qty{X\sm \Union_{i\in J} U_i} = \emptyset$.
We can do this for every $I_j$, so define $A_j \da I_j \intersect U_0$.

Each $A_j$ is closed in $U_0$, and remains irreducible, since any decomposition of $A_j$ would lift to a decomposition of $I_0$.
To see that $A_0 \subsetneq A_1$, i.e. that the inclusions are still proper, note that
\[
x\in A_{i+1}\sm A_i \iff x\in \qty{I_{i+1} \intersect U_0} \sm \qty{I_{i} \intersect U_0} = \qty{I_1 \sm I_2}\intersect U_0 = \emptyset
.\]
But this exhibits a length $n$ chain in $U_0$, so $\dim U_0 \geq n$.
Taking suprema,
\[
n \leq \dim U_0 \leq \sup_{i\in J} \dim U_i = s
.\]

**Part b**: the answer is **no**: we can produce a space $X$ with some $\dim X$ and a subset $U$ satisfying $\dim U < \dim X$.

Define a space and a topology by
\[
X \da \ts{a, b} \qquad \tau \da \ts{\emptyset, X, \ts{a}}
.\]
Here $\ts{b}$ is the only proper closed subset, since its complement is open, so $X$ must be irreducible.
We can find a maximal ascending chain of length $1$,
\[
\emptyset \subsetneq \ts{b} \subsetneq X
,\]
and so $\dim X = 1$.
However, for $U\da \ts{a}$ there is only one possible maximal chain,
\[
\emptyset \subsetneq \ts{a} = U
,\]
so $\dim U = 0$.
:::

::: {.remark}
Erratum: part a of the argument above has three faulty steps.

- The monotonicity step starts from a chain in $V$ and intersects it with $U$, which neither keeps the members irreducible nor keeps the inclusions proper. It should start from a chain $Z_0 \subsetneq \cdots \subsetneq Z_n$ of closed irreducible subsets of $U$: their closures $\overline{Z_j}$ in $V$ are closed and irreducible, and they are distinct because $Z_j = \overline{Z_j} \intersect U$.
- Irreducibility of $A_j = I_j \intersect U_0$ does not come from a decomposition of $I_0$. Once $U_0$ meets $I_0$ it meets every $I_j \supseteq I_0$, and $A_j$ is a nonempty open subset of the irreducible space $I_j$, hence irreducible and dense in $I_j$.
- The displayed computation of $A_{i+1} \sm A_i$ is garbled: it mixes indices and concludes that the difference is empty, which is the opposite of what is wanted. If $A_i = A_{i+1}$, then $I_{i+1} = \overline{A_{i+1}} = \overline{A_i} \subseteq I_i$ by density, contradicting $I_i \subsetneq I_{i+1}$.

In part b the source's topology reads $\ts{\emptyset, X, \ts{1}}$ and its chain ends in $\ts{a} = X$; the example is the one above, with open point $a$ and $U = \ts{a}$.
:::
