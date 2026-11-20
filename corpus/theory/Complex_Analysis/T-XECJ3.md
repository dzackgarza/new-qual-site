---
schema: qual/card@1
id: T-XECJ3
kind: theorem
title: Inverse function theorem
slogan: 'A nonzero derivative makes a holomorphic map locally biholomorphic, with inverse derivative the reciprocal.'
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Biholomorphisms
relations: []
review: draft
---

::: {.theorem}
(i) Let $I\subseteq\RR$ be an open interval, let $f\in C^1(I)$, and let $a\in I$ with $f'(a)\neq0$.
Then there are open intervals $U\ni a$ and $V\ni b\coloneqq f(a)$ such that $f$ restricts to a bijection $U\to V$ whose inverse $g\colon V\to U$ is $C^1$, and
$$
g'(b)=\frac{1}{f'(a)}.
$$

(ii) Let $A\subseteq\RR^n$ be open, let $F\colon A\to\RR^n$ be $C^1$, and let $a\in A$ with $\det DF(a)\neq0$.
Then there are open sets $U\ni a$ and $V\ni F(a)$ such that $F$ restricts to a bijection $U\to V$ whose inverse $F^{-1}\colon V\to U$ is $C^1$, and for every $p\in U$,
$$
D(F^{-1})(F(p))=\bigl(DF(p)\bigr)^{-1}.
$$

(iii) Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, and let $p\in\Omega$ with $f'(p)\neq0$.
Then there is an open set $V\ni p$ such that $f(V)$ is open and $f\restrict_V\colon V\to f(V)$ is a [[D-TM4TE|biholomorphism]].

This is [@Rud76, ch. 9, Theorem 9.24], the inverse function theorem: the case $n=1$ is (i), the case of general $n$ is (ii), and (iii) is (ii) applied to $f$ as a map $\RR^2\to\RR^2$, whose Jacobian determinant at $p$ is $\abs{f'(p)}^2\neq0$, the inverse being holomorphic because its derivative at $f(p)$ is multiplication by $1/f'(p)$.
:::
