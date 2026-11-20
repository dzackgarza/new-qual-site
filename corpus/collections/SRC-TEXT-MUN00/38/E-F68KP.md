---
schema: qual/card@1
id: E-F68KP
kind: problem
title: Nonmetrizability of the Stone--Čech compactification
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metrizability
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Møller, "Solutions to exercises in Munkres", file S38.pdf,
    Exercise 38.9, pages 2-3 of the file (tmp/sources/munkres-solutions-poulsen-S38.pdf; the sheet is
    dated 2 April 2005 and its section-38 items name no author; Internet Archive snapshot 20181222125939
    of web.math.ku.dk/~moller/e02/3gt/opg/S38.pdf). Checked against Munkres, Topology (2000), Section 38
    Exercise 9, printed p. 242, the sequence lemma (Theorem 21.3, or Lemma 30.2 for first countability),
    Theorem 32.2 (metrizable implies normal) and Urysohn's lemma (Theorem 33.1). The sheet's part (a):
    a sequence in X converging to y in beta(X) - X has no repetitions after passing to a subsequence, so
    its set S has no limit point in X, the two sets of even and odd terms are therefore closed in X,
    Urysohn separates them by f, and the extension of f to beta(X) would take the two subsequences to 0
    and to 1 while both converge to y. Part (b): if beta(X) were metrizable, the sequence lemma would
    produce a sequence in X converging to a point of beta(X) - X, contradicting (a). What was corrected:
    the card's step that S has no accumulation point in X said only that an accumulation point "is a
    cluster point of the sequence", which needs the observation that every neighbourhood of such a point
    meets S in infinitely many terms because the terms are distinct; the card states that reason now.
    The card's (a) also dropped the sheet's ordering of the parity, which is irrelevant, so the two
    functions' values are 0 and 1 as above.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The ten leaf steps of parts (a) and (b) asserted their claim with no proof body; each now
    carries one, and the closing QED step also states how the two parts' steps discharge the
    claims. No claim, no numbering and no statement is changed. Cited by number only:
    Theorem 21.3 (the sequence lemma, closure equals sequential closure in a metrizable space),
    Theorem 32.2 (a metrizable space is normal), Urysohn's lemma (Theorem 33.1), and the
    universal property of the Stone--Čech compactification. Checked: that a repeated term would
    give a constant subsequence with a second limit, that an accumulation point of the set of
    distinct terms is a limit of a subsequence, that a subset of a set with no accumulation point
    in the space is closed, and that the two constant subsequences force the two values of the
    extended function to be equal.
---

::: {.exercise}

(a) If $X$ is normal and $y$ is a point of $\beta(X) - X$, show that $y$ is not the limit of a sequence of points of $X$.

(b) Show that if $X$ is completely regular and noncompact, then $\beta(X)$ is not metrizable.
:::

::: {.solution}

::: pf

::: {.pf-step #part-a}
Part (a): Points of $\beta(X) \setminus X$ are not sequential limits of points in $X$:

::: pf-proof

::: pf-step
Suppose for contradiction that there exists a sequence $(x_n)_{n=1}^\infty \subseteq X$ such that $x_n \to y \in \beta(X) \setminus X$.
Each point $x \in X$ occurs only finitely often in the sequence: otherwise a constant subsequence converges to $x \neq y$, which contradicts uniqueness of limits in the Hausdorff space $\beta(X)$. Passing to a subsequence, assume the $x_n$ are pairwise distinct.
Then the set $S = \{x_n \mid n \in \NN\}$ has no accumulation point in $X$: an accumulation point $x \in X$ of $S$ is a cluster point of the sequence, so $x = y$ by the Hausdorff property, which contradicts $y \notin X$. Hence every subset of $S$ is closed in $X$.

::: pf-proof
$\beta(X)$ is compact Hausdorff, so limits of sequences in it are unique: a point occurring infinitely often would be the limit of a constant subsequence and also of the whole sequence, forcing it to equal $y$, which lies outside $X$. Deleting repeated terms leaves a subsequence with pairwise distinct terms, and a subsequence of a convergent sequence converges to the same limit. If $x\in X$ were an accumulation point of $S$, every neighbourhood of $x$ would contain a point of $S$ different from $x$; since the terms are distinct and enumerate $S$, each neighbourhood of $x$ meets $S$ in infinitely many terms, so some subsequence converges to $x$, and then $x=y$ by uniqueness of limits, contradicting $y\notin X$. A subset of a space with no accumulation point in that space is closed: a point of its closure outside it would be an accumulation point. So every subset of $S$, in particular $A$ and $B$ below, is closed in $X$.
:::

:::

::: pf-step
Partition $S$ into two disjoint closed subsets of $X$:
$$
A = \{x_{2k} \mid k \in \ZZ_+\}, \qquad B = \{x_{2k-1} \mid k \in \ZZ_+\}.
$$
Because $X$ is normal, by Urysohn's Lemma there exists a continuous function $f: X \to [0, 1]$ such that:
$$
f(a) = 0 \quad \forall a \in A, \qquad f(b) = 1 \quad \forall b \in B.
$$

::: pf-proof
$A$ and $B$ are disjoint because the terms are distinct, and both are subsets of $S$, so both are closed by step 1.1. Urysohn's lemma (Theorem 33.1) applies to two disjoint closed subsets of a normal space and produces a continuous $f:X\to[0,1]$ that is $0$ on one of them and $1$ on the other.
:::

:::

::: pf-step
By the universal property of the Stone–Čech compactification, $f$ extends to a continuous function $\beta f: \beta(X) \to [0, 1]$.

::: pf-proof
$\beta(X)$ is characterised among compactifications of $X$ by the property that every continuous map from $X$ to a compact Hausdorff space extends uniquely; $[0,1]$ is compact Hausdorff, and $f$ is continuous and bounded, so the extension $\beta f$ exists and is unique.
:::

:::

::: pf-step
Since $x_n \to y$ in $\beta(X)$, continuity of $\beta f$ implies:
$$
\lim_{n \to \infty} f(x_n) = \beta f(y).
$$
However, along the even subsequence, $\lim_{k\to\infty} f(x_{2k}) = \lim_{k\to\infty} 0 = 0$, while along the odd subsequence, $\lim_{k\to\infty} f(x_{2k-1}) = \lim_{k\to\infty} 1 = 1$.
Thus $0 = \beta f(y) = 1$, a contradiction.

::: pf-proof
A continuous map carries convergent sequences to convergent sequences, so $\beta f(x_n)\to\beta f(y)$; and $\beta f$ agrees with $f$ on $X$, so $f(x_n)\to\beta f(y)$. A sequence in a Hausdorff space has at most one limit and each of its subsequences has that same limit, so the even and odd subsequences both converge to $\beta f(y)$; but they are constant equal to $0$ and to $1$ respectively, by the choice of $f$ in step 1.2. Hence $\beta f(y)=0$ and $\beta f(y)=1$.
:::

:::

::: pf-step
Therefore no point $y \in \beta(X) \setminus X$ can be the limit of a sequence in $X$.

::: pf-proof
The supposition of step 1.1 produced the contradiction of step 1.4, so it is false; since $y\in\beta(X)\setminus X$ was arbitrary, no such point is a sequential limit of points of $X$.
:::

:::

:::

:::

::: {.pf-step #part-b}
Part (b): Nonmetrizability of $\beta(X)$ for noncompact completely regular $X$:

::: pf-proof

::: pf-step
Since $X$ is noncompact, $X \subsetneq \beta(X)$, so there exists a point $y \in \beta(X) \setminus X$.

::: pf-proof
$\beta(X)$ is compact by construction and contains $X$ as a subspace; if $X=\beta(X)$ then $X$ would be compact. Since $X$ is not compact, the containment is proper and a point of the difference exists.
:::

:::

::: pf-step
The subspace $X$ is dense in $\beta(X)$, so $y \in \overline{X}$.

::: pf-proof
A compactification is by definition a compact Hausdorff space containing $X$ as a dense subspace; so the closure of $X$ in $\beta(X)$ is $\beta(X)$ itself, and $y$ lies in it.
:::

:::

::: {.pf-step #assume-metrizable-sequence}
Suppose for contradiction that $\beta(X)$ is metrizable.
In any metric space, the topological closure coincides with the sequential closure: every point in the closure of a subset is the limit of a sequence of points in that subset.
Thus there must exist a sequence $(x_n)_{n=1}^\infty \subseteq X$ such that $x_n \to y$ in $\beta(X)$.

::: pf-proof
The sequence lemma (Theorem 21.3) says that in a metrizable space a point of the closure of a subset is the limit of a sequence from that subset. Applying it to the subset $X$ and the point $y\in\overline X$ of step 2.2 gives the stated sequence.
:::

:::

::: pf-step
The subspace $X$ of the metrizable space $\beta(X)$ is metrizable, hence normal.
By step [](#part-a){.pf-ref} applied to the normal space $X$, the point $y \in \beta(X) \setminus X$ is not the limit of a sequence of points of $X$.
This contradicts step [](#assume-metrizable-sequence){.pf-ref}.

::: pf-proof
A subspace of a metrizable space is metrizable, the restriction of the metric inducing its topology, and a metrizable space is normal (Theorem 32.2). Part (a) applies to the normal space $X$ and the point $y\in\beta(X)\setminus X$, and says precisely that no sequence in $X$ converges to $y$; step 2.3 produced one.
:::

:::

::: pf-step
Therefore $\beta(X)$ is not metrizable.

::: pf-proof
The supposition of step 2.3 led to the contradiction of step 2.4, so $\beta(X)$ admits no metric inducing its topology.
:::

:::

:::

:::

::: pf-qed
Step [](#part-a){.pf-ref} proves part (a) and step [](#part-b){.pf-ref} proves part (b).

::: pf-proof
Part (a) is steps 1.1 to 1.5: a sequence converging to a point of the remainder is made injective, its even and odd terms are separated by Urysohn, and the extension of the separating function would take two values at the limit. Part (b) is steps 2.1 to 2.5: metrizability would supply such a sequence by the sequence lemma, contradicting (a).
:::

:::

:::

:::
