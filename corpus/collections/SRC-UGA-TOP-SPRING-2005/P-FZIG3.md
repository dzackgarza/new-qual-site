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
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 1 of the official UGA Spring 2005 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Verified the finite-subcover and distance-to-complement proof and added the
    empty-space case needed for the statement as written.
---

::: {.problem}
Suppose $(X, d)$ is a compact metric space and $\mathcal{U}$ is an open covering of $X$.

Prove that there exists $\delta > 0$ (a **Lebesgue number** for the covering) such that for every $x \in X$, the open ball $B_\delta(x)$ is contained in some element $U \in \mathcal{U}$.
:::

::: {.solution}
**Goal:** Prove the existence of a Lebesgue number $\delta > 0$ for an open cover of a compact metric space using the Extreme Value Theorem applied to an average distance function to closed complements.

::: pf

::: pf-step
Finite subcovering and closed complements:

::: pf-proof

::: pf-step
If $X=\varnothing$, take $\delta=1$. The required condition is then vacuous. Hence assume $X\ne\varnothing$.

:::

::: pf-step
Since $X$ is compact and $\mathcal{U}$ is an open cover, there exists a finite subcover $\{U_1, U_2, \dots, U_n\} \subseteq \mathcal{U}$, with $n\ge1$, such that $X = \bigcup_{i=1}^n U_i$.

:::

::: pf-step
If any $U_i = X$, then for any $\delta > 0$ and all $x \in X$, $B_\delta(x) \subseteq X = U_i$, so the claim holds with $\delta$ arbitrary.

:::

::: pf-step
Assume henceforth that $U_i \subsetneq X$ for all $i \in \{1, \dots, n\}$, and define the closed non-empty complements $C_i = X \setminus U_i$.

:::

:::

:::

::: pf-step
Continuity of the distance-to-set function:

::: pf-proof

::: pf-step
For any non-empty closed set $C \subseteq X$, define $d(x, C) = \inf_{y \in C} d(x, y)$.

:::

::: pf-step
For any $x, x' \in X$ and any $y \in C$, the triangle inequality gives:
$$d(x, y) \le d(x, x') + d(x', y).$$

:::

::: pf-step
Taking the infimum over all $y \in C$:
$$d(x, C) \le d(x, x') + d(x', C) \implies d(x, C) - d(x', C) \le d(x, x').$$

:::

::: pf-step
Reversing the roles of $x$ and $x'$:
$$d(x', C) - d(x, C) \le d(x, x').$$

:::

::: pf-step
Thus $|d(x, C) - d(x', C)| \le d(x, x')$, so $x \mapsto d(x, C)$ is 1-Lipschitz continuous on $X$.

:::

:::

:::

::: {.pf-step #s3}
Construction of the candidate function $f$:

::: pf-proof

::: pf-step
Define $f: X \to \mathbb{R}$ by
$$f(x) = \frac{1}{n} \sum_{i=1}^n d(x, C_i).$$

:::

::: pf-step
Since $f$ is a finite sum of continuous functions, $f$ is continuous on $X$.

:::

::: pf-step
For every $x \in X$, since $\{U_1, \dots, U_n\}$ covers $X$, there is some index $k \in \{1, \dots, n\}$ such that $x \in U_k$.

:::

::: pf-step
Since $U_k$ is open and $x \in U_k$, $x \notin C_k$.

:::

::: pf-step
Since $C_k$ is closed, $d(x, C_k) > 0$.

:::

::: pf-step
Since $d(x, C_i) \ge 0$ for all $i$, we have
$$f(x) \ge \frac{1}{n} d(x, C_k) > 0 \quad \text{for all } x \in X.$$

:::

:::

:::

::: pf-step
Existence of a positive minimum $\delta$:

::: pf-proof

::: pf-step
The function $f$ is continuous on the compact metric space $X$.

:::

::: pf-step
By the Extreme Value Theorem, $f$ attains a global minimum at some point $x_{\text{min}} \in X$:
$$\delta = \min_{x \in X} f(x) = f(x_{\text{min}}).$$

:::

::: pf-step
By step [](#s3){.pf-ref}, $f(x) > 0$ for all $x \in X$, so $\delta > 0$.

:::

:::

:::

::: pf-step
Verification of the Lebesgue condition:

::: pf-proof

::: pf-step
Let $x \in X$ be arbitrary.

:::

::: pf-step
By definition of $\delta$, $f(x) = \frac{1}{n} \sum_{i=1}^n d(x, C_i) \ge \delta$.

:::

::: pf-step
The arithmetic mean of $n$ numbers $\{d(x, C_i)\}_{i=1}^n$ is at least $\delta$, so at least one number must be at least $\delta$:
$$\exists j \in \{1, \dots, n\} \quad \text{such that} \quad d(x, C_j) \ge \delta.$$

:::

::: pf-step
Let $y \in B_\delta(x)$, so $d(x, y) < \delta$.

:::

::: pf-step
If $y \in C_j$, then by definition of infimum $d(x, C_j) \le d(x, y) < \delta$, contradicting $d(x, C_j) \ge \delta$.

:::

::: pf-step
Therefore $y \notin C_j$, so $y \in X \setminus C_j = U_j$.

:::

::: pf-step
Thus $B_\delta(x) \subseteq U_j \in \mathcal{U}$.

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$\delta = \min_{x \in X} f(x) > 0$ is a Lebesgue number for the covering $\mathcal{U}$.
:::

:::

:::

:::
