---
schema: qual/card@1
id: P-JWEN2
kind: problem
title: 'Dini''s theorem: monotone continuous functions decreasing to $0$ on $[0,1]$
  converge uniformly'
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Continuity
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of continuous functions $f_n: [0, 1]\to \RR$ such that
$$
f_n(x) \geq f_{n+1}(x) \geq 0 \quad \forall n\in \NN,\, \forall x\in [0, 1]
.$$
Prove that if $\theset{f_n}$ converges pointwise to $0$ on $[0, 1]$ then it converges to $0$ uniformly on $[0, 1]$.
:::

::: {.solution}
Fix $\varepsilon>0$ and let $U_n=\{x\in[0,1]: f_n(x)<\varepsilon\}$.

::: pf

::: {.pf-step #cover}
The $U_n$ are open in $[0,1]$, increasing, and cover $[0,1]$.

::: pf-proof
$U_n$ is open because $f_n$ is continuous, and $U_n \subseteq U_{n+1}$ because $f_{n+1}\le f_n$.
Since $f_n(x) \to 0$, every $x$ lies in some $U_n$.
:::

:::

::: pf-step
There is $N$ with $0 \leq f_n(x) < \varepsilon$ for all $n \geq N$ and all $x\in[0,1]$.

::: pf-proof
By step [](#cover){.pf-ref} and compactness of $[0,1]$, finitely many $U_n$ cover $[0,1]$, and since they increase, $U_N = [0,1]$ for the largest index $N$ among them.
For $n\ge N$, $0\le f_n(x)\le f_N(x)<\varepsilon$.
:::

:::

:::
:::
