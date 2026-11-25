---
schema: qual/card@1
id: T-SCHPK
kind: theorem
title: Schwarz--Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Hyperbolic Metric
relations: []
review: draft
---

::: {.theorem}
Let $f\colon\DD\to\DD$ be [[D-E7A5W|holomorphic]].
Then for every $z\in\DD$,
$$
\frac{\abs{f'(z)}}{1-\abs{f(z)}^2}\leq\frac{1}{1-\abs z^2},
$$
equivalently $f$ does not increase the [[D-2HXLN|hyperbolic distance]]: $d_{\DD}(f(z),f(w))\leq d_{\DD}(z,w)$ for all $z,w\in\DD$, and it does not increase the pseudo-hyperbolic distance $\varrho(z,w)=\abs{(z-w)/(1-\overline wz)}$.

The derivative form is [@SS03, ch. 8, Exercise 13(b)] and the pseudo-hyperbolic form is part (a) of that exercise, the two being one statement under the increasing change of variable $d_{\DD}=\frac12\log\frac{1+\varrho}{1-\varrho}$; that a holomorphic self-map contracts the hyperbolic distance itself is [@SS03, ch. 8, Problem 3(a)].
The printed exercise states the two inequalities and, in part (a), that an automorphism preserves the pseudo-hyperbolic distance; it states no converse that equality at a pair of distinct points forces an automorphism. The converse assertions below, including the derivative form, are consequences of the equality clause of the [[T-DAETF|Schwarz lemma]], stated here as the card's own reading of it.
Equality in the derivative form at one point, and equality in either distance form at one pair of distinct points, each make $f$ an [[D-MFPYG|automorphism]] of $\DD$, and an automorphism satisfies both equalities at every point and at every pair.
At one point, $z=w$, the distance form reads $0\leq0$ and constrains nothing: $f(z)=z^2$ satisfies it at every $z$ and is not an automorphism, and no derivative equality follows from it.
:::
