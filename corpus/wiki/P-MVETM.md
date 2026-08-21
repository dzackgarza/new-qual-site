---
schema: qual/card@1
id: P-MVETM
kind: problem
title: If every irreducible in $F[x]$ is separable then every element of $F$ is a
  $p$-th power
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
solved: false
---

::: problem
Suppose all irreducible polynomials in $F[x]$ are separable.
Then let $a\in K$ be arbitrary, we will show that there exists some $\beta \in K$ such that $\beta^p = a$.

Given such an $a$, define the polynomial
$$
f(x) = x^p - a \in F[x].
$$

Note that $f$ is *not* separable, since $f'(x) = px^{p-1} = 0$ since $\mathrm{char}(F) = p$, which means (by assumption) that $f$ must be *reducible*.

Thus we can write $f(x) = g(x)h(x)$ where $g \in F[x]$ is some irreducible factor that divides $f$.

Noting that if $\beta \in \overline{F}$ is a any root of $f$, then
$$
f(\beta) = 0 \implies \beta^p = a \implies f(x) = x^p - a = x^p - \beta^p = (x-\beta)^p,
$$

and so $\beta$ is necessarily a multiple root.

Moreover, since $g\divides f$, we must have $g(x) = (x-\beta)^\ell$ for some $1 \leq \ell \leq p$.

But then we can expand $g$ using the binomial formula:
$$
g(x) = (x - \beta)^\ell = \sum_{k=1}^\ell {\ell \choose k}x^{\ell-k}(-\beta)^k = x^\ell + \cdots + (-\beta)^\ell \in F[x].
$$

But since every coefficient must be in $F$, we must have $\beta^\ell \in F$.
We know that $\beta^p = a \in F$ as well, but since $p$ is prime, $\gcd(p, \ell) = 1$.

We can thus find $s, t \in \ZZ$ such that $ps + t\ell = 1$.
But then

$$
\beta = \beta^1 = \beta^{ps + t\ell} = \beta^{st} \beta^{t\ell} = (\beta^\ell)^s (\beta^p)^t,
$$

where since $\beta^\ell, \beta^p \in F$, the entire RHS is in $F$, and thus the LHS $\beta\in F$ as well.

But then $\alpha = \beta^p$ where $\beta \in F$, which is exactly what we wanted to show.
:::
