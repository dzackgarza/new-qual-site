---
schema: qual/card@1
id: P-6VN3T
kind: problem
title: "Assume $f$ is an entire function such that $|f(z)|=1$ on $|z|=1$. Prov\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Assume $f$ is an entire function such that $|f(z)|=1$ on $|z|=1$. Prove that $f(z)=e^{i \theta} z^{n}$, where $\theta$ is a real number and $n$ a non-negative integer. 

> Suggestion: First use the maximum and minimum modulus theorem to show 
$$
f(z)=e^{i \theta} \prod_{k=1}^{n} \frac{z-z_{k}}{1-\bar{z_{k}} z}
$$ 
if $f$ has zeros.

:::

:::{.solution}
First show the hint: assume $f$ has nonzero zeros.
Write $Z(f) \da f\inv(0)$ for the set of zeros in $\bar{\DD}$.

:::{.claim}
If we assume $f$ is continuous on $\DD$, then $\size Z(f) < \infty$
:::

:::{.proof title="?"}
Suppose $\size Z(f) = \infty$, then by compactness of $\bar{\DD}$ there is a limit point $z_0$.
If $z_0 \in \DD$, then there is a sequence $\ts{z_k}\to z_0$ with $f(z_k) = 0$ for every $k$, so $f$ is zero on a set $S\da \ts{z_k}_{k\geq 1} \union \ts{z_0}$ with an accumulation point and this forces $f\equiv 0$ on $\bar{\DD}$ by the identity principle, contradicting $\abs{f} = 1$ on $\bd \DD$>

Otherwise, if $z_0\in \bd \DD$, using continuity of $f$ we have $f(z_k) = 0$ for all $k$ and $z_k\to z_0$ so $f(z_0) = 0$, again contradiicting $\abs{f} = 1$ on $\bd \DD$.
:::

So write $Z(f) = \ts{z_1,\cdots, z_m}$ and define 
\[
g(z) \da \prod_{1\leq k \leq m} {z-z_k \over 1 - \bar{z_k} z},
\quad
h(z) \da {f(z) \over g(z)}
.\]

:::{.claim}
$h(z) \equiv 1$ is constant on $\bar{\DD}$, so that $f = \lambda g$ for some $\lambda \in S^1$, i.e. $\lambda = e^{i\theta}$ for some $\theta$.
:::

:::{.proof title="?"}
Note that $h$ cancels all zeros of $f$, so $h$ is nonzero and holomorphic on $\bar{\DD}$.
Moreover $\abs{g(z)} \leq 1$ on $\bar{\DD}$ since these are well-known to be in $\Aut(\DD)$.
It's also well-known that $\abs{g(z)} = 1$ on $\bd \DD$.
Thus $\abs{h(z)} = 1$ and $\abs{1\over h(z)} =1$ on $\bd \DD$, and by the maximum modulus principle, 
\[
\abs{h(z)} \leq 1 \quad\text{ and }\quad \abs{1\over h(z)}\leq 1 \quad \text{ on } \DD
,\]
forcing $\abs{h(z)}\equiv 1$ and thus $h(z) = e^{i\theta}$ for some $\theta$.



:::

So we now have
\[
f(z) = e^{i\theta} \prod_{1\leq k\leq m} {z-z_k \over 1 -\bar{z_k} z}
,\]
which has poles at points $z$ for which $\bar{z_k}z=1$ for some $z_k\in Z(f)$.
However, since we assumed $f$ was entire, it can have no such poles, which forces $z_k = 0$ for all $k$.
But then
\[
f(z) = e^{i\theta}\prod_{1\leq k \leq m}{z- 0 \over 1 - 0\cdot z} = e^{i\theta}z^m
.\]


:::
