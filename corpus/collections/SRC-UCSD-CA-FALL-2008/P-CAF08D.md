---
schema: qual/card@1
id: P-CAF08D
kind: problem
title: "Analytic continuation and maximum principle for power series with nonnegative coefficients"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: termwise
    differentiation and absolute convergence of the derived series, the triangle
    inequality bound of part (a), Cauchy-Hadamard at 1 - delta and the coefficient
    domination that carries it to (1-delta)e^{i theta}, and the patching of the
    continuations (two balls meet in a convex set containing the midpoint, of modulus at
    most 1 - delta < 1, where both agree with f, so the identity theorem applies). The
    prose left the patching of continuations in part (c) implicit. The collection's
    provenance is the examination paper only, so no retained solution set covers the
    exercise and the argument is the card's own.
---

::: {.problem}
Let $f(z) = \sum_{n=0}^{\infty} a_n z^n$, $a_n \geq 0$ for all $n$, where the series is absolutely convergent for $\abs{z} < 1$.

(a) For any $r$, $0 \leq r < 1$, any $\theta \in \RR$, and any nonnegative integer $k$, prove that $\abs{f^{(k)}(re^{i\theta})} \leq \abs{f^{(k)}(r)}$.

(b) If $f(z)$ extends analytically to $B(1 - \delta; 2\delta)$ for some $\delta$, $0 < \delta < 1$, prove that $f(z)$ extends analytically to $B((1-\delta)e^{i\theta}; 2\delta)$ for any $\theta \in \RR$.

(c) Prove that if $f(z)$ extends analytically to an open neighborhood of $z = 1$, then the radius of convergence of the series $\sum_{n=0}^{\infty} a_n z^n$ is strictly greater than 1.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #derivatives}
For every $k\ge0$ and every $\abs{z}<1$ the series
$$
f^{(k)}(z)=\sum_{n=k}^{\infty}\frac{n!}{(n-k)!}a_n z^{n-k}
$$
converges absolutely.

::: pf-proof
A power series may be differentiated term by term inside its disc of convergence, which is a statement about the radius of convergence being unchanged; here $\abs{z}<1$ and the series for $f$ converges on $\abs{z}<1$ by hypothesis, and the differentiated series has the coefficients $\frac{n!}{(n-k)!}a_n$, whose growth is polynomial in $n$ times $a_n$. Absolute convergence at $\abs{z}<1$ follows from that of $\sum a_nz^n$: choose $z'$ with $\abs{z}<\abs{z'}<1$, so that $\sum a_n\abs{z'}^n<\infty$; the ratios $\frac{n!}{(n-k)!}\abs{z}^{n-k}\big/\abs{z'}^n=\frac{n!}{(n-k)!}\abs{z}^{-k}\left(\abs{z}/\abs{z'}\right)^n$ tend to $0$ as $n\to\infty$, because a polynomial in $n$ is dominated by the geometric decay of $(\abs{z}/\abs{z'})^n$, and so are bounded by a constant $C_k$ independent of $n$. Hence $\sum_n\frac{n!}{(n-k)!}a_n\abs{z}^{n-k}\le C_k\sum_na_n\abs{z'}^n<\infty$.
:::

:::

::: {.pf-step #part-a}
(a) For $0\le r<1$, $\theta\in\RR$ and $k\ge0$,
$$
\abs{f^{(k)}(re^{i\theta})}\le f^{(k)}(r).
$$

::: pf-proof
By step [](#derivatives){.pf-ref} and the triangle inequality,
$$
\abs{f^{(k)}(re^{i\theta})}
\le\sum_{n=k}^{\infty}\frac{n!}{(n-k)!}a_n r^{n-k}\abs{e^{i(n-k)\theta}}
=\sum_{n=k}^{\infty}\frac{n!}{(n-k)!}a_n r^{n-k}.
$$
Since $a_n\ge0$ and $r\ge0$, the right-hand side is the real number $f^{(k)}(r)$, and it is nonnegative, so it equals $\abs{f^{(k)}(r)}$.
:::

:::

::: {.pf-step}
(b) If $f$ extends analytically to $B(1-\delta;2\delta)$ for some $\delta$ with $0<\delta<1$, then for every $\theta$ the function $f$ extends analytically to $B((1-\delta)e^{i\theta};2\delta)$.

::: pf-proof

::: {.pf-step #taylor-at-centre}
The Taylor series of $f$ at $1-\delta$ converges on $B(1-\delta;2\delta)$, so
$$
\limsup_{k\to\infty}\left(\frac{\abs{f^{(k)}(1-\delta)}}{k!}\right)^{1/k}\le\frac{1}{2\delta}.
$$

::: pf-proof
$f$ is analytic on $B(1-\delta;2\delta)$ by hypothesis, so its Taylor series at the centre converges to $f$ on that disc, and the Cauchy--Hadamard formula bounds the radius of convergence from below by $2\delta$.
:::

:::

::: {.pf-step #coefficients}
For every $\theta$ and every $k\ge0$,
$$
\frac{\abs{f^{(k)}((1-\delta)e^{i\theta})}}{k!}\le\frac{\abs{f^{(k)}(1-\delta)}}{k!}.
$$

::: pf-proof
Part (a) of step [](#part-a){.pf-ref} with $r=1-\delta$, which lies in $[0,1)$, and with $k$ arbitrary gives $\abs{f^{(k)}((1-\delta)e^{i\theta})}\le f^{(k)}(1-\delta)=\abs{f^{(k)}(1-\delta)}$.
:::

:::

::: {.pf-step}
For $z_\theta\coloneqq(1-\delta)e^{i\theta}$ the Taylor series of $f$ at $z_\theta$ converges on $B(z_\theta;2\delta)$ and continues $f$ there.

::: pf-proof
By step [](#coefficients){.pf-ref} the coefficient sequence at $z_\theta$ is dominated term by term by that at $1-\delta$, so its $\limsup$ of $k$-th roots is at most $1/(2\delta)$ by step [](#taylor-at-centre){.pf-ref}; Cauchy--Hadamard then gives a radius of convergence of at least $2\delta$. The sum of that series is analytic at $z_\theta$ and equals $f$ on a neighbourhood of $z_\theta$, because both are given there by the same convergent Taylor series of the analytic function $f$ at $z_\theta$; so it is an analytic continuation of $f$ to $B(z_\theta;2\delta)$.
:::

:::

:::

:::

::: {.pf-step}
(c) If $f$ extends analytically to an open neighbourhood of $z=1$, then the radius of convergence of $\sum_{n\ge0}a_nz^n$ is strictly greater than $1$.

::: pf-proof

::: {.pf-step #small-delta}
There is $\delta\in(0,1)$ with $B(1-\delta;2\delta)$ contained in that neighbourhood.

::: pf-proof
Let $U$ be the open neighbourhood of $1$. Some $\delta\in(0,1)$ has $B(1;3\delta)\subset U$, since $U$ is open. If $\abs{z-(1-\delta)}<2\delta$ then $\abs{z-1}\le\abs{z-(1-\delta)}+\delta<3\delta$, so $B(1-\delta;2\delta)\subset B(1;3\delta)\subset U$.
:::

:::

::: {.pf-step #ball-covers}
For every $z$ with $1\le\abs{z}<1+\delta$, the point $z$ lies in $B((1-\delta)e^{i\theta};2\delta)$ for $\theta=\arg z$.

::: pf-proof
With $\theta=\arg z$ the points $z$ and $(1-\delta)e^{i\theta}$ are parallel and point the same way, so
$$
\abs{z-(1-\delta)e^{i\theta}}=\abs{z}-(1-\delta)<(1+\delta)-(1-\delta)=2\delta.
$$
:::

:::

::: {.pf-step #glued}
There is an analytic $g$ on $D\cup\bigcup_{\theta\in\RR}B((1-\delta)e^{i\theta};2\delta)$, where $D$ is the unit disc, that agrees with $f$ on $D$.

::: pf-proof
Write $c_\theta\coloneqq(1-\delta)e^{i\theta}$ and $B_\theta\coloneqq B(c_\theta;2\delta)$, and let $f_\theta$ be the continuation to $B_\theta$ supplied by part (b). Each $B_\theta$ contains $c_\theta\in D$ and is open, so $B_\theta\cap D$ is a nonempty open set on which $f_\theta$ and $f$ agree. If $B_\theta\cap B_{\theta'}\ne\emptyset$, that intersection is convex, hence connected, and it contains $m\coloneqq(c_\theta+c_{\theta'})/2$, which satisfies $\abs{m}\le(\abs{c_\theta}+\abs{c_{\theta'}})/2=1-\delta<1$ and $\abs{m-c_\theta}=\abs{c_\theta-c_{\theta'}}/2<2\delta$. So $m$ lies in the open unit disc, where $f_\theta=f=f_{\theta'}$, and the identity theorem on the connected set $B_\theta\cap B_{\theta'}$ gives $f_\theta=f_{\theta'}$ there. The prescriptions therefore agree on all overlaps, and $D$ meets every $B_\theta$, so they define one analytic function $g$ on the union.
:::

:::

::: {.pf-step}
The radius of convergence of $\sum_{n\ge0}a_nz^n$ is at least $1+\delta$, hence strictly greater than $1$.

::: pf-proof
By steps [](#ball-covers){.pf-ref} and [](#glued){.pf-ref} the germ of the series at $0$ extends analytically to $D\cup\bigcup_\theta B_\theta$, which contains the disc $\abs{z}<1+\delta$; the sum of the series is analytic on the whole disc of radius $1+\delta$, so the radius of convergence, which is the supremum of the radii of the discs about $0$ to which the germ extends, is at least $1+\delta>1$.
:::

:::

:::

:::
:::

:::
