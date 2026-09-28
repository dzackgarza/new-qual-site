---
schema: qual/card@1
id: E-SS1.EX-16
kind: problem
title: Radii of convergence of explicit power, hypergeometric, and Bessel series
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Determine the radius of convergence of $\sum_{n=1}^{\infty}a_nz^n$ when:

(a) $a_n=(\log n)^2$;

(b) $a_n=n!$;

(c) $a_n=\dfrac{n^2}{4^n+3n}$;

(d) $a_n=\dfrac{(n!)^3}{(3n)!}$;

(e) for the hypergeometric series
\[
F(\alpha,\beta,\gamma;z)
=
1+\sum_{n=1}^{\infty}
\frac{\alpha(\alpha+1)\cdots(\alpha+n-1)\,\beta(\beta+1)\cdots(\beta+n-1)}
{n!\,\gamma(\gamma+1)\cdots(\gamma+n-1)}z^n,
\]
where $\alpha,\beta\in\mathbb C$ and $\gamma\ne0,-1,-2,\ldots$;

(f) for the Bessel function of positive integer order $r$,
\[
J_r(z)
=\left(\frac z2\right)^r
\sum_{n=0}^{\infty}
\frac{(-1)^n}{n!(n+r)!}\left(\frac z2\right)^{2n}.
\]
:::

::: {.solution}
<1>1. In part (a), the radius of convergence is $R=1$.
::: {.proof}
By the Cauchy-Hadamard formula,
\[
R^{-1}=\limsup_{n\to\infty}|a_n|^{1/n}.
\]
Here
\[
|a_n|^{1/n}=\exp\!\left(\frac{2\log\log n}{n}\right)\longrightarrow1,
\]
so $R^{-1}=1$.
:::

<1>2. In part (b), the radius of convergence is $R=0$.
::: {.proof}
For the nonzero coefficients $a_n=n!$,
\[
\left|\frac{a_{n+1}}{a_n}\right|=n+1\longrightarrow\infty.
\]
Thus for every $z\ne0$, the ratio of successive absolute values of the terms is $(n+1)|z|\to\infty$, so the terms do not even tend to zero. Hence convergence occurs only at $z=0$.
:::

<1>3. In part (c), the radius of convergence is $R=4$.
::: {.proof}
One has
\[
|a_n|^{1/n}
=
\frac{n^{2/n}}{(4^n+3n)^{1/n}}.
\]
Now $n^{2/n}\to1$, while
\[
(4^n+3n)^{1/n}
=4\left(1+\frac{3n}{4^n}\right)^{1/n}\longrightarrow4.
\]
Therefore $\lim |a_n|^{1/n}=1/4$, so Cauchy-Hadamard gives $R=4$.
:::

<1>4. In part (d), the radius of convergence is $R=27$.
::: {.proof}
The coefficient ratio is
\[
\frac{a_{n+1}}{a_n}
=
\frac{(n+1)^3}{(3n+1)(3n+2)(3n+3)}
\longrightarrow\frac1{27}.
\]
Hence the ratio of successive absolute values of the terms $a_nz^n$ tends to $|z|/27$. The ratio test gives convergence for $|z|<27$ and divergence for $|z|>27$, so the radius is $27$.
:::

<1>5. In part (e), if neither $\alpha$ nor $\beta$ is a nonpositive integer, the hypergeometric series has radius $R=1$.
::: {.proof}
Let
\[
c_n=
\frac{(\alpha)_n(\beta)_n}{n!(\gamma)_n},
\]
where $(q)_n=q(q+1)\cdots(q+n-1)$. Under the stated assumption on $\alpha$ and $\beta$, all $c_n$ are nonzero, and the hypothesis on $\gamma$ makes the denominator nonzero. Thus
\[
\left|\frac{c_{n+1}}{c_n}\right|
=
\left|\frac{(n+\alpha)(n+\beta)}{(n+1)(n+\gamma)}\right|
\longrightarrow1.
\]
The ratio test therefore gives convergence for $|z|<1$ and divergence for $|z|>1$.
:::

<1>6. If $\alpha$ or $\beta$ is a nonpositive integer, the hypergeometric series terminates and has radius $R=\infty$.
::: {.proof}
If, for example, $\alpha=-m$ with $m\in\mathbb Z_{\ge0}$, then $(\alpha)_n=0$ for every $n\ge m+1$. Hence only finitely many coefficients are nonzero, so $F$ is a polynomial. The same argument applies to $\beta$.
:::

<1>7. In part (f), the Bessel series has radius $R=\infty$.
::: {.proof}
Set
\[
c_n=\frac{(-1)^n}{n!(n+r)!}.
\]
As a power series in $w=z^2/4$, its coefficient ratio satisfies
\[
\left|\frac{c_{n+1}}{c_n}\right|
=
\frac1{(n+1)(n+r+1)}\longrightarrow0.
\]
Hence $\sum c_nw^n$ converges for every $w\in\mathbb C$. Substituting $w=z^2/4$ therefore gives convergence for every $z\in\mathbb C$, and multiplication by the polynomial factor $(z/2)^r$ does not change this. Thus $J_r$ is entire and its radius of convergence is infinite.
:::
:::
