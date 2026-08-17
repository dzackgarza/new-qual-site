---
schema: qual/card@1
id: P-3WZXM
kind: problem
title: An entire function with $|f(z)|\ge A|z|^N$ at infinity is a polynomial of degree at least $N$
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - liouville-s-theorem
relations: []
review: draft
solved: true
---

::: problem
Suppose $f$ is entire and there exist $A, R >0$ and natural number $N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show that (i) $f$ is a polynomial and (ii) the degree of $f$ is at least $N$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Suppose $f$ is entire and $\abs{f(z)} \ge A\abs{z}^N$ for $\abs{z} \ge R$.
Show (i) $f$ is a polynomial and (ii) $\deg f \ge N$.

<1>1. All zeros of $f$ lie in $\abs{z} \le R$.
Proof: For $\abs{z} \ge R$, $\abs{f(z)} \ge A\abs{z}^N > 0$, so no zeros outside the disk; finitely many inside by isolation of zeros on a compact set.

<1>2. $f$ is a polynomial.
Proof: Let $p$ be the polynomial with exactly the zeros of $f$ (with multiplicity); $g = f/p$ is entire and zero-free.
Since $\abs{f(z)} \ge A\abs{z}^N$ and $\abs{p(z)} \le C\abs{z}^{\deg p}$ for large $\abs{z}$, we get $\abs{1/g(z)} = \abs{p(z)/f(z)} \le \frac{C}{A}\abs{z}^{\deg p - N} \le C'\abs{z}^{\deg p}$ for large $\abs{z}$ (also bounded on the compact disk $\abs{z} \le R$). So $1/g$ is an entire function of polynomial growth, hence a polynomial (extended Liouville / Cauchy estimates).
As $1/g$ has no zeros, it is constant, so $g$ is constant and $f$ is a polynomial.

<1>3. $\deg f \ge N$.
Proof: If $\deg f = d < N$, then $\abs{f(z)}/\abs{z}^N \to 0$ as $\abs{z} \to \infty$, contradicting $\abs{f(z)} \ge A\abs{z}^N$, i.e. $\abs{f(z)}/\abs{z}^N \ge A > 0$.

<1>4. Q.E.D. Proof: <1>2 and <1>3 prove (i) and (ii).
:::
