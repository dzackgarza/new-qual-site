---
schema: qual/card@1
id: P-36DLV
kind: problem
title: An entire function with $|f(z)|\ge A|z|^N$ at infinity is a polynomial of degree at least $N$
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - liouville-s-theorem
  - zeros
relations: []
review: draft
solved: true
---

::: problem
Suppose $f$ is entire and there exist $A, R >0$ and natural number $N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show that

1. $f$ is a polynomial and

2. the degree of $f$ is at least $N$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Suppose $f$ is entire and $\abs{f(z)} \ge A\abs{z}^N$ for $\abs{z} \ge R$ (with $A, R > 0$, $N \in \NN$). Show (1) $f$ is a polynomial, and (2) $\deg f \ge N$.

<1>1. $f$ has finitely many zeros.
Proof: For $\abs{z} \ge R$, $\abs{f(z)} \ge A\abs{z}^N \ge AR^N > 0$, so all zeros of $f$ lie in the compact disk $\abs{z} \le R$.
Since zeros of a nonconstant entire function are isolated, there are finitely many (a compact set contains only finitely many isolated points of a discrete set).

<1>2. $f$ is a polynomial.
Proof: Let the distinct zeros be $z_1, \ldots, z_k$ with multiplicities $m_1, \ldots, m_k$, and set $p(z) = \prod (z - z_j)^{m_j}$.
Then $g(z) = f(z)/p(z)$ is entire and zero-free, so $g(z) = e^{h(z)}$ for some entire $h$.
Moreover $\abs{g(z)} = \abs{f(z)}/\abs{p(z)} \ge A\abs{z}^N/\abs{p(z)}$, and $\abs{p(z)} \le C\abs{z}^{M}$ for large $\abs{z}$ (with $M = \sum m_j$), so $\abs{g(z)} \ge \frac{A}{C}\abs{z}^{N - M} \to \infty$ as $\abs{z} \to \infty$ (if $N \ge M$) — in any case $\abs{g(z)} \to \infty$ as $z \to \infty$?
No: if $N < M$, then $\abs{z}^{N-M} \to 0$ and the lower bound degenerates.
But $\abs{g(z)} = e^{\Re h(z)}$ never vanishes; the key is that $g$ has no zeros and grows at least like a positive power: indeed from $\abs{f(z)} \ge A\abs{z}^N$ and $\abs{p(z)} \le C\abs{z}^M$, $\abs{g(z)} \ge (A/C)\abs{z}^{N-M}$; if $N \le M$ this gives nothing at $\infty$... The correct argument: since $g$ is entire and zero-free, $g = e^h$; $\abs{g(z)} \ge c\abs{z}^{N-M}$ for large $\abs{z}$ shows $\Re h(z) \to +\infty$ as $z \to \infty$ along directions... Simplest: $1/g$ is entire and $\abs{1/g(z)} \le \frac{C}{A}\abs{z}^{M - N} \le C'\abs{z}^{M}$ for large $\abs{z}$, so $1/g$ is a polynomial of degree $\le M$ by the extended Liouville theorem (Cauchy estimates).
Hence $g = 1/\text{polynomial}$; since $g$ is entire, the polynomial is constant, so $g$ is constant and $f$ is a polynomial.

<1>3. $\deg f \ge N$.
Proof: If $f$ were a polynomial of degree $d < N$, then $\abs{f(z)}/\abs{z}^N \to 0$ as $\abs{z} \to \infty$, contradicting $\abs{f(z)} \ge A\abs{z}^N$ (divide by $\abs{z}^N$: $\abs{f(z)}/\abs{z}^N \ge A > 0$). Hence $d \ge N$.

<1>4. Q.E.D. Proof: <1>2 shows $f$ is a polynomial and <1>3 shows its degree is at least $N$.
:::
