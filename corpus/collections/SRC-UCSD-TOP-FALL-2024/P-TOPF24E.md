---
schema: qual/card@1
id: P-TOPF24E
kind: problem
title: Commutators and maps of a one-holed torus
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $\Sigma$ be a one-holed torus (delete an open disc from a standard torus) whose boundary is identified with the standard $S^1$.
Let $(X, x_0)$ be a based path-connected space, $\alpha$ a loop based at $x_0$, and $[\alpha]$ the corresponding class in $\pi_1(X, x_0)$.
Show that $[\alpha]$ may be expressed algebraically as a commutator $yzy^{-1}z^{-1}$ of two elements $y, z \in \pi_1(X, x_0)$ if and only if "$\alpha$ extends to a map of $\Sigma$", meaning that $\alpha$ may be expressed as $f|_{\partial\Sigma}$ for some map $f \colon \Sigma \to X$.
Is there an analogue of this result for one-holed higher-genus surfaces?
:::

::: {.solution}
Let the basepoint of $\partial\Sigma\cong S^1$ be the basepoint used for $\pi_1(\Sigma)$.

<1>1. The one-holed torus deformation retracts onto a wedge $R=S^1\vee S^1$ with generators $a,b$, and under this retraction the oriented boundary loop represents the commutator
$$
[a,b]=aba^{-1}b^{-1}\in\pi_1(R).
$$
::: {.proof}
Give $\Sigma$ its standard CW structure with one vertex, two $1$-cells $a,b$, and boundary circle. Cutting along the two generating arcs exhibits a polygon whose boundary word is $aba^{-1}b^{-1}c^{-1}$, where $c$ is the boundary component. Equivalently, after retracting $\Sigma$ onto the graph spine $R$, the boundary class maps to $[a,b]$ (up to reversing the chosen boundary orientation, which only replaces the commutator by its inverse).
:::

<1>2. Suppose $[\alpha]=yzy^{-1}z^{-1}$ in $\pi_1(X,x_0)$. Choose based loops $\beta,\gamma$ representing $y,z$ and define a based map
$$
\varphi:R=S^1\vee S^1\longrightarrow X
$$
by sending the two circle summands to $\beta$ and $\gamma$.
::: {.proof}
A map from a wedge of two based circles is specified by two based loops. By construction, $\varphi_*(a)=y$ and $\varphi_*(b)=z$.
:::

<1>3. If $r:\Sigma\to R$ is a deformation retraction, then $F_0=\varphi\circ r$ has boundary loop $\lambda=F_0|_{\partial\Sigma}$ satisfying
$$
[\lambda]=[\alpha]\in\pi_1(X,x_0).
$$
::: {.proof}
By <1>1,
$$
[r|_{\partial\Sigma}]=[a,b].
$$
Hence
$$
[\lambda]=\varphi_*[a,b]=[\varphi_*a,\varphi_*b]=[y,z]=[\alpha].
$$
:::

<1>4. The map $F_0$ can be changed, without changing its existence on the interior, to a map $F:\Sigma\to X$ whose boundary restriction is exactly $\alpha$.
::: {.proof}
Equality $[\lambda]=[\alpha]$ means that there is a based homotopy
$$
H:\partial\Sigma\times I\to X
$$
from $\lambda$ to $\alpha$. The inclusion $\partial\Sigma\hookrightarrow\Sigma$ is a cofibration (for example, it is a CW-subcomplex inclusion in a CW structure adapted to the boundary). Therefore the homotopy extension property extends $H$, together with $F_0$ at time $0$, to a homotopy
$$
\widetilde H:\Sigma\times I\to X.
$$
Set $F=\widetilde H(-,1)$. Then $F|_{\partial\Sigma}=\alpha$ exactly.
:::

<1>5. Conversely, if $F:\Sigma\to X$ satisfies $F|_{\partial\Sigma}=\alpha$, then $[\alpha]$ is a commutator.
::: {.proof}
Let
$$
y=F_*(a),\qquad z=F_*(b).
$$
By <1>1,
$$
[\alpha]=F_*[\partial\Sigma]=F_*[a,b]=[F_*a,F_*b]=[y,z].
$$
:::

<1>6. Hence
$$
\boxed{[\alpha]\text{ is one commutator}\iff \alpha\text{ extends over a one-holed torus}.}
$$
::: {.proof}
The forward implication is <1>2--<1>4 and the reverse implication is <1>5.
:::

<1>7. For the one-holed orientable surface $\Sigma_g^1$ of genus $g$, the boundary class is
$$
[a_1,b_1]\cdots[a_g,b_g].
$$
::: {.proof}
The standard polygonal CW description of $\Sigma_g^1$ gives the boundary word as the product of the $g$ commutators of the $2g$ spine generators.
:::

<1>8. Therefore the higher-genus analogue is
$$
\boxed{\alpha\text{ extends over }\Sigma_g^1
\iff
[\alpha]=\prod_{i=1}^g[y_i,z_i]\text{ in }\pi_1(X,x_0).}
$$
::: {.proof}
For the reverse implication, map the $2g$-circle graph spine to loops representing $y_i,z_i$, obtaining a map whose boundary is based-homotopic to $\alpha$, and use the homotopy extension property as in <1>4. The forward implication follows by applying $F_*$ to the boundary word in <1>7.
:::
:::
