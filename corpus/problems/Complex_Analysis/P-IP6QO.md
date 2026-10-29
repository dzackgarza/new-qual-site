---
schema: qual/card@1
id: P-IP6QO
kind: problem
title: $\int_0^\infty\frac{x\sin x}{x^2+a^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.problem}
Let $a>0$ and evaluate
$$
\int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \, dx.
$$
:::

::: {.solution}
Let $f(z) = \frac{z e^{iz}}{z^2 + a^2}$ and, for $R > a$, let $C_R = \{R e^{i\theta} : \theta \in [0, \pi]\}$ and $\Gamma_R = [-R, R] \cup C_R$, positively oriented.

::: pf

::: {.pf-step #residue}
$\int_{\Gamma_R} f(z)\, dz = \pi i e^{-a}$.

::: pf-proof
The only singularity of $f$ inside $\Gamma_R$ is the simple pole at $ia$, with
$$
\operatorname{Res}(f, ia) = \frac{ia\, e^{i(ia)}}{2ia} = \frac{e^{-a}}{2}.
$$
The residue theorem gives $2\pi i \cdot \frac{e^{-a}}{2}$.
:::

:::

::: {.pf-step #arc}
$\int_{C_R} f(z)\, dz \to 0$ as $R \to \infty$.

::: pf-proof
On $C_R$, $\abs{e^{iz}} = e^{-R \sin \theta}$ and $\abs{z^2 + a^2} \geq R^2 - a^2$, and Jordan's inequality gives $\int_0^\pi e^{-R\sin\theta}\,d\theta < \pi/R$.
Hence
$$
\abs{\int_{C_R} f(z)\, dz} \leq \frac{R}{R^2 - a^2} \int_0^\pi e^{-R \sin \theta} R\, d\theta < \frac{\pi R}{R^2 - a^2}.
$$
:::

:::

::: pf-step
$$
\int_0^\infty \frac{x \sin x}{x^2 + a^2}\, dx = \boxed{\frac{\pi}{2} e^{-a}}.
$$

::: pf-proof
By steps [](#residue){.pf-ref} and [](#arc){.pf-ref}, $\int_{-R}^{R} f(x)\,dx \to \pi i e^{-a}$.
Taking imaginary parts, $\int_{-R}^{R}\frac{x\sin x}{x^2+a^2}\,dx \to \pi e^{-a}$, and this integrand is even, so $\int_0^R \frac{x\sin x}{x^2+a^2}\,dx \to \frac{\pi}{2}e^{-a}$.
:::

:::

:::
:::
