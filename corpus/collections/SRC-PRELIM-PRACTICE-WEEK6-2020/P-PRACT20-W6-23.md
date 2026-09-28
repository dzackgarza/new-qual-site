---
schema: qual/card@1
id: P-PRACT20-W6-23
kind: problem
title: Negating bijectivity of a function
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the opening quotation mark misread as a superscript 66, checked against Week6_solns.pdf (Problem 23).
---

::: {.problem}
Let $f : X \to Y$. Write the negation of “$f$ is bijective” in terms of the following statements:

P: For each $x \in X$, there is $y \in Y$ such that $f(x) = y$

Q: For each $y \in Y$, there is $x \in X$ such that $f(x) = y$

R: There exist $x_1, x_2 \in X$ with $x_1 \neq x_2$ and $f(x_1) = f(x_2)$
:::

::: {.solution}
P is just the statement that f is a function.
Q is the statement that $f$ is surjective.
R is the statement that $f$ is not injective.
Thus

$$
f { \mathrm { ~ i s ~ b i j e c t i v e } } \quad \Longleftrightarrow \quad { \mathrm { ~ Q ~ a n d ~ } } ( \lnot \mathrm { R } ) .
$$

So the negation is

$$
f { \mathrm { ~ i s ~ n o t ~ b i j e c t i v e } } \quad \Longleftrightarrow \quad ( \lnot \mathrm { Q } ) { \mathrm { ~ o r ~ } } \mathrm { R } .
$$
:::
