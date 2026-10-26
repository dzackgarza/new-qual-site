---
schema: qual/card@1
id: P-WESTOP03-01
kind: problem
title: "Cantor's theorem: no set surjects onto its power set"
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Prove that for every set $X$ there is no surjection
\[
X\longrightarrow\mathcal P(X),
\]
where $\mathcal P(X)$ is the power set of $X$.
:::

::: pf

::: pf-step

Suppose, for contradiction, that there is a surjection
\[
f:X\to\mathcal P(X).
\]


::: pf-proof

This assumes the negation of the desired conclusion.

:::

:::

::: pf-step

Define the diagonal subset
\[
D=\{x\in X:x\notin f(x)\}.
\]
Then
\[
D\in\mathcal P(X).
\]


::: pf-proof

The defining condition selects some elements of $X$, so $D$ is a subset of $X$. By definition, every subset of $X$ is an element of its power set.

:::

:::

::: pf-step

Since $f$ is surjective, there exists $d\in X$ such that
\[
f(d)=D.
\]


::: pf-proof

Apply surjectivity of $f$ to the element $D\in\mathcal P(X)$ from step <1>2.

:::

:::

::: pf-step

If $d\in D$, then $d\notin D$.


::: pf-proof

By the definition of $D$ in step <1>2,
\[
d\in D\quad\Longrightarrow\quad d\notin f(d).
\]
Using $f(d)=D$ from step <1>3 gives $d\notin D$.

:::

:::

::: pf-step

If $d\notin D$, then $d\in D$.


::: pf-proof

Again by the definition of $D$,
\[
d\notin D\quad\Longrightarrow\quad d\in f(d).
\]
Step <1>3 identifies $f(d)$ with $D$, so $d\in D$.

:::

:::

::: pf-step

Both possibilities for membership of $d$ in $D$ are contradictory.


::: pf-proof

The law of excluded middle gives either $d\in D$ or $d\notin D$. Step <1>4 contradicts the first alternative and step <1>5 contradicts the second.

:::

:::

::: pf-step

Therefore no surjection
\[
\boxed{X\to\mathcal P(X)}
\]
exists.


::: pf-proof

The assumed surjection in step <1>1 led to the contradiction in step <1>6.

:::

:::

::: pf-qed

Step <1>7 is Cantor's theorem in the required form.

:::

:::
