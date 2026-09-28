---
schema: qual/card@1
id: P-W3PZY
kind: problem
title: In characteristic $p$, an irreducible polynomial is $g(x^{p^e})$ with $g$ separable,
  and every root has multiplicity $p^e$
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.problem}
Let $F$ be a field of characteristic $p>0$ and let $f\in F[x]$ be irreducible. Show that there are a unique integer $e\ge0$ and an irreducible separable polynomial $g\in F[x]$ such that
\[
f(x)=g(x^{p^e}),
\]
and that every root of $f$ in an algebraic closure has multiplicity $p^e$.
:::

::: {.solution}
Choose $e\ge0$ maximal such that every exponent occurring in $f$ is divisible by $p^e$. Then there is a unique polynomial $g\in F[x]$ with
\[
f(x)=g(x^{p^e}).
\]

The polynomial $g$ is irreducible. Indeed, if $g=uv$ with nonconstant $u,v\in F[x]$, then
\[
f(x)=u(x^{p^e})v(x^{p^e})
\]
would be a nontrivial factorization of $f$.

By maximality of $e$, not every exponent occurring in $g$ is divisible by $p$. Hence $g'\ne0$. Since $g$ is irreducible, $\gcd(g,g')=1$, so $g$ is separable.

Now work in an algebraic closure $\overline F$. Since $g$ is separable,
\[
g(y)=a\prod_{i=1}^r(y-\beta_i)
\]
with distinct $\beta_i$. For each $i$, choose $\alpha_i\in\overline F$ with $\alpha_i^{p^e}=\beta_i$. In characteristic $p$,
\[
x^{p^e}-\beta_i=x^{p^e}-\alpha_i^{p^e}=(x-\alpha_i)^{p^e}.
\]
Therefore
\[
f(x)=g(x^{p^e})
=a\prod_{i=1}^r(x-\alpha_i)^{p^e}.
\]
Thus every root of $f$ has multiplicity exactly $p^e$.

Uniqueness of $e$ follows from maximality of the common $p$-power dividing all occurring exponents; then $g$ is forced coefficient-by-coefficient.
:::
