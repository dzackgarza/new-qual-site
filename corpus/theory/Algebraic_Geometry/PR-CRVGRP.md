---
schema: qual/card@1
id: PR-CRVGRP
kind: proposition
title: The group law on an elliptic curve, and multiplication by $n$
slogan: 'Choosing an origin identifies a genus-$1$ curve with its $\Pic^0$; collinearity is addition, and $[n]$ has degree $n^2$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Group Schemes
  - Torsion
relations:
- kind: uses
  target: T-U5QSY
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- Why is an elliptic curve a group?
- Is an elliptic curve a group scheme?
- What is the kernel of multiplication by $n$?
---

::: {.proposition}
Let $k$ be an algebraically closed field and let $E$ be a smooth projective curve of genus $1$ with a chosen point $p_0\in E(k)$.
The Abel--Jacobi morphism
$$
E\longrightarrow \Pic^0_{E/k},\qquad p\longmapsto\OO_E(p-p_0),
$$
is an isomorphism. Transporting the group structure of $\Pic^0_{E/k}$ along this isomorphism makes $E$ a group scheme over $k$ with identity $p_0$.
Under the embedding defined by $\abs{3p_0}$, three points counted with intersection multiplicity sum to $p_0$ exactly when their divisor is cut out by a line.
:::

::: {.proposition title="Multiplication by $n$"}
For $n\geq1$, the multiplication morphism $[n]\colon E\to E$ is finite of degree $n^2$, and its kernel group scheme $E[n]$ has rank $n^2$.
If $n$ is prime to $\operatorname{char}k$, then $E[n]$ is finite étale and
$$
E[n](k)\cong(\ZZ/n\ZZ)^2.
$$
If $\operatorname{char}k=p>0$, then $E[p]$ is finite flat of rank $p^2$, while its group of geometric points satisfies
$$
E[p](k)\cong
\begin{cases}
\ZZ/p\ZZ,& E\text{ ordinary},\\
0,& E\text{ supersingular}.
\end{cases}
$$
In the supersingular case the group scheme $E[p]$ is connected, so the vanishing of $E[p](k)$ does not mean that the kernel scheme is trivial.
:::

::: {.remark}
Riemann--Roch gives the corresponding bijection on $k$-points. If $D$ has degree zero, then $D+p_0$ has degree $1>2g-2=0$, so $\ell(D+p_0)=1$. Hence there is a unique effective divisor $x$ of degree $1$ with $D+p_0\sim x$, and therefore $D\sim x-p_0$.
The Picard-scheme construction upgrades this pointwise correspondence to the isomorphism $E\cong\Pic^0_{E/k}$ above.

For the plane cubic embedding, a line cuts out a divisor linearly equivalent to $3p_0$. Thus the chord-and-tangent rule is the equality $p+q+r=p_0$ in the group law, with tangency encoded by intersection multiplicity.

A morphism of elliptic curves carrying identity to identity is automatically a group homomorphism, and $\operatorname{End}(E)$ is a ring containing the multiplication maps $[n]$, $n\in\ZZ$.
In characteristic zero, $E$ has \dfn{complex multiplication} when $\operatorname{End}(E)$ is strictly larger than $\ZZ$. For $E(\CC)\cong\CC/(\ZZ+\tau\ZZ)$, this is equivalent to $\tau$ being imaginary quadratic.
:::
