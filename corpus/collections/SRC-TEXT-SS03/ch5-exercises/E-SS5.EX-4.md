---
schema: qual/card@1
id: E-SS5.EX-4
kind: problem
title: Growth and zeros of $\prod_n(1-e^{-2\pi nt}e^{2\pi iz})$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Infinite Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The split of the product at
    N = floor(|z|/t) + 1 is now a step with the tail bounded by exp of a convergent series
    (not merely by a constant, which is what the earlier prose asserted without the
    exponential), the zero set is derived from the vanishing of a factor together with the
    normal convergence that forbids other zeros, and the two exponent-of-convergence
    estimates are separated: divergence from the count of lattice points in a disc of radius
    nt, convergence by integral comparison in two variables. The exactness of the order is
    then a Jensen argument against the zero count. Not checked: the book's own text of the
    exercise, since no copy of Stein and Shakarchi is retained in this checkout; the
    statement is as transcribed on the card. No retained solution set covers the exercise
    (the collection's provenance is a Google Books record), so the argument is the card's
    own. No statement repair.
---

::: {.exercise}
Let $t > 0$ be given and fixed, and define $F(z)$ by
$$
F(z) = \prod_{n=1}^{\infty} (1 - e^{-2\pi n t} e^{2\pi i z}).
$$
Note that the product defines an entire function of $z$.

(a) Show that $\abs{F(z)} \le A e^{a \abs{z}^2}$, hence $F$ is of order 2.

(b) Show that $F$ vanishes exactly when $z = -i n t + m$ for $n \ge 1$ and $m \in \ZZ$ (integers).
Deduce that if $\{z_k\}$ is an enumeration of these zeros, we have
$$
\sum_k \frac{1}{\abs{z_k}^2} = \infty \quad \text{but} \quad \sum_k \frac{1}{\abs{z_k}^{2+\varepsilon}} < \infty \quad \text{for any } \varepsilon > 0.
$$

[Hint: To prove (a), write $F(z) = F_1(z)F_2(z)$ where
$$
F_1(z) = \prod_{n=1}^{N}(1 - e^{-2\pi nt}e^{2\pi iz}) \quad \text{and} \quad F_2(z) = \prod_{n=N+1}^{\infty}(1 - e^{-2\pi nt}e^{2\pi iz}).
$$
Choose $N \approx c\abs{z}$ with $c$ appropriately large. Then, since $\qty(\sum_{N+1}^{\infty} e^{-2\pi nt})e^{2\pi\abs{z}} \le 1$, one has $\abs{F_2(z)} \le A$. However, $\abs{1 - e^{-2\pi nt}e^{2\pi iz}} \le 1 + e^{2\pi\abs{z}} \le 2e^{2\pi\abs{z}}$. Thus $\abs{F_1(z)} \le 2^N e^{2\pi N\abs{z}} \le e^{c'\abs{z}^2}$.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Fix $t>0$, put $q=e^{-2\pi t}\in(0,1)$, and
$$
F(z)=\prod_{n\ge1}\bigl(1-q^ne^{2\pi iz}\bigr).
$$

::: pf

::: {.pf-step #entire}
The product converges normally on $\CC$; $F$ is entire, and $F(z)=0$ exactly when one of the factors vanishes.

::: pf-proof
On the disc $\abs{z}\le R$ one has $\abs{q^ne^{2\pi iz}}\le q^ne^{2\pi R}=:u_n$ with $\sum_nu_n=\frac{qe^{2\pi R}}{1-q}<\infty$, so the series of the $u_n$ converges. A product $\prod_n(1+c_n(z))$ with $\sum_n\sup_{\abs{z}\le R}\abs{c_n}<\infty$ converges normally to a holomorphic function, and if no factor vanishes on a compact set then the product has no zeros there: on a compact set $\abs{c_n}\le\frac12$ for $n\ge N$, and $\prod_{n\ge N}(1+c_n)$ is then bounded below by $\exp\bigl(-\sum_{n\ge N}2\abs{c_n}\bigr)>0$ using $\abs{\log(1+c)}\le2\abs{c}$ for $\abs{c}\le\frac12$. Since the remaining finitely many factors are nonvanishing off their own zero sets, the zeros of $F$ are exactly the zeros of the individual factors.
:::

:::

::: {.pf-step #zeros}
(b) $F(z)=0$ if and only if $z=m-int$ for some $n\ge1$ and $m\in\ZZ$.

::: pf-proof
A factor vanishes exactly when $q^ne^{2\pi iz}=1$, that is $e^{2\pi iz}=e^{2\pi nt}$. Writing $z=x+iy$ this says $e^{-2\pi y}e^{2\pi ix}=e^{2\pi nt}$, so $x\in\ZZ$ (the arguments agree mod $2\pi$) and $-2\pi y=2\pi nt$, i.e. $y=-nt$ and $x=m$. So $z=m-int$ with $m\in\ZZ$, conversely such $z$ satisfies $e^{2\pi iz}=e^{2\pi im}e^{2\pi nt}=e^{2\pi nt}$ and is a zero of the $n$-th factor. Together with step [](#entire){.pf-ref} this describes the zero set.
:::

:::

::: {.pf-step #growth}
(a) There are $A,a>0$, depending on $t$, with $\abs{F(z)}\le Ae^{a\abs{z}^2}$.

::: pf-proof
Let $z$ be given, $N=\lfloor\abs{z}/t\rfloor+1$, so that $N\ge1$ and $Nt\ge\abs{z}$. For $n>N$, $\abs{q^ne^{2\pi iz}}\le e^{-2\pi nt+2\pi\abs{z}}\le e^{-2\pi t(n-N)}$, using $\abs{z}\le Nt$; hence
$$
\prod_{n>N}\abs{1-q^ne^{2\pi iz}}\le\prod_{n>N}\bigl(1+e^{-2\pi t(n-N)}\bigr)\le\exp\Bigl(\sum_{j\ge1}e^{-2\pi tj}\Bigr)=:C_t,
$$
using $1+u\le e^u$ and the geometric series. For $n\le N$, $\abs{1-q^ne^{2\pi iz}}\le1+e^{2\pi\abs{z}}\le2e^{2\pi\abs{z}}$, so the first $N$ factors contribute at most $\bigl(2e^{2\pi\abs{z}}\bigr)^N\le\exp\bigl(N\log2+2\pi N\abs{z}\bigr)$. Since $N\le\abs{z}/t+1\le(1+1/t)\abs{z}+1$, the exponent is at most $a\abs{z}^2$ for a suitable $a=a(t)$ and all $\abs{z}\ge1$; for $\abs{z}\le1$ increase $A$ to absorb the bounded factor. So $\abs{F(z)}\le Ae^{a\abs{z}^2}$, which says the order of $F$ is at most $2$.
:::

:::

::: {.pf-step #divergence}
(b) With $\{z_k\}$ enumerating the zeros, $\displaystyle\sum_k\frac{1}{\abs{z_k}^2}=\infty$.

::: pf-proof
The zeros are $m-int$, so $\abs{m-int}^2=m^2+n^2t^2$ by orthogonality of the real and imaginary parts. For each $n\ge1$ and each integer $m$ with $\abs{m}\le nt$ one has $m^2+n^2t^2\le2n^2t^2$, and there are at least $2nt$ such $m$. Hence
$$
\sum_{n\ge1}\sum_{\abs{m}\le nt}\frac{1}{m^2+n^2t^2}\ge\sum_{n\ge1}\frac{2nt}{2n^2t^2}=\frac1t\sum_{n\ge1}\frac1n=\infty,
$$
and the full sum over all zeros dominates this subseries, so it diverges.
:::

:::

::: {.pf-step #convergence}
(b) $\displaystyle\sum_k\frac{1}{\abs{z_k}^{2+\varepsilon}}<\infty$ for every $\varepsilon>0$.

::: pf-proof
Let $p=1+\varepsilon/2>1$. The map $(x,y)\mapsto(x,yt)$ identifies the lattice $\{(m,nt):m\in\ZZ,n\ge1\}$ with a lattice of mesh comparable to $1$ in $\RR^2$, and $(m^2+n^2t^2)^{-p}=\bigl((x^2+y^2t^2)\bigr)^{-p}$. Comparing a sum over a lattice with the integral over the union of unit squares centred at its points, which are contained in an annulus of comparable area, gives
$$
\sum_{n\ge1}\sum_{m\in\ZZ}\frac{1}{(m^2+n^2t^2)^{p}}\le C_p\int_{\RR^2\setminus B(0,1)}\frac{dx\,dy}{(x^2+y^2t^2)^{p}}+C'_p<\infty,
$$
and the integral is finite in polar coordinates because the integrand is $\asymp r^{-2p}$ and $\int_1^\infty r^{1-2p}dr=\int_1^\infty r^{-1-\varepsilon}dr<\infty$. Since $2+\varepsilon=2p$, this is the asserted convergence.
:::

:::

::: {.pf-step #order}
The order of $F$ is exactly $2$.

::: pf-proof
By step [](#growth){.pf-ref} the order is at most $2$. If it were $\rho<2$, choose $\sigma$ with $\rho<\sigma<2$; then $\log M(r)=O(r^\sigma)$, where $M(r)=\sup_{\abs{z}\le r}\abs{F}$. Jensen's formula applied to $F$ on the disc of radius $r$ gives $N(r/2)\log2\le\log M(r)-\log\abs{F(0)}$, where $N$ counts zeros with multiplicity, so $N(r/2)=O(r^\sigma)$. But the zeros are the lattice $m-int$, and the disc of radius $r$ contains at least $c_t r^2$ of them: for each $n\le r/(2t)$ the $m$ with $\abs{m}\le r/2$ give points with $\abs{m-int}\le r$, and there are about $r$ such $m$ for each of about $r/(2t)$ values of $n$. That contradicts $N(r/2)=O(r^\sigma)$ with $\sigma<2$, so the order is $2$, and with steps [](#divergence){.pf-ref} and [](#convergence){.pf-ref} the exponent of convergence of the zero set is also $2$.
:::

:::

:::

:::
