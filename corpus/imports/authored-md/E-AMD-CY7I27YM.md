---
schema: qual/card@1
id: E-AMD-CY7I27YM
kind: exercise
title: Algebraic extensions are transitive
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that if $L/K/F$ with $K/F$ algebraic and $L/K$ algebraic then $L$ is algebraic.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $L/K$ and $K/F$ be algebraic field extensions.
Prove that the composite field extension $L/F$ is algebraic (transitivity of algebraic extensions).

<1>1. Key characterization theorem of algebraic elements and finite extensions: <2>1. An element $\alpha$ in an extension of a field $F_0$ is algebraic over $F_0$ if and only if the simple extension $F_0(\alpha)/F_0$ is a finite extension (i.e., $[F_0(\alpha) : F_0] < \infty$). Proof: If $\alpha$ is algebraic with minimal polynomial $m_\alpha(x) \in F_0[x]$ of degree $d$, then $[F_0(\alpha) : F_0] = d < \infty$.
Conversely, if $[F_0(\alpha) : F_0] = n < \infty$, the $n+1$ elements $\{1, \alpha, \dots, \alpha^n\}$ are linearly dependent over $F_0$, giving a non-zero annihilating polynomial.
<2>2. If each $\alpha_1, \dots, \alpha_k$ is algebraic over $F_0$, then the extension $F_0(\alpha_1, \dots, \alpha_k)/F_0$ is finite.
Proof: By induction on $k$: $F_0(\alpha_1, \dots, \alpha_k) = F_0(\alpha_1, \dots, \alpha_{k-1})(\alpha_k)$.
By the Tower Law $[F_0(\alpha_1, \dots, \alpha_k) : F_0] = [F_0(\alpha_1, \dots, \alpha_k) : F_0(\alpha_1, \dots, \alpha_{k-1})] \cdot [F_0(\alpha_1, \dots, \alpha_{k-1}) : F_0]$.
Since $\alpha_k$ is algebraic over $F_0$, it is algebraic over $F_0(\alpha_1, \dots, \alpha_{k-1})$, so the relative degree is finite.
<2>3. Any finite extension is algebraic: If $[E : F_0] < \infty$, then every $\gamma \in E$ is algebraic over $F_0$.
Proof: For any $\gamma \in E$, $[F_0(\gamma) : F_0] \le [E : F_0] < \infty$, so $\gamma$ is algebraic by <1>1.<2>1.

<1>2. Proof that an arbitrary element $\alpha \in L$ is algebraic over $F$: <2>1. Let $\alpha \in L$ be an arbitrary element.
Proof: Setting an element to prove $L/F$ is algebraic.
<2>2. Since $L/K$ is algebraic, $\alpha$ is algebraic over $K$.
Proof: Hypothesis that $L/K$ is algebraic.
<2>3. There exists a non-zero monic polynomial $p(x) = x^n + c_{n-1} x^{n-1} + \dots + c_1 x + c_0 \in K[x]$ such that $p(\alpha) = 0$.
Proof: Minimal polynomial of $\alpha$ over $K$.
<2>4. The coefficients $c_0, c_1, \dots, c_{n-1}$ belong to $K$.
Proof: $p(x) \in K[x]$.
<2>5. Since $K/F$ is algebraic, each coefficient $c_i \in K$ is algebraic over $F$.
Proof: Hypothesis that $K/F$ is algebraic.
<2>6. Consider the subfield $K_0 = F(c_0, c_1, \dots, c_{n-1}) \subseteq K$.
Proof: Subfield of $K$ generated over $F$ by the finitely many coefficients of $p(x)$.
<2>7. The extension $K_0/F$ is finite: $[K_0 : F] < \infty$.
Proof: By <1>1.<2>2, since each generator $c_i$ is algebraic over $F$.
<2>8. The polynomial $p(x)$ has all its coefficients in $K_0$, so $p(x) \in K_0[x]$.
Proof: By construction of $K_0$.
<2>9. Since $p(\alpha) = 0$ with $p(x) \in K_0[x]$ non-zero, $\alpha$ is algebraic over $K_0$.
Proof: Definition of algebraic element over $K_0$.
<2>10. Therefore, the extension $K_0(\alpha)/K_0$ is finite: $[K_0(\alpha) : K_0] \le \deg(p) = n < \infty$.
Proof: By <1>1.<2>1. <2>11. By the Tower Law for field extensions: $$[K_0(\alpha) : F] = [K_0(\alpha) : K_0] \cdot [K_0 : F].$$ Proof: Multiplicativity of extension degrees.
<2>12. Since $[K_0(\alpha) : K_0] < \infty$ and $[K_0 : F] < \infty$, the product is finite: $[K_0(\alpha) : F] < \infty$.
Proof: Product of two finite positive integers is finite.
<2>13. Since $K_0(\alpha)/F$ is a finite extension and $\alpha \in K_0(\alpha)$, $\alpha$ is algebraic over $F$.
Proof: By <1>1.<2>3.

<1>3. Conclusion: Since $\alpha \in L$ was arbitrary, every element of $L$ is algebraic over $F$, so $L/F$ is an algebraic extension.
Proof: By <1>2.
:::
