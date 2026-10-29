---
schema: qual/card@1
id: P-TRIV-DE18
kind: problem
title: Charge distribution of the Yukawa potential $e^{-ar}/r$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the charge distribution that gives the electrostatic potential

$$
\varphi ( x , y , z ) = { \frac { Z } { 4 \pi \varepsilon _ { 0 } } } { \frac { e ^ { - a r } } { r } }\tag{27}
$$
:::

::: {.solution}

Let $r=\sqrt{x^2+y^2+z^2}$ and let $\delta_0$ denote the Dirac delta distribution at the origin in $\RR^3$.

::: pf

::: {.pf-step #s1-1}

For $r>0$,
\[
\nabla^2\left(\frac{e^{-ar}}r\right)=a^2\frac{e^{-ar}}r.
\]


::: pf-proof

For a radial function $f(r)$ in three dimensions,
\[
\nabla^2 f=f''+\frac2r f'.
\]
Taking $f(r)=e^{-ar}/r$ gives
\[
f'(r)=-e^{-ar}\left(\frac a r+\frac1{r^2}\right)
\]
and
\[
f''(r)=e^{-ar}\left(\frac{a^2}r+\frac{2a}{r^2}+\frac2{r^3}\right).
\]
Substitution cancels the $r^{-2}$ and $r^{-3}$ terms and leaves $a^2e^{-ar}/r$.

:::

:::

::: {.pf-step #s1-2}

Distributionally on $\RR^3$,
\[
\nabla^2\left(\frac{e^{-ar}}r\right)
=a^2\frac{e^{-ar}}r-4\pi\delta_0.
\]


::: pf-proof

Step [](#s1-1){.pf-ref} determines the ordinary-function part away from the origin. To determine the singular term, integrate the Laplacian over the ball $B_\epsilon$ and use the divergence theorem:
\[
\int_{B_\epsilon}\nabla^2\left(\frac{e^{-ar}}r\right)dV
=4\pi\epsilon^2\left[-e^{-a\epsilon}\left(\frac a\epsilon+\frac1{\epsilon^2}\right)\right]
\longrightarrow -4\pi
\]
as $\epsilon\to0^+$. The locally integrable term $a^2e^{-ar}/r$ has integral tending to $0$ over $B_\epsilon$. Hence the singular contribution is $-4\pi\delta_0$.

:::

:::

::: {.pf-step #s1-3}

The charge density is
\[
\boxed{\rho(\mathbf r)=Z\delta_0(\mathbf r)-\frac{Za^2}{4\pi}\frac{e^{-ar}}r}.
\]


::: pf-proof

Poisson's equation in SI units is
\[
\nabla^2\varphi=-\frac\rho{\varepsilon_0}.
\]
Using the given potential and step [](#s1-2){.pf-ref},
\[
\nabla^2\varphi
=\frac{Z}{4\pi\varepsilon_0}
\left(a^2\frac{e^{-ar}}r-4\pi\delta_0\right).
\]
Multiplying by $-\varepsilon_0$ gives the displayed charge distribution.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the charge distribution whose Poisson equation produces the stated potential.

:::

:::

:::
