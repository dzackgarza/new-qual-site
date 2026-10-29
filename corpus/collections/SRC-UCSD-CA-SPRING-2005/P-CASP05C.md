---
schema: qual/card@1
id: P-CASP05C
kind: problem
title: "Schwarz lemma variants: identity for simply connected and bounded domains"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $G \subset \CC$ be a connected open set with $0 \in G$, and $f \in H(G)$, with $f(0) = 0$, $f'(0) = 1$ and $f(G) \subset G$.

(a) Show that if $G \neq \CC$ and $G$ is simply connected (not necessarily bounded) then $f(z) \equiv z$.
Does the same conclusion hold for $G = \CC$?

(b) Show that if $G$ is bounded (not necessarily simply connected) then $f(z) \equiv z$.

Hint for (b): Prove by contradiction.
Consider the $n$th iterate $f_n := f \circ f \circ \cdots \circ f$ ($n$ times), and compute the first non-vanishing coefficient of the Taylor series of $f_n(z) - z$ at 0 in terms of that of $f(z) - z$.
:::

::: {.solution}
For (a), assume first that $G\ne\CC$ is simply connected. By the Riemann
mapping theorem there is a conformal map $\phi:G\to\DD$; composing with a
disk automorphism, arrange $\phi(0)=0$. Then
$$
F=\phi\circ f\circ\phi^{-1}:\DD\to\DD
$$
fixes $0$, and the chain rule gives $F'(0)=f'(0)=1$. Schwarz's lemma and its
equality case imply $F(z)=z$, hence $f(z)=z$ on $G$.

For $G=\CC$ the conclusion need not hold: for example
$f(z)=z+z^2$ satisfies $f(0)=0$ and $f'(0)=1$ and maps $\CC$ into itself,
but is not the identity.

For (b), suppose $G$ is bounded and $f$ is not the identity. Write near $0$
$$
f(z)=z+a_mz^m+O(z^{m+1}),
\qquad m\ge2,\quad a_m\ne0.
$$
An induction under composition gives
$$
f^{\circ n}(z)=z+n a_m z^m+O(z^{m+1}).
$$
Choose $r>0$ with $\overline{D(0,r)}\subset G$. Since $G$ is bounded, there is
$M$ with $|w|\le M$ for every $w\in G$. Every iterate maps $G$ into $G$, so
$$
|f^{\circ n}(z)|\le M\qquad(|z|\le r).
$$
Cauchy's estimate therefore bounds the coefficient of $z^m$ in every iterate
by $M/r^m$, independently of $n$. But that coefficient is $n a_m$, a
contradiction as $n\to\infty$. Hence $f$ is the identity.
:::
