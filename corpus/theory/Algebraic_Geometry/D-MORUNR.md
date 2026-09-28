---
schema: qual/card@1
id: D-MORUNR
kind: definition
title: Unramified morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Unramified Morphisms
  - Ramification
  - Differentials
relations:
- kind: related-to
  target: D-MORFT
review: draft
prompts:
- What is an unramified morphism?
- State the characterisation by differentials.
- What does unramified mean for a map of curves?
---

::: {.definition title="Unramified"}
$f : X \to Y$ locally of finite type is \dfn{unramified} if for every $x \in X$ with $y = f(x)$,
$$
f^\sharp(\mfm_y) \OO_{X,x} = \mfm_x
\qquad\text{and}\qquad
\kappa(x)/\kappa(y) \text{ is a finite separable extension.}
$$
Equivalently, $\Omega_{X/Y} = 0$; equivalently, $\Delta_{X/Y}$ is an open immersion.
:::

::: {.remark}
The first condition says that for every $y\in Y$ and $x\in X_y$, the local ring $\OO_{X_y,x}$ is the field $\kappa(x)$, a finite separable extension of $\kappa(y)$.
Since the diagonal of an unramified morphism is open, two sections $s,t\colon Y\to X$ of an unramified morphism $f$ agree on an open subset of $Y$, namely $(s,t)^{-1}(\Delta_{X/Y})$.

For a nonconstant map of smooth integral curves over an algebraically closed field, the local picture at a closed point is $f^\sharp(\mfm_{f(p)}) \OO_{X,p} = \mfm_p^{e_p}$, and $f$ is unramified exactly when every ramification index $e_p$ equals $1$.
For $n>1$, $t \mapsto t^n$ on $\AA^1$ is ramified at the origin. In characteristic $p$ dividing $n$, its differential vanishes everywhere and the induced function-field extension is inseparable.
For an unramified finite separable morphism $f\colon X\to Y$ of smooth projective curves, the ramification divisor is $0$, and Riemann--Hurwitz gives $2g_X-2=(\deg f)(2g_Y-2)$.
:::
