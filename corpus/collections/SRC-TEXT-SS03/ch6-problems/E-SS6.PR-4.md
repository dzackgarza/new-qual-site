---
schema: qual/card@1
id: E-SS6.PR-4
kind: problem
title: The periodic antiderivatives $Q_k$ are Bernoulli polynomials, and $\zeta(2k)$ in terms of $B_{2k}$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Bernoulli Numbers
relations: []
review: draft
---

::: {.exercise}
$4 . ^ { * }$ The functions $Q _ { k }$ in the previous problem are related to the Bernoulli polynomials $B _ { k } ( x )$ by the formula

$$
Q _ {k} (x) = \frac {B _ {k + 1} (x)}{(k + 1) !} \quad \text {for} \quad 0 \leq x \leq 1.
$$

Also, if k is a positive integer, then

$$
2 \zeta (2 k) = (- 1) ^ {k + 1} \frac {(2 \pi) ^ {2 k}}{(2 k) !} B _ {2 k},
$$

where $B _ { k } = B _ { k } ( 0 )$ are the Bernoulli numbers. For the definition of $B _ { k } ( x )$ and $B _ { k }$ see Chapter 3 in Book I.
:::

::: {.solution}
Let $B_m(x)$ be the Bernoulli polynomials, defined by
$$
\frac{z e^{xz}}{e^z-1}=\sum_{m=0}^\infty B_m(x)\frac{z^m}{m!},\qquad |z|<2\pi,
$$
and write $B_m=B_m(0)$. The generating function gives $B_0(x)=1$ and $B_1(x)=x-\frac12$. The functions $Q_k$ are those of [[E-SS6.PR-3|the previous problem]].

::: pf

::: {.pf-step #bernoulli-identities}
For every $m\ge1$,
$$
B_m'(x)=mB_{m-1}(x),\qquad B_m(x+1)-B_m(x)=mx^{m-1}.
$$
Consequently $B_m(1)=B_m(0)$ for $m\ge2$, $B_1(1)-B_1(0)=1$, and $\int_0^1B_m(x)\,dx=0$ for $m\ge1$.

::: pf-proof
Differentiate the generating function with respect to $x$ and compare the coefficients of $z^m/m!$ to obtain the derivative identity. Subtract the generating function at $x$ from the generating function at $x+1$; the left side is $z e^{xz}$, whose coefficient of $z^m/m!$ is $m x^{m-1}$, so the difference identity follows. Set $x=0$ in the difference identity: the right side is $1$ for $m=1$ and $0$ for $m\ge2$. Finally, $B_m=B_{m+1}'/(m+1)$ and $B_{m+1}(1)=B_{m+1}(0)$ for $m+1\ge2$, so
$$
\int_0^1B_m(x)\,dx=\frac{B_{m+1}(1)-B_{m+1}(0)}{m+1}=0.
$$
:::

:::

::: {.pf-step #qk-bernoulli}
For every $k\ge0$ and every $0\le x<1$,
$$
Q_k(x)=\frac{B_{k+1}(x)}{(k+1)!}.
$$
For $k\ge1$ the identity also holds at $x=1$.

::: pf-proof
Use induction on $k$. For $k=0$, $Q_0(x)=x-\frac12=B_1(x)$ on $[0,1)$. Suppose the identity holds for $k$. For $0\le x<1$,
$$
Q_{k+1}(x)=Q_{k+1}(0)+\int_0^xQ_k(t)\,dt
=Q_{k+1}(0)+\frac{B_{k+2}(x)-B_{k+2}(0)}{(k+2)!}.
$$
The normalization $\int_0^1Q_{k+1}=0$ gives
$$
0=Q_{k+1}(0)+\frac{1}{(k+2)!}\left(\int_0^1B_{k+2}(t)\,dt-B_{k+2}(0)\right)
=Q_{k+1}(0)-\frac{B_{k+2}(0)}{(k+2)!},
$$
because $\int_0^1B_{k+2}=0$ by step [](#bernoulli-identities){.pf-ref}. Thus $Q_{k+1}(0)=B_{k+2}(0)/(k+2)!$, and the identity holds for $k+1$. For $k\ge1$, periodicity gives $Q_k(1)=Q_k(0)$, and $B_{k+1}(1)=B_{k+1}(0)$ because $k+1\ge2$, so the identity extends to $x=1$. For $k=0$ the literal endpoint is exceptional: $Q_0(1)=-\frac12$ while $B_1(1)=\frac12$.
:::

:::

:::

For the second identity, put
$$
\widehat B_m(n)=\int_0^1B_m(x)e^{-2\pi i n x}\,dx
$$
for $m\ge0$ and $n\in\ZZ\setminus\{0\}$.

::: pf

::: {.pf-step #fourier-coefficients}
For every $m\ge1$ and every nonzero integer $n$,
$$
\widehat B_m(n)=\frac{m!}{(2\pi i n)^{m-1}}\widehat B_1(n),
\qquad
\widehat B_1(n)=\frac{i}{2\pi n}.
$$

::: pf-proof
For $m=1$,
$$
\widehat B_1(n)=\int_0^1\left(x-\frac12\right)e^{-2\pi i n x}\,dx
=\left[\frac{x e^{-2\pi i n x}}{-2\pi i n}\right]_0^1
=\frac{i}{2\pi n},
$$
since $\int_0^1e^{-2\pi i n x}\,dx=0$. For $m\ge2$, integrate by parts:
$$
\widehat B_m(n)
=\left[\frac{B_m(x)e^{-2\pi i n x}}{-2\pi i n}\right]_0^1
+\frac{1}{2\pi i n}\int_0^1B_m'(x)e^{-2\pi i n x}\,dx.
$$
The boundary term vanishes because $B_m(1)=B_m(0)$ by step [](#bernoulli-identities){.pf-ref}. Since $B_m'=mB_{m-1}$, the recursion $\widehat B_m(n)=\frac{m}{2\pi i n}\widehat B_{m-1}(n)$ follows, and iteration gives the formula.
:::

:::

::: {.pf-step #even-coefficients}
For every $k\ge1$ and every nonzero integer $n$,
$$
\widehat B_{2k}(n)=(-1)^{k+1}\frac{(2k)!}{(2\pi n)^{2k}}.
$$

::: pf-proof
Set $m=2k$ in step [](#fourier-coefficients){.pf-ref}:
$$
\widehat B_{2k}(n)=\frac{(2k)!}{(2\pi i n)^{2k-1}}\frac{i}{2\pi n}
=\frac{(2k)!}{i^{2k-2}(2\pi n)^{2k}}.
$$
Since $i^{2k-2}=(-1)^{k-1}=(-1)^{k+1}$, the formula follows.
:::

:::

::: {.pf-step #fourier-series}
For every $k\ge1$ and every $0\le x\le1$,
$$
B_{2k}(x)=(-1)^{k+1}\frac{2(2k)!}{(2\pi)^{2k}}
\sum_{n=1}^\infty\frac{\cos(2\pi n x)}{n^{2k}}.
$$

::: pf-proof
By step [](#even-coefficients){.pf-ref},
$$
\sum_{n\ne0}\left|\widehat B_{2k}(n)\right|
=\frac{2(2k)!}{(2\pi)^{2k}}\sum_{n=1}^\infty\frac{1}{n^{2k}}<\infty
$$
because $k\ge1$. Hence the Fourier series converges absolutely and uniformly to a continuous $1$-periodic function $F$. The same series converges to $B_{2k}$ in $L^2([0,1])$, so $F=B_{2k}$ almost everywhere; both functions are continuous, so $F=B_{2k}$ everywhere. The coefficient at $n=0$ is $\int_0^1B_{2k}=0$ by step [](#bernoulli-identities){.pf-ref}. Pair the terms $n$ and $-n$ and use $\widehat B_{2k}(-n)=\widehat B_{2k}(n)$ to obtain the cosine series.
:::

:::

::: {.pf-step #euler-formula}
For every positive integer $k$,
$$
2\zeta(2k)=(-1)^{k+1}\frac{(2\pi)^{2k}}{(2k)!}B_{2k}.
$$

::: pf-proof
Set $x=0$ in step [](#fourier-series){.pf-ref}. Since $\cos 0=1$ and $B_{2k}(0)=B_{2k}$,
$$
B_{2k}=(-1)^{k+1}\frac{2(2k)!}{(2\pi)^{2k}}\sum_{n=1}^\infty\frac{1}{n^{2k}}
=(-1)^{k+1}\frac{2(2k)!}{(2\pi)^{2k}}\zeta(2k).
$$
Multiplying by $(-1)^{k+1}(2\pi)^{2k}/(2(2k)!)$ and then by $2$ gives the stated identity.
:::

:::

:::

:::
