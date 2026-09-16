---
schema: qual/card@1
id: FF-Z3E3C
kind: fact
title: Bernoulli's inequality
prompts:
- State Bernoulli's inequality and say for which $x$ and $n$ it holds.
classification:
  areas:
  - real-analysis
  topics:
  - Bernoulli
relations: []
review: draft
---

::: {.fact}
Let $x\in\RR$.

1. If $n\geq 0$ is an integer and $x\geq -1$, then $(1+x)^n \geq 1 + nx$.

2. If $n\geq 0$ is an even integer, then $(1+x)^n \geq 1 + nx$ for every $x\in\RR$.

3. If $r\geq 1$ is real and $x\geq -1$, then $(1+x)^r \geq 1 + rx$.
:::

::: {.proof}
(1) By induction on $n$: the case $n = 0$ is $1\geq 1$, and if $(1+x)^n\geq 1+nx$, then since $1+x\geq 0$,
$$
(1+x)^{n+1}\geq(1+nx)(1+x) = 1 + (n+1)x + nx^2\geq 1+(n+1)x.
$$

(2) For $x\geq -1$ this is (1). For $x<-1$ and even $n\geq 2$, $(1+x)^n\geq 0$ while $1+nx<1-n<0$; the case $n=0$ is $1\geq 1$.

(3) The function $\varphi(t)\coloneqq(1+t)^r$ is convex on $[-1,\infty)$ because $\varphi''(t) = r(r-1)(1+t)^{r-2}\geq 0$ for $t>-1$ and $\varphi$ is continuous at $-1$, so $\varphi$ lies above its tangent line $1+rt$ at $t = 0$.
:::

::: {.corollary}
For all $x\in\RR$,
$$
1-x \leq e^{-x} .
$$
:::
