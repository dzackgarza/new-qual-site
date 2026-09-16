---
schema: qual/card@1
id: C-C2GYX
kind: corollary
title: Inseparable irreducible polynomials are polynomials in $x^p$
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Polynomials
relations: []
review: draft
---

::: {.corollary}
Let $k$ be a field of [[D-JNCUB|characteristic]] $p > 0$, and let $f\in k[x]$ be [[D-BVMTZ|irreducible]].
Then $f$ is inseparable if and only if $f(x) = g(x^p)$ for some $g\in k[x]$.
Moreover, there are a unique integer $n \geq 0$ and an irreducible [[D-ZT46D|separable]] polynomial $g\in k[x]$ with $f(x) = g(x^{p^n})$, and $f$ is inseparable if and only if $n \geq 1$.
:::

::: {.proof}
A polynomial has a repeated root in a splitting field if and only if it shares a root with its derivative.
Since $f$ is irreducible, $f$ shares a root with $f'$ if and only if $f \divides f'$, and since $\deg f' < \deg f$ this holds if and only if $f' = 0$.
Writing $f = \sum_i a_i x^i$, we have $f' = \sum_i i a_i x^{i-1}$, which vanishes if and only if $a_i = 0$ whenever $p \nmid i$, that is, if and only if $f(x) = g(x^p)$ for some $g\in k[x]$.

For the second statement, let $n$ be the largest integer with $f\in k[x^{p^n}]$; it exists because $\deg f \geq 1$.
Write $f(x) = g(x^{p^n})$.
A factorization of $g$ into nonconstant polynomials would give one of $f$, so $g$ is irreducible, and $g\notin k[x^p]$ by maximality of $n$, so $g$ is separable by the first statement.
Conversely, if $f(x) = g(x^{p^m})$ with $g$ separable and irreducible, then $g\notin k[x^p]$ by the first statement, so $f\notin k[x^{p^{m+1}}]$ and $m = n$.
Finally, $n\geq 1$ if and only if $f\in k[x^p]$, which by the first statement holds if and only if $f$ is inseparable.
:::
