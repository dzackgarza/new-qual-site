---
schema: qual/card@1
id: T-DTXIA
kind: theorem
title: Fourier inversion
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
---

::: {.theorem}
Let $f\in L^1(\RR^n)$, and suppose its [[D-5LZQ4|Fourier transform]] $\widehat f(\xi)=\int_{\RR^n}f(x)e^{-2\pi i x\cdot\xi}\,dx$ also lies in $L^1(\RR^n)$.
Then
$$
F(x)\coloneqq\int_{\RR^n}\widehat f(\xi)e^{2\pi i x\cdot\xi}\,d\xi
$$
defines a bounded continuous function $F\colon\RR^n\to\CC$, and $F(x)=f(x)$ for almost every $x\in\RR^n$.
More precisely, $F(x)=f(x)$ at every Lebesgue point $x$ of $f$, that is, every $x$ with
$$
\lim_{r\to0^+}\frac{1}{m(B_r(x))}\int_{B_r(x)}\abs{f(y)-f(x)}\,dy=0 ;
$$
in particular, $F(x)=f(x)$ at every point $x$ at which $f$ is continuous.
:::

::: {.proof}
Since $\abs{\widehat f(\xi)e^{2\pi ix\cdot\xi}}=\abs{\widehat f(\xi)}$ and $\widehat f\in L^1$, the bound $\abs{F(x)}\leq\norm{\widehat f}_1$ holds and dominated convergence shows that $F$ is continuous.

For $t>0$, set
$$
G_t(x)\coloneqq t^{-n}e^{-\pi \abs{x}^2/t^2}.
$$
Its Fourier transform is
$$
\widehat{G_t}(\xi)=e^{-\pi t^2\abs{\xi}^2}.
$$
Indeed, in one dimension the function
$$
H(\xi)\coloneqq\int_{\RR}e^{-\pi x^2}e^{-2\pi i x\xi}\,dx
$$
satisfies, by differentiation under the integral sign and integration by parts,
$$
H'(\xi)=-2\pi\xi H(\xi),
\qquad H(0)=1,
$$
so $H(\xi)=e^{-\pi\xi^2}$.
The $n$-dimensional identity follows by Fubini's theorem, since $e^{-\pi\abs{x}^2}=\prod_{j=1}^ne^{-\pi x_j^2}$, and the formula for $G_t$ follows by the substitution $x=ty$.
Since $G_t$ is even, the same computation gives $\int_{\RR^n}e^{2\pi i w\cdot\xi}e^{-\pi t^2\abs{\xi}^2}\,d\xi=G_t(w)$ for $w\in\RR^n$.

Fix $x\in\RR^n$. By Fubini's theorem [[T-4GPEF]],
$$
\begin{aligned}
\int_{\RR^n}\widehat f(\xi)
 e^{2\pi i x\cdot\xi}e^{-\pi t^2\abs{\xi}^2}\,d\xi
&=\int_{\RR^n}f(y)
 \qty{\int_{\RR^n}e^{2\pi i(x-y)\cdot\xi}
 e^{-\pi t^2\abs{\xi}^2}\,d\xi}dy\\
&=\int_{\RR^n}f(y)G_t(x-y)\,dy\\
&=(f*G_t)(x).
\end{aligned}
$$
Fubini's theorem applies because
$$
\int_{\RR^n}\int_{\RR^n} \abs{f(y)}e^{-\pi t^2\abs{\xi}^2}\,d\xi\,dy=\norm{f}_1\,t^{-n}<\infty.
$$

As $t\to0^+$, dominated convergence on the left, with dominating function $\abs{\widehat f}$, gives
$$
\int_{\RR^n}\widehat f(\xi)e^{2\pi i x\cdot\xi}e^{-\pi t^2\abs{\xi}^2}\,d\xi
\longrightarrow F(x).
$$
On the right, $G_t(y)=t^{-n}G_1(y/t)$, where $G_1\geq0$ has $\int G_1=1$ and is radial and decreasing in $\abs{y}$, so $(G_t)_{t>0}$ is an [[D-ARQFC|approximate identity]] with a radially decreasing integrable majorant.
For such a family, $(f*G_t)(x)\to f(x)$ as $t\to0^+$ at every Lebesgue point $x$ of $f$.
Therefore $F(x)=f(x)$ at every Lebesgue point of $f$.
By the Lebesgue differentiation theorem, almost every point of $\RR^n$ is a Lebesgue point of $f$, and every point of continuity of $f$ is a Lebesgue point.
:::
