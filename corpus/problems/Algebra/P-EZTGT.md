---
schema: qual/card@1
id: P-EZTGT
kind: problem
title: $p$-adic numbers and valuations
classification:
  areas:
  - algebra
  topics:
  - Valuation Rings
  - Number Theory
  - Local Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) What is a valuation on a field $K$ (specifically a discrete valuation)?
(2) Define the $p$-adic valuation $v_p$ and the $p$-adic absolute value $|\cdot|_p$ on $\mathbb{Q}$.
(3) Define the ring of $p$-adic integers $\mathbb{Z}_p$ and the field of $p$-adic numbers $\mathbb{Q}_p$ (both algebraically via inverse limits and analytically via completion).
:::

::: solution
**Goal:** Define valuations, the $p$-adic absolute value, and construct the $p$-adic numbers $\mathbb{Q}_p$ and integers $\mathbb{Z}_p$.

<1>1. Definition of a Valuation:
    *Proof:*
    <2>1. Let $K$ be a field. A **discrete valuation** on $K$ is a surjective function $v: K \to \mathbb{Z} \cup \{\infty\}$ satisfying for all $x, y \in K$:
        1. $v(x) = \infty \iff x = 0$,
        2. $v(x y) = v(x) + v(y)$,
        3. $v(x + y) \ge \min(v(x), v(y))$ (the **ultrametric / non-Archimedean inequality**).
    <2>2. The **valuation ring** is $\mathcal{O}_v = \{x \in K \mid v(x) \ge 0\}$, with unique maximal ideal $\mathfrak{m}_v = \{x \in K \mid v(x) > 0\}$ and group of units $\mathcal{O}_v^\times = \{x \in K \mid v(x) = 0\}$.

<1>2. The $p$-adic Valuation and Metric on $\mathbb{Q}$:
    *Proof:*
    <2>1. Fix a prime integer $p$. Any non-zero rational $x \in \mathbb{Q}^\times$ can be written uniquely as $x = p^k \frac{a}{b}$ with $k, a, b \in \mathbb{Z}$ and $p \nmid a, p \nmid b$.
    <2>2. The **$p$-adic valuation** is $v_p(x) = k$ (and $v_p(0) = \infty$).
    <2>3. The **$p$-adic absolute value** on $\mathbb{Q}$ is defined by:
        $$|x|_p = p^{-v_p(x)} \quad (\text{with } |0|_p = 0).$$
    <2>4. $|x|_p$ satisfies the **ultrametric inequality**: $|x + y|_p \le \max(|x|_p, |y|_p)$.
    <2>5. By **Ostrowski's Theorem**, every non-trivial absolute value on $\mathbb{Q}$ is equivalent to either the standard Euclidean absolute value $|\cdot|_\infty$ or a $p$-adic absolute value $|\cdot|_p$ for some prime $p$.

<1>3. Analytic Construction of $\mathbb{Q}_p$ and $\mathbb{Z}_p$ (Completion):
    *Proof:*
    <2>1. The **field of $p$-adic numbers** $\mathbb{Q}_p$ is the Cauchy completion of $\mathbb{Q}$ with respect to the $p$-adic metric $d_p(x, y) = |x - y|_p$:
        $$\mathbb{Q}_p \coloneqq \widehat{\mathbb{Q}}_{|\cdot|_p}.$$
    <2>2. The **ring of $p$-adic integers** $\mathbb{Z}_p$ is the closed unit ball in $\mathbb{Q}_p$:
        $$\mathbb{Z}_p = \{x \in \mathbb{Q}_p \mid |x|_p \le 1\} = \{x \in \mathbb{Q}_p \mid v_p(x) \ge 0\}.$$

<1>4. Algebraic Construction (Inverse Limit and Laurent Series):
    *Proof:*
    <2>1. $\mathbb{Z}_p$ is the **inverse limit** of the projective system of finite rings $\mathbb{Z}/p^n\mathbb{Z}$:
        $$\mathbb{Z}_p \cong \varprojlim_{n} \mathbb{Z}/p^n\mathbb{Z} = \left\{ (x_n)_{n=1}^\infty \in \prod_{n=1}^\infty \mathbb{Z}/p^n\mathbb{Z} \;\middle|\; x_{n+1} \equiv x_n \pmod{p^n} \right\}.$$
    <2>2. Every element $x \in \mathbb{Z}_p$ has a unique canonical $p$-adic expansion:
        $$x = \sum_{n=0}^\infty c_n p^n \quad \text{with digits } c_n \in \{0, 1, \dots, p-1\}.$$
    <2>3. The field of fractions is $\mathbb{Q}_p = \operatorname{Frac}(\mathbb{Z}_p) = \mathbb{Z}_p[1/p]$, where elements have Laurent expansions $\sum_{n=-N}^\infty c_n p^n$.

<1>5. Conclusion:
    Valuations measure order of vanishing at a prime, and $p$-adic numbers $\mathbb{Q}_p$ complete $\mathbb{Q}$ under the ultrametric $|x|_p = p^{-v_p(x)}$. Q.E.D.
:::
