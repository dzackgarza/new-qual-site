---
schema: qual/card@1
id: P-CASP22A
kind: problem
title: "Analytic self-map of a bounded simply connected region fixing a point with derivative 1 is the identity"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Holomorphic Functions
  - Fixed Points
relations: []
review: draft
---

::: {.problem}
Let $G \subset \mathbb{C}$ be a bounded, simply connected region and let $a \in G$.
Let $f$ be an analytic self-map of $G$ (i.e., $f(G) \subset G$) such that $f(a) = a$ and $f'(a) = 1$.
Show that $f(z) = z$.
:::

::: {.solution}
By the Riemann mapping theorem choose a biholomorphism
\[
\phi:G\to\mathbb D
\]
with $\phi(a)=0$. Set
\[
F=\phi\circ f\circ\phi^{-1}.
\]
Then $F:\mathbb D\to\mathbb D$ is holomorphic, $F(0)=0$, and by the chain
rule
\[
F'(0)=f'(a)=1.
\]
Schwarz's lemma gives $|F(z)|\le|z|$, and equality in the derivative bound
$|F'(0)|\le1$ forces
\[
F(z)=e^{i\theta}z.
\]
Since $F'(0)=1$, we have $e^{i\theta}=1$. Thus $F$ is the identity, and hence
$f$ is the identity on $G$.
:::
