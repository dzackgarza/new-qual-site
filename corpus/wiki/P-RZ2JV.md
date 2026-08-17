---
schema: qual/card@1
id: P-RZ2JV
kind: problem
title: Maximal submodules are those with simple quotient, and the roots of unity have no maximal submodule
classification:
  areas:
  - algebra
  topics:
  - modules
  - maximal-ideals
  - roots-of-unity
relations: []
review: draft
solved: true
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

- $N$ is maximal:

- $\iff$ no such (proper, nontrivial) submodule $A$ exists

- $\iff$ there are no (proper, nontrivial) submodules of $M/N$

- $\iff M/N$ is simple.
:::

::: {.proof title="of b"}
Identify $\ZZ\dash$modules with abelian groups, then by (a), $N$ is maximal $\iff$ $M/N$ is simple $\iff$ $M/N$ has no nontrivial proper subgroups.
\

Suppose $\abs{M/N}$ is finite and composite, and let $a$ be a **prime** divisor of it with $a < \abs{M/N}$.
Cauchy's theorem applies to $a$ and gives an element, and thus a cyclic subgroup, of order $a$.
Since $1 < a < \abs{M/N}$ this subgroup is proper and nontrivial, so $M/N$ is not simple.
So $\abs{M/N}$ can not be composite, and therefore must be prime.
Note Cauchy's theorem needs its divisor to be prime, so the argument picks a prime factor rather than an arbitrary factorisation $ab$.
:::

::: {.proof title="of c"}
\envlist

- Let $G = \theset{x \in \CC \suchthat x^n=1 \text{ for some }n\in \NN}$, and suppose $H < G$ is a maximal submodule.

- By (b), $\abs{G/H} = q$ for some prime $q$.
  So $G/H$ has exponent dividing $q$, that is, $x^q \in H$ for every $x\in G$.

- But $G$ is a **divisible** group: given $x\in G$ with $x^n = 1$, the element $x$ has a $q\dash$th root inside $G$, since any $y\in\CC$ with $y^q = x$ satisfies $y^{qn} = 1$ and so is itself a root of unity.

- Therefore every $x\in G$ can be written $x = y^q$ with $y\in G$, and the previous point puts $x = y^q \in H$.
  So $G \subseteq H$, contradicting $H < G$.

> The tempting shortcut, that infinitely many elements lie outside $H$ and so the index must be infinite, does not follow.
> A subgroup of finite index can omit infinitely many elements: $2\ZZ$ has index $2$ in $\ZZ$ and misses infinitely many integers.
:::
:::
