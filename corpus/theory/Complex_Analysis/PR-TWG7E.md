---
schema: qual/card@1
id: PR-TWG7E
kind: proposition
title: Möbius map from the unit disc to the right half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.proposition}
Let $\HH_R\coloneqq\ts{w\st\Re w>0}$ be the right half-plane.
The map
$$
F\colon\DD\to\HH_R,\qquad F(z)=\frac{1+z}{1-z},
$$
is a [[D-TM4TE|biholomorphism]], with inverse $F^{-1}(w)=\frac{w-1}{w+1}$.
It sends $-1,0,1$ to $0,1,\infty$ respectively.
:::

::: {.proof}
For $z\in\DD$,
$$
F(z)=\frac{(1+z)(1-\bar z)}{\abs{1-z}^2}=\frac{1-\abs{z}^2+2i\Im z}{\abs{1-z}^2},
$$
so $\Re F(z)>0$.
For $w\in\HH_R$, $w$ is closer to $1$ than to $-1$, so $\abs{\frac{w-1}{w+1}}<1$.
Solving $w=\frac{1+z}{1-z}$ gives $z=\frac{w-1}{w+1}$, so the two maps are mutually inverse.
:::

::: {.remark}
The [[PR-OOHFS|Cayley transform]] $\Psi(z)=\frac{z-i}{z+i}$ from the upper half-plane $\HH$ onto $\DD$ is related to $F$ by rotations.
Its inverse is $\Psi^{-1}(w)=i\,\frac{1+w}{1-w}=iF(w)$, the composite $\DD\xrightarrow{F}\HH_R\xrightarrow{w\mapsto iw}\HH$.
Conversely, $\Psi(z)=F^{-1}(-iz)$, the composite $\HH\xrightarrow{z\mapsto -iz}\HH_R\xrightarrow{F^{-1}}\DD$:
$$
F^{-1}(-iz)=\frac{-iz-1}{-iz+1}=\frac{z-i}{z+i}.
$$
:::

::: {.remark}
On the boundary, $F(e^{i\theta})=i\cot(\theta/2)$ for $0<\theta<2\pi$, so the unit circle minus $1$ is mapped onto the imaginary axis, and the segment $(-1,1)$ is mapped onto $(0,\infty)$.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_20-38-28.png)
:::

::: {.example}
The restriction of $F$ to the upper half-disc $\ts{z\in\DD\st\Im z>0}$ is a biholomorphism onto the first quadrant: by the formula for $F(z)$ in the proof, $\Im F(z)>0$ exactly when $\Im z>0$.
This is [[PR-PW4Z6]].

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_19-36-20.png)
:::
