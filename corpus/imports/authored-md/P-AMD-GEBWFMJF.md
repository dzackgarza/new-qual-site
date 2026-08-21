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
solved: true
---

::: {.problem}
Prove the Ham Sandwich theorem.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $A_1, A_2, \dots, A_n \subset \mathbb{R}^n$ be $n$ bounded Lebesgue measurable subsets of finite measure $\mu(A_i) < \infty$.
Prove the Ham Sandwich Theorem: there exists an affine hyperplane $H \subset \mathbb{R}^n$ that simultaneously bisects all $n$ sets, i.e., divides each $A_i$ into two pieces of equal measure.

<1>1. Parameterize oriented hyperplanes via the sphere $S^n$.
<2>1. Embed $\mathbb{R}^n$ into $\mathbb{R}^{n+1}$ at height 1: $\iota(x) = (x, 1) \in \mathbb{R}^{n+1}$.
<2>2. For each unit vector $u = (v, w) \in S^n \subset \mathbb{R}^{n+1}$ (with $v \in \mathbb{R}^n, w \in \mathbb{R}$), define the closed affine half-space in $\mathbb{R}^n$: $$H^+(u) = \{ x \in \mathbb{R}^n \mid \langle \iota(x), u \rangle \ge 0 \} = \{ x \in \mathbb{R}^n \mid \langle x, v \rangle + w \ge 0 \}.$$ <2>3. The opposite vector $-u$ gives the complementary half-space: $$H^+(-u) = \{ x \in \mathbb{R}^n \mid \langle x, -v \rangle - w \ge 0 \} = \{ x \in \mathbb{R}^n \mid \langle x, v \rangle + w \le 0 \}.$$ <2>4. The boundary hyperplane is $H(u) = \{ x \in \mathbb{R}^n \mid \langle x, v \rangle + w = 0 \}$.
<2>5. Since $H(u)$ has Lebesgue measure zero in $\mathbb{R}^n$, $\mu(A_i \cap H(u)) = 0$, so: $$\mu(A_i \cap H^+(u)) + \mu(A_i \cap H^+(-u)) = \mu(A_i) \quad \text{for each } i \in \{1, \dots, n\}.$$ <2>6. Proof: By standard geometric parametrization of affine hyperplanes.
Q.E.D.

<1>2. Define a continuous map $F \colon S^n \to \mathbb{R}^n$.
<2>1. For each $i \in \{1, \dots, n\}$, define the $i$-th coordinate function $f_i \colon S^n \to \mathbb{R}$ by: $$f_i(u) = \mu(A_i \cap H^+(u)).$$ <2>2. $f_i$ is continuous: Let $u_k \to u$ in $S^n$.
The characteristic functions $\chi_{A_i \cap H^+(u_k)}$ converge almost everywhere to $\chi_{A_i \cap H^+(u)}$ (except possibly on the hyperplane $H(u)$, which is a null set).
Since $|\chi_{A_i \cap H^+(u_k)}| \le \chi_{A_i}$ and $\mu(A_i) < \infty$, the Dominated Convergence Theorem implies: $$\lim_{k \to \infty} f_i(u_k) = \lim_{k \to \infty} \int_{\mathbb{R}^n} \chi_{A_i \cap H^+(u_k)} \, d\mu = \int_{\mathbb{R}^n} \chi_{A_i \cap H^+(u)} \, d\mu = f_i(u).$$ <2>3. Define $F \colon S^n \to \mathbb{R}^n$ by $F(u) = (f_1(u), f_2(u), \dots, f_n(u))$.
<2>4. Since each component $f_i$ is continuous, $F$ is continuous.
<2>5. Proof: By Lebesgue Dominated Convergence Theorem.
Q.E.D.

<1>3. Apply the Borsuk-Ulam theorem to $F$.
<2>1. By the Borsuk-Ulam theorem (proved in P-AMD-6OJQMSOZ for $n=2$, and holding for all $n \ge 1$), for any continuous map $F \colon S^n \to \mathbb{R}^n$, there exists a point $u^* \in S^n$ such that: $$F(u^*) = F(-u^*).$$ <2>2. In terms of coordinate functions, this means for all $i \in \{1, \dots, n\}$: $$f_i(u^*) = f_i(-u^*) \iff \mu(A_i \cap H^+(u^*)) = \mu(A_i \cap H^+(-u^*)).$$ <2>3. Combining with the total measure equality from <1>1: $$\mu(A_i \cap H^+(u^*)) + \mu(A_i \cap H^+(-u^*)) = \mu(A_i) \implies 2 \mu(A_i \cap H^+(u^*)) = \mu(A_i) \implies \mu(A_i \cap H^+(u^*)) = \frac{1}{2} \mu(A_i).$$ <2>4. If $v^* = 0$, then $u^* = (0, \pm 1)$, giving $H^+(u^*) = \mathbb{R}^n$ or $\emptyset$, which would mean $\mu(A_i) = 0$ for all $i$.
If any $\mu(A_i) > 0$, then $v^* \neq 0$, so $H(u^*)$ is a genuine affine hyperplane in $\mathbb{R}^n$.
<2>5. The hyperplane $H(u^*)$ bisects all $n$ sets $A_1, \dots, A_n$ simultaneously.
<2>6. Proof: By Borsuk-Ulam theorem.
Q.E.D.

<1>4. Q.E.D. <2>1. Proof: <1>1–<1>3 establish the Ham Sandwich theorem for any $n$ measurable sets of finite measure in $\mathbb{R}^n$.
:::
