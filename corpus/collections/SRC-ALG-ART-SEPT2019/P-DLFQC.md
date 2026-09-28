---
schema: qual/card@1
id: P-DLFQC
kind: problem
title: Density in affine varieties via the Nullstellensatz
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Commutative Algebra
  - Maximal Ideals
relations: []
review: draft
---

::: {.problem}
Work over an algebraically closed field $F$ of characteristic zero.

a. Let $X$ be an affine variety with coordinate algebra $F[X]$. State the *Nullstellensatz*. Then use it to show that a subset $S \subseteq X$ is dense (in the Zariski topology) if and only if the following property holds for all $f \in F[X]$:
$$(f(s)=0 \text{ for all } s\in S) \Rightarrow f=0.$$
b. Given affine varieties $X$ and $Y$ and dense subsets $S \subseteq X$ and $T \subseteq Y$, prove that $S\times T$ is dense in $X\times Y$.
c. Show that the integer lattice $\mathbb{Z}^n$ is dense in $F^n$.
:::

::: {.solution}
**(a)** Nullstellensatz: there are mutually inverse, inclusion-reversing bijections $$V: \{\text{radical ideals of }F[X]\} \leftrightarrow \{\text{closed subsets of }X\} : I$$ given by $V(J) = \{x\in X \mid f(x)=0\ \forall f\in J\}$ and $I(S) = \{f\in F[X] \mid f(x)=0\ \forall x\in S\}$.

The stated property says $I(S)=(0)$, so the density criterion is the equivalence $\overline S = X \iff I(S) = (0)$.

First, $\overline S = V(I(S))$:
$S \subseteq V(I(S))$ closed, hence $\overline S \subseteq V(I(S))$.
If $S \subseteq V(J)$ for $J = \sqrt J$, $V(I(S)) \subseteq V(I(V(J))) = V(J)$.
This shows $V(I(S)) \subseteq \overline S$.

Hence, $\overline S = X \iff V(I(S)) = X \iff I(S) = I(X) = (0)$.

**(b)** The coordinate ring of the product is $F[X\times Y] = F[X]\otimes F[Y]$.

Let $\theta \in F[X\times Y]$ be zero on $S\times T$.
Write $\theta = \sum_i f_i\otimes g_i \in F[X]\otimes F[Y]$, $f_i$'s linearly independent.
For any $t\in T$, $\sum_i f_ig_i(t) \in F[X]$ is zero on $S$, hence zero as $S$ is dense in $X$.
As $f_i$'s are linearly independent, this implies $g_i(t)=0$ for all $t\in T$, so $g_i=0$ as $T$ is dense in $Y$.
Therefore $\theta=0$.

**(c)** Since $\operatorname{char}F=0$, $\mathbb{Z}$ is an infinite subset of $F$, and a nonzero polynomial in $F[x]$ has finitely many roots, so $\mathbb{Z}$ is dense in $F$ by (a). Part (b) and induction on $n$ give density of $\mathbb{Z}^n=\mathbb{Z}^{n-1}\times\mathbb{Z}$ in $F^n$.
:::
