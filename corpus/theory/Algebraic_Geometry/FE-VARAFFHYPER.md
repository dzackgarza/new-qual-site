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
Let $k$ be an algebraically closed field and let $f\in k[x_0,\ldots,x_n]$ be a nonzero homogeneous form.
Then $\PP^n_k\sm V(f)$ is an affine variety.
:::

::: {.proof}
Put $X=\PP^n_k\sm V(f)$. On the chart $U_i=D_+(x_i)$ with affine ring $A_i=k[x_0/x_i,\ldots,x_n/x_i]$, the open subset $X\cap U_i$ is the nonvanishing locus of $f/x_i^{\deg f}$ in $U_i$, hence is $\Spec (A_i)_{f/x_i^{\deg f}}$ and is affine ([[D-VARQAP]]).
The regular functions $g_i=x_i^{\deg f}/f$ on $X$ have no common zero, so they generate the unit ideal of $\Gamma(X,\OO_X)$, and $X_{g_i}=X\cap U_i$; the affine criterion then gives that $X$ is affine [@Har77, Exercise II.2.17].
:::
