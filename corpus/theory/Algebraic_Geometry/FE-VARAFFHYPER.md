---
schema: qual/card@1
id: FE-VARAFFHYPER
kind: example
title: The complement of a hypersurface in projective space is affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Varieties
  - Projective Varieties
  - Hypersurfaces
relations:
- kind: uses
  target: D-VARQAP
- kind: related-to
  target: PR-EFW6B
review: draft
prompts:
- Is the complement of a hypersurface in $\PP^n$ affine?
- Why is $\PP^2 \setminus V(f)$ affine?
---

::: {.example}
Let $k$ be an algebraically closed field and let $f\in k[x_0,\ldots,x_n]$ be a nonzero homogeneous form of positive degree.
Then $\PP^n_k\sm V(f)$ is an affine variety.
:::

::: {.proof}
Let $d=\deg f$ and let $M_0,\ldots,M_N$ be the monomials of degree $d$ in $x_0,\ldots,x_n$.
The $d$-uple embedding
$$\rho_d\colon \PP^n_k\to\PP^N_k,\qquad P\mapsto \thevector{M_0(P):\cdots:M_N(P)}$$
is an isomorphism of $\PP^n_k$ onto its image [@Har77, Exercise I.2.12; @Har77, Exercise I.3.4].
Write $f=\sum_{j=0}^N\alpha_jM_j$ and let $\ell=\sum_{j=0}^N\alpha_jy_j$ be the corresponding linear form on $\PP^N_k$; since $f\ne0$, the form $\ell$ is not zero.
For $P\in\PP^n_k$ one has $\ell(\rho_d(P))=f(P)$, so
$$\rho_d\bigl(V(f)\bigr)=\rho_d(\PP^n_k)\cap Z(\ell).$$
Choose $i$ with $\alpha_i\ne0$ and let $\phi$ be the linear automorphism of $\PP^N_k$ sending $y_i$ to $\ell$ and fixing $y_j$ for $j\ne i$.
Then $\phi$ carries $Z(\ell)$ to the coordinate hyperplane $Z(y_i)$, hence carries $\rho_d(\PP^n_k)\sm Z(\ell)$ isomorphically onto $\phi(\rho_d(\PP^n_k))\cap U_i$, where $U_i=\theset{y_i\ne0}$ is isomorphic to $\AA^N_k$ ([[D-VARQAP]]).
That intersection is a closed subset of an affine variety, hence affine.
Since $\rho_d$ is an isomorphism onto its image, $\PP^n_k\sm V(f)$ is affine.
:::

::: {.remark title="Published solution"}
The argument is transcribed from William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise I.3.5, text version `tmp/sources/hartshorne-solutions-troiani.md`: he writes $f=\sum_j\alpha_jM_j$, observes that $\theta^{-1}(f)=\sum_j\alpha_jy_j$ is linear, and applies a linear change of coordinates in $\PP^N$ carrying that hyperplane to a coordinate hyperplane.
The printed statement and hint are [@Har77, Exercise I.3.5]; the embedding and its isomorphism property are [@Har77, Exercise I.2.12] and [@Har77, Exercise I.3.4].
The hypothesis $d>0$ is needed: for $f$ a nonzero constant, $\PP^n_k\sm V(f)$ is empty, and the $d$-uple embedding exists only for $d>0$.
:::
