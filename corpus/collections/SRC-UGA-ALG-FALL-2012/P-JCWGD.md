---
schema: qual/card@1
id: P-JCWGD
kind: problem
title: The stabilizer is a subgroup, and the orbit-stabilizer bijection $G\cdot x\simeq
  G/G_x$
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---

::: problem
Let $G$ be a finite group and $X$ a set on which $G$ acts.

a. Let $x\in X$ and $G_x \definedas \theset{g\in G \suchthat g\cdot x = x}$.
Show that $G_x$ is a subgroup of $G$.

b. Let $x\in X$ and $G\cdot x \definedas \theset{g\cdot x \suchthat g\in G}$.
Prove that there is a bijection between elements in $G\cdot x$ and the left cosets of $G_x$ in $G$.
:::

::: solution
(a) The identity fixes $x$, so $e\in G_x$. If $g,h\in G_x$, then
\[
(gh^{-1})\cdot x
=g\cdot(h^{-1}\cdot x)
=g\cdot x
=x,
\]
because $h\cdot x=x$ implies $h^{-1}\cdot x=x$. Hence $gh^{-1}\in G_x$.
By the subgroup test, $G_x\le G$.

(b) Define
\[
\Phi:G/G_x\longrightarrow G\cdot x,
\qquad
\Phi(gG_x)=g\cdot x.
\]
This is well defined. Indeed, if $gG_x=hG_x$, then
$h^{-1}g\in G_x$, so $(h^{-1}g)\cdot x=x$ and therefore
$g\cdot x=h\cdot x$.

The map is surjective by the definition of the orbit. It is injective because
if $g\cdot x=h\cdot x$, then
\[
(h^{-1}g)\cdot x=x,
\]
so $h^{-1}g\in G_x$, hence $gG_x=hG_x$. Thus $\Phi$ is a bijection.
:::
