---
schema: qual/card@1
id: P-AGXGATHNOETHCPT
kind: problem
title: Noetherian spaces are quasicompact, but complex affine varieties are not compact
classification:
  areas:
  - algebraic-geometry
  topics:
  - Noetherian Spaces
  - Compactness
  - Classical Topology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Gathmann 2.36 in the retained native source at revision 7eafedfc0
    and compared both parts with the current card. The retained source states
    the exercise but gives no worked solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read both parts. Checked the minimal-closed-subset finite-subcover
    argument, Noetherianity of Zariski-open subsets of affine varieties, and
    the Noether-normalization contradiction using surjectivity by lying-over
    and continuity in the classical topology.
---

::: {.problem}
Prove the following:

a. Every noetherian topological space is compact.
In particular, every open subset of an affine variety is compact in the Zariski topology.

b. A complex affine variety of dimension at least 1 is never compact in the classical topology.
:::

::: {.solution}
In part (a), compactness means that every open cover has a finite subcover;
no Hausdorff hypothesis is used.

<1>1. (a) Every Noetherian topological space is compact.

::: {.proof}
Let $X$ be Noetherian and let
$$
X=\bigcup_{i\in I}U_i
$$
be an open cover. Suppose that no finite subfamily covers $X$.

Let $\mathcal C$ be the collection of closed subsets of $X$ that are not
covered by finitely many of the $U_i$. By assumption $X\in\mathcal C$.
Since $X$ is Noetherian, its closed subsets satisfy the descending-chain
condition, so $\mathcal C$ has a minimal element $F$.

The set $F$ is nonempty, because the empty set is covered by the empty
subfamily. Choose $x\in F$, and choose $j\in I$ with $x\in U_j$. Then
$$
F' = F\cap (X\setminus U_j)
$$
is a proper closed subset of $F$. By minimality of $F$, the set $F'$
is covered by finitely many members of the original cover. Adding $U_j$
gives a finite subcover of $F$, contradicting $F\in\mathcal C$.
Therefore the original cover of $X$ has a finite subcover.
:::

<1>2. (a) Every open subset of an affine variety is compact in the Zariski topology.

::: {.proof}
Let $X$ be an affine variety. Its coordinate ring
$$
A(X)=k[x_1,\ldots,x_n]/I(X)
$$
is Noetherian by the Hilbert basis theorem. A descending chain of Zariski
closed subsets of $X$ yields an ascending chain of their vanishing ideals
in $A(X)$, so the chain of closed subsets stabilizes. Hence $X$ is a
Noetherian topological space; equivalently, its open subsets satisfy the
ascending-chain condition ([[D-9DIKB|Noetherian spaces]]).

If $U\subseteq X$ is open, every open subset of $U$ is open in $X$.
Thus every ascending chain of open subsets of $U$ is also an ascending
chain of open subsets of $X$, and therefore stabilizes. Hence $U$ is
Noetherian. Step <1>1 applied to $U$ shows that $U$ is compact in the
Zariski topology.
:::

<1>3. (b) A complex affine variety of positive dimension is not compact in the classical topology.

::: {.proof}
Let $X$ be a complex affine variety with $\dim X\geq1$, and suppose for
contradiction that $X$ is compact in the classical topology.

Choose an irreducible component $Y\subseteq X$ of dimension
$$
d\geq1.
$$
The component $Y$ is Zariski closed in $X$, hence is also closed in the
classical topology because polynomial zero sets are classically closed.
Therefore $Y$ is compact.

By affine Noether normalization
([[T-MORFIBDIM|Noether normalization]]), there is a finite morphism
$$
\pi:Y\longrightarrow\AA^d_{\CC}.
$$
On coordinate rings, Noether normalization gives an integral inclusion
$$
\CC[t_1,\ldots,t_d]\hookrightarrow A(Y).
$$
The lying-over theorem therefore implies that every maximal ideal of
$\CC[t_1,\ldots,t_d]$ has a maximal ideal of $A(Y)$ lying over it.
Thus $\pi$ is surjective on complex points:
$$
\pi(Y)=\CC^d.
$$

The coordinate functions of $\pi$ are regular functions on the affine
variety $Y$, hence polynomial functions in affine coordinates and therefore
continuous for the classical topology. Consequently $\pi(Y)$ must be
compact as the continuous image of the compact space $Y$.

This is impossible, since $\CC^d$ is not compact for $d\geq1$; for
example, it is unbounded in its Euclidean topology. Hence $X$ cannot be
compact in the classical topology.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove part (a), and step <1>3 proves part (b).
:::
:::
