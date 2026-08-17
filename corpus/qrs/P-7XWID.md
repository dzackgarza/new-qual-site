---
schema: qual/card@1
id: P-7XWID
kind: problem
title: "Let $\\left\\{x_{n}\\right\\}_{n-1}^{\\infty}$ be a sequence of real numbers such that $x_{1}>0$ and $x_{n+1}=1-\\left(2+x_{n}\\right)^{-1}=\\frac{1+x_{n}}{2+x_{n}} \\text {. }$ Prove\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
  - fixed-points
relations: []
review: draft
solved: true
---

::: problem
Let $\left\{x_{n}\right\}_{n-1}^{\infty}$ be a sequence of real numbers such that $x_{1}>0$ and
\[
x_{n+1}=1-\left(2+x_{n}\right)^{-1}=\frac{1+x_{n}}{2+x_{n}} \text {. }
\]
Prove that the sequence $\left\{x_{n}\right\}$ converges, and find its limit.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The sequence stays positive: $x_n > 0$ for all $n$.
Proof: $x_1 > 0$ by hypothesis, and $x_{n+1} = \frac{1 + x_n}{2 + x_n} > 0$ whenever $x_n > 0$; induction.

<1>2. Let $f(x) = \frac{1 + x}{2 + x}$; the fixed points of $f$ solve $x = \frac{1+x}{2+x}$, i.e. $x^2 + x - 1 = 0$.
Proof: $x(2 + x) = 1 + x \iff x^2 + x - 1 = 0$.

<1>3. The positive fixed point is $\alpha = \frac{\sqrt 5 - 1}{2}$.
Proof: the roots of $x^2 + x - 1 = 0$ are $\frac{-1 \pm \sqrt 5}{2}$; the positive one is $\frac{\sqrt 5 - 1}{2}$.

<1>4. $f$ is a contraction on $[0, \infty)$ with constant $1/4$.
<2>1. $f'(x) = \frac{1}{(2 + x)^2}$.
Proof: quotient rule: $f'(x) = \frac{(2+x) - (1+x)}{(2+x)^2}$.
<2>2. $|f'(x)| \le 1/4$ for all $x \ge 0$.
Proof: $2 + x \ge 2$, so $(2+x)^2 \ge 4$.

<1>5. The sequence converges to $\alpha$.
<2>1. $|x_{n+1} - \alpha| = |f(x_n) - f(\alpha)| \le \frac{1}{4}|x_n - \alpha|$.
Proof: mean value theorem using <1>4 (the interval between $x_n$ and $\alpha$ lies in $[0,\infty)$ since both are $\ge 0$). <2>2. $|x_n - \alpha| \le \left(\frac{1}{4}\right)^{n-1}|x_1 - \alpha| \to 0$.
Proof: iterate <2>1. <2>3. Q.E.D. Proof: <2>2 is convergence to $\alpha$.
:::
