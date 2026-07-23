---
schema: qual/card@1
id: P-PHC7M
kind: problem
title: "Let $f(z)$ be entire and assume that $\\abs{f(z)} \\leq M |z|^2$ outside\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $f(z)$ be entire and assume that $\abs{f(z)} \leq M |z|^2$ outside of some disk for some constant $M$. 
Show that $f(z)$ is a polynomial in $z$ of degree $\leq 2$.
:::


:::{.solution}
\envlist

- Prove a more general statement: if $\abs{f(z)} \leq M\abs{z}^n$, then $f$ is a polynomial of degree at most $n$.
- Since $f$ is entire, it is analytic everywhere, so $f(z) = \sum_{k\geq 0}c_k z^k$ where $c_k = f^{(k)}(0)/n!$ is given by the coefficient of its Taylor expansion about $z=0$.
- Applying Cauchy's estimate, on a circle of radius $R$, 
\[
\abs{f^{(k)}(0)} \leq { \sup_{\gamma}\abs{f(z)} n! \over R^k} \leq {M\abs{z}^n n! \over R^k} = {M R^n n! \over R^k} 
.\]

- So for $k \geq n+1$, this goes to zero as $R\to \infty$, so $\abs{f^{k}(0)} = 0$ for all such $k$.
- But then $f$ is a power series annihilated by taking $n+1$ derivatives, so it is a polynomial of degree at most $n$.
:::

