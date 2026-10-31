---
schema: qual/card@1
id: P-PRACT20-W6-25
kind: problem
title: Injectivity of $g\circ f$ forces injectivity of $f$
classification:
  areas:
  - prelim
  topics:
  - Functions
  - Injectivity
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow lost from g composed with f, checked against Week6_solns.pdf (Problem 25).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the garbled quantifier x, y in S in the solution, checked against Week6_solns.pdf (Problem 25).
---

::: {.problem}
Let $S, T, U$ be nonempty sets and $f : S \to T$, $g : T \to U$ be functions such that $g \circ f : S \to U$ is one-to-one.

(a) Prove that $f$ is one-to-one.

(b) Show by example that $g$ need not be one-to-one.
:::

::: {.solution}
(a) Suppose $f$ is not one-to-one: there are $x\neq y$ in $S$ with $f(x)=f(y)$. Then $(g\circ f)(x)=g(f(x))=g(f(y))=(g\circ f)(y)$, so $g\circ f$ is not one-to-one. By contraposition, if $g\circ f$ is one-to-one, so is $f$.

(b) If $g\circ f$ is one-to-one, $g$ need only be one-to-one on the image of $f$. Let $S=T=U=\RR$, $f(x)=e^x$ and $g(x)=x^2$. Then $(g\circ f)(x)=e^{2x}$ is one-to-one, while $g$ is not, since $g(-1)=g(1)$.
:::
