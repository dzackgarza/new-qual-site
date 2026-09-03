---
schema: qual/card@1
id: E-TTDES
kind: problem
title: Compact, limit-point compact, and sequentially compact coincide for second-countable
  Hausdorff or metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Countability
  - Convergence
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Show that if $X$ is second-countable and Hausdorff (or a metric space), then the following are equivalent:
(1) $X$ is compact (every open cover has a finite subcover).
(2) $X$ is limit-point compact (every infinite subset $A \subseteq X$ has a limit point in $X$).
(3) $X$ is sequentially compact (every sequence in $X$ has a convergent subsequence in $X$).
:::

::: solution
**Goal:** Prove $(1) \implies (2) \implies (3) \implies (1)$ for second-countable Hausdorff spaces (and metric spaces).

<1>1. $(1) \implies (2)$ (Compact $\implies$ Limit-Point Compact):
    *Proof:*
    <2>1. Suppose $X$ is compact. Let $A \subseteq X$ be an infinite subset.
    <2>2. Suppose, for contradiction, that $A$ has no limit points in $X$.
    <2>3. Then for every point $x \in X$, there exists an open neighborhood $U_x$ such that $U_x \cap A$ is either $\{x\}$ (if $x \in A$) or $\varnothing$ (if $x \notin A$).
    <2>4. The collection $\{U_x\}_{x \in X}$ forms an open cover of $X$.
    <2>5. Since $X$ is compact, there is a finite subcover $\{U_{x_1}, \dots, U_{x_n}\}$.
    <2>6. Then $A = A \cap X \subseteq \bigcup_{j=1}^n (U_{x_j} \cap A) \subseteq \{x_1, \dots, x_n\}$, which implies $A$ is finite.
    <2>7. This contradicts the assumption that $A$ is infinite. Thus $A$ must have a limit point.

<1>2. $(2) \implies (3)$ (Limit-Point Compact $\implies$ Sequentially Compact for $T_1$ first-countable/second-countable spaces):
    *Proof:*
    <2>1. Let $(x_n)_{n=1}^\infty$ be a sequence in $X$.
    <2>2. **Case 1: The set of terms $S = \{x_n \mid n \ge 1\}$ is finite.**
        - By the Pigeonhole Principle, some value $x \in S$ appears infinitely many times: $x_{n_k} = x$ for a subsequence $n_1 < n_2 < \dots$.
        - Then $(x_{n_k})$ is a constant subsequence converging to $x$.
    <2>3. **Case 2: The set $S = \{x_n \mid n \ge 1\}$ is infinite.**
        - By limit-point compactness, the infinite set $S$ has a limit point $x_0 \in X$.
        - Since $X$ is second-countable (or metric), $x_0$ has a countable nested neighborhood basis $B_1 \supset B_2 \supset \cdots$.
        - Because $x_0$ is a limit point and $X$ is $T_1$, each open set $B_k$ contains infinitely many distinct points of $S$.
        - We can inductively choose indices $n_1 < n_2 < n_3 < \dots$ such that $x_{n_k} \in B_k$.
        - Then $x_{n_k} \to x_0$ as $k \to \infty$.

<1>3. $(3) \implies (1)$ (Sequentially Compact $\implies$ Compact):
    *Proof:*
    <2>1. In a second-countable space $X$, every open cover has a countable subcover (Lindelöf property).
    <2>2. Let $\{U_n\}_{n=1}^\infty$ be a countable open cover of $X$.
    <2>3. Suppose, for contradiction, that no finite subcollection covers $X$.
    <2>4. For each $N \ge 1$, choose a point $x_N \in X \setminus \bigcup_{n=1}^N U_n$.
    <2>5. By sequential compactness, the sequence $(x_N)$ has a subsequence $(x_{N_k})$ converging to some point $x^* \in X$.
    <2>6. Since $\{U_n\}$ covers $X$, $x^* \in U_m$ for some index $m \ge 1$.
    <2>7. Since $U_m$ is open and $x_{N_k} \to x^*$, there exists $K$ such that for all $k \ge K$, $x_{N_k} \in U_m$.
    <2>8. But for $k$ large enough such that $N_k \ge m$, by construction $x_{N_k} \notin \bigcup_{n=1}^{N_k} U_n \supseteq U_m$, a contradiction!
    <2>9. Thus $\{U_n\}$ has a finite subcover, so $X$ is compact.

<1>4. Conclusion:
    $(1) \iff (2) \iff (3)$ holds for all second-countable Hausdorff spaces and metric spaces. Q.E.D.
:::
