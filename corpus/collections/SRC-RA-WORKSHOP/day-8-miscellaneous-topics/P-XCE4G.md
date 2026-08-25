---
schema: qual/card@1
id: P-XCE4G
kind: problem
title: Pointwise and locally uniform convergence of $\sum\frac{x^k}{1+x^k}$ on $[0,1)$,
  and differentiability of the sum
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Uniform Convergence
  - Differentiation
relations: []
review: draft
---

::: problem
Let $f_n \colon [0,1) \to \mathbb{R}$ be the function defined by
$$f_n(x):= \sum_{k=1}^n \frac{x^k}{1+x^k}.$$



1.  
Prove that $f_n$ converges to a function
$f \colon [0,1) \to \mathbb{R}$.



2.  
Prove that for every $0 < a < 1$ the convergence is uniform on
$[0,a]$.



3.  
Prove that $f$ is differentiable on $(0,1)$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Pointwise convergence on $[0,1)$.
    Proof: for $x \in [0,1)$, $0 \le \frac{x^k}{1+x^k} \le x^k$, and $\sum_k x^k$ is a convergent geometric series; hence $\sum_k \frac{x^k}{1+x^k}$ converges, defining $f(x)$.
<1>2. Uniform convergence on $[0,a]$ for $0 < a < 1$.
    Proof: for $x \le a$, $\frac{x^k}{1+x^k} \le a^k$, and $\sum_k a^k$ converges (geometric, $a < 1$); by the Weierstrass $M$-test the convergence is uniform on $[0,a]$.
<1>3. $f$ is differentiable on $(0,1)$.
    Proof: each term $g_k(x) = \frac{x^k}{1+x^k}$ is differentiable with $g_k'(x) = \frac{kx^{k-1}}{(1+x^k)^2}$. Fix $0 < a < 1$. For $x \le a$,
    \[
    |g_k'(x)| \le k a^{k-1},
    \]
    and $\sum_k k a^{k-1} < \infty$ (ratio test: $\frac{(k+1)a^k}{ka^{k-1}} = \frac{k+1}{k}a \to a < 1$). Hence $\sum_k g_k'$ converges uniformly on $[0,a]$. By the term-by-term differentiation theorem, $f$ is differentiable on $(0,a)$ with $f' = \sum_k g_k'$; since $a < 1$ is arbitrary, $f$ is differentiable on all of $(0,1)$.
<1>4. Q.E.D.
:::
