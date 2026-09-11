---
schema: qual/card@1
id: P-AGH352HILBPOLY
kind: problem
title: Existence of the Hilbert polynomial of a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomial
  - Euler Characteristic
  - Coherent Sheaves
relations: []
review: draft
---

::: problem
a. Let $X$ be a projective scheme over a field $k$, let $\mco_X(1)$ be a very ample invertible sheaf on $X$ over $k$, and let $\mcf$ be a coherent sheaf on $X$.
Show that there is a polynomial $P(z) \in \QQ[z]$, such that $\chi(\mcf(n))=P(n)$ for all $n \in \ZZ$.
We call $P$ the **Hilbert polynomial** of $\mcf$ with respect to the sheaf $\mco_X(1)$.

Hints: Use induction on $\dim \operatorname{Supp} \mcf$, general properties of numerical polynomials (I, 7.3), and suitable exact sequences
\[
0 \to \mcr \to \mcf(-1) \to \mcf \to \mcl \to 0.
\]

b. Now let $X=\PP_k^r$, and let $M=\Gamma_*(\mcf)$, considered as a graded $S=k[x_0, \ldots, x_r]$-module.
Use (5.2) to show that the Hilbert polynomial of $\mcf$ just defined is the same as the Hilbert polynomial of $M$ defined in (I, §7).
:::
