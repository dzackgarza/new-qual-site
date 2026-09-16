---
schema: qual/card@1
id: P-FBOFF
kind: problem
title: Dense values near an accumulation point of poles, versus Casorati–Weierstrass
classification:
  areas:
  - complex-analysis
  topics:
  - Casorati-Weierstrass
  - Poles
  - Singularities
  - Meromorphic Functions
relations: []
review: draft
---

::: {.problem}
(1) Let $f$ be analytic in $\Omega: 0<|z-a|<r$ except at a sequence of poles $a_n \in \Omega$ with $\lim_{n \rightarrow \infty} a_n = a$.
Show that for any $w \in \mathbb C$, there exists a sequence $z_n \in \Omega$ such that $\lim_{n \rightarrow \infty} f(z_n) = w$.

(2) Explain the similarity and difference between the above assertion and the Weierstrass-Casorati theorem.
:::

::: {.solution}
(1) Fix $w\in\mathbb C$. For each pole $a_n$, the function
\[
h_n(z)=\frac{1}{f(z)-w}
\]
is holomorphic in a punctured neighborhood of $a_n$ and has a removable
singularity there with value $0$. Since $h_n$ is nonconstant, the open mapping
theorem implies that every sufficiently small neighborhood of $a_n$ contains
points where $h_n$ takes arbitrarily small nonzero values. Equivalently, in
every sufficiently small neighborhood of $a_n$, the values of $f$ come
arbitrarily close to $w$.

Choose $z_n$ so close to $a_n$ that
\[
|z_n-a_n|<\frac1n,
\qquad |f(z_n)-w|<\frac1n.
\]
Since $a_n\to a$, we also have $z_n\to a$, and by construction
$f(z_n)\to w$.

(2) The conclusion resembles Casorati--Weierstrass: near the distinguished
point $a$, the image is dense in $\mathbb C$. The difference is structural.
Casorati--Weierstrass concerns a single isolated essential singularity at $a$.
Here $a$ need not even be an isolated singularity of $f$; instead, $a$ is an
accumulation point of poles, and the density conclusion is forced by the local
behavior near those poles together with their accumulation at $a$.
:::
