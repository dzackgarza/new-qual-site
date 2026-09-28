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
---

::: {.exercise}

(a) If $X$ is normal and $y$ is a point of $\beta(X) - X$, show that $y$ is not the limit of a sequence of points of $X$.

(b) Show that if $X$ is completely regular and noncompact, then $\beta(X)$ is not metrizable.
:::

::: {.solution}
<1>1. Part (a): Points of $\beta(X) \setminus X$ are not sequential limits of points in $X$:
<2>1. Suppose for contradiction that there exists a sequence $(x_n)_{n=1}^\infty \subseteq X$ such that $x_n \to y \in \beta(X) \setminus X$.
Each point $x \in X$ occurs only finitely often in the sequence: otherwise a constant subsequence converges to $x \neq y$, which contradicts uniqueness of limits in the Hausdorff space $\beta(X)$. Passing to a subsequence, assume the $x_n$ are pairwise distinct.
Then the set $S = \{x_n \mid n \in \mathbb{N}\}$ has no accumulation point in $X$: an accumulation point $x \in X$ of $S$ is a cluster point of the sequence, so $x = y$ by the Hausdorff property, which contradicts $y \notin X$. Hence every subset of $S$ is closed in $X$.
<2>2. Partition $S$ into two disjoint closed subsets of $X$:
\[
A = \{x_{2k} \mid k \in \mathbb{N}\}, \qquad B = \{x_{2k-1} \mid k \in \mathbb{N}\}.
\]
Because $X$ is normal, by Urysohn's Lemma there exists a continuous function $f: X \to [0, 1]$ such that:
\[
f(a) = 0 \quad \forall a \in A, \qquad f(b) = 1 \quad \forall b \in B.
\]
<2>3. By the universal property of the Stone–Čech compactification, $f$ extends to a continuous function $\beta f: \beta(X) \to [0, 1]$.
<2>4. Since $x_n \to y$ in $\beta(X)$, continuity of $\beta f$ implies:
\[
\lim_{n \to \infty} f(x_n) = \beta f(y).
\]
However, along the even subsequence, $\lim_{k\to\infty} f(x_{2k}) = \lim_{k\to\infty} 0 = 0$, while along the odd subsequence, $\lim_{k\to\infty} f(x_{2k-1}) = \lim_{k\to\infty} 1 = 1$.
Thus $0 = \beta f(y) = 1$, a contradiction.
<2>5. Therefore no point $y \in \beta(X) \setminus X$ can be the limit of a sequence in $X$.

<1>2. Part (b): Nonmetrizability of $\beta(X)$ for noncompact completely regular $X$:
<2>1. Since $X$ is noncompact, $X \subsetneq \beta(X)$, so there exists a point $y \in \beta(X) \setminus X$.
<2>2. The subspace $X$ is dense in $\beta(X)$, so $y \in \overline{X}$.
<2>3. Suppose for contradiction that $\beta(X)$ is metrizable.
In any metric space, the topological closure coincides with the sequential closure: every point in the closure of a subset is the limit of a sequence of points in that subset.
Thus there must exist a sequence $(x_n)_{n=1}^\infty \subseteq X$ such that $x_n \to y$ in $\beta(X)$.
<2>4. The subspace $X$ of the metrizable space $\beta(X)$ is metrizable, hence normal.
By step <1>1 applied to the normal space $X$, the point $y \in \beta(X) \setminus X$ is not the limit of a sequence of points of $X$.
This contradicts step <2>3.
<2>5. Therefore $\beta(X)$ is not metrizable.

<1>3. Q.E.D.
Step <1>1 proves part (a) and step <1>2 proves part (b).
:::
