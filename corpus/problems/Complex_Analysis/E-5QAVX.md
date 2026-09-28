---
schema: qual/card@1
id: E-5QAVX
kind: problem
title: $\abs{f''(0)}\le2$ for a self-map of $\DD$ with $f(0)=f'(0)=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Cauchy Estimates
  - Zeros
relations: []
review: draft
---

::: {.exercise}
Let $f:\DD\to \DD$ with $f(0) = f'(0) = 0$.
Show that $\abs{f''(0)} \leq 2$ and describe all $f$ for which this is an equality.

:::

::: {.solution}
By Schwarz, $\abs{f(z)}\leq \abs z$.
Write $g(z) \da f(z)/z$, which is holomorphic on $\DD$ since $f$ has a zero of order at least one at $0$, and $\abs{g(z)}\leq 1$.
Write $f(z) = \sum_k c_kz^k$; then $c_0 = 0$ since $f(0) = 0$ and $c_1 = 0$ since $f'(0) = 0$, so $f(z)=c_2z^2 + \bigo(z^3)$.
Thus $g(z) = c_2z + \bigo(z^2)$ and $g(0) = 0$. By the maximum modulus principle, the nonconstant function $g$ with $\abs g\le1$ satisfies $\abs g<1$ on $\DD$ (and $g\equiv0$ if $g$ is constant), so $g:\DD\to\DD$ and Schwarz applies:

- $\abs{g(z)}\leq \abs{z}$
- $\abs{g'(0)} \leq 1$

We have $g'(z) = c_2 + \bigo(z)$ so $g'(0) = c_2 = {f^{(2)}(0) \over 2!}$.
\[
1 \geq \abs{g'(0)} = \abs{c_2} = \abs{f^{(2)}(0) \over 2} \implies \abs{ f^{(2)}(0) } \leq 2!
.\]

Suppose this is an equality -- then Schwarz on $g$ shows $g$ is a rotation, so
\[
{f(z)\over z} = g(z) = \lambda z \implies f(z) = \lambda z^2 \qquad \lambda \in S^1
.\]
Conversely, $f(z)=\lambda z^2$ with $\abs\lambda=1$ satisfies the hypotheses and $\abs{f''(0)}=2$.
:::
