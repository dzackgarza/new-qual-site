---
schema: qual/card@1
id: P-PRACT20-W6-23
kind: problem
title: Negating bijectivity of a function
classification:
  areas:
  - prelim
  topics:
  - Logic
  - Functions
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
$P$ says that $f$ is defined at every point of $X$, which holds for any function. $Q$ says that $f$ is surjective, and $R$ says that $f$ is not injective. Thus

$$
f\text{ is bijective}\iff Q\text{ and }(\lnot R),
$$

so the negation is

$$
f\text{ is not bijective}\iff(\lnot Q)\text{ or }R.
$$
:::
