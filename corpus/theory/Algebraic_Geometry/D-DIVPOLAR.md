---
schema: qual/card@1
id: D-DIVPOLAR
kind: definition
title: Polarizations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Polarizations
  - Ample Line Bundles
  - Neron-Severi Group
relations:
- kind: uses
  target: D-DIVAMPLE
- kind: uses
  target: D-DIVEQUIV
review: draft
prompts:
- What is a polarization?
---

::: {.definition}
Let $X$ be a projective variety.
A \dfn{polarization} on $X$ is an ample invertible sheaf $\mcl$.
A \dfn{polarized variety} is a pair $(X,\mcl)$, and an isomorphism
$$
f\colon(X,\mcl)\xrightarrow{\sim}(X',\mcl')
$$
is an isomorphism $f\colon X\to X'$ together with an isomorphism
$f^*\mcl'\cong\mcl$.

The class $h=[\mcl]\in\NS(X)$ is an \dfn{ample numerical class}.
A \dfn{numerical polarization} is such a class $h$, and a \dfn{numerically polarized variety} is a pair $(X,h)$.
An isomorphism $(X,h)\to(X',h')$ is an isomorphism $f\colon X\to X'$ with $f^*h'=h$ in $\NS(X)$.

If $\dim X=n$, the \dfn{degree} is the top self-intersection
$$
\deg(X,\mcl)=c_1(\mcl)^n=h^n,
$$
which depends only on the numerical polarization.
:::

::: {.example}
$(\PP^n, \OO(1))$ is polarized of degree $1$, and a hypersurface of degree $d$ with $\OO(1)$ is polarized of degree $d$.
A K3 surface with an ample numerical class $h$ has a numerical polarization of degree $h^2$, an even integer written $2g - 2$, and a quartic surface in $\PP^3$ has degree $4$ with respect to $\OO(1)$.
For an abelian variety $A$, an ample invertible sheaf $\mcl$ determines the polarization isogeny
$$
\lambda_{\mcl}\colon A\to \dualof{A},
\qquad
x\mapsto t_x^*\mcl\tensor_{\OO_A}\mcl^{-1}.
$$
It is \dfn{principal} when $\lambda_{\mcl}$ is an isomorphism, as for the theta divisor on the Jacobian of a curve; $\lambda_{\mcl}$ depends only on the class of $\mcl$ in $\NS(A)$.
:::
