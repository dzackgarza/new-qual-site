---
schema: qual/card@1
id: P-UCLARA17S-05
kind: problem
title: Decay of Fourier coefficients passes to absolutely continuous measures
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $d\mu$ be a finite complex Borel measure on $[0,1]$ such that
\[
\widehat\mu(n)=\int_0^1 e^{2\pi i n x}\,d\mu(x)\to0\qquad(n\to\infty).
\]
Let $d\nu$ be a finite complex Borel measure on $[0,1]$ absolutely continuous with respect to $d\mu$. Show that
\[
\widehat\nu(n)\to0\qquad(n\to\infty).
\]
:::

::: pf

::: {.pf-step #s1-1}

The assertion is false as written for complex measures on the closed interval $[0,1]$.


::: pf-proof

Let
$$
\mu\coloneqq\delta_0-\delta_1.
$$
Then for every integer $n$,
$$
\widehat\mu(n)
=\int_0^1 e^{2\pi i n x}\,d\mu(x)
=1-e^{2\pi i n}
=0.
$$
Now let
$$
f(x)\coloneqq1-x
$$
and define $\nu$ by $d\nu=f\,d\mu$. Since $f(0)=1$ and $f(1)=0$,
$$
\nu=\delta_0.
$$
Thus $\nu$ is absolutely continuous with respect to $\mu$ even in the density sense used by the retained source solution, but
$$
\widehat\nu(n)=1
$$
for every integer $n$. Hence the printed conclusion fails.

:::

:::

::: pf-step

The failure in step [](#s1-1){.pf-ref} comes from the fact that the characters
$$
x\longmapsto e^{2\pi i n x}
$$
identify the two distinct endpoints $0$ and $1$.


::: pf-proof

For every integer $n$,
$$
e^{2\pi i n\cdot0}=e^{2\pi i n\cdot1}=1.
$$
Thus the Fourier coefficients cannot distinguish $\delta_0$ from $\delta_1$, which is exactly the cancellation used in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The intended statement is true on the circle $\mathbb T=\RR/\ZZ$ (equivalently on the half-open interval $[0,1)$): if $\mu$ is a finite complex Borel measure on $\mathbb T$ with
$$
\widehat\mu(n)\to0
\qquad(n\to\infty)
$$
and $\nu\ll\mu$, then
$$
\boxed{\widehat\nu(n)\to0}.
$$


::: pf-proof

By the Radon--Nikodym theorem for complex measures, write
$$
d\nu=f\,d\mu
$$
with $f\in L^1(|\mu|)$. Let $\varepsilon>0$. Continuous functions are dense in $L^1(|\mu|)$ on the compact metric space $\mathbb T$, and trigonometric polynomials are uniformly dense in $C(\mathbb T)$ by the Stone--Weierstrass theorem. Hence there is a trigonometric polynomial
$$
P(x)=\sum_{m=-N}^N c_m e^{2\pi i m x}
$$
such that
$$
\int_{\mathbb T}|f-P|\,d|\mu|<\varepsilon.
$$
For every $n$,
$$
\begin{aligned}
\left|\widehat\nu(n)-\int_{\mathbb T}e^{2\pi i n x}P(x)\,d\mu(x)\right|
&=\left|\int_{\mathbb T}e^{2\pi i n x}(f-P)\,d\mu\right|\\
&\le\int_{\mathbb T}|f-P|\,d|\mu|\\
&<\varepsilon.
\end{aligned}
$$
Moreover,
$$
\int_{\mathbb T}e^{2\pi i n x}P(x)\,d\mu(x)
=\sum_{m=-N}^N c_m\widehat\mu(n+m)
\longrightarrow0,
$$
because each $n+m\to\infty$ as $n\to\infty$ and the sum is finite. Therefore
$$
\limsup_{n\to\infty}|\widehat\nu(n)|\le\varepsilon.
$$
Since $\varepsilon>0$ is arbitrary, $\widehat\nu(n)\to0$.

The same proof applies on $[0,1)$ after identifying it Borel-isomorphically with $\mathbb T$ by $x\mapsto e^{2\pi i x}$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} refutes the literal source statement, and step [](#s1-3){.pf-ref} proves the corrected periodic version that the retained source solution attempts to use.

:::

:::
