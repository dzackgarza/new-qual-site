---
schema: qual/card@1
id: E-SS7.PR-2
kind: problem
title: The explicit formula for $\psi_1(x)$ as a sum over zeros of $\zeta$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Prime Number Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: deepseek-v4.1-flash-free
  date: 2026-10-27
  note: Checked Problem 2 on p.204 against the source PDF. The printed formula has $x^\rho/(\rho(\rho+1))$ and $E=c_1x+c_0+\cdots$; the contour shift of Proposition 2.3 gives $x^{\rho+1}/(\rho(\rho+1))$ and the constant $+c_0$, so the corrected error term is $c_1x-c_0+\cdots$. The solution proves the corrected formula.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints $x^\rho/(\rho(\rho+1))$ and $E(x)=c_1x+c_0+\cdots$; the statement now has $x^{\rho+1}/(\rho(\rho+1))$ and $E(x)=c_1x-c_0+\cdots$.
---

::: {.exercise}
$^\ast$ One of the “explicit formulas” in the theory of primes is as follows: if $\psi _ { 1 }$ is the integrated Tchebychev function considered in Section 2, then

$$
\psi_ {1} (x) = \frac {x ^ {2}}{2} - \sum_ {\rho} \frac {x ^ {\rho + 1}}{\rho (\rho + 1)} - E (x)
$$

where the sum is taken over all zeros $\rho$ of the zeta function in the critical strip.
The error term is given by $E ( x ) = c _ { 1 } x - c _ { 0 } + \sum _ { k = 1 } ^ { \infty } x ^ { 1 - 2 k } / ( 2 k ( 2 k - 1 ) )$ , where $c _ { 1 } = \zeta ^ { \prime } ( 0 ) / \zeta ( 0 )$ and $c _ { 0 } = \zeta ^ { \prime } ( - 1 ) / \zeta ( - 1 )$ . Note that $\textstyle \sum _ { \rho } 1 / \abs{ \rho } ^ { 1 + \epsilon } < \infty$ for every $\epsilon > 0$ , because $( 1 - s ) \zeta ( s )$ has order of growth 1. (See Exercise 8.) Also, obviously $E ( x ) = O ( x )$ as $x \to \infty$
:::

::: {.solution}
Let $x>1$, and put
$$
c_1=\frac{\zeta'(0)}{\zeta(0)},\qquad c_0=\frac{\zeta'(-1)}{\zeta(-1)}.
$$

::: pf

::: {.pf-step #perron-integral}
For every $c>1$,
$$
\psi_1(x)=\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{x^{s+1}}{s(s+1)}\left(-\frac{\zeta'}{\zeta}(s)\right)ds.
$$

::: pf-proof
For $\Re s>1$, the Dirichlet series
$$
-\frac{\zeta'}{\zeta}(s)=\sum_{n=1}^\infty\Lambda(n)n^{-s}
$$
converges absolutely and locally uniformly. Hence
$$
\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{x^{s+1}}{s(s+1)}\left(-\frac{\zeta'}{\zeta}(s)\right)ds
=x\sum_{n=1}^\infty\Lambda(n)\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{(x/n)^s}{s(s+1)}ds.
$$
The interchange is justified because
$$
\sum_{n=1}^\infty\Lambda(n)n^{-c}\int_{-\infty}^{\infty}\frac{x^c}{\abs{c+it}\abs{c+1+it}}dt<\infty.
$$
By Lemma 2.4, the inner integral is $1-n/x$ when $n<x$, and it is $0$ when $n\ge x$. Therefore
$$
x\sum_{n=1}^\infty\Lambda(n)\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\frac{(x/n)^s}{s(s+1)}ds
=\sum_{n<x}\Lambda(n)(x-n)=\psi_1(x).
$$
The term $n=x$ contributes $0$, so the sum over $n<x$ equals the sum over $n\le x$.
:::

:::

::: {.pf-step #contour}
Let
$$
F(s)=\frac{x^{s+1}}{s(s+1)}\left(-\frac{\zeta'}{\zeta}(s)\right).
$$
For $T>0$ avoiding the ordinates of the nontrivial zeros and $A>2$ avoiding the trivial zeros, the residue theorem on the rectangle $R$ with vertices $c\pm iT$, $-A\pm iT$ gives
$$
\frac{1}{2\pi i}\int_{\partial R}F(s)\,ds
=\sum_{\text{poles inside }R}\operatorname{Res}(F,s).
$$

::: pf-proof
The poles of $F$ inside $R$ are $s=1$, $s=0$, $s=-1$, the nontrivial zeros $\rho$ with $\abs{\Im\rho}<T$, and the trivial zeros $-2,\ldots,-2K$ with $2K<A$. There are no other poles inside the rectangle. The residue theorem applies because $F$ is meromorphic on a neighborhood of $R$ and the boundary contains no poles.
:::

:::

::: {.pf-step #residues}
The residue sum is
$$
\frac{x^2}{2}-c_1x+c_0
-\sum_{\abs{\Im\rho}<T}\frac{x^{\rho+1}}{\rho(\rho+1)}
-\sum_{k=1}^{K}\frac{x^{1-2k}}{2k(2k-1)}.
$$

::: pf-proof
At $s=1$, $\zeta$ has a simple pole with residue $1$, so $-\zeta'/\zeta$ has residue $1$; the factor $x^{s+1}/(s(s+1))$ equals $x^2/2$ there. At $s=0$, $-\zeta'/\zeta(0)=-c_1$ and $x^{s+1}/(s+1)=x$, so the residue is $-c_1x$. At $s=-1$, $-\zeta'/\zeta(-1)=-c_0$ and $x^{s+1}/s=-1$, so the residue is $c_0$. At a nontrivial zero $\rho$, $-\zeta'/\zeta$ has residue $-1$, and the factor is $x^{\rho+1}/(\rho(\rho+1))$. At a trivial zero $-2k$, $-\zeta'/\zeta$ has residue $-1$, and the factor is $x^{1-2k}/(2k(2k-1))$. Summing these residues gives the displayed expression.
:::

:::

::: {.pf-step #boundary}
The integrals of $F$ over the left side and the two horizontal sides of $R$ tend to $0$ as $A\to\infty$ and $T\to\infty$.

::: pf-proof
On the contour, the standard estimate
$$
\abs{\frac{\zeta'}{\zeta}(s)}=O(\log(2+\abs{t}))
$$
holds uniformly for $\sigma\ge0$, away from the pole at $s=1$. For $\sigma<0$, the functional equation
$$
\zeta(s)=2^s\pi^{s-1}\sin\left(\frac{\pi s}{2}\right)\Gamma(1-s)\zeta(1-s)
$$
and Stirling's formula give the same bound. On the left side $s=-A+it$,
$$
\abs{\int_{C_L}F(s)\,ds}
\le Cx^{1-A}\int_{-\infty}^{\infty}\frac{\log(2+\abs{t})}{1+t^2}\,dt
=O(x^{1-A}).
$$
On the horizontal sides $s=\sigma\pm iT$,
$$
\abs{\int_{C_T^\pm}F(s)\,ds}
\le CT^{-2}\log(2+T)\int_{-\infty}^{c}x^{\sigma+1}\,d\sigma
=O(T^{-2}\log T).
$$
Both bounds tend to $0$.
:::

:::

::: {.pf-step #limit}
Letting $T\to\infty$ and $A\to\infty$ gives
$$
\psi_1(x)=\frac{x^2}{2}-c_1x+c_0
-\sum_\rho\frac{x^{\rho+1}}{\rho(\rho+1)}
-\sum_{k=1}^\infty\frac{x^{1-2k}}{2k(2k-1)}.
$$

::: pf-proof
The residue theorem gives the original integral as the residue sum minus the left and horizontal integrals; those integrals vanish by step [](#boundary){.pf-ref}. The partial sums over the nontrivial zeros converge absolutely to the full sum because
$$
\sum_\rho\abs{\frac{x^{\rho+1}}{\rho(\rho+1)}}
\le Cx^2\sum_\rho\frac{1}{\abs{\rho}^2}<\infty,
$$
and the problem gives $\sum_\rho1/\abs{\rho}^{1+\epsilon}<\infty$ for every $\epsilon>0$. The trivial-zero series converges because $x>1$ and $2k(2k-1)\sim4k^2$. Therefore the residue sum tends to the displayed formula.
:::

:::

::: {.pf-step #error}
With
$$
E(x)=c_1x-c_0+\sum_{k=1}^\infty\frac{x^{1-2k}}{2k(2k-1)},
$$
one has $E(x)=O(x)$ as $x\to\infty$.

::: pf-proof
For $x\ge2$,
$$
\abs{\sum_{k=1}^\infty\frac{x^{1-2k}}{2k(2k-1)}}
\le x^{-1}\sum_{k=1}^\infty\frac{1}{2k(2k-1)}=O(x^{-1}).
$$
Since $c_0$ is constant, $E(x)=c_1x+O(1)=O(x)$.
:::

:::

:::

:::
