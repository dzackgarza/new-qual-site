---
schema: qual/card@1
id: P-MMAQ-2LKTOV7NE6
kind: problem
title: "Define $f(x) = \\sum_{n=1}^{\\infty} \\frac{1}{n^{x}}$ Show that $f$ converges to a differentiable function on\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - series-of-numbers
relations: []
review: draft
solved: true
---

::: problem
Define
$$
f(x) = \sum_{n=1}^{\infty} \frac{1}{n^{x}}.
$$

Show that $f$ converges to a differentiable function on $(1, \infty)$ and that
$$
f'(x)  =\sum_{n=1}^{\infty}\left(\frac{1}{n^{x}}\right)^{\prime}.
$$

> Hint:
> $$
> \left(\frac{1}{n^{x}}\right)^{\prime}=-\frac{1}{n^{x}} \ln n
> $$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f(x) = \sum_{n=1}^\infty \frac{1}{n^x} = \zeta(x)$. Prove that $f$ converges to a differentiable function on $(1, \infty)$ with term-by-term derivative $f'(x) = \sum_{n=1}^\infty \left(\frac{1}{n^x}\right)' = -\sum_{n=1}^\infty \frac{\ln n}{n^x}$.

<1>1. **Derivatives of individual terms.**
  <2>1. For each $n \geq 1$, let $u_n(x) = \frac{1}{n^x} = e^{-x \ln n}$.
  <2>2. Each $u_n$ is infinitely differentiable on $(1, \infty)$ with derivative:
    $$
    u_n'(x) = \frac{d}{dx} e^{-x \ln n} = (-\ln n) e^{-x \ln n} = -\frac{\ln n}{n^x}.
    $$
    Proof: Direct application of the chain rule to the exponential function.

<1>2. **Pointwise convergence of the original series.**
  <2>1. For every $x_0 \in (1, \infty)$, the series $\sum_{n=1}^\infty \frac{1}{n^{x_0}}$ converges in $\RR$.
    Proof: By the $p$-series test (integral test), $\sum_{n=1}^\infty n^{-p} < \infty$ for all $p > 1$.

<1>3. **Local uniform convergence of the differentiated series.**
  <2>1. Let $a > 1$ be arbitrary. We show that $\sum_{n=1}^\infty u_n'(x)$ converges uniformly on $[a, \infty)$.
  <2>2. For any $x \geq a$ and $n \geq 1$:
    $$
    |u_n'(x)| = \frac{\ln n}{n^x} \leq \frac{\ln n}{n^a}.
    $$
    Proof: For $x \geq a$, $n^x \geq n^a$, so $\frac{1}{n^x} \leq \frac{1}{n^a}$, and $\ln n \geq 0$ for $n \geq 1$.
  <2>3. The numeric series $M_n \definedas \frac{\ln n}{n^a}$ satisfies $\sum_{n=1}^\infty M_n < \infty$.
    Proof: Choose $\eps = \frac{a-1}{2} > 0$, so that $a - \eps = 1 + \eps > 1$. Since $\lim_{n\to\infty} \frac{\ln n}{n^\eps} = 0$, there exists a constant $C > 0$ such that $\ln n \leq C n^\eps$ for all $n \geq 1$. Then:
    $$
    M_n = \frac{\ln n}{n^a} \leq \frac{C n^\eps}{n^a} = \frac{C}{n^{a-\eps}} = \frac{C}{n^{1+\eps}}.
    $$
    Since $1+\eps > 1$, the $p$-series $\sum_{n=1}^\infty \frac{1}{n^{1+\eps}}$ converges, and by the direct comparison test, $\sum_{n=1}^\infty M_n < \infty$.
  <2>4. By the Weierstrass $M$-test, $\sum_{n=1}^\infty u_n'(x) = -\sum_{n=1}^\infty \frac{\ln n}{n^x}$ converges uniformly and absolutely on $[a, \infty)$.
    Proof: For all $x \in [a, \infty)$ and all $n \geq 1$, $|u_n'(x)| \leq M_n$ with $\sum_{n=1}^\infty M_n < \infty$.

<1>4. **Term-by-term differentiation theorem.**
  <2>1. On every interval $[a, b] \subset (1, \infty)$ with $1 < a < b < \infty$:
    1. Each $u_n(x)$ is $C^1([a, b])$;
    2. The series $\sum_{n=1}^\infty u_n(x)$ converges at least at one point (in fact everywhere on $[a, b]$ by <1>2);
    3. The differentiated series $\sum_{n=1}^\infty u_n'(x)$ converges uniformly on $[a, b]$ (by <1>3).
  <2>2. By the standard theorem on term-by-term differentiation of series of functions, the sum function $f(x) = \sum_{n=1}^\infty u_n(x)$ is differentiable on $[a, b]$ and:
    $$
    f'(x) = \sum_{n=1}^\infty u_n'(x) = -\sum_{n=1}^\infty \frac{\ln n}{n^x} \quad \text{for all } x \in [a, b].
    $$
  <2>3. Since $(1, \infty) = \bigcup_{k=2}^\infty [1 + 1/k, k]$ is an open set covered by such closed intervals, $f$ is differentiable on all of $(1, \infty)$ and $f'(x) = \sum_{n=1}^\infty \left(\frac{1}{n^x}\right)'$ for all $x \in (1, \infty)$.
    Proof: Differentiability is a local property: for every $x \in (1, \infty)$, choose $a \in (1, x)$ and $b > x$; the result on $[a, b]$ applies in a neighborhood of $x$.

<1>5. **Conclusion.**
  $f$ converges to a differentiable function on $(1, \infty)$ and its derivative is given by the sum of term derivatives. Q.E.D.
:::
