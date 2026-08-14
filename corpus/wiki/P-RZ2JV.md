---
schema: qual/card@1
id: P-RZ2JV
kind: problem
title: "Let $R$ be a commutative ring, and let $M$ be an $R\\dash$module. An $R\\dash$\u2026"
classification:
  areas:
  - algebra
  topics:
  - modules
  - maximal-ideals
  - roots-of-unity
relations: []
review: draft
---

Let $R$ be a commutative ring, and let $M$ be an $R\dash$module.
An $R\dash$submodule $N$ of $M$ is maximal if there is no $R\dash$module $P$ with $N \subsetneq P \subsetneq M$.

a. Show that an $R\dash$submodule $N$ of $M$ is maximal $\iff M /N$ is a simple $R\dash$module: i.e., $M /N$ is nonzero and has no proper, nonzero $R\dash$submodules.

b. Let $M$ be a $\ZZ\dash$module.
Show that a $\ZZ\dash$submodule $N$ of $M$ is maximal $\iff \size M /N$ is a prime number.

c. Let $M$ be the $\ZZ\dash$module of all roots of unity in $\CC$ under multiplication.
Show that there is no maximal $\ZZ\dash$submodule of $M$.

::: {.concept}
\envlist

- Todo
:::

::: {.solution}
\envlist

::: {.proof title="of a"}
By the correspondence theorem, submodules of $M/N$ biject with submodules $A$ of $M$ containing $N$.

So

- $M$ is maximal:

- $\iff$ no such (proper, nontrivial) submodule $A$ exists

- $\iff$ there are no (proper, nontrivial) submodules of $M/N$

- $\iff M/N$ is simple.
:::

::: {.proof title="of b"}
Identify $\ZZ\dash$modules with abelian groups, then by (a), $N$ is maximal $\iff$ $M/N$ is simple $\iff$ $M/N$ has no nontrivial proper subgroups.
\

By Cauchy's theorem, if $\abs{M/N} = ab$ is a composite number, then $a\divides ab \implies$ there is an element (and thus a subgroup) of order $a$.
In this case, $M/N$ contains a nontrivial proper cyclic subgroup, so $M/N$ is not simple.
So $\abs{M/N}$ can not be composite, and therefore must be prime.
:::

::: {.proof title="of c"}
\envlist

- Let $G = \theset{x \in \CC \suchthat x^n=1 \text{ for some }n\in \NN}$, and suppose $H < G$ is a proper submodule.

- Since $H\neq G$, there is some $p$ and some $k$ such that $\zeta_{p^k}\not\in H$.

  - Otherwise, if $H$ contains every $\zeta_{p^k}$ it contains every $\zeta_n$

Then there must be a prime $p$ such that the $\zeta_{p^k} \not \in H$ for all $k$ greater than some constant $m$ -- otherwise, we can use the fact that if $\zeta_{p^k} \in H$ then $\zeta_{p^\ell} \in H$ for all $\ell \leq k$, and if $\zeta_{p^k} \in H$ for all $p$ and all $k$ then $H = G$.

But this means there are infinitely many elements in $G\setminus H$, and so $\infty = [G: H] = \abs{G/H}$ is not a prime.
Thus by (b), $H$ can not be maximal, a contradiction.
:::
:::
