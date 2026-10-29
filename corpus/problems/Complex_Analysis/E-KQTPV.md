---
schema: qual/card@1
id: E-KQTPV
kind: problem
title: Injective conformal maps from $\{\Re z>0,\ |z-1|>1\}$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Biholomorphisms
  - Blaschke Factors
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source asks for "all of the injective conformal maps G -> D"; injective maps into D that are not onto form no describable list, so the statement asks for maps of G onto D, as the title does. The earlier solution described Aut(G) through an incorrect map; it is replaced.
---

::: {.problem}
Define
$$
G \coloneqq \theset{z\in \CC\suchthat \Re(z) > 0, \, \abs{z-1} > 1}
.$$

Find all of the injective conformal maps of $G$ onto $\DD$.
These may be expressed as compositions of maps, but explain why this list is complete.
:::

::: {.solution}
::: pf

::: {.pf-step #strip}
$z\mapsto1/z$ maps $G$ bijectively onto the strip $S\coloneqq\theset{w\st0<\Re w<\frac12}$.

::: pf-proof
$z\mapsto1/z$ is a holomorphic involution of $\CC^\times$ and $0\notin G$. For $w=1/z$, $\Re z>0$ if and only if $\Re w>0$, and $\abs{z-1}>1$ if and only if $\abs{1-w}>\abs w$, that is, $\Re w<\frac12$.
:::

:::

::: {.pf-step #model}
$F(z)\coloneqq\dfrac{e^{2\pi i/z}-i}{e^{2\pi i/z}+i}$ is a biholomorphism of $G$ onto $\DD$.

::: pf-proof
By step [](#strip){.pf-ref}, compose: $w\mapsto2\pi iw$ maps $S$ onto the strip $\theset{0<\Im\zeta<\pi}$; $\zeta\mapsto e^\zeta$ maps that strip bijectively onto $\HH$; and the Cayley map $\eta\mapsto\frac{\eta-i}{\eta+i}$ maps $\HH$ onto $\DD$. Each map is a biholomorphism.
:::

:::

::: pf-step
The injective conformal maps of $G$ onto $\DD$ are exactly $\boxed{\psi\circ F}$ with $\psi(w)=\lambda\frac{w-a}{1-\bar aw}$, $\abs\lambda=1$, $a\in\DD$.

::: pf-proof
Each such $\psi$ lies in $\Aut(\DD)$, so $\psi\circ F$ is a biholomorphism onto $\DD$ by step [](#model){.pf-ref}. Conversely, if $\varphi:G\to\DD$ is an injective holomorphic surjection, then $\psi\coloneqq\varphi\circ F^{-1}\in\Aut(\DD)$ and $\varphi=\psi\circ F$. Every element of $\Aut(\DD)$ has the stated form.
:::

:::

:::

:::
