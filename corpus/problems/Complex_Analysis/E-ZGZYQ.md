---
schema: qual/card@1
id: E-ZGZYQ
kind: problem
title: Principal values of $\int_\RR \sin x/x\,dx$ and $\int_\RR \cos x/x\,dx$
classification:
  areas:
    - complex-analysis
  topics:
    - Residues
    - Contour Integration
    - Integrals
    - Trigonometry
relations: []
review: draft
audit:
  - event: source-corrected
    by: Claude Opus 5.5
    date: 2026-10-29
    note: 'The source reads "Compute I_1 := PV int sin(x)/x dx = pi, I_2 := PV int cos(x)/x dx = 0", which states the values it asks for; the statement asks to show these values.'
---

::: {.exercise}
Show that
$$
I_1 \coloneqq \PV\int_\RR \frac{\sin x}{x}\dx = \pi,
\qquad
I_2 \coloneqq \PV\int_\RR \frac{\cos x}{x}\dx = 0.
$$
:::

::: {.solution}

Let $f(z) \coloneqq e^{iz}/z$.
For $0<\varepsilon<R$, let $C_R$ be the upper semicircle $\abs{z}=R$ traversed counterclockwise, and let $C_\varepsilon$ be the upper semicircle $\abs{z}=\varepsilon$ traversed clockwise.
Let $\Gamma$ be the closed curve formed by $[-R,-\varepsilon]$, $C_\varepsilon$, $[\varepsilon,R]$ and $C_R$.

::: pf

::: {.pf-step #cauchy}
$\int_\Gamma f(z)\dz = 0$.

::: pf-proof
The function $f$ is holomorphic on $\CC\sm\theset{0}$, and $\Gamma$ bounds a region whose closure does not contain $0$, so Cauchy's theorem applies.
:::

:::

::: {.pf-step #jordan}
$\int_{C_R} f(z)\dz \to 0$ as $R\to\infty$.

::: pf-proof
This is Jordan's lemma for $e^{iz}g(z)$ with $g(z)=1/z$, since $\sup_{\abs{z}=R}\abs{g(z)} = 1/R \to 0$.
:::

:::

::: {.pf-step #small-arc}
$\int_{C_\varepsilon} f(z)\dz \to -i\pi$ as $\varepsilon\to 0$.

::: pf-proof
Write $f(z) = 1/z + h(z)$ with $h(z) = (e^{iz}-1)/z$, which extends to an entire function and is therefore bounded by some $M$ on $\abs{z}\leq 1$.
With $z=\varepsilon e^{i\theta}$ and $\theta$ running from $\pi$ to $0$, $\int_{C_\varepsilon}\frac{\dz}{z} = \int_\pi^0 i\,d\theta = -i\pi$, while $\abs{\int_{C_\varepsilon} h(z)\dz}\leq \pi\varepsilon M\to 0$.
:::

:::

::: pf-step
$I_1 = \boxed{\pi}$ and $I_2 = \boxed{0}$.

::: pf-proof
By steps [](#cauchy){.pf-ref}, [](#jordan){.pf-ref} and [](#small-arc){.pf-ref},
$$
\int_{\varepsilon<\abs{x}<R} \frac{e^{ix}}{x}\dx
= -\int_{C_R} f(z)\dz - \int_{C_\varepsilon} f(z)\dz
\to i\pi
$$
as $\varepsilon\to 0$ and $R\to\infty$.
The real part of the left side is $\int_{\varepsilon<\abs{x}<R} \frac{\cos x}{x}\dx$ and its imaginary part is $\int_{\varepsilon<\abs{x}<R} \frac{\sin x}{x}\dx$.
:::

:::

:::

:::
