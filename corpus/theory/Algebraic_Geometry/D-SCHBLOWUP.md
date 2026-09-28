---
schema: qual/card@1
id: D-SCHBLOWUP
kind: definition
title: Blowing up a scheme along a closed subscheme, and blowing down
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Relative Proj
  - Cartier Divisors
relations:
- kind: uses
  target: D-SCHRELSPECPROJ
- kind: related-to
  target: D-VARBLOW
- kind: related-to
  target: T-SRFCAST
review: draft
prompts:
- What is the blowup of a scheme along a closed subscheme?
- What is the blowdown of a scheme?
---

::: {.definition title="Blowup"}
Let $X$ be a Noetherian scheme and $Z \subseteq X$ a closed subscheme with ideal sheaf $\mathcal{I}$.
The \dfn{Rees algebra} of $\mathcal{I}$ is the graded quasicoherent $\OO_X$-algebra $\bigoplus_{d \geq 0} \mathcal{I}^d$, with $\mathcal{I}^0 = \OO_X$; it is generated in degree $1$.
The \dfn{blowup} of $X$ along $Z$ is the $X$-scheme
$$\pi \colon \Bl_Z X \coloneqq \operatorname{\mathbf{Proj}}_X \bigoplus_{d \geq 0} \mathcal{I}^d \to X,$$
using the relative Proj of [[D-SCHRELSPECPROJ]].
The \dfn{exceptional divisor} is the closed subscheme $E = \pi^{-1}(Z)$ of $\Bl_Z X$, with ideal sheaf $\mathcal{I} \cdot \OO_{\Bl_Z X}$.
:::

::: {.theorem title="Properties and universal property"}
Let $\pi \colon \Bl_Z X \to X$ be the blowup of a Noetherian scheme along a closed subscheme $Z$.

1. $\pi$ is projective, $E$ is an effective Cartier divisor, and $\pi$ restricts to an isomorphism $\Bl_Z X \setminus E \to X \setminus Z$.

2. If $X$ is integral and $Z \neq X$, then $\Bl_Z X$ is integral and $\pi$ is birational.

3. For every morphism $f \colon Y \to X$ such that $f^{-1}(Z)$, the closed subscheme with ideal sheaf $f^{-1}\mathcal{I} \cdot \OO_Y$, is an effective Cartier divisor on $Y$, there is a unique morphism $g \colon Y \to \Bl_Z X$ with $f = \pi \circ g$.
:::

::: {.example}
Let $X = \AA^2_k = \Spec k[x,y]$ and $Z$ the origin, $\mathcal{I} = (x, y)$.
Since $x, y$ is a regular sequence, the Rees algebra is $k[x,y][s,t]/(xt - ys)$, with $s \mapsto x$ and $t \mapsto y$ in degree $1$.
So $\Bl_0 \AA^2 = V(xt - ys) \subseteq \AA^2_k \times \PP^1_k$.
On the chart $s \neq 0$ with coordinate $u = t/s$, the equation becomes $y = xu$, the chart is $\Spec k[x, u] \cong \AA^2$, and $E$ is the line $V(x)$ there; the two charts glue $E$ to $\PP^1_k$.
This recovers the blowup of a variety at a point in [[D-VARBLOW]].
:::

::: {.definition title="Blowdown"}
A proper birational morphism $\rho \colon Y \to X$ of integral Noetherian schemes is the \dfn{blowdown} of a closed subscheme $F \subseteq Y$ if there are a closed subscheme $Z \subseteq X$ and an isomorphism $Y \cong \Bl_Z X$ over $X$ carrying $F$ to the exceptional divisor.
Then $X$ is obtained from $Y$ by \dfn{blowing down} $F$, and $\rho$ contracts $F$ to $Z$.
:::

::: {.example}
If $Y$ is a smooth projective surface over an algebraically closed field and $F \subseteq Y$ is a curve with $F \cong \PP^1$ and $F^2 = -1$, then by Castelnuovo's criterion [[T-SRFCAST]] there is a smooth projective surface $X$ and a point $p \in X$ with $Y \cong \Bl_p X$ and $F$ the exceptional curve, so $F$ can be blown down.
:::
