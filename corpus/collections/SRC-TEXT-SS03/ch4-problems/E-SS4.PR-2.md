---
schema: qual/card@1
id: E-SS4.PR-2
kind: problem
title: "SS 4.PR-2: Solving a linear ODE with the Fourier transform"
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
2. The problem is to solve the diferential equation

$$
a _ {n} \frac {d ^ {n}}{d t ^ {n}} u (t) + a _ {n - 1} \frac {d ^ {n - 1}}{d t ^ {n - 1}} u (t) + \dots + a _ {0} u (t) = f (t),
$$

where $a _ { 0 } , a _ { 1 } , \ldots , a _ { n }$ are complex constants, and $f$ is a given function.
Here we suppose that $f$ has bounded support and is smooth (say of class $C ^ { 2 } )$

(a) Let

$$
\hat {f} (z) = \int_ {- \infty} ^ {\infty} f (t) e ^ {- 2 \pi i z t} d t.
$$

Observe that $\hat { f }$ is an entire function, and using integration by parts show that

$$
| \hat {f} (x + i y) | \leq \frac {A}{1 + x ^ {2}}
$$

if $| y | \le a$ for any fixed $a \geq 0$

(b) Write

$$
P (z) = a _ {n} (2 \pi i z) ^ {n} + a _ {n - 1} (2 \pi i z) ^ {n - 1} + \dots + a _ {0}.
$$

Find a real number c so that $P ( z )$ does not vanish on the line

$$
L = \{z: z = x + i c, x \in \mathbb {R} \}.
$$

(c) Set

$$
u (t) = \int_ {L} \frac {e ^ {2 \pi i z t}}{P (z)} \hat {f} (z) d z.
$$

Check that

$$
\sum_{j=0}^n a_j\left(\frac{d}{dt}\right)^j u(t)
=\int_L e^{2\pi i zt}\hat f(z)\,dz
$$

and

$$
\int_L e^{2\pi i zt}\hat f(z)\,dz
=\int_{-\infty}^{\infty}e^{2\pi ixt}\hat f(x)\,dx.
$$

Conclude by the Fourier inversion theorem that

$$
\sum_{j=0}^n a_j\left(\frac{d}{dt}\right)^j u(t)=f(t).
$$
:::

::: {.solution}
Let the support of $f$ be contained in $[-R,R]$.

For (a), since the defining integral is over a compact interval and its integrand is entire in $z$, differentiation under the integral sign shows that $\widehat f$ is entire. Because $f$ is $C^2$ with compact support, integration by parts twice gives, for $z\ne0$,
\[
\widehat f(z)
=\frac1{(2\pi iz)^2}
\int_{-R}^{R}f''(t)e^{-2\pi izt}\,dt.
\tag{1}
\]
If $z=x+iy$ and $|y|\le a$, then
\[
|e^{-2\pi izt}|=e^{2\pi yt}\le e^{2\pi aR}.
\]
Hence for $|x|\ge1$,
\[
|\widehat f(x+iy)|
\le \frac{e^{2\pi aR}\|f''\|_1}{4\pi^2|x+iy|^2}
\le \frac{C_a}{x^2}.
\]
For $|x|\le1$, the original integral gives the uniform bound
\[
|\widehat f(x+iy)|\le e^{2\pi aR}\|f\|_1.
\]
Combining the two estimates yields
\[
|\widehat f(x+iy)|\le \frac{A_a}{1+x^2}
\qquad(|y|\le a).
\tag{2}
\]

For (b), assuming the differential operator is nonzero, $P$ is a nonzero polynomial and therefore has finitely many roots. Choose any real number $c$ that is not the imaginary part of any root of $P$. Then
\[
L=\{x+ic:x\in\mathbb R\}
\]
contains no zero of $P$.

For (c), parametrize $L$ by $z=x+ic$. The estimate (2), together with polynomial growth of $P$, shows that
\[
u(t)=\int_L\frac{e^{2\pi izt}}{P(z)}\widehat f(z)\,dz
\]
converges absolutely. Moreover, differentiating $j\le n$ times multiplies the integrand by $(2\pi iz)^j$; after division by the degree-$n$ polynomial $P(z)$ and multiplication by the $O(x^{-2})$ factor $\widehat f(z)$, the resulting integrand is still absolutely integrable. Thus differentiation under the integral sign is justified and
\[
\begin{aligned}
\sum_{j=0}^n a_j\left(\frac d{dt}\right)^j u(t)
&=\int_L
\frac{\sum_{j=0}^n a_j(2\pi iz)^j}{P(z)}
e^{2\pi izt}\widehat f(z)\,dz\\
&=\int_L e^{2\pi izt}\widehat f(z)\,dz.
\end{aligned}
\tag{3}
\]

It remains to move $L$ to the real axis. The integrand in (3) is entire. On the vertical sides of the rectangle joining $[-N,N]$ to $[-N+ic,N+ic]$, estimate (2) uniformly for imaginary parts between $0$ and $c$; for fixed $t$ the exponential factor is also uniformly bounded there. Hence each vertical-side integral is $O(N^{-2})$ and tends to $0$. Cauchy's theorem therefore gives
\[
\int_L e^{2\pi izt}\widehat f(z)\,dz
=\int_{-\infty}^{\infty}e^{2\pi ixt}\widehat f(x)\,dx.
\tag{4}
\]
Since $f$ is compactly supported and $C^2$, Fourier inversion applies to the right side of (4), giving $f(t)$. Combining (3) and (4),
\[
\boxed{
\sum_{j=0}^n a_j\left(\frac d{dt}\right)^j u(t)=f(t)}.
\]
Thus the displayed contour integral gives a solution of the original constant-coefficient ODE. Its form depends on the chosen horizontal line $L$, equivalently on $c$.
:::
