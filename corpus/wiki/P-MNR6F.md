---
schema: qual/card@1
id: P-MNR6F
kind: problem
title: $f^{-1}(f(S))=S$ for all $S$ iff $f$ is injective
classification:
  areas:
  - prelim
  topics:
  - functions-and-relations
relations: []
review: draft
solved: false
---

::: problem
1. Claim: this holds iff $f$ is injective iff $f$ has a left inverse.

   1. $\implies$: Suppose this holds, and let $x_1,x_2 \in X$.
      Then suppose $f(a) = f(b)$.
      We have $f^{-1}(f(\theset{a})) = \theset{a}$ and $f^{-1}(f(\theset{b})) = \theset{b}$ by assumption, so combining these we have
   $$
   a = \theset{a} = f\inv f(\theset{a}) = f^{-1}f(a) = f^{-1}f(b) f\inv f(\theset b)= \theset{b} = b,
   $$
   so $f$ is injective.

   1. $\neg \implies$ Suppose that this does not hold, then there is some $S \subset X$ such that $f\inv f(S) \neq S$.
      Then $S - f\inv f(S) \neq \emptyset$,  so pick an element $x$ from it.

      Then $f(x) \definedas y \in f(S)$ since $x\in S$, but $f\inv (y) \in f\inv f(S)$ and so there is some $x'$ such that $f\inv (y) = x'$, where $x' \in f\inv(f(S))$.
      Since $x \in S-f\inv f(S)$ but $x' \in f\inv f (S)$, we have $x\neq x'$, and by definition we have $f(x) = y = f(x')$, we must conclude that $f$ is not injective.
:::
