---
schema: qual/card@1
id: P-CASP06D
kind: problem
title: "Finite order entire functions agreeing on a sufficiently dense sequence are equal"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Assume that $f$ and $g$ are entire functions of finite order $\lambda$.
Assume that for a sequence $a_n$, $f(a_n) = g(a_n)$ and $\sum |a_n|^{-(\lambda + \epsilon)} = \infty$ for some $\epsilon > 0$.
Show that $f = g$.
:::

::: {.solution}
Set $h=f-g$. Then $h$ is entire of order at most $\lambda$. Suppose that
$h\not\equiv0$. The points $a_n$ are zeros of $h$.

For an entire function of finite order at most $\lambda$, Jensen's formula
implies that for every $\delta>0$ its zero-counting function satisfies
\[
n_h(r)=O(r^{\lambda+\delta}).
\]
Take $\delta=\epsilon/2$. Ordering the nonzero zeros of $h$ by increasing
modulus and using the standard Stieltjes-integral identity,
\[
\sum_{|a_n|\ge1}|a_n|^{-(\lambda+\epsilon)}
=(\lambda+\epsilon)
\int_1^\infty
\frac{n_h(t)}{t^{\lambda+\epsilon+1}}\,dt,
\]
up to the harmless finite contribution of zeros in $|z|<1$. The estimate on
$n_h$ makes the integral converge, because
\[
\frac{n_h(t)}{t^{\lambda+\epsilon+1}}
=O(t^{-1-\epsilon/2}).
\]
Hence
\[
\sum |a_n|^{-(\lambda+\epsilon)}<\infty,
\]
contrary to the hypothesis. Therefore $h\equiv0$, i.e. $f=g$.
:::
