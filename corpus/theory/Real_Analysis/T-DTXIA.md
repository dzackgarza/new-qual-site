---
schema: qual/card@1
id: T-DTXIA
kind: theorem
title: Fourier Inversion
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
---

::: {.theorem}
Use the convention
\[
\widehat f(\xi)=\int_{\mathbb R^n}f(x)e^{-2\pi i x\cdot\xi}\,dx.
\]
If $f\in L^1(\mathbb R^n)$ and $\widehat f\in L^1(\mathbb R^n)$, then
\[
F(x):=\int_{\mathbb R^n}\widehat f(\xi)e^{2\pi i x\cdot\xi}\,d\xi
\]
defines a bounded continuous function and
\[
F(x)=f(x)
\]
for almost every $x$. More precisely, equality holds at every Lebesgue point of $f$; in particular, if $f$ is continuous then it holds for every $x$.
:::

::: {.proof}
Since $\widehat f\in L^1$, dominated convergence immediately shows that $F$ is bounded and continuous.

For $t>0$, set
\[
G_t(x)=t^{-n}e^{-\pi |x|^2/t^2}.
\]
The normalized Gaussian satisfies
\[
\widehat{G_t}(\xi)=e^{-\pi t^2|\xi|^2}.
\]
Indeed, in one dimension the function
\[
H(\xi)=\int_{\mathbb R}e^{-\pi x^2}e^{-2\pi i x\xi}\,dx
\]
satisfies, by differentiation under the integral sign and integration by parts,
\[
H'(\xi)=-2\pi\xi H(\xi),
\qquad H(0)=1,
\]
so $H(\xi)=e^{-\pi\xi^2}$. The $n$-dimensional identity follows by Fubini, and the formula for $G_t$ follows by scaling.

Fix $x\in\mathbb R^n$. By Fubini's theorem,
\[
\begin{aligned}
\int_{\mathbb R^n}\widehat f(\xi)
 e^{2\pi i x\cdot\xi}e^{-\pi t^2|\xi|^2}\,d\xi
&=\int_{\mathbb R^n}f(y)
 \left(\int_{\mathbb R^n}e^{-2\pi i(y-x)\cdot\xi}
 e^{-\pi t^2|\xi|^2}\,d\xi\right)dy\\
&=\int_{\mathbb R^n}f(y)G_t(x-y)\,dy\\
&=(f*G_t)(x).
\end{aligned}
\]
The use of Fubini is justified because
\[
\int\!\int |f(y)|e^{-\pi t^2|\xi|^2}\,d\xi\,dy<\infty.
\]

As $t\downarrow0$, dominated convergence on the left, with dominating function $|\widehat f|$, gives
\[
\int\widehat f(\xi)e^{2\pi i x\cdot\xi}e^{-\pi t^2|\xi|^2}\,d\xi
\longrightarrow F(x).
\]
On the right, $(G_t)_{t>0}$ is an approximate identity: $G_t\ge0$, $\int G_t=1$, and for every $\delta>0$,
\[
\int_{|y|>\delta}G_t(y)\,dy\longrightarrow0.
\]
Hence the Lebesgue differentiation theorem gives
\[
(f*G_t)(x)\longrightarrow f(x)
\]
at every Lebesgue point of $f$. Therefore $F(x)=f(x)$ at every Lebesgue point, and almost every point of an $L^1$ function is a Lebesgue point.

If $f$ is continuous, the usual approximate-identity argument gives $(f*G_t)(x)\to f(x)$ at every $x$, so inversion holds pointwise everywhere.
:::
