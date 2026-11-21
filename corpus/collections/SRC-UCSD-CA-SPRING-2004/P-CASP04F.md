---
schema: qual/card@1
id: P-CASP04F
kind: problem
title: "Interpolation by analytic functions with prescribed values and derivatives"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-18
  note: Read against the UCSD Complex Analysis Qualifying Exam, Spring 2004; statement and hint match.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own proof:
    the Weierstrass zero divisor, the invertible jet map determining each rational
    principal part, Mittag--Leffler for the global meromorphic sum, and cancellation
    against the zero divisor. Checked that the triangular jet map has nonzero diagonal.
---

::: {.problem}
Let $G$ be an open region in $\CC$ and $\{z_n\}$ a sequence of distinct points in $G$ without limit points in $G$.
Suppose that for each $n$, you are given an integer $m_n$ and a sequence of complex numbers $\{w_{n,k}\}_{k=0}^{m_n}$.
Show that there is $f \in H(G)$ such that, for every $n$, $$f^{(k)}(z_n) = w_{n,k}, \quad k = 0, 1, \ldots, m_n.$$

Hint: First show that, given an integer $m$, complex numbers $w_k$ for $k = 1, \ldots, m$, a point $z = a$, and an analytic function $g$ which vanishes to order $m+1$ at $z = a$, then one can find a rational function $$S(z) = \sum_{k=1}^{m+1} \frac{b_k}{(z-a)^k}$$ such that the product $f(z) = S(z)g(z)$ has a removable singularity at $z = a$ and $f^{(k)}(a) = w_k$ for $k = 0, 1, \ldots, m$.
:::

::: {.solution}

No retained solution set covers this examination; the argument below is the card's own.

::: pf

::: {.pf-step #zero-divisor}
There is $g\in H(G)$ whose only zeros are at the points $z_n$, with $\operatorname{ord}_{z_n}g=m_n+1$.

::: pf-proof
The sequence has no limit point in $G$, so the prescribed multiplicity function is a divisor on the plane domain $G$. The Weierstrass theorem on prescribed zeros gives a holomorphic $g$ with exactly these zeros and orders.
:::
:::

::: {.pf-step #local-jet-map}
At each $z_n$, write $g(z)=(z-z_n)^{m_n+1}u_n(z)$ with $u_n(z_n)\ne0$. For arbitrary prescribed $w_{n,0},\ldots,w_{n,m_n}$, there are unique $b_{n,1},\ldots,b_{n,m_n+1}$ such that
$$
S_n(z)=\sum_{j=1}^{m_n+1}\frac{b_{n,j}}{(z-z_n)^j}
$$
has $S_ng$ removable at $z_n$ with the prescribed jet.

::: pf-proof
Multiplying the principal part by $g$ gives $(z-z_n)^{-j}(z-z_n)^{m_n+1}u_n(z)=(z-z_n)^{m_n+1-j}u_n(z)$. The coefficient of $(z-z_n)^r$, for $0\le r\le m_n$, depends on $b_{n,m_n+1-r}$ and, when $r>0$, on earlier coefficients. The diagonal coefficient is $u_n(z_n)\ne0$, so the triangular linear system has a unique solution for every jet.
:::
:::

::: {.pf-step #global-principal-parts}
There is a meromorphic $S$ on $G$ whose principal part at $z_n$ is $S_n$ and which has no other poles.

::: pf-proof
The prescribed principal parts have no accumulation point in $G$, so the Mittag--Leffler theorem produces such an $S$.
:::
:::

::: {.pf-step #product}
The product $f=gS$ has removable singularities at every $z_n$, and its holomorphic extension satisfies $f^{(k)}(z_n)=w_{n,k}$ for $0\le k\le m_n$.

::: pf-proof
Near $z_n$, $f=g(S-S_n)+gS_n$. The first term is holomorphic because $g$ vanishes to order $m_n+1$ and $S-S_n$ is holomorphic; the second has a removable singularity with the prescribed jet by step [](#local-jet-map){.pf-ref}. Away from the $z_n$, both $g$ and $S$ are holomorphic. Extending across the removable points therefore gives the required $f\in H(G)$.
:::
:::

:::
:::
