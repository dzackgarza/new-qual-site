---
schema: qual/card@1
id: P-FZIG3
kind: problem
title: The Lebesgue number lemma for compact metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: problem
Suppose $(X, d)$ is a compact metric space and $\mathcal{U}$ is an open covering of $X$.

Prove that there exists $\delta > 0$ (a **Lebesgue number** for the covering) such that for every $x \in X$, the open ball $B_\delta(x)$ is contained in some element $U \in \mathcal{U}$.
:::

::: solution
**Goal:** Prove the existence of a Lebesgue number $\delta > 0$ for an open cover of a compact metric space using the Extreme Value Theorem applied to an average distance function to closed complements.

<1>1. Finite subcovering and closed complements:
::: {.proof}
    <2>1. Since $X$ is compact and $\mathcal{U}$ is an open cover, there exists a finite subcover $\{U_1, U_2, \dots, U_n\} \subseteq \mathcal{U}$ such that $X = \bigcup_{i=1}^n U_i$.
    <2>2. If any $U_i = X$, then for any $\delta > 0$ and all $x \in X$, $B_\delta(x) \subseteq X = U_i$, so the claim holds trivially.
    <2>3. Assume henceforth that $U_i \subsetneq X$ for all $i \in \{1, \dots, n\}$, and define the closed non-empty complements $C_i = X \setminus U_i$.

:::

<1>2. Continuity of the distance-to-set function:
::: {.proof}
    <2>1. For any non-empty closed set $C \subseteq X$, define $d(x, C) = \inf_{y \in C} d(x, y)$.
    <2>2. For any $x, x' \in X$ and any $y \in C$, the triangle inequality gives:
    $$d(x, y) \le d(x, x') + d(x', y).$$
    <2>3. Taking the infimum over all $y \in C$:
    $$d(x, C) \le d(x, x') + d(x', C) \implies d(x, C) - d(x', C) \le d(x, x').$$
    <2>4. Reversing the roles of $x$ and $x'$:
    $$d(x', C) - d(x, C) \le d(x, x').$$
    <2>5. Thus $|d(x, C) - d(x', C)| \le d(x, x')$, so $x \mapsto d(x, C)$ is 1-Lipschitz continuous on $X$.

:::

<1>3. Construction of the candidate function $f$:
::: {.proof}
    <2>1. Define $f: X \to \mathbb{R}$ by
    $$f(x) = \frac{1}{n} \sum_{i=1}^n d(x, C_i).$$
    <2>2. Since $f$ is a finite sum of continuous functions, $f$ is continuous on $X$.
    <2>3. For every $x \in X$, since $\{U_1, \dots, U_n\}$ covers $X$, there is some index $k \in \{1, \dots, n\}$ such that $x \in U_k$.
    <2>4. Since $U_k$ is open and $x \in U_k$, $x \notin C_k$.
    <2>5. Since $C_k$ is closed, $d(x, C_k) > 0$.
    <2>6. Since $d(x, C_i) \ge 0$ for all $i$, we have
    $$f(x) \ge \frac{1}{n} d(x, C_k) > 0 \quad \text{for all } x \in X.$$

:::

<1>4. Existence of a positive minimum $\delta$:
::: {.proof}
    <2>1. The function $f$ is continuous on the compact metric space $X$.
    <2>2. By the Extreme Value Theorem, $f$ attains a global minimum at some point $x_{\text{min}} \in X$:
    $$\delta = \min_{x \in X} f(x) = f(x_{\text{min}}).$$
    <2>3. By <1>3, $f(x) > 0$ for all $x \in X$, so $\delta > 0$.

:::

<1>5. Verification of the Lebesgue condition:
::: {.proof}
    <2>1. Let $x \in X$ be arbitrary.
    <2>2. By definition of $\delta$, $f(x) = \frac{1}{n} \sum_{i=1}^n d(x, C_i) \ge \delta$.
    <2>3. The arithmetic mean of $n$ numbers $\{d(x, C_i)\}_{i=1}^n$ is at least $\delta$, so at least one number must be at least $\delta$:
    $$\exists j \in \{1, \dots, n\} \quad \text{such that} \quad d(x, C_j) \ge \delta.$$
    <2>4. Let $y \in B_\delta(x)$, so $d(x, y) < \delta$.
    <2>5. If $y \in C_j$, then by definition of infimum $d(x, C_j) \le d(x, y) < \delta$, contradicting $d(x, C_j) \ge \delta$.
    <2>6. Therefore $y \notin C_j$, so $y \in X \setminus C_j = U_j$.
    <2>7. Thus $B_\delta(x) \subseteq U_j \in \mathcal{U}$.

:::

<1>6. Conclusion:
::: {.proof}
    $\delta = \min_{x \in X} f(x) > 0$ is a Lebesgue number for the covering $\mathcal{U}$.
:::
:::

