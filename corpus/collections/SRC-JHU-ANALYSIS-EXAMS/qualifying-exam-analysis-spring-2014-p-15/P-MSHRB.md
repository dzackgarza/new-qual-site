---
schema: qual/card@1
id: P-MSHRB
kind: problem
title: Nonzero smooth compactly supported function with compactly supported Fourier transform
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Fall 2013 problem 4 on PDF page 16; both the function and its Fourier transform are required to have compact support."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Justified holomorphic dependence of the Fourier integral by dominated differentiation on compact parameter sets, and verified the hypotheses for pointwise Fourier inversion."
---

::: {.problem}
Determine whether there is a nonzero smooth compactly supported function on $\mathbb{R}$ whose Fourier transform is also compactly supported?
:::

::: {.solution}
No. Let $f$ be smooth with $\operatorname{supp}f\subseteq[-S,S]$ and put $F(\zeta)\definedas\int_{-S}^Sf(x)e^{-2\pi ix\zeta}\,dx$ for $\zeta\in\CC$, so that $F=\widehat f$ on $\RR$.

::: pf

::: {.pf-step #s1}

$F$ is entire.

::: pf-proof

On $[-S,S]\times K$, for $K\subset\CC$ compact, the integrand and its $\zeta$-derivative are bounded by $\abs{f(x)}$ times $e^{2\pi S\sup_K\abs{\Im\zeta}}$ and $2\pi Se^{2\pi S\sup_K\abs{\Im\zeta}}$. Dominated convergence permits differentiation under the integral [@Fol13].

:::

:::

::: {.pf-step #s2}

If $\widehat f$ has compact support, then $F\equiv0$.

::: pf-proof

$F$ vanishes on a real interval outside the support of $\widehat f$, which has accumulation points, so $F\equiv0$ by the identity theorem and step [](#s1){.pf-ref} [@SS03].

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $\widehat f\equiv0$. A smooth compactly supported function is a Schwartz function, so Fourier inversion gives $f(x)=\int\widehat f(\xi)e^{2\pi ix\xi}\,d\xi=0$ for every $x$ [@SS03a].

:::

:::

:::
