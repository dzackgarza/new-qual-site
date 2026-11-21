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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof. The five container steps keep their nested steps and now state why
    those subclaims suffice, and the 25 leaf steps that asserted their claim with no justification each
    carry a sentence deriving it from the preceding steps. The mathematics is unchanged: the empty space,
    the cover with a member equal to X, and the proper-subset case, then the Lipschitz estimate for
    d(.,C), the average f, its positivity, its minimum delta, and the verification that B_delta(x) lies in
    the member U_j with d(x,C_j) at least delta. Checked against the statement on the card, problem 1 of
    the UGA Spring 2005 topology exam. Theorem 27.4 is cited for the extreme value theorem. Nothing was
    found to correct in the statement.
---

::: {.problem}
Suppose $(X, d)$ is a compact metric space and $\mathcal{U}$ is an open covering of $X$.

Prove that there exists $\delta > 0$ (a **Lebesgue number** for the covering) such that for every $x \in X$, the open ball $B_\delta(x)$ is contained in some element $U \in \mathcal{U}$.
:::

::: {.solution}
::: pf

::: pf-step
Finite subcovering and closed complements:

::: pf-proof
The subclaims dispose of the empty space and of a cover with a member equal to $X$, and then reduce to the case in which every member is a proper subset, which is the only case that needs an argument.

::: pf-step
If $X=\varnothing$, take $\delta=1$. The required condition is then vacuous. Hence assume $X\ne\varnothing$.

::: pf-proof
The condition concerns every $x\in X$, and there is no such point, so it holds for $\delta=1$; with that case settled the argument continues under $X\neq\varnothing$.
:::

:::

::: pf-step
Since $X$ is compact and $\mathcal{U}$ is an open cover, there exists a finite subcover $\{U_1, U_2, \dots, U_n\} \subseteq \mathcal{U}$, with $n\ge1$, such that $X = \bigcup_{i=1}^n U_i$.

::: pf-proof
Compactness gives a finite subcover, and it is non-empty because $X\neq\varnothing$ is covered; its members may therefore be listed as $U_1,\dots,U_n$ with $n\ge1$.
:::

:::

::: pf-step
If any $U_i = X$, then for any $\delta > 0$ and all $x \in X$, $B_\delta(x) \subseteq X = U_i$, so the claim holds with $\delta$ arbitrary.

::: pf-proof
For $\delta>0$ and $x\in X$ the ball $B_\delta(x)$ is a subset of $X$, which is the member $U_i$ of $\mathcal{U}$ required by the statement.
:::

:::

::: pf-step
Assume henceforth that $U_i \subsetneq X$ for all $i \in \{1, \dots, n\}$, and define the closed non-empty complements $C_i = X \setminus U_i$.

::: pf-proof
Each $C_i$ is closed because $U_i$ is open, and it is non-empty because $U_i$ is a proper subset of $X$; this is the case left open by the two preceding subclaims.
:::

:::

:::

:::

::: pf-step
Continuity of the distance-to-set function:

::: pf-proof
The subclaims establish the Lipschitz estimate for a fixed non-empty closed set $C$, which is the only property of $d(\cdot,C)$ used afterwards.

::: pf-step
For any non-empty closed set $C \subseteq X$, define $d(x, C) = \inf_{y \in C} d(x, y)$.

::: pf-proof
For each $x$ the set $\{d(x,y):y\in C\}$ is a non-empty subset of $[0,\infty)$, bounded below, so its infimum exists and is a real number.
:::

:::

::: pf-step
For any $x, x' \in X$ and any $y \in C$, the triangle inequality gives:
$$d(x, y) \le d(x, x') + d(x', y).$$

::: pf-proof
This is the triangle inequality for the metric $d$, applied to the triple $x,x',y$.
:::

:::

::: pf-step
Taking the infimum over all $y \in C$:
$$d(x, C) \le d(x, x') + d(x', C) \implies d(x, C) - d(x', C) \le d(x, x').$$

::: pf-proof
The preceding inequality holds for every $y\in C$, so $d(x,C)=\inf_{y\in C}d(x,y)\le\inf_{y\in C}\bigl(d(x,x')+d(x',y)\bigr)=d(x,x')+d(x',C)$, and subtracting the finite number $d(x',C)$ gives the second inequality.
:::

:::

::: pf-step
Reversing the roles of $x$ and $x'$:
$$d(x', C) - d(x, C) \le d(x, x').$$

::: pf-proof
The same argument with $x$ and $x'$ interchanged, using the symmetry $d(x,x')=d(x',x)$.
:::

:::

::: pf-step
Thus $\abs{d(x, C) - d(x', C)} \le d(x, x')$, so $x \mapsto d(x, C)$ is 1-Lipschitz continuous on $X$.

::: pf-proof
The two preceding subclaims say that both $d(x,C)-d(x',C)$ and its negative are at most $d(x,x')$, which is the absolute value bound; a Lipschitz map is continuous.
:::

:::

:::

:::

::: {.pf-step #s3}
Construction of the candidate function $f$:

::: pf-proof
The subclaims define $f$ and show that it is continuous and everywhere positive; positivity is what makes its minimum a legitimate Lebesgue number.

::: pf-step
Define $f: X \to \RR$ by
$$f(x) = \frac{1}{n} \sum_{i=1}^n d(x, C_i).$$

::: pf-proof
Each $d(\cdot,C_i)$ is a real-valued function on $X$ by the preceding container, so the finite average defines a function $X\to\RR$.
:::

:::

::: pf-step
Since $f$ is a finite sum of continuous functions, $f$ is continuous on $X$.

::: pf-proof
Each $d(\cdot,C_i)$ is continuous by the Lipschitz estimate of the preceding container; finite sums and scalar multiples of continuous real functions are continuous.
:::

:::

::: pf-step
For every $x \in X$, since $\{U_1, \dots, U_n\}$ covers $X$, there is some index $k \in \{1, \dots, n\}$ such that $x \in U_k$.

::: pf-proof
This is exactly the statement that the $U_i$ cover $X$.
:::

:::

::: pf-step
Since $U_k$ is open and $x \in U_k$, $x \notin C_k$.

::: pf-proof
$C_k$ is defined as the complement $X\setminus U_k$.
:::

:::

::: pf-step
Since $C_k$ is closed, $d(x, C_k) > 0$.

::: pf-proof
The complement of the closed set $C_k$ is an open neighbourhood of $x$, so it contains a ball $B_r(x)$; every point of $C_k$ is then at distance at least $r$ from $x$, whence $d(x,C_k)\ge r>0$.
:::

:::

::: pf-step
Since $d(x, C_i) \ge 0$ for all $i$, we have
$$f(x) \ge \frac{1}{n} d(x, C_k) > 0 \quad \text{for all } x \in X.$$

::: pf-proof
Each summand is a distance and so is non-negative, which makes the average at least the single term $\frac1n d(x,C_k)$; that term is positive by the preceding subclaim.
:::

:::

:::

:::

::: pf-step
Existence of a positive minimum $\delta$:

::: pf-proof
Continuity on a compact space converts the pointwise positivity of $f$ into a uniform positive lower bound.

::: pf-step
The function $f$ is continuous on the compact metric space $X$.

::: pf-proof
Continuity is step [](#s3){.pf-ref}, and $X$ is compact by hypothesis.
:::

:::

::: pf-step
By the Extreme Value Theorem, $f$ attains a global minimum at some point $x_{\text{min}} \in X$:
$$\delta = \min_{x \in X} f(x) = f(x_{\text{min}}).$$

::: pf-proof
A continuous real-valued function on a non-empty compact space attains its minimum (Theorem 27.4), and $X\neq\varnothing$ was assumed in the first container.
:::

:::

::: pf-step
By step [](#s3){.pf-ref}, $f(x) > 0$ for all $x \in X$, so $\delta > 0$.

::: pf-proof
$\delta$ is the value of $f$ at the point $x_{\text{min}}$, and every value of $f$ is positive.
:::

:::

:::

:::

::: pf-step
Verification of the Lebesgue condition:

::: pf-proof
The subclaims show that the member $U_j$ on which $d(x,C_j)$ is largest contains the whole ball $B_\delta(x)$.

::: pf-step
Let $x \in X$ be arbitrary.

::: pf-proof
Nothing is assumed about $x$ beyond membership in $X$, so the conclusion obtained below holds for every point.
:::

:::

::: pf-step
By definition of $\delta$, $f(x) = \frac{1}{n} \sum_{i=1}^n d(x, C_i) \ge \delta$.

::: pf-proof
$\delta$ is the minimum of $f$ over $X$, so it is at most the value at $x$.
:::

:::

::: pf-step
The arithmetic mean of $n$ numbers $\{d(x, C_i)\}_{i=1}^n$ is at least $\delta$, so at least one number must be at least $\delta$:
$$\exists j \in \{1, \dots, n\} \quad \text{such that} \quad d(x, C_j) \ge \delta.$$

::: pf-proof
If every term were less than $\delta$, their average would be less than $\delta$ because $n\ge1$; the preceding subclaim says the average is at least $\delta$, so some term is at least $\delta$.
:::

:::

::: pf-step
Let $y \in B_\delta(x)$, so $d(x, y) < \delta$.

::: pf-proof
This is the definition of the open ball of radius $\delta$ about $x$.
:::

:::

::: pf-step
If $y \in C_j$, then by definition of infimum $d(x, C_j) \le d(x, y) < \delta$, contradicting $d(x, C_j) \ge \delta$.

::: pf-proof
$d(x,C_j)$ is the infimum of the numbers $d(x,z)$ with $z\in C_j$, and $d(x,y)$ is one of them, so it is at least the infimum.
:::

:::

::: pf-step
Therefore $y \notin C_j$, so $y \in X \setminus C_j = U_j$.

::: pf-proof
$C_j$ is by definition the complement of $U_j$.
:::

:::

::: pf-step
Thus $B_\delta(x) \subseteq U_j \in \mathcal{U}$.

::: pf-proof
Every $y\in B_\delta(x)$ lies in $U_j$, and $U_j$ is one of the members of $\mathcal{U}$ extracted from the cover.
:::

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
The preceding container shows that for every $x\in X$ the ball $B_\delta(x)$ is contained in a member of $\mathcal{U}$, and $\delta=\min_{x\in X}f(x)>0$; that is the definition of a Lebesgue number, so $\delta$ is one for $\mathcal{U}$.
:::

:::

:::

:::
