---
schema: qual/card@1
id: E-GAGCW
kind: problem
title: Schwarz–Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
---

:::{.problem}
Suppose $f:\DD\to \DD$ is analytic.
Prove that 
\[  
\forall a\in \DD, \qquad {\abs{f'(a)} \over 1 - \abs{f(a)}^2 } \leq {1 \over 1 - \abs{a}^2}
.\]

:::

:::{.solution}


:::{.claim}
Holomorphic maps on $\DD$ contract Blaschke factors:
\[
\abs{ \psi_w(z) } \geq \abs{\psi_{f(w)}(f(z)) } 
,\]
i.e. 
\[
\abs{f(w) - f(z) \over 1 - \bar{f(w)}f(z)} \leq \abs{w-z \over 1-\bar{w} z}
.\]
:::

:::{.proof}
Make a change of variables $a\da \psi_w(z)$ so $z=\psi_w\inv(a) = \psi_w(a)$, then the desired inequality follows if we can show
\[
\abs{ \psi_{f(w)}(f(\psi_w(a))) } \leq \abs{a}
.\]

So define $F \da \psi_{f(w)} \circ f \circ \psi_w$, then since $\psi_w(0) = w$,
\[
F(0) = \psi_{f(w)}(f(w)) = 0
.\]
Moreover $\abs{F(z)}\leq 1$ since each constituent is a map $\DD\to \DD$.
So $F$ satisfies Schwarz and the claim follows.
:::

Given this, there's just a clever rearrangement to obtain the stated result:
\[
\abs{f(w) - f(z) \over 1 - \bar{f(w)}f(z)} 
&\leq \abs{w-z \over 1-\bar{w} z} \\
\implies 
\abs{ 1\over 1-\bar{f(w)}f(z) } \cdot \abs{f(z) - f(w) \over z-w} 
&\leq \abs{1\over 1-\bar{w}z} \\
    ,\]
and taking $z\to w$ on both sides yields
\[
{\abs{f'(w)}\over 1 - \abs{f(w)}^2 } \leq {1\over 1-\abs{w}^2}
\implies
\abs{f'(w)} \leq {1-\abs{f(w)}^2\over 1-\abs{w}^2 }
.\]

:::
