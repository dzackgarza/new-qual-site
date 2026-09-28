---
schema: qual/card@1
id: P-BKF16-1A
kind: problem
title: Euler product for $\zeta(s)$ and divergence of $\sum_p 1/p$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: finite
    Euler products expand by unique factorization, and divergence of the
    prime reciprocal sum follows by bounding the Euler products uniformly
    under the contrary convergence assumption.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked passage from finite to infinite Euler products, convergence of
    the comparison product under an assumed convergent prime reciprocal
    sum, and unboundedness of zeta(s) as s decreases to 1.
---

::: {.problem}
(a) Prove that if $s > 1$ then $\textstyle \sum _ { n > 0 } n ^ { - s } = \prod _ { p } 1 / ( 1 - p ^ { - s } )$ , where the product is over all primes p.

(b) Prove that the sum $\textstyle \sum _ { p } 1 / p$ over all primes p diverges.
:::

::: {.solution}
For $s>1$, write
$$
\zeta(s)\coloneqq\sum_{n=1}^{\infty}\frac1{n^s}.
$$

<1>1. For every finite set $P$ of primes,
$$
\prod_{p\in P}\frac1{1-p^{-s}}
=
\sum_{\substack{n\ge1\\
\text{every prime divisor of }n\text{ lies in }P}}
\frac1{n^s}.
$$

::: {.proof}
For each $p\in P$, since $s>1$,
$$
\frac1{1-p^{-s}}
=
\sum_{k=0}^{\infty}p^{-ks}.
$$
Multiplying these finitely many absolutely convergent geometric
series gives a sum indexed by exponent tuples
$$
(k_p)_{p\in P}.
$$
The corresponding term is
$$
\prod_{p\in P}p^{-k_ps}
=
\left(
\prod_{p\in P}p^{k_p}
\right)^{-s}.
$$
By unique factorization, the products
$$
\prod_{p\in P}p^{k_p}
$$
are exactly the positive integers all of whose prime divisors lie in
$P$, each occurring once.
:::

<1>2. For $s>1$,
$$
\boxed{
\zeta(s)
=
\prod_p\frac1{1-p^{-s}}.
}
$$

::: {.proof}
Let $P_m$ be the set of the first $m$ primes. By step <1>1,
$$
\prod_{p\in P_m}\frac1{1-p^{-s}}
$$
is the sum of $n^{-s}$ over positive integers whose prime factors all
belong to $P_m$. These sets of integers increase with $m$, and every
positive integer belongs to one of them by unique factorization.

All terms are nonnegative, so the corresponding partial sums increase
to
$$
\sum_{n=1}^{\infty}n^{-s}
=
\zeta(s).
$$
Thus the limit of the finite Euler products is the claimed infinite
product. This proves part (a).
:::

<1>3. Suppose, for contradiction, that
$$
\sum_p\frac1p
$$
converges. Then the product
$$
M\coloneqq\prod_p\frac1{1-p^{-1}}
$$
converges to a finite number.

::: {.proof}
For $0\le x\le1/2$,
$$
-\log(1-x)
=
\int_0^x\frac{dt}{1-t}
\le
2x.
$$
Since $1/p\le1/2$ for every prime $p$,
$$
0
\le
\sum_p-\log(1-p^{-1})
\le
2\sum_p\frac1p
<
\infty.
$$
Hence the logarithms of the finite products
$$
\prod_{p\in P_m}(1-p^{-1})^{-1}
$$
increase to a finite limit. Exponentiating shows that these products
converge to a finite positive number $M$.
:::

<1>4. Under the assumption in step <1>3,
$$
\zeta(s)\le M
$$
for every $s>1$.

::: {.proof}
For every prime $p$ and every $s>1$,
$$
0<p^{-s}\le p^{-1},
$$
and therefore
$$
\frac1{1-p^{-s}}
\le
\frac1{1-p^{-1}}.
$$
Thus each finite Euler product for exponent $s$ is at most the
corresponding finite product for exponent $1$. Passing to the limits
and using steps <1>2--<1>3 gives
$$
\zeta(s)
\le
M.
$$
:::

<1>5. The function $\zeta(s)$ is unbounded as $s\downarrow1$.

::: {.proof}
Let $B>0$. The harmonic partial sums are unbounded: for $r\ge1$,
$$
\begin{aligned}
\sum_{n=1}^{2^r}\frac1n
&=
1+\sum_{j=1}^r
\sum_{n=2^{j-1}+1}^{2^j}\frac1n\\
&\ge
1+\frac r2.
\end{aligned}
$$
Choose $N$ such that
$$
\sum_{n=1}^N\frac1n>B+1.
$$
For this fixed finite $N$,
$$
\sum_{n=1}^N n^{-s}
\longrightarrow
\sum_{n=1}^N\frac1n
$$
as $s\downarrow1$. Hence for $s>1$ sufficiently close to $1$,
$$
\zeta(s)
\ge
\sum_{n=1}^N n^{-s}
>
B.
$$
Since $B$ was arbitrary, $\zeta(s)$ is unbounded near $1$.
:::

<1>6. The prime reciprocal series diverges:
$$
\boxed{\sum_p\frac1p=\infty}.
$$

::: {.proof}
If it converged, step <1>4 would bound $\zeta(s)$ uniformly for all
$s>1$, contradicting step <1>5. This proves part (b).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), and step <1>6 proves part (b).
:::
:::
