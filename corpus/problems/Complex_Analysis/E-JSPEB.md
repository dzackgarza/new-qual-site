---
schema: qual/card@1
id: E-JSPEB
kind: problem
title: Bound on $\abs{f(\frac{1+i}{2})}$ for a self-map of $\DD$ with $\abs{f}\le\abs{e^z}$ on
  $\abs z=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
---

::: {.exercise}
Suppose $f: \DD\to \DD$ with $f(0) = 0$ and $\abs{f(z)} \leq \abs{e^z}$ when $\abs{z} = 1$.
Find an upper bound for $f\qty{1+i\over 2}$.

:::

::: {.solution}
Assume $f$ extends continuously to $\overline\DD$, so that the boundary condition makes sense.
Consider $g(z) \definedas f(z)e^{-z}$, holomorphic on $\DD$ and continuous on $\overline\DD$ with $g(0) = 0$. On $\abs z=1$, $\abs{g(z)}\le1$, so by the maximum modulus principle $\abs g\le1$ on $\DD$; as $g(0)=0$, $g$ is not a unimodular constant, so $g(\DD)\subseteq\DD$. Schwarz applies and
\[
\abs{g(z)}\leq \abs{z} \implies \abs{f(z)} \leq \abs{z}\abs{e^z} = \abs z e^{\Re z}
.\]
So
\[
\abs{f\qty{1+i\over 2}} \leq \abs{1+i\over 2}e^{1/2}= {\sqrt{2e} \over 2}
.\]
:::
