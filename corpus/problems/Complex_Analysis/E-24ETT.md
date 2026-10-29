---
schema: qual/card@1
id: E-24ETT
kind: problem
title: $g(\{|z|<r\})\subseteq f(\{|z|<r\})$ when $f\colon\DD\to\Omega$ is biholomorphic
  and $f(0)=g(0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Biholomorphisms
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Suppose $f, g: \DD\to \Omega$ are holomorphic with $f$ injective and $f(0) = g(0)$." This is false without $f(\DD)=\Omega$ (take $\Omega=\CC$, $f(z)=z$, $g(z)=2z$); the statement now requires $f$ to be a bijection onto $\Omega$. The source also noted that the first part of the problem asks for a statement of the Schwarz lemma.'
---

::: {.problem}
Suppose $f, g: \DD\to \Omega$ are holomorphic with $f$ a bijection onto $\Omega$ and $f(0) = g(0)$.

Show that
$$
\Forall 0 < r < 1,\qquad g\qty{\theset{\abs{z} < r}} \subseteq f\qty{\theset{\abs{z} < r}}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$F\coloneqq \inverseof{f}\circ g$ is a holomorphic map $\DD\to\DD$ with $F(0)=0$.

::: pf-proof

The inverse $\inverseof{f}\colon\Omega\to\DD$ of the bijective holomorphic map $f$ is holomorphic, and $g(\DD)\subseteq\Omega$, so $F$ is defined and holomorphic on $\DD$ with values in $\DD$.
Since $g(0)=f(0)$, we have $F(0)=\inverseof{f}(f(0))=0$.

:::

:::

::: {.pf-step #s2}

$\abs{F(z)}\le\abs{z}$ for all $z\in\DD$.

::: pf-proof

This is the Schwarz lemma applied to $F$, which step [](#s1){.pf-ref} permits.

:::

:::

::: pf-qed

Let $0<r<1$ and $\abs{z}<r$. By step [](#s2){.pf-ref}, $w\coloneqq F(z)$ satisfies $\abs{w}<r$, so $g(z)=f(F(z))=f(w)\in f\qty{\theset{\abs{w}<r}}$.

:::

:::

:::

::: {.remark}
The inclusion requires $f(\DD)=\Omega$, not only injectivity of $f$.
For $\Omega=\CC$, $f(z)=z$ and $g(z)=2z$, the image $g\qty{\theset{\abs z<r}}$ is the disk of radius $2r$, which is not contained in $f\qty{\theset{\abs z<r}}$.
:::
