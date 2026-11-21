---
schema: qual/card@1
id: FE-O47RH
kind: example
title: $e^z$ is conformal on $\CC$ but not injective
prompts:
- Give a conformal map that is not injective.
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Counterexamples
relations: []
review: draft
---

::: {.example}
A [[D-TM4TE|conformal map]] need not be injective.
The map $f\colon\CC\to\CC$, $f(z)=e^z$, is holomorphic with $f'(z)=e^z\neq0$ for all $z$, so it is conformal on $\CC$.
It is not injective because it is periodic: $e^{z+2\pi i}=e^z$.
It is also not surjective, since $e^z\neq0$ for all $z\in\CC$.

The two facts are those of [@Ahl73, ch. 2, §3.3, The Periodicity], which shows that a period of $e^z$ satisfies $e^c=1$, so that the periods are the numbers $2\pi i n$ with $n$ integral and the map is not injective; and of [@Ahl73, ch. 3, §2.3, Conformal Mapping], which shows that an analytic function with nonvanishing derivative preserves angles at each point, so $f(z)=e^z$, whose derivative is everywhere nonzero, is conformal on $\CC$.
:::
