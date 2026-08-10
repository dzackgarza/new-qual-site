---
schema: qual/card@1
id: T-RA-WORKSHOP-D5-4-3
kind: theorem
title: 'Theorem 4.3: Taylor’s theorem with remainder'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.theorem title="Theorem 4.3 (Taylor’s Theorem)"}
Suppose $f:[a,b]\to\mathbb R$ is $n$ times continuously differentiable on $[a,b]$,
$f^{(n+1)}$ exists on $(a,b)$, and $c\in[a,b]$. Then, for any $x\in[a,b]$ with $x\ne c$ there exists
some $\xi$ between $c$ and $x$ so that
$$
f(x)=f(c)+f'(c)(x-c)+\cdots+\frac{f^{(n)}(c)}{n!}(x-c)^n
      +\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}.
$$
In particular, if $|f^{(n+1)}(x)|\le M$ on $[a,b]$ then
$$|f(x)-P_n(x)|\le\frac{M|x-c|^{n+1}}{(n+1)!}$$
for all $x\in[a,b]$.
:::
