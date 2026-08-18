---
schema: qual/card@1
id: P-IP6QO
kind: problem
title: $\int_0^\infty\frac{x\sin x}{x^2+a^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Let $a>0$ and evaluate $$\displaystyle{ \int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \,
dx }.$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Since the integrand $\frac{x \sin(x)}{x^2 + a^2}$ is even in $x$:
$$
I = \int_0^\infty \frac{x \sin(x)}{x^2 + a^2}\, dx = \frac{1}{2} \int_{-\infty}^\infty \frac{x \sin(x)}{x^2 + a^2}\, dx = \frac{1}{2} \operatorname{Im} \left( \operatorname{p.v.} \int_{-\infty}^\infty \frac{x e^{ix}}{x^2 + a^2}\, dx \right).
$$

Consider the complex contour integral of $f(z) = \frac{z e^{iz}}{z^2 + a^2}$ over the standard semi-circular contour $\Gamma_R = [-R, R] \cup C_R$, where $C_R = \{R e^{i\theta} : \theta \in [0, \pi]\}$ in the upper half-plane with $R > a$.

1. **Residue Calculation:** The only singularity of $f(z)$ in the upper half-plane is a simple pole at $z = ia$.
   The residue is:
   $$
   \operatorname{Res}(f, ia) = \lim_{z \to ia} (z - ia) \frac{z e^{iz}}{(z - ia)(z + ia)} = \frac{ia e^{i(ia)}}{2ia} = \frac{e^{-a}}{2}.
   $$
   By the Residue Theorem:
   $$
   \int_{\Gamma_R} f(z)\, dz = 2\pi i \operatorname{Res}(f, ia) = 2\pi i \left(\frac{e^{-a}}{2}\right) = \pi i e^{-a}.
   $$

2. **Arc Estimate (Jordan's Lemma):** On $C_R$, $z = R e^{i\theta}$, $|z| = R$, and $|e^{iz}| = e^{-R \sin \theta}$.
   For $R > a$, $|z^2 + a^2| \geq R^2 - a^2$.
   $$
   \left| \int_{C_R} \frac{z e^{iz}}{z^2 + a^2}\, dz \right| \leq \frac{R}{R^2 - a^2} \int_0^\pi e^{-R \sin \theta} R\, d\theta < \frac{\pi R}{R^2 - a^2} \to 0 \quad \text{as } R \to \infty.
   $$

3. **Limit:** Taking $R \to \infty$:
   $$
   \int_{-\infty}^\infty \frac{x e^{ix}}{x^2 + a^2}\, dx = \pi i e^{-a}.
   $$
   Taking the imaginary part and dividing by 2:
   $$
   \int_0^\infty \frac{x \sin(x)}{x^2 + a^2}\, dx = \frac{1}{2} \operatorname{Im}(\pi i e^{-a}) = \frac{\pi}{2} e^{-a}.
   $$
:::
