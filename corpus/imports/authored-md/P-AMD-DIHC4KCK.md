---
schema: qual/card@1
id: P-AMD-DIHC4KCK
kind: problem
title: $L^2$-bounded a.e. convergent sequences remain in $L^2$ with $\int f_k\to\int f$
classification:
  areas:
  - real-analysis
  topics:
  - l2
  - fatou
  - egorov
  - convergence-of-integrals
relations: []
review: draft
solved: true
---

::: {.problem}
Let $\{f_k\}$ be any sequence of functions in $L^2([0, 1])$ satisfying $\norm{f_k}_2 \leq M$ for all $k ∈ \NN$.

Prove that if $f_k \to f$ almost everywhere, then $f ∈ L^2([0, 1])$ with $\norm{f}_2 \leq M$ and
$$
\lim _{k \rightarrow \infty} \int_{0}^{1} f_{k}(x) dx = \int_{0}^{1} f(x) d x
$$

> Hint: Try using Fatou’s Lemma to show that $\norm{f}_2 \leq M$ and then try applying Egorov’s Theorem.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $\{f_k\}$ be a sequence in $L^2([0, 1])$ with $\|f_k\|_2 \leq M$ for all $k \in \NN$. Suppose $f_k(x) \to f(x)$ a.e. on $[0, 1]$. Prove:
1. $f \in L^2([0, 1])$ with $\|f\|_2 \leq M$;
2. $\lim_{k\to\infty} \int_0^1 f_k(x)\,dx = \int_0^1 f(x)\,dx$.

<1>1. **$f \in L^2([0, 1])$ with $\|f\|_2 \leq M$.**
  <2>1. The sequence of non-negative measurable functions $|f_k|^2$ converges almost everywhere to $|f|^2$ on $[0, 1]$.
    Proof: Since $f_k \to f$ a.e. and the mapping $t \mapsto |t|^2$ is continuous on $\mathbb{R}$ (or $\mathbb{C}$), $|f_k(x)|^2 \to |f(x)|^2$ for almost every $x \in [0, 1]$.
  <2>2. By Fatou's Lemma, $\int_0^1 |f(x)|^2\,dx \leq \liminf_{k\to\infty} \int_0^1 |f_k(x)|^2\,dx$.
    Proof: Fatou's Lemma applies to the sequence of non-negative measurable functions $\{|f_k|^2\}_{k=1}^\infty$.
  <2>3. $\int_0^1 |f(x)|^2\,dx \leq M^2$, so $f \in L^2([0, 1])$ and $\|f\|_2 \leq M$.
    Proof: Since $\|f_k\|_2 \leq M$ for all $k \in \NN$, we have $\int_0^1 |f_k|^2\,dx = \|f_k\|_2^2 \leq M^2$. Thus $\liminf_{k\to\infty} \int_0^1 |f_k|^2\,dx \leq M^2$. By <2>2, $\|f\|_2^2 = \int_0^1 |f|^2\,dx \leq M^2$, which implies $\|f\|_2 \leq M$ and $f \in L^2([0, 1])$.

<1>2. **$\lim_{k\to\infty} \int_0^1 f_k(x)\,dx = \int_0^1 f(x)\,dx$.**
  <2>1. Let $\eps > 0$ be given. By Egorov's Theorem, there exists a measurable set $E \subseteq [0, 1]$ such that $m(E^c) < \frac{\eps^2}{16M^2}$ (where $E^c = [0, 1] \setminus E$) and $f_k \to f$ uniformly on $E$.
    Proof: The measure space $([0, 1], \mathcal B, m)$ has finite measure $m([0, 1]) = 1 < \infty$, the functions $f_k, f$ are measurable and finite a.e., and $f_k \to f$ a.e. By Egorov's Theorem, for any $\delta = \frac{\eps^2}{16M^2} > 0$, there exists a measurable set $E \subseteq [0, 1]$ with $m(E^c) < \delta$ on which $f_k \to f$ uniformly.
  <2>2. Decompose the integral:
    $$
    \left| \int_0^1 (f_k(x) - f(x))\,dx \right| \leq \int_E |f_k(x) - f(x)|\,dx + \int_{E^c} |f_k(x) - f(x)|\,dx.
    $$
    Proof: Triangle inequality for integrals and partition of $[0, 1] = E \cup E^c$.
  <2>3. $\int_{E^c} |f_k(x) - f(x)|\,dx < \frac{\eps}{2}$ for all $k$.
    <3>1. $\int_{E^c} |f_k(x) - f(x)|\,dx \leq \|f_k - f\|_2 \sqrt{m(E^c)}$.
      Proof: By Cauchy-Schwarz inequality applied to $|f_k - f| \cdot \chi_{E^c}$ in $L^2([0, 1])$,
      $$
      \int_0^1 |f_k - f|\chi_{E^c}\,dx \leq \left(\int_0^1 |f_k - f|^2\,dx\right)^{1/2} \left(\int_0^1 \chi_{E^c}^2\,dx\right)^{1/2} = \|f_k - f\|_2 \sqrt{m(E^c)}.
      $$
    <3>2. $\|f_k - f\|_2 \leq \|f_k\|_2 + \|f\|_2 \leq 2M$.
      Proof: Triangle inequality in $L^2([0, 1])$, since $\|f_k\|_2 \leq M$ and $\|f\|_2 \leq M$ from <1>1.
    <3>3. $\int_{E^c} |f_k(x) - f(x)|\,dx \leq 2M \sqrt{m(E^c)} < 2M \sqrt{\frac{\eps^2}{16M^2}} = \frac{\eps}{2}$.
      Proof: Follows directly from <3>1, <3>2, and the choice of $E$ where $m(E^c) < \frac{\eps^2}{16M^2}$.
  <2>4. There exists $K_0 \in \NN$ such that for all $k \geq K_0$, $\int_E |f_k(x) - f(x)|\,dx < \frac{\eps}{2}$.
    Proof: Since $f_k \to f$ uniformly on $E$, there exists $K_0 \in \NN$ such that $\sup_{x \in E} |f_k(x) - f(x)| < \frac{\eps}{2}$ for all $k \geq K_0$. Then:
    $$
    \int_E |f_k(x) - f(x)|\,dx \leq \sup_{x \in E} |f_k(x) - f(x)| \cdot m(E) \leq \frac{\eps}{2} \cdot 1 = \frac{\eps}{2}.
    $$
  <2>5. For all $k \geq K_0$, $\left| \int_0^1 f_k(x)\,dx - \int_0^1 f(x)\,dx \right| < \eps$.
    Proof: Combining <2>2, <2>3, and <2>4:
    $$
    \left| \int_0^1 f_k(x)\,dx - \int_0^1 f(x)\,dx \right| \leq \int_E |f_k - f|\,dx + \int_{E^c} |f_k - f|\,dx < \frac{\eps}{2} + \frac{\eps}{2} = \eps.
    $$

<1>3. **Conclusion.**
  Both claims have been demonstrated rigorously. Q.E.D.
:::
