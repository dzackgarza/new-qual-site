---
schema: qual/card@1
id: T-DAETF
kind: theorem
title: "Schwarz Lemma"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.theorem title="Schwarz Lemma" ref="SchwarzzLemma"}
If $f: \DD \to \DD$ is holomorphic with $f(0) = 0$, then

1. $\abs{f(z)} \leq \abs z$ for all $z\in \DD$
2. $\abs{f'(0)} \leq 1$.

Moreover, if 

- $\abs{f(z_0)} = \abs{z_0}$ for any $z_0\in \DD\smz$, or 
- $\abs{f'(0)} = 1$, 

then $f$ is a rotation, i.e. $f(z) = \lambda z$ for some $\abs{\lambda} = 1$.
:::
