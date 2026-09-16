---
schema: qual/card@1
id: FF-MUJDE
kind: fact
title: Cyclotomic polynomial $\Phi_p$ for a prime $p$
prompts:
- What is the cyclotomic polynomial $\Phi_p(x)$ for $p$ prime?
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Polynomials
relations: []
review: draft
---

::: {.fact}
For a prime $p$, the [[D-BLV6F|cyclotomic polynomial]] $\Phi_p$ is
$$
\Phi_p(x)=\frac{x^p-1}{x-1}=1+x+x^2+\cdots+x^{p-1}.
$$
:::

::: {.proof}
The roots of $x^p-1$ are the $p$th roots of unity, and every one of them other than $1$ is primitive because $p$ is prime.
So $x^p-1=(x-1)\Phi_p(x)$, and dividing by $x-1$ with [[FF-ED3CD]] at $a=1$ gives the sum.
:::
