---
schema: qual/card@1
id: P-CAFA21B
kind: problem
title: "Polynomial approximation and polynomial hull of a compact set"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $K = \{ z \in \mathbb{C} : |z| \leq 3,\, |z-1| \geq 1,\, |z+1| \geq 1 \}$.

(i) True/false: every holomorphic function in a neighborhood of $K$ is the local uniform limit on $K$ of a sequence of polynomials.
Please justify your answer.

(ii) Determine, with justification, the set
$$
\widehat{K} = \{ z \in \mathbb{C} : |p(z)| \leq \sup_{w \in K} |p(w)| \text{ for all polynomials } p \}.
$$
:::

::: {.solution}
(i) False. The complement of $K$ has two bounded components, namely the open
unit disks centered at $1$ and $-1$. For instance,
\[
f(z)=\frac1{z-1}
\]
is holomorphic on a neighborhood of $K$ but cannot be uniformly approximated
there by polynomials.

Indeed, if $p_n\to f$ uniformly on $K$, then
\[
q_n(z)=(z-1)p_n(z)-1
\]
converges uniformly to $0$ on $K$. But $1$ lies in the polynomial hull of $K$,
so
\[
|q_n(1)|\le \sup_K|q_n|.
\]
The left side is $1$, a contradiction.

(ii) In one complex variable, the polynomial hull of a compact set is obtained
by filling in all bounded components of its complement. Here filling the two
holes gives the whole closed disk of radius $3$. Thus
\[
\boxed{\widehat K=\{z:|z|\le3\}.}
\]
:::
