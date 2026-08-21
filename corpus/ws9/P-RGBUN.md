---
schema: qual/card@1
id: P-RGBUN
kind: problem
title: Contour integral $\int_0^\infty\frac{\log x}{x^2+2}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Contour Integration
  - Residues
  - Integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Evaluate $\int_0^\infty \frac{\log x}{x^2+2}dx$ by contour integration using the positively oriented contour from $-R$ to $R$ on the real axis (indented at the origin) and the positively oriented semicircle $|z|=R$, $\operatorname{Im} z > 0$.
Choose an appropriate branch of logarithm.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Evaluate $I = \int_0^\infty \frac{\log x}{x^2 + 2}\, dx$ by contour integration, using the branch of the logarithm with $\arg z \in (0, 2\pi)$.

<1>1. Setup: take the branch of the logarithm with $\arg z \in (-\pi/2, 3\pi/2)$ (branch cut along the negative imaginary axis), and integrate $f(z) = \frac{\Log z}{z^2 + 2}$ over the contour $\Gamma$: the real segment from $-R$ to $R$ (indented at the origin by a small semicircle in the upper half-plane of radius $\varepsilon$) plus the upper semicircle $|z| = R$.
Proof: the branch cut (negative imaginary axis) does not meet $\Gamma$ or its interior (the upper half-plane), so $\Log z$ is analytic on and inside $\Gamma$; on the positive real axis $\Log x = \log x$ (argument $0$) and on the negative real axis $\Log(-x) = \log x + i\pi$ (argument $\pi$).

<1>2. The poles inside $\Gamma$ are $z = i\sqrt{2}$ (upper half-plane), with $\Res_{z = i\sqrt2} f = \frac{\log\sqrt{2} + i\tfrac{\pi}{2}}{2i\sqrt{2}}$.
Proof: $z^2 + 2 = (z - i\sqrt2)(z + i\sqrt2)$; at $z = i\sqrt2$ (argument $\pi/2$), $\Res = \frac{\Log(i\sqrt2)}{2i\sqrt2} = \frac{\log\sqrt2 + i\pi/2}{2i\sqrt2}$.

<1>3. Arc contributions vanish: the big semicircle $\to 0$ as $R \to \infty$ and the small indentation $\to 0$ as $\varepsilon \to 0$.
Proof: on $|z| = R$, $|f(z)| \le \frac{\log R + 2\pi}{R^2 - 2}$, so the arc integral is $O(\pi R\frac{\log R}{R^2}) \to 0$; on the small semicircle $z = \varepsilon e^{i\theta}$, the integral is $O(\varepsilon \log\tfrac{1}{\varepsilon}) \to 0$.

<1>4. The real-axis part converges to $2\int_0^\infty \frac{\log x}{x^2+2}\,dx + i\pi\int_0^\infty \frac{dx}{x^2 + 2}$.
Proof: on $(-\infty, 0)$, $\Log(-x) = \log x + i\pi$; combining $\int_{-R}^{-\varepsilon} + \int_{\varepsilon}^{R}$ and letting $\varepsilon \to 0, R \to \infty$ gives $\int_0^\infty \frac{\log x + (\log x + i\pi)}{x^2 + 2}\, dx$.

<1>5. Evaluate $\int_0^\infty \frac{dx}{x^2+2} = \frac{\pi}{2\sqrt2}$.
Proof: $\frac{1}{\sqrt2}\arctan\qty{\frac{x}{\sqrt2}}\Big|_0^\infty = \frac{\pi}{2\sqrt2}$.

<1>6. Equate real parts.
<2>1. Residue theorem: $2\pi i\cdot\frac{\log\sqrt2 + i\pi/2}{2i\sqrt2} = \frac{\pi}{\sqrt2}\qty{\log\sqrt2 + \tfrac{i\pi}{2}}$.
Proof: <1>2 with $2\pi i$.
<2>2. $2I + i\pi\cdot\frac{\pi}{2\sqrt2} = \frac{\pi\log\sqrt2}{\sqrt2} + i\frac{\pi^2}{2\sqrt2}$.
Proof: <1>3–<1>5 give the total integral; the imaginary parts match (both $\frac{i\pi^2}{2\sqrt2}$), and the real parts give $2I = \frac{\pi\log\sqrt2}{\sqrt2}$.

<1>7. $I = \frac{\pi\log 2}{4\sqrt2}$.
Proof: from <2>2, $I = \frac{\pi\log\sqrt2}{2\sqrt2} = \frac{\pi\log 2}{4\sqrt2}$.

<1>8. Q.E.D. Proof: <1>1–<1>7 evaluate the integral.
:::
