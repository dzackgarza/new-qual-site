---
schema: qual/card@1
id: P-57CAX
kind: problem
title: Polynomial growth of entire functions and Liouville for bounded real part
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Liouville's Theorem
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(a) Let Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire function.
Assume the existence of a non-negative integer $m$, and of positive constants $L$ and $R$, such that for all $z$ with $|z|>R$ the inequality $$|f(z)| \leq L |z|^m$$ holds.
Prove that $f$ is a polynomial of degree $\leq m$.

(b) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire function.
Suppose that there exists a real number M such that for all $z\in {\mathbb C}$ $$\mbox{\textrm Re} (f) \leq M.$$ Prove that $f$ must be a constant.
:::

::: {.solution}
**Goal:** (a) If an entire $f$ satisfies $\abs{f(z)} \leq L\abs z^m$ for $\abs z > R$, prove $f$ is a polynomial of degree $\leq m$; (b) if $\Re f \leq M$ everywhere, prove $f$ is constant.

::: pf

::: {.pf-step #s1}

(a): For every $n > m$, $f^{(n)}(0) = 0$.

::: pf-proof

Fix $\rho > R$.

By the Cauchy estimates on $\abs z = \rho$, $\abs{f^{(n)}(0)} \leq \frac{n!}{\rho^n} \max_{\abs z = \rho}\abs{f(z)} \leq \frac{n! L \rho^m}{\rho^n} = n! L \rho^{m-n}$.
For $n > m$, $\rho^{m-n} \to 0$ as $\rho \to \infty$, so $f^{(n)}(0) = 0$.

:::

:::

::: {.pf-step #s2}

(a): $f$ is a polynomial of degree $\leq m$.

::: pf-proof

The Taylor expansion of the entire function $f$ about $0$ is $f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}z^n$; by step [](#s1){.pf-ref} all terms with $n > m$ vanish.

:::

:::

::: {.pf-step #s3}

(b): $g(z) \definedas e^{f(z)}$ is entire and bounded by $e^M$.

::: pf-proof

$g$ is entire (composition of entire functions), and $\abs{g(z)} = e^{\Re f(z)} \leq e^M$ by hypothesis.

:::

:::

::: {.pf-step #s4}

(b): $g$ is constant, hence $f$ is constant.

::: pf-proof

By Liouville's theorem, the bounded entire function $g$ of step [](#s3){.pf-ref} is constant; then $f = \log g$ is locally constant, and since $\CC$ is connected, $f$ is constant.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves (a) and step [](#s4){.pf-ref} proves (b).

:::

:::

:::
