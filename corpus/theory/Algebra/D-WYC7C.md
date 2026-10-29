---
schema: qual/card@1
id: D-WYC7C
kind: definition
title: Group actions, orbits, and stabilizers
prompts:
- For a group action $G \actson X$, what is $G_x$?
- What is the stabilizer of a point under a group action?
classification:
  areas:
  - algebra
  topics:
  - Groups
relations: []
review: reviewed
---

::: {.definition}
Let $G$ be a group with identity $e$ and $X$ a set.
An \dfn{action} of $G$ on $X$ is a map $G\times X\to X$, written $(g,x)\mapsto g\cdot x$, such that for all $g,h\in G$ and $x\in X$,
$$
e\cdot x=x
\qquad\text{and}\qquad
g\cdot(h\cdot x)=(gh)\cdot x.
$$

For $x\in X$, the \dfn{orbit} and the \dfn{stabilizer} of $x$ are
$$
G\cdot x\coloneqq\theset{g\cdot x \st g\in G},
\qquad
G_x\coloneqq\theset{g\in G \st g\cdot x=x}.
$$
The \dfn{fixed-point set} of the action is $X^G\coloneqq\theset{x\in X \st g\cdot x=x\text{ for every }g\in G}$.
:::

::: {.proposition}
Let $G$ act on $X$.

(a) The orbits of the action partition $X$.

(b) The action is [[D-KGGWK|transitive]] if and only if it has exactly one orbit, provided $X\neq\emptyset$.

(c) The kernel of the associated homomorphism $G\to\Sym(X)$, $g\mapsto(x\mapsto g\cdot x)$, is $\bigcap_{x\in X}G_x$.

(d) For every $x\in X$, the stabilizer $G_x$ is a [[D-IQ4OX|subgroup]] of $G$.
:::

::: {.proof}
(a) Write $x\sim y$ if $y=g\cdot x$ for some $g\in G$.
This relation is reflexive because $e\cdot x=x$, symmetric because $y=g\cdot x$ gives $g^{-1}\cdot y=(g^{-1}g)\cdot x=x$, and transitive because $y=g\cdot x$ and $z=h\cdot y$ give $z=(hg)\cdot x$.
Its equivalence classes are the orbits.

(b) The action is transitive exactly when every two points of $X$ are related by $\sim$, that is, when the nonempty set $X$ is a single equivalence class.

(c) An element $g$ acts as the identity permutation if and only if $g\cdot x=x$ for every $x\in X$, that is, $g\in G_x$ for every $x$.

(d) $e\in G_x$ because $e\cdot x=x$; if $g,h\in G_x$, then $(gh)\cdot x=g\cdot(h\cdot x)=x$; and if $g\in G_x$, then $g^{-1}\cdot x=g^{-1}\cdot(g\cdot x)=(g^{-1}g)\cdot x=x$.
:::
