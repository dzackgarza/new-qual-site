---
schema: qual/card@1
id: E-SS3.EX-4
kind: problem
title: $\int_{-\infty}^\infty\frac{x\sin x}{x^2+a^2}\,dx=\pi e^{-a}$
classification:
  areas:
    - complex-analysis
  topics: [Residue Theorem, Contour Integration, Fourier Integrals]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Lamport structure over the prose that was already there. The Jordan bound is
      now proved rather than named, with the estimate sin(theta) >= 2 theta / pi on
      the first quadrant; the residue is computed from the limit definition; and
      the passage from the contour integral to the improper integral on the real
      axis is justified, both by the vanishing semicircle and by the convergence of
      the two real improper integrals, which is conditional and so is stated. Not
      checked: the book's own text of the exercise, which is not retained in this
      checkout; the statement is as transcribed on the card. No retained solution
      set covers the exercise (the collection's provenance is a Google Books
      record), so the argument is the card's own. No statement repair.
---

::: {.exercise}
Show that
$$
\int_{-\infty}^{\infty} \frac{x\sin x}{x^2 + a^2}\, dx = \pi e^{-a}, \quad \text{for all } a > 0.
$$
:::

::: {.solution}
The statement is Exercise 4 of [@SS03, ch. 3 (p. 103)], printed as $\int_{-\infty}^\infty\frac{x\sin x}{x^2+a^2}\,dx=\pi e^{-a}$ for $a>0$. No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Let $a>0$ and put
$$
F(z)=\frac{z\,e^{iz}}{z^2+a^2},
$$
which is meromorphic on $\CC$ with poles exactly where $z^2+a^2=0$. For $R>a$ let $\Gamma_R$ be the closed contour running along $[-R,R]$ and back along the upper semicircle $C_R=\{Re^{i\theta}:0\le\theta\le\pi\}$. All integrals below are oriented counterclockwise.

::: pf

::: {.pf-step #poles}
$F$ has no pole on $\RR$, and its only pole in the upper half-plane is $z=ia$, a simple pole.

::: pf-proof
$z^2+a^2=(z-ia)(z+ia)$ and $a>0$, so the zeros of the denominator are $ia$ and $-ia$; these are distinct, each factor is simple, and the numerator does not vanish at either (the numerator vanishes only at $z=0$). Hence both poles are simple, $-ia$ lies in the lower half-plane, and no pole is real. So $F$ is holomorphic on a neighbourhood of $\Gamma_R$ and of its interior for every $R>a$.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=ia}F(z)=\dfrac{e^{-a}}{2}$.

::: pf-proof
For a simple pole the residue is $\lim_{z\to ia}(z-ia)F(z)=\lim_{z\to ia}\dfrac{z\,e^{iz}}{z+ia}$, and by continuity of the numerator and denominator at $ia$ this limit is
$$
\frac{ia\,e^{i\cdot ia}}{ia+ia}=\frac{ia\,e^{-a}}{2ia}=\frac{e^{-a}}{2},
$$
using $i\cdot ia=-a$ and $e^{-a}\in\RR$.
:::

:::

::: {.pf-step #jordan}
$\displaystyle\lim_{R\to\infty}\int_{C_R}F(z)\,dz=0$.

::: pf-proof
On $C_R$ one has $\abs{e^{iz}}=e^{-\operatorname{Im}z}=e^{-R\sin\theta}$ and
$$
\abs{\frac{z}{z^2+a^2}}=\frac{R}{\abs{R^2e^{2i\theta}+a^2}}\le\frac{R}{R^2-a^2}=:M_R,
$$
which tends to $0$ as $R\to\infty$. Since $dz=iRe^{i\theta}d\theta$,
$$
\abs{\int_{C_R}F(z)\,dz}\le M_R\int_0^{\pi}e^{-R\sin\theta}R\,d\theta .
$$
Split at $\pi/2$ and use $\sin\theta\ge2\theta/\pi$ for $0\le\theta\le\pi/2$, which gives $\sin\theta\ge 2(\pi-\theta)/\pi$ on the other half by symmetry:
$$
\int_0^{\pi}e^{-R\sin\theta}R\,d\theta\le 2R\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta=2R\cdot\frac{\pi}{2R}\bigl(1-e^{-R}\bigr)\le\pi .
$$
Hence $\abs{\int_{C_R}F\,dz}\le\pi M_R\to0$.
:::

:::

::: {.pf-step #contour}
For every $R>a$,
$$
\int_{-R}^{R}F(x)\,dx+\int_{C_R}F(z)\,dz=2\pi i\operatorname{Res}_{z=ia}F(z)=\pi i\,e^{-a}.
$$

::: pf-proof
$F$ is holomorphic on a neighbourhood of the closed contour $\Gamma_R$ and of its interior except at the single simple pole $ia$ inside, by step [](#poles){.pf-ref}. The residue theorem gives $\oint_{\Gamma_R}F=2\pi i\operatorname{Res}_{ia}F$, which is the displayed identity after evaluating the residue by step [](#residue){.pf-ref} and splitting the contour integral into its two pieces.
:::

:::

::: {.pf-step #real}
$\displaystyle\int_{-\infty}^{\infty}\frac{x\,e^{ix}}{x^2+a^2}\,dx=\pi i\,e^{-a}$, the improper integral converging.

::: pf-proof
Let $R\to\infty$ in step [](#contour){.pf-ref}. The semicircular contribution tends to $0$ by step [](#jordan){.pf-ref}. For the real piece, $F(x)=\dfrac{x\cos x}{x^2+a^2}+i\dfrac{x\sin x}{x^2+a^2}$ with $\dfrac{x}{x^2+a^2}$ real, decreasing to $0$ for $x$ large, and $\cos$, $\sin$ have bounded primitives, so each of the two real improper integrals converges by Dirichlet's test; the convergence is conditional, not absolute, since $\abs{x}/(x^2+a^2)$ is comparable to $1/x$ at infinity. So the limit of the real pieces exists and equals $\pi i\,e^{-a}$.
:::

:::

::: {.pf-step}
$\displaystyle\int_{-\infty}^{\infty}\frac{x\sin x}{x^2+a^2}\,dx=\pi e^{-a}$.

::: pf-proof
Taking imaginary parts in step [](#real){.pf-ref} is legitimate because the improper integral there converges, and the imaginary part of the integrand is the integrand on the left, while $\operatorname{Im}\bigl(\pi i\,e^{-a}\bigr)=\pi e^{-a}$ because $e^{-a}\in\RR$. Hence the displayed identity, for every $a>0$.
:::

:::

:::

:::

::: {.remark title="Variations"}
At $a=1$ the main statement gives $\int_\RR\frac{x\sin x}{1+x^2}\,dx=\frac{\pi}{e}$.
:::
