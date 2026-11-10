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
:::

::: pf-step
By the universal property of the Stone–Čech compactification, $f$ extends to a continuous function $\beta f: \beta(X) \to [0, 1]$.
:::

::: pf-step
Since $x_n \to y$ in $\beta(X)$, continuity of $\beta f$ implies:
$$
\lim_{n \to \infty} f(x_n) = \beta f(y).
$$
However, along the even subsequence, $\lim_{k\to\infty} f(x_{2k}) = \lim_{k\to\infty} 0 = 0$, while along the odd subsequence, $\lim_{k\to\infty} f(x_{2k-1}) = \lim_{k\to\infty} 1 = 1$.
Thus $0 = \beta f(y) = 1$, a contradiction.
:::

::: pf-step
Therefore no point $y \in \beta(X) \setminus X$ can be the limit of a sequence in $X$.
:::

:::

:::

::: {.pf-step #part-b}
Part (b): Nonmetrizability of $\beta(X)$ for noncompact completely regular $X$:

::: pf-proof

::: pf-step
Since $X$ is noncompact, $X \subsetneq \beta(X)$, so there exists a point $y \in \beta(X) \setminus X$.
:::

::: pf-step
The subspace $X$ is dense in $\beta(X)$, so $y \in \overline{X}$.
:::

::: {.pf-step #assume-metrizable-sequence}
Suppose for contradiction that $\beta(X)$ is metrizable.
In any metric space, the topological closure coincides with the sequential closure: every point in the closure of a subset is the limit of a sequence of points in that subset.
Thus there must exist a sequence $(x_n)_{n=1}^\infty \subseteq X$ such that $x_n \to y$ in $\beta(X)$.
:::

::: pf-step
The subspace $X$ of the metrizable space $\beta(X)$ is metrizable, hence normal.
By step [](#part-a){.pf-ref} applied to the normal space $X$, the point $y \in \beta(X) \setminus X$ is not the limit of a sequence of points of $X$.
This contradicts step [](#assume-metrizable-sequence){.pf-ref}.
:::

::: pf-step
Therefore $\beta(X)$ is not metrizable.
:::

:::

:::

::: pf-qed
Step [](#part-a){.pf-ref} proves part (a) and step [](#part-b){.pf-ref} proves part (b).
:::

:::

:::
