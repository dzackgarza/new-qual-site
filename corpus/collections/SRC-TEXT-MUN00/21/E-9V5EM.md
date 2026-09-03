---
schema: qual/card@1
id: E-9V5EM
kind: problem
title: Powers converge pointwise but not uniformly on [0,1]
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Define $f_n: [0,1] \to \mathbb{R}$ by the equation $f_n(x) = x^n$.
Show that the sequence $(f_n(x))$ converges for each $x \in [0,1]$, but that the sequence $(f_n)$ does not converge uniformly.
:::

::: solution
**Goal:** Prove that the sequence of power functions $f_n(x) = x^n$ on $[0, 1]$ converges pointwise to a discontinuous limit function and fails to converge uniformly.

<1>1. Pointwise convergence:
    *Proof:*
    <2>1. If $x \in [0, 1)$, then $|x| < 1$, so $\lim_{n \to \infty} x^n = 0$.
    <2>2. If $x = 1$, then $f_n(1) = 1^n = 1$ for all $n$, so $\lim_{n \to \infty} f_n(1) = 1$.
    <2>3. Thus the sequence $(f_n)$ converges pointwise on $[0, 1]$ to the limit function:
        $$f(x) = \begin{cases}
        0 & \text{if } 0 \le x < 1, \\
        1 & \text{if } x = 1.
        \end{cases}$$

<1>2. Failure of uniform convergence:
    *Proof:*
    <2>1. **Via the Uniform Limit Theorem:**
        Each monomial $f_n(x) = x^n$ is continuous on $[0, 1]$.
        By the Uniform Limit Theorem (Theorem 21.5), the uniform limit of a sequence of continuous functions must be continuous.
        The pointwise limit function $f$ is discontinuous at $x = 1$ because $\lim_{x \to 1^-} f(x) = 0 \neq 1 = f(1)$.
        Therefore, $(f_n)$ cannot converge uniformly to $f$ on $[0, 1]$.
    <2>2. **Via direct supremum norm estimation:**
        For each $n \ge 1$:
        $$\|f_n - f\|_\infty = \sup_{x \in [0, 1]} |f_n(x) - f(x)| = \sup_{x \in [0, 1)} x^n = 1.$$
        Specifically, evaluating at $x_n = (1/2)^{1/n} \in [0, 1)$ gives $|f_n(x_n) - f(x_n)| = 1/2$.
        Because $\lim_{n \to \infty} \|f_n - f\|_\infty = 1 \neq 0$, the convergence is not uniform.

<1>3. Conclusion:
    $(f_n)$ converges pointwise to $f$ but does not converge uniformly on $[0, 1]$. Q.E.D.
:::
