---
schema: qual/card@1
id: E-MIIW7
kind: exercise
title: "Schwarz with domain/codomain scaled"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
relations: []
review: draft
---
:::{.exercise title="Schwarz with domain/codomain scaled"}
If $f: \DD_R(a)\to\DD_M(0)$ with $f(a) = 0$, then 
\[
\abs{f(z)}\leq {M\over R}\abs{z-a}
.\]

:::

:::{.solution}
Set $g(z) \da {f(Rz + a) \over M}$, then $g: \DD\to \DD$ with $g(0) = f(a)/M = 0$, so unwinding Schwarz yields
\[
\abs{g(z)} \leq \abs{z} 
\implies \abs{f(Rz+a)\over M}
&\leq \abs{z} \\
\implies \abs{f(Rz+a)} &\leq M\abs{z} \\
\implies \abs{f(w)} &\leq M\abs{w-a\over R} \qquad w = Rz+a\implies z={w-a\over R}
.\]
:::
