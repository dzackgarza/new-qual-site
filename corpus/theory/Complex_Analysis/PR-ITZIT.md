---
schema: qual/card@1
id: PR-ITZIT
kind: proposition
title: Factorization of zeros out of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $D\subseteq\CC$ be a connected open set, let $f$ be [[D-E7A5W|holomorphic]] on $D$ and not identically zero, and let $z_0\in D$ with $f(z_0)=0$.
Then there exist an integer $k\ge1$ and a function $g$ holomorphic on $D$ with $g(z_0)\neq0$ such that
$$
f(z)=(z-z_0)^kg(z)\quad\text{for all } z\in D.
$$
:::

::: {.proof}
Choose $r>0$ with $D(z_0,r)\subseteq D$.
Since $f$ is not identically zero on the connected set $D$, not every derivative $f^{(j)}(z_0)$ vanishes, and $f(z_0)=0$; let $k\ge1$ be the least integer with $f^{(k)}(z_0)\neq0$.
On $D(z_0,r)$,
$$
f(z)=\sum_{j\ge k}\frac{f^{(j)}(z_0)}{j!}(z-z_0)^j=(z-z_0)^k\sum_{j\ge0}\frac{f^{(j+k)}(z_0)}{(j+k)!}(z-z_0)^j.
$$
Define
$$
g(z)\coloneqq\begin{cases}\displaystyle\sum_{j\ge0}\frac{f^{(j+k)}(z_0)}{(j+k)!}(z-z_0)^j, & z\in D(z_0,r),\\[1ex] \dfrac{f(z)}{(z-z_0)^k}, & z\in D\setminus\theset{z_0}.\end{cases}
$$
The two formulas agree on $D(z_0,r)\setminus\theset{z_0}$, so $g$ is well defined; it is holomorphic on $D(z_0,r)$ as a convergent power series and on $D\setminus\theset{z_0}$ as a quotient of holomorphic functions, hence on $D$.
Moreover $g(z_0)=f^{(k)}(z_0)/k!\neq0$ and $f(z)=(z-z_0)^kg(z)$ on $D$.
:::
