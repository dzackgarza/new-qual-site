---
schema: qual/card@1
id: E-AMD-H7JVMMY4
kind: problem
title: Algebraicity of $\alpha\pm\beta$ and $\alpha\beta^{\pm 1}$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that if $\alpha, \beta$ are algebraic over $F$, then $\alpha\pm \beta, \alpha\beta$, and $\alpha\beta^{-1}$ (for $\beta \neq 0$) are all algebraic over $F$.
:::

::: solution
**Goal:** Prove that the set of elements algebraic over a field $F$ in an extension field forms a subfield, so $\alpha \pm \beta, \alpha\beta$, and $\alpha\beta^{-1}$ (for $\beta \neq 0$) are algebraic over $F$.

<1>1. Finiteness of the composite extension $F(\alpha, \beta)$:
    *Proof:*
    <2>1. Because $\alpha$ is algebraic over $F$, the simple extension has finite degree $[F(\alpha) : F] = \deg(m_{\alpha, F}) < \infty$.
    <2>2. Because $\beta$ is algebraic over $F$, its minimal polynomial $m_{\beta, F}(x) \in F[x] \subseteq F(\alpha)[x]$ annihilates $\beta$.
    <2>3. Thus $\beta$ is algebraic over $F(\alpha)$, and $[F(\alpha, \beta) : F(\alpha)] \le [F(\beta) : F] < \infty$.
    <2>4. By the Tower Law:
        $$[F(\alpha, \beta) : F] = [F(\alpha, \beta) : F(\alpha)] \cdot [F(\alpha) : F] < \infty.$$
    <2>5. Hence $F(\alpha, \beta)$ is a finite field extension of $F$.

<1>2. Every element of a finite extension is algebraic:
    *Proof:*
    <2>1. Let $d = [F(\alpha, \beta) : F]$.
    <2>2. For any element $\gamma \in F(\alpha, \beta)$, the $d + 1$ powers $\{1, \gamma, \gamma^2, \dots, \gamma^d\}$ must be linearly dependent over $F$ because $\dim_F F(\alpha, \beta) = d$.
    <2>3. There exist coefficients $c_0, c_1, \dots, c_d \in F$, not all zero, such that:
        $$\sum_{i=0}^d c_i \gamma^i = 0.$$
    <2>4. Thus $\gamma$ is the root of a non-zero polynomial $p(x) = \sum_{i=0}^d c_i x^i \in F[x]$, so $\gamma$ is algebraic over $F$.

<1>3. Closure under algebraic operations:
    *Proof:*
    <2>1. Since $F(\alpha, \beta)$ is a field containing $\alpha$ and $\beta$, it contains:
        - $\alpha + \beta \in F(\alpha, \beta)$,
        - $\alpha - \beta \in F(\alpha, \beta)$,
        - $\alpha \beta \in F(\alpha, \beta)$,
        - $\alpha \beta^{-1} \in F(\alpha, \beta)$ (for $\beta \neq 0$).
    <2>2. Applying <1>2 to each of these elements shows that they are all algebraic over $F$.

<1>4. Conclusion:
    $\alpha \pm \beta, \alpha \beta$, and $\alpha \beta^{-1}$ (for $\beta \neq 0$) are all algebraic over $F$. Q.E.D.
:::
