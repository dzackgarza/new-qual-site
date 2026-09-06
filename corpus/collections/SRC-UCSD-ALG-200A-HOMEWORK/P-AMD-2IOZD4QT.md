---
schema: qual/card@1
id: P-AMD-2IOZD4QT
kind: problem
title: Fixed-point-free elements in group actions on finite sets
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Burnside's Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 3, Exercise 5. Restored
    the source hypothesis that the action on X is transitive; without it the
    claimed fixed-point-free element need not exist.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    For finite G and X, Burnside's lemma makes the average number of fixed
    points equal to one; the identity already fixes at least two points, so
    some group element must fix none. For infinite G and finite X, passed to
    the finite transitive permutation image. For both infinite, used the
    finitary symmetric group on an infinite set: it is transitive but every
    element fixes all but finitely many points.
---

::: {.problem}
Let $G$ act transitively on a finite set $X$ with $|X|\ge2$.

1. If $G$ is finite, prove that there exists $g\in G$ having no fixed point in $X$.

2. Prove the same conclusion when $G$ is infinite and $X$ is finite.

3. Give an example showing that the conclusion can fail when both $G$ and $X$ are infinite, even when the action is transitive.
:::

::: {.solution}
For $g\in G$, write
\[
\operatorname{Fix}(g)=\{x\in X:gx=x\}.
\]

<1>1. If both $G$ and $X$ are finite, some $g\in G$ has
\[
\operatorname{Fix}(g)=\varnothing.
\]
::: {.proof}
Since the action is transitive, it has exactly one orbit.
Burnside's counting lemma therefore gives
\[
1
=\frac1{|G|}\sum_{g\in G}|\operatorname{Fix}(g)|,
\]
so
\[
\sum_{g\in G}|\operatorname{Fix}(g)|=|G|.
\]

The identity element fixes every point of $X$, hence
\[
|\operatorname{Fix}(e)|=|X|\ge2.
\]
If every $g\in G$ fixed at least one point, then
\[
\sum_{g\in G}|\operatorname{Fix}(g)|
\ge |X|+(|G|-1)
\ge |G|+1,
\]
contradicting the Burnside count.
Thus some $g\in G$ fixes no point.
:::

<1>2. The same conclusion holds if $G$ is infinite and $X$ is finite.
::: {.proof}
Let
\[
\rho:G\longrightarrow \operatorname{Sym}(X)
\]
be the permutation representation of the action, and let
\[
Q=\rho(G).
\]
Because $X$ is finite, $\operatorname{Sym}(X)$ is finite, so $Q$ is finite.
The $Q$-action on $X$ is transitive because it has exactly the same point orbits as the original $G$-action.

By <1>1, there exists $q\in Q$ with no fixed point on $X$.
Choose $g\in G$ with
\[
\rho(g)=q.
\]
Then $g$ acts on $X$ exactly as $q$ does, so $g$ also has no fixed point.
:::

<1>3. The conclusion can fail when both the group and the set are infinite.
::: {.proof}
Let $X$ be any infinite set and let
\[
G=\operatorname{FSym}(X)
\]
be the group of permutations of $X$ having finite support.

The natural action of $G$ on $X$ is transitive: given $x,y\in X$ with $x\ne y$, the transposition $(x\ y)$ lies in $G$ and sends $x$ to $y$.

The group $G$ is infinite.
However, every $g\in G$ moves only finitely many points, so it fixes every point outside its finite support.
Since $X$ is infinite,
\[
X\setminus\operatorname{supp}(g)\ne\varnothing.
\]
Thus every $g\in G$ has a fixed point.
Hence this transitive action has no fixed-point-free element.
:::
:::
