---
schema: qual/card@1
id: P-RAF23A
kind: problem
title: "True/false on distributional derivative of monotone function and countable sets"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
TRUE or FALSE: Prove it if true and disprove it if false.

(i) Let $f(t)$ be a monotone non-increasing function on $\mathbb{R}$.
Then its distributional derivative is always a Radon measure.

(ii) Let $E \subset [0,1] \subset \mathbb{R}$ be a countable subset.
Then for any $\epsilon > 0$, there is a finite cover of $E$ by open intervals $\{I_k\}_{k=1}^{n}$ such that
$$
\sum_{k=1}^{n} m(I_k) < \epsilon.
$$
:::

::: solution
**Goal:** Determine the truth value of each statement with complete mathematical proofs.

<1>1. Statement (i) is TRUE.
    *Proof:*
    <2>1. A locally integrable function $f \in L_{\text{loc}}^1(\mathbb{R})$ defines a distribution whose derivative $f' \in \mathcal{D}'(\mathbb{R})$ acts on test functions $\phi \in C_c^\infty(\mathbb{R})$ by
    $$\langle f', \phi \rangle = -\int_{-\infty}^\infty f(t) \phi'(t)\,dt.$$
    <2>2. We claim that $-f'$ is a positive distribution: for any test function $\phi \in C_c^\infty(\mathbb{R})$ with $\phi(t) \ge 0$ for all $t$, $\langle -f', \phi \rangle = \int_{-\infty}^\infty f(t) \phi'(t)\,dt \ge 0$.
    <2>3. Let $\eta \in C_c^\infty(\mathbb{R})$ be a standard non-negative mollifier with $\int \eta = 1$, and let $\eta_\varepsilon(t) = \frac{1}{\varepsilon}\eta(t/\varepsilon)$.
    For $\varepsilon > 0$, the mollified function $f_\varepsilon = f * \eta_\varepsilon$ is smooth. Since $f$ is monotone non-increasing, for any $h > 0$:
    $$f_\varepsilon(t + h) - f_\varepsilon(t) = \int_{-\infty}^\infty (f(t + h - s) - f(t - s)) \eta_\varepsilon(s)\,ds \le 0,$$
    which implies $f_\varepsilon'(t) \le 0$ for all $t \in \mathbb{R}$.
    <2>4. Integrating by parts on the smooth functions:
    $$\int_{-\infty}^\infty f_\varepsilon(t) \phi'(t)\,dt = -\int_{-\infty}^\infty f_\varepsilon'(t) \phi(t)\,dt \ge 0,$$
    because $-f_\varepsilon'(t) \ge 0$ and $\phi(t) \ge 0$.
    <2>5. Since $f \in L_{\text{loc}}^1(\mathbb{R})$, $f_\varepsilon \to f$ in $L_{\text{loc}}^1(\mathbb{R})$ as $\varepsilon \to 0^+$. Because $\phi'$ is smooth and compactly supported:
    $$\langle -f', \phi \rangle = \int_{-\infty}^\infty f(t) \phi'(t)\,dt = \lim_{\varepsilon \to 0^+} \int_{-\infty}^\infty f_\varepsilon(t) \phi'(t)\,dt \ge 0.$$
    <2>6. By the Riesz–Markov–Kakutani / Schwartz Representation Theorem for positive distributions, every positive distribution on $\mathbb{R}$ is represented by a unique positive Radon measure $\mu \ge 0$ on $\mathbb{R}$, so $\langle -f', \phi \rangle = \int_\mathbb{R} \phi\,d\mu$.
    <2>7. Thus $f' = -\mu$ is a non-positive Radon measure on $\mathbb{R}$.

<1>2. Statement (ii) is FALSE.
    *Proof:*
    <2>1. Consider the set $E = \mathbb{Q} \cap [0, 1]$. The set $E$ is countable and satisfies $E \subset [0, 1]$.
    <2>2. Suppose $\{I_k\}_{k=1}^n$ is any finite cover of $E$ by open intervals $I_k = (a_k, b_k)$. Then $E \subseteq \bigcup_{k=1}^n I_k$.
    <2>3. Taking topological closures in $\mathbb{R}$ of both sides:
    $$[0, 1] = \overline{\mathbb{Q} \cap [0, 1]} = \overline{E} \subseteq \overline{\bigcup_{k=1}^n I_k} = \bigcup_{k=1}^n \overline{I_k} = \bigcup_{k=1}^n [a_k, b_k].$$
    <2>4. The Lebesgue measure of a closed interval is $m([a_k, b_k]) = b_k - a_k = m(I_k)$.
    <2>5. By the monotonicity and subadditivity of Lebesgue measure:
    $$1 = m([0, 1]) \le m\left( \bigcup_{k=1}^n [a_k, b_k] \right) \le \sum_{k=1}^n m([a_k, b_k]) = \sum_{k=1}^n m(I_k).$$
    <2>6. Thus the sum of lengths $\sum_{k=1}^n m(I_k)$ is at least 1 for any finite open cover of $E$.
    <2>7. Choosing $\epsilon \in (0, 1)$ shows that no such finite cover can satisfy $\sum_{k=1}^n m(I_k) < \epsilon$.

<1>3. Conclusion:
    *Proof:*
    Statement (i) is TRUE, and statement (ii) is FALSE.
:::
