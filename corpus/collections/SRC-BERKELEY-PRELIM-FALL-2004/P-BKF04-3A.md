---
schema: qual/card@1
id: P-BKF04-3A
kind: problem
title: A nonconstant entire $f$ composed with an essential singularity of $g$ gives an essential singularity
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f$ and $g$ be functions that are holomorphic on all of $\CC$, except that $g$ has an essential singularity at the complex number $c$. Prove that either $f$ is constant, or the composition $f\circ g$ has an essential singularity at $c$. (Hint: you may assume the Casorati-Weierstrass Theorem, which states that if a function $f$ has an essential singularity at $c$, then for any punctured neighborhood $N$ of $c$ on which $f$ is holomorphic, the image $f(N)$ is dense in $\CC$.)
:::

::: {.solution}

The argument is the card's own: Casorati--Weierstrass makes $g(N)$ dense, and a nonconstant $f$ then has two distinct cluster values along any punctured neighbourhood.

::: pf

::: {.pf-step #distinct}

If $f$ is not constant, there are $a,b\in\CC$ with $f(a)\ne f(b)$.

::: pf-proof

A constant function takes one value; a nonconstant entire function takes at least two distinct values, since if $f(\CC)=\{w\}$ then $f$ is the constant $w$. Choose $a\ne b$ with $f(a)\ne f(b)$ if the two values occur at distinct points, and if not, note that a nonconstant $f$ cannot take exactly one value.

:::

:::

::: {.pf-step #dense}

For every punctured neighbourhood $N$ of $c$, the closures of $f(g(N))$ contain $f(a)$ and $f(b)$.

::: pf-proof

$g$ is holomorphic on $N$ with an essential singularity at $c$, so by Casorati--Weierstrass $g(N)$ is dense in $\CC$. There are thus sequences $z_{k}\to c$ inside $N$ with $g(z_{k})\to a$ and, along a subsequence, $g(z_{k})\to b$; more precisely, choose $w_{k}\in g(N)$ — say $w_{k}=g(z_{k})$ — with $w_{k}\to a$, and similarly $u_{k}=g(\zeta_{k})\to b$. Continuity of $f$ at $a$ and $b$ gives $f(w_{k})\to f(a)$ and $f(u_{k})\to f(b)$, and $f(w_{k}),f(u_{k})\in f(g(N))$. So both $f(a)$ and $f(b)$ lie in the closure of $f(g(N))$.

:::

:::

::: {.pf-step #nolimit}

$\lim_{z\to c}f(g(z))$ neither exists in $\CC$ nor equals $\infty$.

::: pf-proof

Suppose the limit existed and equalled $L\in\CC$. Then for every neighbourhood $N$ of $c$, the closure of $f(g(N))$ would be contained in an arbitrarily small disc around $L$, hence would be a single point at best; but by step [](#dense){.pf-ref} it contains the two distinct points $f(a)\ne f(b)$ of step [](#distinct){.pf-ref}. So the limit does not exist as a complex number. It is not $\infty$ either: the limit is $\infty$ only if $\abs{f(g(z))}\to\infty$, which fails since $\abs{f(w_{k})}\to\abs{f(a)}<\infty$ along $w_{k}\to a$.

:::

:::

::: {.pf-step #conclusion}

$f\circ g$ has an essential singularity at $c$.

::: pf-proof

$f\circ g$ is holomorphic on a punctured neighbourhood of $c$, the image of $g$ avoiding nothing that matters: $g$ is holomorphic on $\CC$ except at $c$, so $f\circ g$ is holomorphic there. An isolated singularity is removable, a pole, or essential; step [](#nolimit){.pf-ref} rules out the first two, since a removable singularity gives a finite limit and a pole gives the limit $\infty$. Hence
$$
\boxed{f \text{ nonconstant}\implies f\circ g \text{ has an essential singularity at } c.}
$$

:::

:::

:::

:::
