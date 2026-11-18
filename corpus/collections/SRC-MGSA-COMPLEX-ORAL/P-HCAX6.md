---
schema: qual/card@1
id: P-HCAX6
kind: problem
title: Areas of spherical and hyperbolic triangles
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Geometry
relations: []
review: draft
---

::: {.problem}
Determine and prove the area formulas for spherical and hyperbolic triangles in terms of their angles.
:::

::: {.solution}

No retained solution set covers this question: the card's own Gauss–Bonnet derivation follows, with the geodesic-curvature term, the exterior angles and the two curvature cases as separate steps.

::: pf

::: {.pf-step #gauss-bonnet}
For a geodesic triangle $T$ with interior angles $\alpha,\beta,\gamma$ on a surface of constant curvature $K$, Gauss–Bonnet gives
$$K\cdot\operatorname{Area}(T)+(\pi-\alpha)+(\pi-\beta)+(\pi-\gamma)=2\pi.$$

::: pf-proof
Gauss–Bonnet for a geodesic polygon reads $\iint_{T}K\,dA+\oint_{\partial T}k_{g}\,ds+\sum_{\text{vertices}}(\pi-\text{interior angle})=2\pi$. The sides are geodesics, so $k_{g}=0$ along them; each vertex contributes the exterior angle $\pi-\alpha$; and $K$ is constant, so the double integral is $K\cdot\operatorname{Area}(T)$.
:::

:::

::: {.pf-step #solve}
$\operatorname{Area}(T)=\dfrac{\alpha+\beta+\gamma-\pi}{K}$.

::: pf-proof
The equation of step [](#gauss-bonnet){.pf-ref} reads $K\cdot\operatorname{Area}(T)+3\pi-(\alpha+\beta+\gamma)=2\pi$, that is $K\cdot\operatorname{Area}(T)=(\alpha+\beta+\gamma)-\pi$.
:::

:::

::: {.pf-step #sphere}
On the unit sphere, $K=1$ and $\operatorname{Area}(T)=\alpha+\beta+\gamma-\pi$; in particular this is positive, which is the spherical excess.

::: pf-proof
Put $K=1$ in step [](#solve){.pf-ref}. A geodesic triangle on the sphere has $\alpha+\beta+\gamma>\pi$, consistent with a positive area.
:::

:::

::: {.pf-step #hyperbolic}
In the hyperbolic plane normalized to $K=-1$, $\operatorname{Area}(T)=\pi-(\alpha+\beta+\gamma)$; in particular $\alpha+\beta+\gamma<\pi$.

::: pf-proof
Put $K=-1$ in step [](#solve){.pf-ref}: $\operatorname{Area}(T)=\frac{\alpha+\beta+\gamma-\pi}{-1}=\pi-(\alpha+\beta+\gamma)$, and an area is positive, so the angle sum is less than $\pi$; the defect $\pi-(\alpha+\beta+\gamma)$ is the area.
:::

:::

::: {.pf-qed}
The spherical formula is step [](#sphere){.pf-ref} and the hyperbolic formula is step [](#hyperbolic){.pf-ref}, both from the Gauss–Bonnet computation of steps [](#gauss-bonnet){.pf-ref} and [](#solve){.pf-ref}. For general constant curvature $K\ne0$ the area is $(\alpha+\beta+\gamma-\pi)/K$, and the formulas as usually stated are the normalizations $K=\pm1$.
:::

:::

:::
