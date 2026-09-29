---
schema: qual/card@1
id: P-AMD-GEBWFMJF
kind: problem
title: Ham Sandwich theorem
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove the Ham Sandwich theorem.
:::

::: {.solution}
**Goal:** Let $A_1, A_2, \dots, A_n \subset \mathbb{R}^n$ be $n$ bounded Lebesgue measurable subsets of finite measure $\mu(A_i) < \infty$.
Prove the Ham Sandwich Theorem: there exists an affine hyperplane $H \subset \mathbb{R}^n$ that simultaneously bisects all $n$ sets, i.e., divides each $A_i$ into two pieces of equal measure.

::: pf

::: {.pf-step #s1}
Parameterize oriented hyperplanes via the sphere $S^n$.

::: pf-proof

::: pf-step
Embed $\mathbb{R}^n$ into $\mathbb{R}^{n+1}$ at height 1: $\iota(x) = (x, 1) \in \mathbb{R}^{n+1}$.
:::

::: pf-step
For each unit vector $u = (v, w) \in S^n \subset \mathbb{R}^{n+1}$ (with $v \in \mathbb{R}^n, w \in \mathbb{R}$), define the closed affine half-space in $\mathbb{R}^n$: $$H^+(u) = \{ x \in \mathbb{R}^n \mid \langle \iota(x), u \rangle \ge 0 \} = \{ x \in \mathbb{R}^n \mid \langle x, v \rangle + w \ge 0 \}.$$
:::

::: pf-step
The opposite vector $-u$ gives the complementary half-space: $$H^+(-u) = \{ x \in \mathbb{R}^n \mid \langle x, -v \rangle - w \ge 0 \} = \{ x \in \mathbb{R}^n \mid \langle x, v \rangle + w \le 0 \}.$$
:::

::: pf-step
The boundary hyperplane is $H(u) = \{ x \in \mathbb{R}^n \mid \langle x, v \rangle + w = 0 \}$.
:::

::: pf-step
Since $H(u)$ has Lebesgue measure zero in $\mathbb{R}^n$, $\mu(A_i \cap H(u)) = 0$, so: $$\mu(A_i \cap H^+(u)) + \mu(A_i \cap H^+(-u)) = \mu(A_i) \quad \text{for each } i \in \{1, \dots, n\}.$$
:::

::: pf-qed
The two half-spaces $H^+(u)$ and $H^+(-u)$ are complementary, overlapping only on the hyperplane $H(u)$; since $H(u)$ has measure zero, the measures of the two intersections add to $\mu(A_i)$.
:::

:::

:::

::: {.pf-step #s2}
Define a continuous map $F \colon S^n \to \mathbb{R}^n$.

::: pf-proof

::: pf-step
For each $i \in \{1, \dots, n\}$, define the $i$-th coordinate function $f_i \colon S^n \to \mathbb{R}$ by: $$f_i(u) = \mu(A_i \cap H^+(u)).$$
:::

::: pf-step
$f_i$ is continuous: Let $u_k \to u$ in $S^n$.
The characteristic functions $\chi_{A_i \cap H^+(u_k)}$ converge almost everywhere to $\chi_{A_i \cap H^+(u)}$ (except possibly on the hyperplane $H(u)$, which is a null set).
Since $|\chi_{A_i \cap H^+(u_k)}| \le \chi_{A_i}$ and $\mu(A_i) < \infty$, the Dominated Convergence Theorem implies: $$\lim_{k \to \infty} f_i(u_k) = \lim_{k \to \infty} \int_{\mathbb{R}^n} \chi_{A_i \cap H^+(u_k)} \, d\mu = \int_{\mathbb{R}^n} \chi_{A_i \cap H^+(u)} \, d\mu = f_i(u).$$
:::

::: pf-step
Define $F \colon S^n \to \mathbb{R}^n$ by $F(u) = (f_1(u), f_2(u), \dots, f_n(u))$.
:::

::: pf-step
Since each component $f_i$ is continuous, $F$ is continuous.
:::

::: pf-qed
The Dominated Convergence Theorem applies because the integrands are dominated by $\chi_{A_i}$ and $\mu(A_i) < \infty$, so each $f_i$ is continuous; hence $F$ is continuous.
:::

:::

:::

::: {.pf-step #s3}
Apply the Borsuk-Ulam theorem to $F$.

::: pf-proof

::: pf-step
By the Borsuk-Ulam theorem (proved in P-AMD-6OJQMSOZ for $n=2$, and holding for all $n \ge 1$), for any continuous map $F \colon S^n \to \mathbb{R}^n$, there exists a point $u^* \in S^n$ such that: $$F(u^*) = F(-u^*).$$
:::

::: {.pf-step #s3-2}
In terms of coordinate functions, this means for all $i \in \{1, \dots, n\}$: $$f_i(u^*) = f_i(-u^*) \iff \mu(A_i \cap H^+(u^*)) = \mu(A_i \cap H^+(-u^*)).$$
:::

::: {.pf-step #s3-3}
Combining with the total measure equality from step [](#s1){.pf-ref}: $$\mu(A_i \cap H^+(u^*)) + \mu(A_i \cap H^+(-u^*)) = \mu(A_i) \implies 2 \mu(A_i \cap H^+(u^*)) = \mu(A_i) \implies \mu(A_i \cap H^+(u^*)) = \frac{1}{2} \mu(A_i).$$
:::

::: pf-step
If $v^* = 0$, then $u^* = (0, \pm 1)$, giving $H^+(u^*) = \mathbb{R}^n$ or $\emptyset$, which would mean $\mu(A_i) = 0$ for all $i$.
If any $\mu(A_i) > 0$, then $v^* \neq 0$, so $H(u^*)$ is a genuine affine hyperplane in $\mathbb{R}^n$.
:::

::: pf-step
The hyperplane $H(u^*)$ bisects all $n$ sets $A_1, \dots, A_n$ simultaneously.
:::

::: pf-qed
Borsuk–Ulam gives $F(u^*) = F(-u^*)$, which by steps [](#s3-2){.pf-ref} and [](#s3-3){.pf-ref} forces $\mu(A_i \cap H^+(u^*)) = \frac{1}{2}\mu(A_i)$ for every $i$; hence $H(u^*)$ bisects each $A_i$.
:::

:::

:::

::: pf-step
Conclusion.

::: pf-proof
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} establish the Ham Sandwich theorem for any $n$ measurable sets of finite measure in $\mathbb{R}^n$.
:::

:::

:::
:::
