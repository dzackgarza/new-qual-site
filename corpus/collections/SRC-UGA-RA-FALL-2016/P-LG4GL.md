---
schema: qual/card@1
id: P-LG4GL
kind: problem
title: $\left(\int\frac{|\phi|^n}{1+x^2}\,dx\right)^{1/n}\to\|\phi\|_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Lp Spaces
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UGA August 2016 real-analysis qualifying exam; normalized the weighted finite-measure Lp-to-Linfinity argument.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $\phi\in L^\infty(\RR)$. Show that the following limit exists and satisfies the equality
\[
\lim _{n \to \infty} \left(\int _{\mathbb{R}} \frac{|\phi(x)|^{n}}{1+x^{2}} \, dx \right) ^ {\frac{1}{n}} 
= \norm{\phi}_\infty.
\]

::: solution

Put
\[
M:=\|\phi\|_\infty,
\qquad
A_n:=\left(\int_{\mathbb R}\frac{|\phi(x)|^n}{1+x^2}\,dx\right)^{1/n}.
\]
If $M=0$, then $\phi=0$ a.e. and $A_n=0$ for every $n$. Assume $M>0$.

Since $|\phi|\le M$ a.e.,
\[
A_n^n\le M^n\int_{\mathbb R}\frac{dx}{1+x^2}=\pi M^n,
\]
so
\[
\limsup_{n\to\infty}A_n\le M.
\]

Now fix $0<\varepsilon<M$ and let
\[
E_\varepsilon:=\{x:|\phi(x)|>M-\varepsilon\}.
\]
By the definition of essential supremum, $m(E_\varepsilon)>0$. Since $(1+x^2)^{-1}>0$ everywhere,
\[
c_\varepsilon:=\int_{E_\varepsilon}\frac{dx}{1+x^2}>0.
\]
Therefore
\[
A_n^n\ge (M-\varepsilon)^n c_\varepsilon,
\]
and hence
\[
A_n\ge (M-\varepsilon)c_\varepsilon^{1/n}.
\]
Letting $n\to\infty$ gives
\[
\liminf_{n\to\infty}A_n\ge M-\varepsilon.
\]
Since $\varepsilon>0$ is arbitrary,
\[
\liminf_{n\to\infty}A_n\ge M.
\]
Together with the upper bound,
\[
\boxed{\lim_{n\to\infty}A_n=\|\phi\|_\infty.}
\]
:::
