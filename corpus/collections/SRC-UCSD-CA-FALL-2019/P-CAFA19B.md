---
schema: qual/card@1
id: P-CAFA19B
kind: problem
title: "Zero-free disk and characterization of extremal functions for bounded analytic functions"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f$ be analytic on $\mathbb{D}$ with $|f(z)| \leq 1/2$ on $\mathbb{D}$ and $f(0) = r \in \mathbb{R}$, where $0 < r < 1/2$.

(a) Prove that $f(z)$ has no zeros in the disk $\{|z| < 2r\}$.

(b) Can $f(z)$ have a zero on the circle $\{|z| = 2r\}$?
If so, find all such functions $f(z)$.
:::

::: solution
Set $g=2f$. Then $g:\mathbb D\to\mathbb D$ is holomorphic and $g(0)=2r$.

If $g(a)=0$, Schwarz--Pick gives
\[
\left|\frac{g(0)-g(a)}{1-\overline{g(a)}g(0)}\right|
\le
\left|\frac{0-a}{1-\bar a\,0}\right|,
\]
hence
\[
2r\le |a|.
\]
Therefore $f$ has no zero in $|z|<2r$.

Now suppose $f(a)=0$ with $|a|=2r$. Equality holds in Schwarz--Pick at the
distinct points $0$ and $a$, so $g$ is an automorphism of the disk. Thus
\[
g(z)=e^{i\theta}\frac{z-a}{1-\bar a z}.
\]
Writing $a=2re^{i\phi}$ and using $g(0)=2r$ gives
$e^{i\theta}=-e^{-i\phi}$. Hence
\[
g(z)=\frac{2r-e^{-i\phi}z}{1-2r e^{-i\phi}z},
\]
and therefore
\[
\boxed{\displaystyle
f(z)=\frac12\frac{2r-e^{-i\phi}z}{1-2r e^{-i\phi}z},
\qquad \phi\in\mathbb R.}
\]
Conversely, each of these functions maps $\mathbb D$ into the disk of radius
$1/2$, satisfies $f(0)=r$, and has its zero at $2re^{i\phi}$. These are exactly
the extremal functions.
:::
