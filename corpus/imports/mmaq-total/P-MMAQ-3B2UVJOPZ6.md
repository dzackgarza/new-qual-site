---
schema: qual/card@1
id: P-MMAQ-3B2UVJOPZ6
kind: problem
title: Absolute continuity of the integral of an $L^1$ function
classification:
  areas:
  - real-analysis
  topics:
  - l1
  - continuity-of-measure
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
Let $f\in L^1(\RR)$.
Show that
$$
\forall\varepsilon > 0 ~~\exists \delta > 0 \text{ such that } m(E) < \delta \implies \int_{E}|f(x)| d x<\varepsilon
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f \in L^1(\RR)$. Prove absolute continuity of the Lebesgue integral: for every $\eps > 0$, there exists $\delta > 0$ such that for every Lebesgue measurable set $E \subseteq \RR$, $m(E) < \delta \implies \int_E |f(x)|\,dx < \eps$.

<1>1. **Truncation approximation of $|f|$.**
  <2>1. For each $N \in \NN$, define $f_N(x) = \min(|f(x)|, N) = |f(x)| \chi_{\{|f| \leq N\}}(x) + N \chi_{\{|f| > N\}}(x)$.
  <2>2. The sequence $\{f_N\}_{N=1}^\infty$ is a sequence of non-negative measurable functions satisfying $0 \leq f_1(x) \leq f_2(x) \leq \dots \nearrow |f(x)|$ pointwise as $N \to \infty$.
    Proof: For every $x \in \RR$, since $|f(x)| < \infty$ almost everywhere, $\min(|f(x)|, N) = |f(x)|$ for all $N \geq |f(x)|$.
  <2>3. $\lim_{N\to\infty} \int_\RR f_N(x)\,dx = \int_\RR |f(x)|\,dx$.
    Proof: By the Monotone Convergence Theorem applied to the non-decreasing sequence of non-negative measurable functions $f_N \nearrow |f|$.
  <2>4. For any given $\eps > 0$, there exists $N_0 \in \NN$ such that $\int_\RR (|f(x)| - f_{N_0}(x))\,dx < \frac{\eps}{2}$.
    Proof: Since $f \in L^1(\RR)$, $\int_\RR |f(x)|\,dx < \infty$. From <2>3, $\int_\RR (|f| - f_N)\,dx = \int_\RR |f|\,dx - \int_\RR f_N\,dx \to 0$ as $N \to \infty$. Thus there exists $N_0$ such that the integral difference is strictly less than $\frac{\eps}{2}$.

<1>2. **Choice of $\delta$ and bounding the integral over $E$.**
  <2>1. Set $\delta = \frac{\eps}{2 N_0} > 0$.
  <2>2. Let $E \subseteq \RR$ be any measurable set with $m(E) < \delta$.
  <2>3. Decompose $\int_E |f(x)|\,dx$:
    $$
    \int_E |f(x)|\,dx = \int_E (|f(x)| - f_{N_0}(x))\,dx + \int_E f_{N_0}(x)\,dx.
    $$
    Proof: By linearity of the Lebesgue integral.
  <2>4. $\int_E (|f(x)| - f_{N_0}(x))\,dx \leq \int_\RR (|f(x)| - f_{N_0}(x))\,dx < \frac{\eps}{2}$.
    Proof: Since $|f(x)| - f_{N_0}(x) \geq 0$ for all $x \in \RR$, integrating over a subset $E \subseteq \RR$ gives an integral bounded by the integral over the entire space $\RR$, which is $< \frac{\eps}{2}$ by <1>1 (<2>4).
  <2>5. $\int_E f_{N_0}(x)\,dx \leq N_0 \cdot m(E) < N_0 \delta = \frac{\eps}{2}$.
    Proof: Since $f_{N_0}(x) = \min(|f(x)|, N_0) \leq N_0$ for all $x$, we have $\int_E f_{N_0}(x)\,dx \leq \int_E N_0\,dx = N_0 m(E) < N_0 \left(\frac{\eps}{2N_0}\right) = \frac{\eps}{2}$.
  <2>6. $\int_E |f(x)|\,dx < \frac{\eps}{2} + \frac{\eps}{2} = \eps$.
    Proof: Combining <2>3, <2>4, and <2>5.

<1>3. **Conclusion.**
  For every $\eps > 0$, $\delta = \frac{\eps}{2 N_0} > 0$ satisfies $m(E) < \delta \implies \int_E |f(x)|\,dx < \eps$. Q.E.D.
:::
