---
schema: qual/card@1
id: P-MBQNL
kind: problem
title: $\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi 2$
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
  date: 2026-08-25
---

::: problem
Show that

\[
\int_{0}^{\infty} \frac{\sin x}{x} d x=\frac{\pi}{2}
.\]

> Hint: use the fact that this integral eexercises $\frac{1}{2 i} \int_{-\infty}^{\infty} \frac{e^{i x}-1}{x} d x$, and integrate around an indented semicircle.
:::

::: {.solution}
**Goal:** Show that $\int_0^{\infty} \frac{\sin x}{x}\, dx = \frac{\pi}{2}$.

<1>1. Reduce to a full-line integral: $\int_0^{\infty} \frac{\sin x}{x}\, dx = \frac{1}{2}\, \Im\qty(\int_{-\infty}^{\infty} \frac{e^{ix}}{x}\, dx)$ (principal value).
    <2>1. $\frac{e^{ix}}{x} = \frac{\cos x}{x} + i\frac{\sin x}{x}$.
        ::: {.proof}
        Euler's formula $e^{ix} = \cos x + i \sin x$.
        :::
    <2>2. $\int_{-\infty}^{\infty} \frac{\cos x}{x}\, dx = 0$.
        ::: {.proof}
        The real part is odd, so its principal value vanishes.
        :::
    <2>3. $\int_{-\infty}^{\infty} \frac{\sin x}{x}\, dx = 2\int_0^{\infty} \frac{\sin x}{x}\, dx$.
        ::: {.proof}
        $\sin x / x$ is even.
        :::
    <2>4. The reduction follows.
        ::: {.proof}
        <2>1--<2>3 give $\frac{1}{2}\Im\qty(\int e^{ix}/x\, dx) = \frac{1}{2}\int_{-\infty}^{\infty} \frac{\sin x}{x}\, dx = \int_0^{\infty} \frac{\sin x}{x}\, dx$.
        :::

<1>2. Integrate $f(z) := \frac{e^{iz}}{z}$ over the indented semicircle: the segment $[-R, -\varepsilon]$, the small semicircle $\gamma_\varepsilon$ from $-\varepsilon$ to $\varepsilon$ through the upper half-plane, the segment $[\varepsilon, R]$, and the upper semicircle $\Gamma_R$ of radius $R$.

<1>3. The integral over the closed contour is $0$.
    ::: {.proof}
    The simple pole of $f$ at $z = 0$ is excluded by the indentation $\gamma_\varepsilon$; inside the contour $f$ is holomorphic, so Cauchy's theorem applies.
    :::

<1>4. The integral over the small semicircle tends to $-i\pi$ as $\varepsilon \to 0$.
    <2>1. Parametrize $z = \varepsilon e^{it}$ with $t$ running from $\pi$ to $0$.
        ::: {.proof}
        This traces the upper semicircle from $-\varepsilon$ to $\varepsilon$.
        :::
    <2>2. $\int_{\gamma_\varepsilon} f\, dz = i\int_\pi^0 e^{i\varepsilon e^{it}}\, dt \to i\int_\pi^0 1\, dt = -i\pi$.
        ::: {.proof}
        The exponential is continuous, so the limit passes inside; the sign is negative because the semicircle is traversed clockwise (as part of the positively oriented boundary, going from $-\varepsilon$ to $\varepsilon$ in the upper half-plane).
        :::

<1>5. The integral over the large semicircle tends to $0$ as $R \to \infty$.
    <2>1. On $\Gamma_R$, $z = Re^{it}$ with $t \in [0, \pi]$, and $\Im z = R\sin t \geq 0$, so $\abs{e^{iz}} = e^{-R\sin t} \leq 1$.
        ::: {.proof}
        Direct computation of the modulus on the arc.
        :::
    <2>2. $\int_{\Gamma_R} \frac{e^{iz}}{z}\, dz = \int_0^\pi i e^{iRe^{it}}\, dt \to 0$.
        ::: {.proof}
        The crude bound $\abs{e^{iz}} \leq 1$ only gives $\pi$; the correct estimate is Jordan's lemma: $e^{-R\sin t} \to 0$ pointwise on $(0, \pi)$ and is dominated by $1$, so dominated convergence gives $\int_0^\pi i e^{iRe^{it}}\, dt \to \int_0^\pi i \cdot 0\, dt = 0$.
        :::

<1>6. Pass to the limit.
    ::: {.proof}
    $0 = \int_{[-R,-\varepsilon]} f + \int_{\gamma_\varepsilon} f + \int_{[\varepsilon,R]} f + \int_{\Gamma_R} f$; letting $\varepsilon \to 0$ and $R \to \infty$ and using <1>4 and <1>5 gives $\int_{-\infty}^{\infty} \frac{e^{ix}}{x}\, dx - i\pi = 0$, i.e. the principal value is $i\pi$.
    :::

<1>7. Q.E.D.
    ::: {.proof}
    <1>1 and <1>6 give $\int_0^{\infty} \frac{\sin x}{x}\, dx = \frac{1}{2} \Im(i\pi) = \frac{\pi}{2}$.
    :::

:::

