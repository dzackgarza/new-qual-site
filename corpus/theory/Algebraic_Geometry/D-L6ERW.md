---
schema: qual/card@1
id: D-L6ERW
kind: definition
title: The Hilbert polynomial and its coefficients
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomial
  - Degree
  - Arithmetic Genus
relations:
- kind: uses
  target: D-CP2MH
- kind: uses
  target: D-5LJUX
review: draft
prompts:
- What is the Hilbert polynomial of a projective variety?
- What does the leading term of $P_X(r)$ mean?
- What does the constant term of $P_X(r)$ represent?
---

::: {.definition title="Hilbert polynomial"}
For $X \subseteq \PP^n$ closed with homogeneous coordinate ring $S(X) = k[x_0,\ldots,x_n]/I(X)$, the \dfn{Hilbert function} is
$$
h_X(r) \da \dim_k S(X)_r .
$$
For $r \gg 0$ it agrees with a polynomial $P_X(r)$, the \dfn{Hilbert polynomial} of $X$.

For a coherent sheaf $\mcf$ on a closed subscheme $X \subseteq \PP^n_k$, the \dfn{Hilbert function of $\mcf$} is $h_\mcf(m) \da h^0(X, \mcf(m))$.
:::

::: {.proposition}
For $m \gg 0$, $h_\mcf(m) = \chi(X, \mcf(m)) = P_\mcf(m)$, the value of the Hilbert polynomial of $\mcf$ ([[D-COHEULER]]), and $P_X = P_{\OO_X}$.
[@Har10a, Exercise III.5.2]
:::

::: {.remark title="Reading off the coefficients"}
Write $\dim X = d$.
Then $\deg P_X = d$, and

- the leading coefficient is $\deg(X)/d!$; this defines the degree of $X$ [@Har10a, §I.7];

- the constant term is $P_X(0) = \chi(\OO_X)$, and the arithmetic genus is $p_a(X) = (-1)^d \qty(P_X(0) - 1)$, which is $1 - \chi(\OO_X)$ for a curve.

The leading coefficient, and hence the degree, depends on the embedding: $\PP^1$ embedded by $\OO(3)$ has degree $3$.
The constant term $\chi(X,\OO_X)$ and the arithmetic genus do not depend on the embedding [@Har10a, Exercise III.5.2].
:::

::: {.example title="Hilbert polynomials of $\PP^n$ and the twisted cubic"}
$P_{\PP^n}(r) = \binom{r+n}{n}$, of degree $n$ and leading coefficient $1/n!$, so $\deg \PP^n = 1$ and $p_a(\PP^n) = 0$.

On $\PP^1$, one has $h^0(\PP^1,\OO(m))=m+1$ for $m\ge0$ and zero for $m<0$ [@Har10a, Proposition II.5.13].
Taking $m=3r$ for $r\ge0$ gives the Hilbert polynomial of the twisted cubic, $P(r)=3r+1$, with degree $3$ and arithmetic genus $0$.
:::
