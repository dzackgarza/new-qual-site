---
schema: qual/card@1
id: P-MMAQ-DGLROO56SW
kind: problem
title: Show that the space $C^1([a, b])$ is a Banach space when equipped…
classification:
  areas:
  - real-analysis
  topics:
  - function-spaces
  - norms
  - completeness
relations: []
review: draft
---

::: problem
Show that the space $C^1([a, b])$ is a Banach space when equipped with the norm
$$
\|f\|:=\sup _{x \in[a, b]}|f(x)|+\sup _{x \in[a, b]}\left|f^{\prime}(x)\right|.
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that the space $C^1([a, b])$ with norm $\|f\|_{C^1} = \|f\|_\infty + \|f'\|_\infty = \sup_{x \in [a, b]} |f(x)| + \sup_{x \in [a, b]} |f'(x)|$ is a Banach space (a complete normed vector space).

<1>1. **Verification of the Norm Axioms on $C^1([a, b])$.**
  <2>1. Non-negativity: $\|f\|_{C^1} \geq 0$ for all $f \in C^1([a, b])$.
    Proof: Sum of two non-negative suprema.
  <2>2. Positive definiteness: $\|f\|_{C^1} = 0 \iff f = 0$.
    Proof: If $\|f\|_{C^1} = 0$, then $\|f\|_\infty = 0$, so $|f(x)| = 0$ for all $x \in [a, b]$, hence $f \equiv 0$. Conversely, if $f \equiv 0$, then $f' \equiv 0$, so $\|f\|_\infty = \|f'\|_\infty = 0$.
  <2>3. Absolute homogeneity: $\|\alpha f\|_{C^1} = |\alpha| \|f\|_{C^1}$ for all $\alpha \in \RR$ (or $\CC$).
    Proof: $\|(\alpha f)'\|_\infty = \|\alpha f'\|_\infty = |\alpha| \|f'\|_\infty$, so $\|\alpha f\|_\infty + \|\alpha f'\|_\infty = |\alpha| (\|f\|_\infty + \|f'\|_\infty)$.
  <2>4. Triangle inequality: $\|f + g\|_{C^1} \leq \|f\|_{C^1} + \|g\|_{C^1}$.
    Proof: By linearity of differentiation $(f+g)' = f' + g'$, and the triangle inequality for the supremum norm:
    $$
    \|f+g\|_{C^1} = \|f+g\|_\infty + \|f'+g'\|_\infty \leq (\|f\|_\infty + \|g\|_\infty) + (\|f'\|_\infty + \|g'\|_\infty) = \|f\|_{C^1} + \|g\|_{C^1}.
    $$

<1>2. **Completeness: Every Cauchy sequence in $(C^1([a, b]), \|\cdot\|_{C^1})$ converges in $C^1([a, b])$.**
  <2>1. Let $\{f_n\}_{n=1}^\infty$ be a Cauchy sequence in $(C^1([a, b]), \|\cdot\|_{C^1})$.
  <2>2. $\{f_n\}$ and $\{f_n'\}$ are Cauchy sequences in $(C([a, b]), \|\cdot\|_\infty)$.
    Proof: For any $\eps > 0$, there exists $N \in \NN$ such that for all $n, m \geq N$:
    $$
    \|f_n - f_m\|_\infty \leq \|f_n - f_m\|_{C^1} < \eps \quad \text{and} \quad \|f_n' - f_m'\|_\infty \leq \|f_n - f_m\|_{C^1} < \eps.
    $$
  <2>3. There exist continuous functions $f, g \in C([a, b])$ such that $f_n \to f$ uniformly on $[a, b]$ and $f_n' \to g$ uniformly on $[a, b]$.
    Proof: The space $(C([a, b]), \|\cdot\|_\infty)$ is complete (a Banach space), so every Cauchy sequence in the supremum norm converges uniformly to a continuous limit function.
  <2>4. $f$ is continuously differentiable on $[a, b]$ and $f'(x) = g(x)$ for all $x \in [a, b]$.
    <3>1. For each $n \geq 1$ and all $x \in [a, b]$, by the Fundamental Theorem of Calculus:
      $$
      f_n(x) = f_n(a) + \int_a^x f_n'(t)\,dt.
      $$
    <3>2. Since $f_n' \to g$ uniformly on $[a, b]$, we can pass the limit inside the integral:
      $$
      \lim_{n\to\infty} \int_a^x f_n'(t)\,dt = \int_a^x \lim_{n\to\infty} f_n'(t)\,dt = \int_a^x g(t)\,dt.
      $$
    <3>3. Since $f_n(a) \to f(a)$ and $f_n(x) \to f(x)$ pointwise, taking $n \to \infty$ in <3>1 yields:
      $$
      f(x) = f(a) + \int_a^x g(t)\,dt.
      $$
    <3>4. Since $g \in C([a, b])$, by the Fundamental Theorem of Calculus $f$ is differentiable on $[a, b]$ and $f'(x) = g(x)$ for all $x \in [a, b]$. Since $g$ is continuous, $f \in C^1([a, b])$.
  <2>5. $\|f_n - f\|_{C^1} \to 0$ as $n \to \infty$.
    Proof: $\|f_n - f\|_{C^1} = \|f_n - f\|_\infty + \|f_n' - f'\|_\infty = \|f_n - f\|_\infty + \|f_n' - g\|_\infty \to 0 + 0 = 0$ as $n \to \infty$.

<1>3. **Conclusion.**
  $C^1([a, b])$ is complete with respect to $\|\cdot\|_{C^1}$, hence it is a Banach space. Q.E.D.
:::
