---
schema: qual/card@1
id: FD-JI2RH
kind: proposition
title: Injective maps are the maps with a left inverse
prompts:
- What condition on inverses characterises an injective function?
classification:
  areas:
  - algebra
  topics:
  - Functions and Relations
relations: []
review: draft
---

::: {.proposition}
Let $X$ be a nonempty set and $f\colon X\to Y$ a map of sets.
Then $f$ is injective, that is, $f(x) = f(x')$ implies $x=x'$ for all $x,x'\in X$, if and only if $f$ has a left inverse: a map $g\colon Y\to X$ with $g(f(x))=x$ for every $x\in X$.
:::

::: {.proof}
If $g$ is a left inverse and $f(x)=f(x')$, then $x=g(f(x))=g(f(x'))=x'$.
Conversely, suppose $f$ is injective and fix $x_0\in X$.
Define $g(y)$ to be the unique $x\in X$ with $f(x)=y$ when $y\in f(X)$, and $g(y)\coloneqq x_0$ otherwise; then $g(f(x))=x$ for every $x\in X$.
:::

::: {.remark}
The hypothesis $X\neq\emptyset$ is needed: for a nonempty set $Y$, the empty map $\emptyset\to Y$ is injective but has no left inverse, since there is no map $Y\to\emptyset$.
:::
