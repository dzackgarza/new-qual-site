---
schema: qual/card@1
id: E-SS4.EX-3
kind: problem
title: "SS 4.3: The Poisson kernel as a Fourier transform pair"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 notation and exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
3. Show, by contour integration, that if $a > 0$ and $\xi \in \mathbb { R }$ then

$$
\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {a}{a ^ {2} + x ^ {2}} e ^ {- 2 \pi i x \xi} d x = e ^ {- 2 \pi a | \xi |},
$$

and check that

$$
\int_ {- \infty} ^ {\infty} e ^ {- 2 \pi a | \xi |} e ^ {2 \pi i \xi x} d \xi = \frac {1}{\pi} \frac {a}{a ^ {2} + x ^ {2}}.
$$
:::

::: {.solution}
Let
\[
I(\xi)=\int_{-\infty}^{\infty}\frac{a}{a^2+x^2}e^{-2\pi i x\xi}\,dx.
\]
For $\xi>0$, close the contour in the lower half-plane. Since
\[
|e^{-2\pi i z\xi}|=e^{2\pi \xi\Im z},
\]
the exponential decays there, and the semicircular contribution tends to $0$. The contour is clockwise and contains only the pole $z=-ia$. Its residue is
\[
\operatorname{Res}_{z=-ia}
\frac{a e^{-2\pi i z\xi}}{(z-ia)(z+ia)}
=\frac{a e^{-2\pi a\xi}}{-2ia}
=-\frac{e^{-2\pi a\xi}}{2i}.
\]
Hence
\[
I(\xi)=-2\pi i\left(-\frac{e^{-2\pi a\xi}}{2i}\right)
=\pi e^{-2\pi a\xi}.
\]
For $\xi<0$, close in the upper half-plane; the pole at $ia$ gives
\[
I(\xi)=\pi e^{2\pi a\xi}.
\]
At $\xi=0$, direct integration gives $I(0)=\pi$. Therefore
\[
\frac1\pi I(\xi)=e^{-2\pi a|\xi|}.
\]

For the inverse transform, split at $0$:
\[
\begin{aligned}
\int_{-\infty}^{\infty}e^{-2\pi a|\xi|}e^{2\pi i\xi x}\,d\xi
&=\int_0^\infty e^{-2\pi(a-ix)\xi}\,d\xi
 +\int_0^\infty e^{-2\pi(a+ix)\xi}\,d\xi\\
&=\frac1{2\pi(a-ix)}+\frac1{2\pi(a+ix)}\\
&=\frac1\pi\frac{a}{a^2+x^2}.
\end{aligned}
\]
:::
