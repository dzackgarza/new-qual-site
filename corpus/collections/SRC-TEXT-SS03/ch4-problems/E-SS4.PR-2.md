---
schema: qual/card@1
id: E-SS4.PR-2
kind: problem
title: 'Solving a constant-coefficient linear ODE with the Fourier transform'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 source; repaired the statement where needed.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
The problem is to solve the differential equation
$$
a_n \frac{d^n}{dt^n} u(t) + a_{n-1} \frac{d^{n-1}}{dt^{n-1}} u(t) + \cdots + a_0 u(t) = f(t),
$$
where $a_0, a_1, \ldots, a_n$ are complex constants, and $f$ is a given function. Here we suppose that $f$ has bounded support and is smooth (say of class $C^2$).

(a) Let
$$
\hat{f}(z) = \int_{-\infty}^{\infty} f(t) e^{-2\pi i zt}\, dt.
$$
Observe that $\hat{f}$ is an entire function, and using integration by parts show that
$$
\abs{\hat{f}(x + iy)} \leq \frac{A}{1 + x^2}
$$
if $\abs{y} \leq a$ for any fixed $a \geq 0$.

(b) Write
$$
P(z) = a_n (2\pi iz)^n + a_{n-1} (2\pi iz)^{n-1} + \cdots + a_0.
$$
Find a real number $c$ so that $P(z)$ does not vanish on the line
$$
L = \{z : z = x + ic,\ x \in \RR\}.
$$

(c) Set
$$
u(t) = \int_L \frac{e^{2\pi izt}}{P(z)} \hat{f}(z)\, dz.
$$
Check that
$$
\sum_{j=0}^{n} a_j \left( \frac{d}{dt} \right)^j u(t) = \int_L e^{2\pi izt} \hat{f}(z)\, dz
$$
and
$$
\int_L e^{2\pi izt} \hat{f}(z)\, dz = \int_{-\infty}^{\infty} e^{2\pi ixt} \hat{f}(x)\, dx.
$$
Conclude by the Fourier inversion theorem that
$$
\sum_{j=0}^{n} a_j \left( \frac{d}{dt} \right)^j u(t) = f(t).
$$
:::

::: {.solution}
Let the support of $f$ be contained in $[-R,R]$.

For (a), since the defining integral is over a compact interval and its integrand is entire in $z$, differentiation under the integral sign shows that $\widehat f$ is entire. Because $f$ is $C^2$ with compact support, integration by parts twice gives, for $z\ne0$,
$$
\widehat f(z)
=\frac1{(2\pi iz)^2}
\int_{-R}^{R}f''(t)e^{-2\pi izt}\,dt.
\tag{1}
$$
If $z=x+iy$ and $\abs{y}\le a$, then
$$
\abs{e^{-2\pi izt}}=e^{2\pi yt}\le e^{2\pi aR}.
$$
Hence for $\abs{x}\ge1$,
$$
\abs{\widehat f(x+iy)}
\le \frac{e^{2\pi aR}\norm{f''}_1}{4\pi^2\abs{x+iy}^2}
\le \frac{C_a}{x^2}.
$$
For $\abs{x}\le1$, the original integral gives the uniform bound
$$
\abs{\widehat f(x+iy)}\le e^{2\pi aR}\norm{f}_1.
$$
Combining the two estimates yields
$$
\abs{\widehat f(x+iy)}\le \frac{A_a}{1+x^2}
\qquad(\abs{y}\le a).
\tag{2}
$$

For (b), assuming the differential operator is nonzero, $P$ is a nonzero polynomial and therefore has finitely many roots. Choose any real number $c$ that is not the imaginary part of any root of $P$. Then
$$
L=\{x+ic:x\in\RR\}
$$
contains no zero of $P$.

For (c), parametrize $L$ by $z=x+ic$. The estimate (2), together with polynomial growth of $P$, shows that
$$
u(t)=\int_L\frac{e^{2\pi izt}}{P(z)}\widehat f(z)\,dz
$$
converges absolutely. Moreover, differentiating $j\le n$ times multiplies the integrand by $(2\pi iz)^j$; after division by the degree-$n$ polynomial $P(z)$ and multiplication by the $O(x^{-2})$ factor $\widehat f(z)$, the resulting integrand is still absolutely integrable. Thus differentiation under the integral sign is justified and
$$
\begin{aligned}
\sum_{j=0}^n a_j\left(\frac d{dt}\right)^j u(t)
&=\int_L
\frac{\sum_{j=0}^n a_j(2\pi iz)^j}{P(z)}
e^{2\pi izt}\widehat f(z)\,dz\\
&=\int_L e^{2\pi izt}\widehat f(z)\,dz.
\end{aligned}
\tag{3}
$$

It remains to move $L$ to the real axis. The integrand in (3) is entire. On the vertical sides of the rectangle joining $[-N,N]$ to $[-N+ic,N+ic]$, estimate (2) uniformly for imaginary parts between $0$ and $c$; for fixed $t$ the exponential factor is also uniformly bounded there. Hence each vertical-side integral is $O(N^{-2})$ and tends to $0$. Cauchy's theorem therefore gives
$$
\int_L e^{2\pi izt}\widehat f(z)\,dz
=\int_{-\infty}^{\infty}e^{2\pi ixt}\widehat f(x)\,dx.
\tag{4}
$$
Since $f$ is compactly supported and $C^2$, Fourier inversion applies to the right side of (4), giving $f(t)$. Combining (3) and (4),
$$
\boxed{
\sum_{j=0}^n a_j\left(\frac d{dt}\right)^j u(t)=f(t)}.
$$
Thus the displayed contour integral gives a solution of the original constant-coefficient ODE. Its form depends on the chosen horizontal line $L$, equivalently on $c$.
:::
