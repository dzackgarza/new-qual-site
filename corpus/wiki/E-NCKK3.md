---
schema: qual/card@1
id: E-NCKK3
kind: exercise
title: "Let $\\bar B(a, r)$ denote the closed disc of radius $r$ about $a\\in \\CC$. Let $f$ be\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
  - cauchy-estimates
relations: []
review: draft
---
:::{.problem title="?"}
Let $\bar B(a, r)$ denote the closed disc of radius $r$ about $a\in \CC$.
Let $f$ be holomorphic on an open set containing $\bar B(a, r)$ and let 
\[  
M \definedas \sup_{z\in \bar B(a, r)} \abs{f(z)}
.\]

Prove that 
\[  
z\in \bar B\qty{a, {r\over 2}},\,z\neq a, \qquad {\abs{ f(z) - f(a)} \over \abs{z-a}} \leq {2M \over r}
.\]

:::

:::{.solution}
Set 
\[
g(z) \da {f(Rz+a) - f(a) \over 2M}
,\]
so that $g(0) = 0$ and $g:\DD\to \DD$ so Schwarz applies,
\[
\abs{g(z)} \leq \abs{z} 
\implies \abs{ f(Rz+a) - f(a) \over 2M } &\leq \abs{z} \\
\implies \abs{ f(Rz+a) - f(a) } &\leq 2M \abs{z} \\
\implies \abs{ f(w) - f(a) } &\leq 2M\abs{ w-a\over R} \\
\implies \abs{f(w) - f(a) \over w-a} &\leq {2M \over R}
.\]

:::
