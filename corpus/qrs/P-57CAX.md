---
schema: qual/card@1
id: P-57CAX
kind: problem
title: "(a) Let Let $f:{\\mathbb C}\\rightarrow {\\mathbb C}$ be an entire"
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - liouville-s-theorem
  - cauchy-estimates
relations: []
review: draft
solved: true
---

::: problem
(a) Let Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire function.
Assume the existence of a non-negative integer $m$, and of positive constants $L$ and $R$, such that for all $z$ with $|z|>R$ the inequality $$|f(z)| \leq L |z|^m$$ holds.
Prove that $f$ is a polynomial of degree $\leq m$.

(b) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire function.
Suppose that there exists a real number M such that for all $z\in {\mathbb C}$ $$\mbox{\textrm Re} (f) \leq M.$$ Prove that $f$ must be a constant.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) If an entire $f$ satisfies $\abs{f(z)} \leq L\abs z^m$ for $\abs z > R$, prove $f$ is a polynomial of degree $\leq m$; (b) if $\Re f \leq M$ everywhere, prove $f$ is constant.

<1>1. (a): For every $n > m$, $f^{(n)}(0) = 0$.
Proof: Fix $\rho > R$.
By the Cauchy estimates on $\abs z = \rho$, $\abs{f^{(n)}(0)} \leq \frac{n!}{\rho^n} \max_{\abs z = \rho}\abs{f(z)} \leq \frac{n! L \rho^m}{\rho^n} = n! L \rho^{m-n}$.
For $n > m$, $\rho^{m-n} \to 0$ as $\rho \to \infty$, so $f^{(n)}(0) = 0$.

<1>2. (a): $f$ is a polynomial of degree $\leq m$.
Proof: The Taylor expansion of the entire function $f$ about $0$ is $f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}z^n$; by <1>1 all terms with $n > m$ vanish.

<1>3. (b): $g(z) \definedas e^{f(z)}$ is entire and bounded by $e^M$.
Proof: $g$ is entire (composition of entire functions), and $\abs{g(z)} = e^{\Re f(z)} \leq e^M$ by hypothesis.

<1>4. (b): $g$ is constant, hence $f$ is constant.
Proof: By Liouville's theorem, the bounded entire function $g$ of <1>3 is constant; then $f = \log g$ is locally constant, and since $\CC$ is connected, $f$ is constant.

<1>5. Q.E.D. Proof: <1>2 proves (a) and <1>4 proves (b).
:::
