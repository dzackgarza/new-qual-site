---
schema: qual/card@1
id: P-WCDZA
kind: problem
title: Riemann-Lebesgue lemma and convolution identity
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved JHU May 2013 Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

(a) Prove the Riemann-Lebesgue Lemma: if $f \in L^1(\mathbb{R}^d)$, then the Fourier transform of $f$,

$$\hat{f}(\xi) = \int_{\mathbb{R}^d} f(x) e^{-2\pi i x \cdot \xi} \, dx \to 0, \quad \text{as } |\xi| \to \infty.$$

(b) Use part (a) to justify whether there exists a function $h \in L^1(\mathbb{R}^d)$ such that

$$f * h = f \quad \text{for all } f \in L^1(\mathbb{R}^d).$$

Here $f * h$ is the convolution of $f$ and $h$ defined by

$$(f * h)(x) = \int_{\mathbb{R}^d} f(x - y) h(y) \, dy.$$

::: {.solution}
<1>1. Prove the Riemann--Lebesgue lemma for $C_c^1$ functions.
::: {.proof}
Let $\varphi\in C_c^1(\mathbb R^d)$. For $\xi\ne0$, choose an index $j$ such that
\[
|\xi_j|\ge \frac{|\xi|}{\sqrt d}.
\]
Integration by parts in the $x_j$ variable gives
\[
\widehat\varphi(\xi)
=\frac{1}{2\pi i\xi_j}
\int_{\mathbb R^d}\partial_j\varphi(x)e^{-2\pi i x\cdot\xi}\,dx.
\]
Therefore
\[
|\widehat\varphi(\xi)|
\le \frac{\sqrt d}{2\pi|\xi|}\,\|\partial_j\varphi\|_1
\le \frac{\sqrt d}{2\pi|\xi|}
\sum_{k=1}^d\|\partial_k\varphi\|_1.
\]
Hence
\[
\widehat\varphi(\xi)\to0
\qquad(|\xi|\to\infty).
\]
:::

<1>2. Extend the result to every $f\in L^1(\mathbb R^d)$.
::: {.proof}
Fix $\varepsilon>0$. Since $C_c^1(\mathbb R^d)$ is dense in $L^1(\mathbb R^d)$, choose $\varphi\in C_c^1$ such that
\[
\|f-\varphi\|_1<\varepsilon.
\]
For every $\xi$,
\[
|\widehat f(\xi)-\widehat\varphi(\xi)|
\le \|f-\varphi\|_1<\varepsilon.
\]
By Step 1, $|\widehat\varphi(\xi)|<\varepsilon$ for all sufficiently large $|\xi|$. Thus
\[
|\widehat f(\xi)|<2\varepsilon
\]
for all sufficiently large $|\xi|$. Since $\varepsilon$ is arbitrary,
\[
\boxed{\widehat f(\xi)\to0\quad\text{as }|\xi|\to\infty.}
\]
:::

<1>3. Show that no $L^1$ convolution identity exists.
::: {.proof}
Suppose $h\in L^1(\mathbb R^d)$ satisfied
\[
f*h=f
\qquad\text{for every }f\in L^1(\mathbb R^d).
\]
Taking Fourier transforms gives
\[
\widehat f(\xi)\widehat h(\xi)=\widehat f(\xi)
\]
for every $f$ and every $\xi$.

Take the Gaussian
\[
f(x)=e^{-\pi|x|^2},
\]
whose Fourier transform is itself and is strictly positive everywhere. Hence
\[
\widehat h(\xi)=1
\qquad\text{for every }\xi\in\mathbb R^d.
\]
But Step 2 applied to $h\in L^1$ gives
\[
\widehat h(\xi)\to0
\qquad(|\xi|\to\infty),
\]
a contradiction. Therefore no such $h\in L^1(\mathbb R^d)$ exists.
:::
:::
