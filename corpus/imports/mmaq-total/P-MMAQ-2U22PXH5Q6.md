---
schema: qual/card@1
id: P-MMAQ-2U22PXH5Q6
kind: problem
title: "Let $(X, d)$ and $(Y, \\rho)$ be metric spaces, $f: X\\to Y$, and $x_0 \\in X$. Prove that the\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - completeness
relations: []
review: draft
solved: true
---

::: problem
Let $(X, d)$ and $(Y, \rho)$ be metric spaces, $f: X\to Y$, and $x_0 \in X$.

Prove that the following statements are equivalent:

1. For every $\varepsilon > 0 \quad \exists \delta > 0$ such that $\rho( f(x), f(x_0)  ) < \varepsilon$ whenever $d(x, x_0) < \delta$.

2. The sequence $\theset{f(x_n)}_{n=1}^\infty \to f(x_0)$ for every sequence $\theset{x_n} \to x_0$ in $X$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $(X, d)$ and $(Y, \rho)$ be metric spaces, $f: X \to Y$, and $x_0 \in X$. Prove that $(1) \iff (2)$, where:
(1) $\forall \eps > 0, \exists \delta > 0$ such that $d(x, x_0) < \delta \implies \rho(f(x), f(x_0)) < \eps$ ($\eps$-$\delta$ continuity at $x_0$);
(2) For every sequence $\{x_n\} \subseteq X$ with $x_n \to x_0$, $f(x_n) \to f(x_0)$ in $Y$ (sequential continuity at $x_0$).

<1>1. **Direction $(1) \implies (2)$ (Cauchy/Weierstrass continuity implies sequential continuity).**
  <2>1. Assume (1) holds. Let $\{x_n\}_{n=1}^\infty \subseteq X$ be an arbitrary sequence such that $x_n \to x_0$ in $(X, d)$.
  <2>2. Let $\eps > 0$ be given.
  <2>3. By (1), there exists $\delta > 0$ such that $\rho(f(x), f(x_0)) < \eps$ whenever $d(x, x_0) < \delta$.
  <2>4. Since $x_n \to x_0$, there exists $N \in \NN$ such that $d(x_n, x_0) < \delta$ for all $n \geq N$.
    Proof: By the definition of sequence convergence in the metric space $(X, d)$ with tolerance $\delta > 0$.
  <2>5. For all $n \geq N$, $\rho(f(x_n), f(x_0)) < \eps$.
    Proof: By <2>4, $d(x_n, x_0) < \delta$ for each $n \geq N$, so by <2>3, $\rho(f(x_n), f(x_0)) < \eps$.
  <2>6. Therefore, $\lim_{n\to\infty} f(x_n) = f(x_0)$ in $(Y, \rho)$.
    Proof: Since $\eps > 0$ was arbitrary, this satisfies the definition of sequential convergence in $(Y, \rho)$.

<1>2. **Direction $(2) \implies (1)$ (Sequential continuity implies $\eps$-$\delta$ continuity).**
  <2>1. We prove the contrapositive: $\neg (1) \implies \neg (2)$.
  <2>2. Assume $\neg (1)$ holds.
    Proof: The negation of (1) is: there exists $\eps_0 > 0$ such that for every $\delta > 0$, there exists some $x \in X$ with $d(x, x_0) < \delta$ and $\rho(f(x), f(x_0)) \geq \eps_0$.
  <2>3. For each $n \in \NN$, choose $\delta_n = \frac{1}{n} > 0$. By <2>2, there exists $x_n \in X$ such that:
    $$
    d(x_n, x_0) < \frac{1}{n} \quad \text{and} \quad \rho(f(x_n), f(x_0)) \geq \eps_0.
    $$
  <2>4. The sequence $\{x_n\}_{n=1}^\infty$ satisfies $x_n \to x_0$ in $(X, d)$.
    Proof: For any $\eta > 0$, choosing $N = \lceil 1/\eta \rceil$, for all $n \geq N$ we have $d(x_n, x_0) < 1/n \leq 1/N \leq \eta$. Thus $d(x_n, x_0) \to 0$ as $n \to \infty$.
  <2>5. The sequence $\{f(x_n)\}_{n=1}^\infty$ does NOT converge to $f(x_0)$ in $(Y, \rho)$.
    Proof: For all $n \in \NN$, $\rho(f(x_n), f(x_0)) \geq \eps_0 > 0$. If $f(x_n) \to f(x_0)$, then $\rho(f(x_n), f(x_0)) < \eps_0$ for sufficiently large $n$, a contradiction.
  <2>6. Thus (2) fails to hold.
    Proof: $\{x_n\}$ is a sequence converging to $x_0$ whose image sequence $\{f(x_n)\}$ does not converge to $f(x_0)$.
  <2>7. Therefore, $(2) \implies (1)$ holds by contraposition.

<1>3. **Conclusion.**
  Statements (1) and (2) are equivalent. Q.E.D.
:::
