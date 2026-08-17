---
schema: qual/card@1
id: P-LIA5G
kind: problem
title: Maximum modulus principle and zeros when $|f|$ is constant on $\partial U$
classification:
  areas:
  - complex-analysis
  topics:
  - maximum-modulus-principle
  - open-mapping-theorem
  - zeros
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose that $U$ is a bounded, open and simply connected domain in $\mathbb{C}$ and that $f(z)$ is a complex-valued non-constant continuous function on $\bar{U}$ whose restriction to $U$ is holomorphic.

- Prove the maximum modulus principle by showing that if $z_{0} \in U$, then

$$
\left|f\left(z_{0}\right)\right|<\sup \{|f(z)|: z \in \partial U\} .
$$

- Show furthermore that if $|f(z)|$ is constant on $\partial U$, then $f(z)$ has a zero in $U$ (i.e., there exists $z_{0} \in U$ for which $f\left(z_{0}\right)=0$ ).
:::

::: {.solution}
Let $M\da \sup_{z\in \bd U}\abs{f(z)}$.
If $M=0$, then $f$ must be the constant zero function, so assume $M>0$.

Suppose toward a contradiction that there exists a $z_0 \in U$ with $\abs{f(z_0)} = M$.
Note that the map $z\mapsto \abs{z}$ is an open in discs that don't intersect $z=0$.
Since $f$ is holomorphic, by the open mapping theorem $f$ is an open map, so consider $D_\eps(z_0)$ a small disk not containing $0$.
Then $f(D_\eps(z_0))$ is open, and the composition $z\mapsto f(z) \mapsto \abs{f(z)}$ is an open map $D_\eps(z_0)\to \RR$.
Now if $f$ is nonconstant, $\abs{f(D_\eps(z_0))} \contains (M-\eps, M+\eps)$ contains some open interval about $M$, which contradicts maximality of $f$ at $z_0$.

> See notes for a proof using the mean value theorem.

Suppose toward a contradiction that $f$ has no zeros in $U$.
Then $g(z) \da 1/f(z)$ is holomorphic in $U$.
Now if $\abs{f(z)} = C$ on $\bd U$, we have $\abs{g(z)} = \abs{1\over f(z)} = {1\over C}$ on $\bd U$, so $\max_{z\in U} \abs{f(z)} = C$ and $\min_{\abs{f(z)}} = {1\over C}$.
Since $\abs{f(z)}$ is constant on the boundary, we must have $\max \abs{f(z)} = \min \abs{f(z)} = C$, so $f$ is constant on $\bd U$.
By the identity principle, $f$ is constant on $U$, a contradiction.
:::
