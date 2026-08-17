---
schema: qual/card@1
id: P-B3LJA
kind: problem
title: Uniform convergence of $(1+z/n)^n$ to $e^z$ on compact subsets of $\mathbb{C}$
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - sequences-of-functions
  - entire-functions
relations: []
review: draft
solved: true
---

::: problem
Prove that the sequence $\left(1+\frac{z}{n}\right)^{n}$ converges uniformly to $e^{z}$ on compact subsets of $\mathbb{C}$.

> Hint: $e^{\pi \log w_{n}}=w_{n}^{n}$ and $e^{x}$ is uniform continuous on compact subsets of $\mathbb{C}$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that $\qty(1 + \frac{z}{n})^n \to e^z$ uniformly on every compact subset of $\CC$.

<1>1. Fix a compact set $K \subseteq \CC$ and choose $R > 0$ with $K \subseteq \theset{\abs z \leq R}$.
Proof: Compact subsets of $\CC$ are bounded, so such an $R$ exists.

<1>2. For $\abs z \leq R$ and $n > R$, the principal logarithm of $1 + z/n$ is defined.
Proof: $\abs{z/n} \leq R/n < 1$, so $1 + z/n$ lies in the disk $D(1, 1) \subseteq \CC \setminus (-\infty, 0]$, where the principal branch $\Log$ is holomorphic.

<1>3. $n\Log\qty(1 + \frac{z}{n}) \to z$ uniformly on $\abs z \leq R$.
<2>1. Expand the logarithm: $n\Log\qty(1 + \frac{z}{n}) = z - \frac{z^2}{2n} + \frac{z^3}{3n^2} - \cdots$.
Proof: The power series $\Log(1 + w) = w - w^2/2 + w^3/3 - \cdots$ converges absolutely for $\abs w < 1$; multiply by $n$ and substitute $w = z/n$.
<2>2. Bound the remainder uniformly.
Proof: For $\abs z \leq R$ and $n \geq 2R$, $$\abs{n\Log\qty(1 + \frac{z}{n}) - z} \leq \sum_{k=2}^{\infty} \frac{\abs z^k}{k\, n^{k-1}} \leq \frac{1}{n}\sum_{k=2}^{\infty} R^k \qty(\frac{1}{n})^{k-2} \cdot \frac{1}{k} \leq \frac{R^2}{n} \sum_{j=0}^{\infty} \qty(\frac{R}{n})^j = \frac{R^2}{n - R} \to 0.$$ <2>3. Hence $w_n(z) := n\Log\qty(1 + \frac{z}{n})$ converges to $z$ uniformly on $\abs z \leq R$.
Proof: <2>2 gives $\sup_{\abs z \leq R} \abs{w_n(z) - z} \to 0$.

<1>4. $\qty(1 + \frac{z}{n})^n = e^{w_n(z)}$ for $\abs z \leq R$.
Proof: By <1>2, $\exp(n\Log w) = \qty(e^{\Log w})^n = w^n$ with $w = 1 + z/n$.

<1>5. $e^{w_n(z)} \to e^z$ uniformly on $\abs z \leq R$.
<2>1. The values $\theset{w_n(z), z : \abs z \leq R, n \geq 1}$ lie in a common compact set.
Proof: <1>3.3 shows $w_n \to z$ uniformly, so $\sup_{n, \abs z \leq R} \abs{w_n(z)} < \infty$.
<2>2. $\exp$ is uniformly continuous on that compact set.
Proof: $\exp$ is continuous, and continuous functions on compact sets are uniformly continuous.
<2>3. Therefore $\sup_{\abs z \leq R} \abs{e^{w_n(z)} - e^z} \to 0$.
Proof: Uniform convergence <1>3.3 composed with the uniformly continuous $\exp$; standard epsilon/3 argument.

<1>6. Q.E.D. Proof: Steps <1>4 and <1>5 give $\qty(1 + \frac{z}{n})^n \rightrightarrows e^z$ on $\abs z \leq R \supseteq K$; since $K$ was arbitrary, the convergence is uniform on all compact sets.
:::
