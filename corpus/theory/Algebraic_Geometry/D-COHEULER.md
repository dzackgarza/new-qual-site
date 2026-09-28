---
schema: qual/card@1
id: D-COHEULER
kind: definition
title: The Euler characteristic and the Hilbert polynomial
classification:
  areas:
  - algebraic-geometry
  topics:
  - Euler Characteristic
  - Hilbert Polynomial
  - Cohomology
relations:
- kind: uses
  target: T-COHFIN
- kind: uses
  target: T-COHSVAN
review: draft
prompts:
- Define the Euler characteristic of a coherent sheaf.
- Why is the Euler characteristic additive?
- How is the Hilbert polynomial defined cohomologically?
---

::: {.definition title="Euler characteristic"}
For a scheme $X$ projective over a field $k$ and a coherent sheaf $\mcf$, its \dfn{Euler characteristic} is
$$
\chi(X,\mcf)\coloneqq\sum_{i\ge0}(-1)^i\dim_kH^i(X,\mcf).
$$
The sum is finite and its terms are finite by cohomological vanishing and finiteness [@Har10a, Theorems III.2.7 and III.5.2].
Write $\chi(\mcf)$ when the scheme is fixed.
:::

::: {.definition title="Hilbert polynomial"}
Choose a very ample invertible sheaf $L$ on the projective $k$-scheme $X$ and put $\mcf(n)=\mcf\otimes L^{\otimes n}$, using the dual of $L$ for negative powers.
The \dfn{Hilbert polynomial} of $\mcf$ with respect to $L$ is the unique $P_{\mcf,L}\in\QQ[z]$ satisfying
$$
P_{\mcf,L}(n)=\chi(X,\mcf(n))\qquad(n\in\ZZ)
$$
[@Har10a, Exercise III.5.2].
It depends on the chosen twisting sheaf; its value at zero is the intrinsic Euler characteristic $\chi(X,\mcf)$.
:::

::: {.definition title="Arithmetic and geometric genus"}
For a nonempty projective scheme $X$ over a field of dimension $n$, the \dfn{arithmetic genus} is $p_a(X)\coloneqq(-1)^n(\chi(\OO_X)-1)$, so $p_a(X)=1-\chi(\OO_X)$ for a curve.
For a nonsingular projective integral variety $X$ of dimension $n$ over an algebraically closed field, the \dfn{geometric genus} is $p_g(X)\coloneqq h^0(X,\omega_X)$, and Serre duality gives $p_g(X)=h^n(X,\OO_X)$.
[@Har10a, §II.8, Exercise III.5.3]
:::

::: {.example}
For a nonsingular projective integral curve over an algebraically closed field, $p_a=p_g$.
For a nonsingular projective integral surface over that field, $p_a=h^2(\OO_X)-h^1(\OO_X)=p_g-q$ with $q=h^1(X,\OO_X)$.
For example, an abelian surface has $h^0(\OO_X)=h^2(\OO_X)=1$ and $h^1(\OO_X)=2$, hence $p_g=1$ and $p_a=-1$.
The product of two nonsingular plane cubics gives an explicit example, computed in [[P-AGH283PRODDIFF]].
:::

::: {.proposition}
$\chi$ is additive: $\chi(\mcf) = \chi(\mcf') + \chi(\mcf'')$ for every short exact sequence $0 \to \mcf' \to \mcf \to \mcf'' \to 0$.
This follows by taking the alternating sum of the dimensions in the finite long exact cohomology sequence, as proved in [[P-AGH351EULERCHAR]].
:::

::: {.remark}
For sufficiently large $n$, Serre vanishing gives $H^i(X,\mcf(n))=0$ for all $i>0$, so $P_{\mcf,L}(n)=h^0(X,\mcf(n))$ [@Har10a, Theorem III.5.2].
For small $n$ this can fail: on $X=\PP^1$ with $L=\OO(1)$, $P_{\OO_X,L}(n)=n+1$, so $P_{\OO_X,L}(-2)=-1$, while $h^0(\PP^1,\OO(-2))=0$.
:::
