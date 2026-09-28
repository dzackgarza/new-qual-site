---
schema: qual/card@1
id: E-24ETT
kind: problem
title: $g(\{|z|<r\})\subseteq f(\{|z|<r\})$ when $f$ is injective holomorphic and
  $f(0)=g(0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Biholomorphisms
  - Conformal Maps
relations: []
review: draft
---

::: {.problem}
Suppose $f, g: \DD\to \Omega$ are holomorphic with $f$ injective and $f(0) = g(0)$.

Show that
\[
\Forall 0 < r < 1,\qquad g\qty{\theset{\abs{z} < r}} \subseteq f\qty{\theset{\abs{z} < r}}
.\]

> The first part of this problem asks for a statement of the Schwarz lemma.

:::

::: {.solution}
Assume that $f$ is a bijection $\DD\to\Omega$; the remark gives a counterexample without this hypothesis.

<1>1. $F\coloneqq \inverseof{f}\circ g$ is a holomorphic map $\DD\to\DD$ with $F(0)=0$.

::: {.proof}
The inverse $\inverseof{f}\colon\Omega\to\DD$ of the bijective holomorphic map $f$ is holomorphic, and $g(\DD)\subseteq\Omega$, so $F$ is defined and holomorphic on $\DD$ with values in $\DD$.
Since $g(0)=f(0)$, we have $F(0)=\inverseof{f}(f(0))=0$.
:::

<1>2. $\abs{F(z)}\le\abs{z}$ for all $z\in\DD$.

::: {.proof}
This is the Schwarz lemma applied to $F$, which step <1>1 permits.
:::

<1>3. Q.E.D.

::: {.proof}
Let $0<r<1$ and $\abs{z}<r$. By step <1>2, $w\coloneqq F(z)$ satisfies $\abs{w}<r$, so $g(z)=f(F(z))=f(w)\in f\qty{\theset{\abs{w}<r}}$.
:::
:::

::: {.remark}
The inclusion requires $f(\DD)=\Omega$.
For $\Omega=\CC$, $f(z)=z$ and $g(z)=2z$, the image $g\qty{\theset{\abs z<r}}$ is the disk of radius $2r$, which is not contained in $f\qty{\theset{\abs z<r}}$.
:::
