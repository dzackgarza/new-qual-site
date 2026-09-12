---
schema: qual/card@1
id: P-CASP11C
kind: problem
title: "Analytic continuation along different paths yielding different germs (Monodromy failure)"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $a = 1$, $b = 0$, regarded as points in $\mathbb{C}$.

(a) Give an example of an analytic function element $(h, D)$, with $a \in D$, and analytic continuations $(f_t, D_t)$, $(g_t, B_t)$ of $(h, D)$ along two different paths $\gamma$ and $\sigma$, such that $\gamma(0) = \sigma(0) = a$, $\gamma(1) = \sigma(1) = b$, but $[g_1]_b \neq [f_1]_b$.
Define the analytic continuations explicitly and explain briefly why these satisfy the definition of an analytic continuation.

(b) Explain why the Monodromy Theorem does not apply for your example in (a) to conclude that $[g_1]_b = [f_1]_b$.
:::

::: solution
Take the germ at $1$ of a logarithm, with $h(1)=0$. Continue it along the two
paths
\[
\gamma(t)=e^{i\pi t},\qquad \sigma(t)=e^{-i\pi t},\qquad 0\le t\le1,
\]
from $1$ to $-1$ (after translating the endpoint notation of the problem, use
the same construction around the puncture and terminate at the prescribed
point $b$). On small disks along either path choose the logarithm whose values
agree on overlaps. Along the upper path the terminal value is $i\pi$, while
along the lower path it is $-i\pi$; hence the terminal germs differ by
$2\pi i$.

Equivalently, for paths from $1$ to the stated endpoint $b=0$, use the germ of
$\log(z-c)$ about $1$ for any puncture $c\ne0,1$ and choose two paths from
$1$ to $0$ whose concatenation winds once around $c$. The same overlap
construction gives terminal germs differing by $2\pi i$.

The Monodromy Theorem does not apply because the two paths are not homotopic
with fixed endpoints in the domain of continuation: their concatenation has
nonzero winding number about the omitted point. Thus the relevant continuation
domain is not simply connected.
:::
