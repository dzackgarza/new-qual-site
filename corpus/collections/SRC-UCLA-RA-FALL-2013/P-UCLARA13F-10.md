---
schema: qual/card@1
id: P-UCLARA13F-10
kind: problem
title: Fourier transforms and self-convolutions of L2 functions
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
(a) Let $f\in L^2(\mathbb R)$ and define
\[
h(x)=\int_{\mathbb R}f(x-y)f(y)\,dy.
\]
Show that there exists $g\in L^1(\mathbb R)$ such that
\[
h(\xi)=\int_{\mathbb R}e^{-i\xi x}g(x)\,dx.
\]

(b) Conversely, show that if $g\in L^1(\mathbb R)$, then there exists $f\in L^2(\mathbb R)$ whose self-convolution
\[
h(x)=\int_{\mathbb R}f(x-y)f(y)\,dy
\]
is the Fourier transform of $g$.
:::

Use the Fourier-transform convention
\[
\widehat q(\xi)=\int_{\mathbb R}e^{-i\xi x}q(x)\,dx.
\]
With this convention, Plancherel extends the Fourier transform to $L^2(\mathbb R)$ and
\[
\widehat{f*f}=\widehat f^{,2}.
\]

::: pf

::: pf-step

Let $f\in L^2(\mathbb R)$. For every $x\in\mathbb R$, the self-convolution
\[
h(x)=\int_{\mathbb R}f(x-y)f(y)\,dy
\]
is absolutely convergent.


::: pf-proof

Translation preserves the $L^2$ norm. Hence Cauchy--Schwarz gives
\[
\int_{\mathbb R}|f(x-y)f(y)|\,dy
\leq\|f(x-\cdot)\|_2\|f\|_2
=\|f\|_2^2<\infty.
\]

:::

:::

::: pf-step

Let
\[
F=\widehat f
\]
in the $L^2$ Plancherel sense. Then
\[
F^2\in L^1(\mathbb R).
\]


::: pf-proof

Plancherel gives $F\in L^2$. Therefore
\[
\int_{\mathbb R}|F(\xi)^2|\,d\xi
=\int_{\mathbb R}|F(\xi)|^2\,d\xi<\infty.
\]

:::

:::

::: pf-step

The convolution theorem gives, with the stated normalization,
\[
h(x)=\frac1{2\pi}\int_{\mathbb R}e^{ix\xi}F(\xi)^2\,d\xi.
\]


::: pf-proof

First prove the identity for approximations $f_j\in L^1\cap L^2$ converging to $f$ in $L^2$. For such $f_j$, the usual convolution theorem and Fourier inversion apply. Moreover,
\[
\|f_j*f_j-f*f\|_\infty
\leq(\|f_j\|_2+\|f\|_2)\|f_j-f\|_2\to0
\]
by Cauchy--Schwarz, while Plancherel gives $F_j\to F$ in $L^2$ and hence
\[
\|F_j^2-F^2\|_1
\leq(\|F_j\|_2+\|F\|_2)\|F_j-F\|_2\to0.
\]
Passing to the limit in the inversion formula yields the displayed identity.

:::

:::

::: pf-step

Define
\[
g(t)=\frac1{2\pi}F(-t)^2.
\]
Then $g\in L^1(\mathbb R)$ and
\[
h(x)=\widehat g(x).
\]


::: pf-proof

Integrability follows from step <1>2. Substituting $t=-\xi$ in step <1>3 gives
\[
h(x)=\frac1{2\pi}\int_{\mathbb R}e^{-ixt}F(-t)^2\,dt
=\int_{\mathbb R}e^{-ixt}g(t)\,dt.
\]
This proves part (a).

:::

:::

::: pf-step

Conversely, let $g\in L^1(\mathbb R)$. There exists a measurable function $F$ such that
\[
F(-t)^2=2\pi g(t)
\]
for almost every $t$ and
\[
F\in L^2(\mathbb R).
\]


::: pf-proof

Choose a measurable square root of the complex-valued function $2\pi g(t)$ and define
\[
F(-t)=\sqrt{2\pi g(t)}.
\]
Then
\[
|F(-t)|^2=2\pi|g(t)|,
\]
so
\[
\|F\|_2^2=2\pi\|g\|_1<\infty.
\]

:::

:::

::: pf-step

By Plancherel, there exists $f\in L^2(\mathbb R)$ whose Fourier transform is $F$.


::: pf-proof

The Fourier transform, with the corresponding normalization factor, is a bijective isometry up to the fixed constant on $L^2(\mathbb R)$. Since $F\in L^2$ by step <1>5, it has an inverse Fourier transform $f\in L^2$.

:::

:::

::: pf-step

The self-convolution $h=f*f$ satisfies
\[
h(x)=\widehat g(x).
\]


::: pf-proof

Apply step <1>3 to the $f$ from step <1>6:
\[
h(x)=\frac1{2\pi}\int_{\mathbb R}e^{ix\xi}F(\xi)^2\,d\xi.
\]
Set $t=-\xi$ and use step <1>5:
\[
h(x)=\frac1{2\pi}\int_{\mathbb R}e^{-ixt}F(-t)^2\,dt
=\int_{\mathbb R}e^{-ixt}g(t)\,dt
=\widehat g(x).
\]

:::

:::

::: pf-step

Thus both implications hold.


::: pf-proof

Step <1>4 proves part (a), and steps <1>5--<1>7 prove part (b).

:::

:::

::: pf-qed

Step <1>8 proves the two requested statements.

:::

:::
