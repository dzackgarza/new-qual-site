---
schema: qual/card@1
id: P-CIEHS
kind: problem
title: Holomorphic self-maps of the disk with a zero of order $k$ at $0$ and $\abs{f}\to
  1$ at the boundary
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source misspells "satisfies" as "satsifies".'
---

::: {.problem}
Suppose $f:\DD\to\DD$ is analytic, has a single zero of order $k$ at $z=0$, and satisfies $\lim_{\abs z \to 1} \abs{f(z)} = 1$.
Give with proof a formula for $f(z)$.
:::

::: {.solution}

The hypothesis says that $0$ is the only zero of $f$ and that it has order $k$.
The answer is $f(z)=\alpha z^k$ with $\abs{\alpha}=1$.

::: pf

::: {.pf-step #define-h}
$h(z)\coloneqq f(z)/z^k$ is holomorphic and zero-free on $\DD$.

::: pf-proof
The zero of $f$ at $0$ has order $k$, so the singularity of $h$ at $0$ is removable with $h(0)\ne0$, and $f$ has no other zeros.
:::

:::

::: {.pf-step #boundary}
$\abs{h(z)}\to1$ as $\abs{z}\to1$.

::: pf-proof
$\abs{h(z)}=\abs{f(z)}/\abs{z}^k$, and both $\abs{f(z)}\to1$ and $\abs{z}^k\to1$.
:::

:::

::: {.pf-step #unimodular}
$\abs{h}\equiv1$ on $\DD$.

::: pf-proof
Let $\varepsilon>0$.
By step [](#boundary){.pf-ref} there is $r_0<1$ with $1-\varepsilon<\abs{h}<1+\varepsilon$ on $r_0<\abs{z}<1$.
For $r_0<r<1$, the maximum modulus principle applied to $h$ and to $1/h$, which is holomorphic by step [](#define-h){.pf-ref}, gives $1-\varepsilon\le\abs{h}\le1+\varepsilon$ on $\abs{z}\le r$.
Since $\varepsilon$ is arbitrary, $\abs{h}\equiv1$.
:::

:::

::: pf-step
$f(z)=\alpha z^k$ for a constant $\abs{\alpha}=1$, and every such function satisfies the hypotheses.

::: pf-proof
By step [](#unimodular){.pf-ref} and the open mapping theorem, $h$ is a constant $\alpha$ of modulus $1$.
Conversely, $\alpha z^k$ maps $\DD$ into $\DD$, vanishes only at $0$, to order $k$, and has modulus $\abs{z}^k\to1$.
:::

:::

:::

:::
