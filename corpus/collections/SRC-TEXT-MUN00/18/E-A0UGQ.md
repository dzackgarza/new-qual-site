---
schema: qual/card@1
id: E-A0UGQ
kind: exercise
title: A function continuous at exactly one point
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Find a function $f: \mathbb{R} \to \mathbb{R}$ that is continuous at precisely one point.
:::

::: solution
**Goal:** Construct an explicit function $f: \mathbb{R} \to \mathbb{R}$ and prove that it is continuous at precisely one point $x = 0$.

<1>1. Definition of the function $f$:
    Define $f: \mathbb{R} \to \mathbb{R}$ by:
    $$f(x) = \begin{cases}
    x & \text{if } x \in \mathbb{Q}, \\
    0 & \text{if } x \notin \mathbb{Q}.
    \end{cases}$$

<1>2. Proof of continuity at $x = 0$:
    *Proof:*
    <2>1. Notice that for all $x \in \mathbb{R}$, $|f(x)| \le |x|$.
    <2>2. Let $\varepsilon > 0$. Choose $\delta = \varepsilon$.
    <2>3. If $|x - 0| < \delta$, then $|f(x) - f(0)| = |f(x)| \le |x| < \delta = \varepsilon$.
    <2>4. Thus $\lim_{x \to 0} f(x) = f(0) = 0$, proving $f$ is continuous at $x = 0$.

<1>3. Proof of discontinuity at every $x_0 \neq 0$:
    *Proof:*
    <2>1. **Case 1: $x_0 \in \mathbb{Q} \setminus \{0\}$.**
        Here $f(x_0) = x_0 \neq 0$.
        By density of the irrationals $\mathbb{R} \setminus \mathbb{Q}$, choose a sequence of irrational numbers $(y_n)_{n=1}^\infty$ with $y_n \to x_0$.
        Then $f(y_n) = 0$ for all $n$, so $\lim_{n \to \infty} f(y_n) = 0 \neq x_0 = f(x_0)$.
        Hence $f$ is discontinuous at $x_0$.
    <2>2. **Case 2: $x_0 \notin \mathbb{Q}$.**
        Here $f(x_0) = 0$.
        By density of the rationals $\mathbb{Q}$, choose a sequence of rational numbers $(q_n)_{n=1}^\infty$ with $q_n \to x_0$.
        Then $f(q_n) = q_n$ for all $n$, so $\lim_{n \to \infty} f(q_n) = x_0 \neq 0 = f(x_0)$.
        Hence $f$ is discontinuous at $x_0$.

<1>4. Conclusion:
    $f$ is continuous at $x = 0$ and discontinuous at every $x \neq 0$, so $f$ is continuous at precisely one point. Q.E.D.
:::
