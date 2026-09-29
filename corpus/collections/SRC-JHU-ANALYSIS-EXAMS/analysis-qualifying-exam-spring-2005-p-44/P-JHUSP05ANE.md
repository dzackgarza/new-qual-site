---
schema: qual/card@1
id: P-JHUSP05ANE
kind: problem
title: "Nonzero C_c^∞ function with compactly supported Fourier transform"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.problem}
Do there exist functions $f \in \mathcal{C}_c^{\infty}(\mathbb{R})$ such that $f$ is not identically zero and $\widehat{f} \in \mathcal{C}_c^{\infty}(\mathbb{R})$?
If so, find one.
If not, prove that none exist.

Notation: $\mathcal{C}_c^{\infty}(\mathbb{R})$ denotes the compactly supported functions in $\mathcal{C}^{\infty}(\mathbb{R})$, and $\widehat{f}$ denotes the Fourier transform of $f$.
:::

::: {.solution}
No such function exists. Let $f\in\mathcal C_c^\infty(\RR)$ with $\operatorname{supp}f\subseteq[-M,M]$, and put $F(z)\da\int_{-M}^Mf(x)e^{-ixz}\,dx$ for $z\in\CC$, so that $F=\widehat f$ on $\RR$.

::: pf

::: {.pf-step #s1}

$F$ is entire.

::: pf-proof

The integrand is continuous on $[-M,M]\times\CC$ and holomorphic in $z$, and its $z$-derivative $-ixf(x)e^{-ixz}$ is bounded by $M\norm f_\infty e^{M\sup_K\abs{\Im z}}$ on $[-M,M]\times K$ for each compact $K\subset\CC$. Differentiation under the integral sign makes $F$ complex differentiable everywhere.

:::

:::

::: {.pf-step #s2}

If $\widehat f$ has compact support, then $F\equiv0$.

::: pf-proof

$F$ vanishes on $(R,\infty)$ for some $R$, a set with accumulation points, so $F\equiv0$ by the identity theorem and step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $\widehat f\equiv0$. Since $f$ and $\widehat f$ are integrable, the Fourier inversion theorem gives $f(x)=\frac1{2\pi}\int\widehat f(\xi)e^{ix\xi}\,d\xi=0$ for all $x$.

:::

:::

:::
