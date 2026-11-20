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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (a) rewritten. The old step inferred from "every neighbourhood of an
    accumulation point meets the set of distinct terms" that a subsequence
    converges to it, which needs first countability and is not available under
    the hypothesis of normality. The argument now transcribes Møller's Exercise
    38.9 solution and uses closures in beta(X): for x in X with x not equal to
    y, disjoint neighbourhoods of x and y together with convergence of the
    sequence to y show that a neighbourhood of x meets the set of terms in
    only finitely many points, so the even and odd sets are closed in X;
    Urysohn's lemma separates them, Theorem 38.4 extends the separator to
    beta(X), the two closures are disjoint, and both contain y. Also corrected:
    the sequence lemma is Lemma 21.2, not Theorem 21.3. Cited by number only:
    Lemma 21.2, Theorem 32.2, Theorem 33.1, Theorem 38.4.
---

::: {.exercise}

(a) If $X$ is normal and $y$ is a point of $\beta(X) - X$, show that $y$ is not the limit of a sequence of points of $X$.

(b) Show that if $X$ is completely regular and noncompact, then $\beta(X)$ is not metrizable.
:::

::: {.solution}

The argument of part (a) is transcribed from Jesper Michael Møller, Solutions to exercises in Munkres, Exercise 38.9, and checked against Munkres, Topology, §38 Exercise 9.

::: pf

::: {.pf-step #part-a}
Part (a): Points of $\beta(X) \setminus X$ are not sequential limits of points in $X$:

::: pf-proof

::: pf-step
Suppose for contradiction that there exists a sequence $(x_n)_{n=1}^\infty \subseteq X$ such that $x_n \to y \in \beta(X) \setminus X$.
After passing to a subsequence, the terms $x_n$ are pairwise distinct.

::: pf-proof
$\beta(X)$ is compact Hausdorff, so a sequence has at most one limit: if a point $x \in X$ occurred infinitely often, the constant subsequence at $x$ would converge to $x$, and a subsequence of a convergent sequence converges to the same limit, so $x = y$, contradicting $y \notin X$. Hence each point of $X$ occurs only finitely often, so infinitely many distinct values occur; deleting the repeated occurrences leaves an infinite subsequence with pairwise distinct terms, and it still converges to $y$.
:::

:::

::: {.pf-step #closed-discrete}
Let $S = \{x_n \mid n \in \NN\}$ be the set of terms.
Every point of $X$ has an open neighbourhood in $\beta(X)$ meeting $S$ in at most one point; consequently $S$ is closed and discrete in $X$, and every subset of $S$ is closed in $X$.

::: pf-proof
Let $x \in X$. Since $x \neq y$, the Hausdorff space $\beta(X)$ supplies disjoint open sets $U \ni x$ and $V \ni y$. Since $x_n \to y$, there is $N$ with $x_n \in V$ for all $n \ge N$, so $U \cap S \subseteq \{x_1, \ldots, x_{N-1}\}$ is finite. As $\beta(X)$ is T1, intersecting $U$ with the complements of the finitely many points of $U \cap S$ that differ from $x$ gives an open neighbourhood of $x$ that meets $S$ only possibly at $x$.
Now let $T \subseteq S$ and $x \in X \setminus T$. If $x \notin S$, the neighbourhood just produced misses $S$, hence misses $T$; if $x \in S \setminus T$, it meets $S$ only in $x$, hence misses $T$. So $X \setminus T$ is open and $T$ is closed in $X$. In particular $S$ itself is closed in $X$, and $S$ is discrete in the subspace topology.
:::

:::

::: {.pf-step #urysohn}
The sets
$$
A = \{x_{2k} \mid k \in \ZZ_+\}, \qquad B = \{x_{2k-1} \mid k \in \ZZ_+\}
$$
are disjoint closed subsets of $X$, so by Urysohn's lemma there is a continuous $f: X \to [0, 1]$ with $f(a) = 0$ for all $a \in A$ and $f(b) = 1$ for all $b \in B$.

::: pf-proof
$A$ and $B$ are disjoint because the terms are distinct, and both are subsets of $S$, so both are closed in $X$ by step [](#closed-discrete){.pf-ref}. Urysohn's lemma (Theorem 33.1) applies to two disjoint closed subsets of a normal space and produces a continuous $f: X \to [0,1]$ that is $0$ on one of them and $1$ on the other.
:::

:::

::: {.pf-step #extension}
By the universal property of the Stone–Čech compactification, $f$ extends to a continuous function $\beta f: \beta(X) \to [0, 1]$.

::: pf-proof
$X$ is normal, hence completely regular by Urysohn's lemma (Theorem 33.1), so $\beta(X)$ is defined. Theorem 38.4 states that every continuous map from $X$ to a compact Hausdorff space extends uniquely to $\beta(X)$; $[0,1]$ is compact Hausdorff and $f$ is continuous, so the extension $\beta f$ exists and is unique.
:::

:::

::: {.pf-step #closures-disjoint}
The closures of $A$ and of $B$ in $\beta(X)$ are disjoint.

::: pf-proof
$\beta f$ is continuous and $\{0\}$ is closed in $[0,1]$, so $(\beta f)^{-1}(0)$ is closed in $\beta(X)$; it contains $A$, hence contains the closure $\bar A$ of $A$ in $\beta(X)$. Similarly $(\beta f)^{-1}(1)$ is closed and contains $\bar B$. The two preimages are disjoint, so $\bar A \cap \bar B = \varnothing$.
:::

:::

::: {.pf-step #closure-limits}
The point $y$ lies in both $\bar A$ and $\bar B$.

::: pf-proof
The even-indexed terms form a subsequence of $(x_n)$, so $x_{2k} \to y$; since each $x_{2k}$ lies in $A$, and a limit of a sequence of points of a set lies in the closure of that set, $y \in \bar A$. The same argument with the odd-indexed terms gives $y \in \bar B$.
:::

:::

::: pf-step
Therefore no point $y \in \beta(X) \setminus X$ can be the limit of a sequence in $X$.

::: pf-proof
Steps [](#closures-disjoint){.pf-ref} and [](#closure-limits){.pf-ref} give $y \in \bar A \cap \bar B = \varnothing$, a contradiction. The supposition of step 1.1 is therefore false, and since $y \in \beta(X) \setminus X$ was arbitrary, no such point is a sequential limit of points of $X$.
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
The sequence lemma (Lemma 21.2) says that in a metrizable space a point of the closure of a subset is the limit of a sequence from that subset. Applying it to the subset $X$ and the point $y\in\overline X$ of step 2.2 gives the stated sequence.
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
