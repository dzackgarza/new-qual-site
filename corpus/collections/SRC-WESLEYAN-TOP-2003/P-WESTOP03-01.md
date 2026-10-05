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

::: {.solution}
<1>1. Suppose, for contradiction, that there is a surjection
\[
f:X\to\mathcal P(X).
\]

::: {.proof}
This assumes the negation of the desired conclusion.
:::

<1>2. Define the diagonal subset
\[
D=\{x\in X:x\notin f(x)\}.
\]
Then
\[
D\in\mathcal P(X).
\]

::: {.proof}
The defining condition selects some elements of $X$, so $D$ is a subset of $X$. By definition, every subset of $X$ is an element of its power set.
:::

<1>3. Since $f$ is surjective, there exists $d\in X$ such that
\[
f(d)=D.
\]

::: {.proof}
Apply surjectivity of $f$ to the element $D\in\mathcal P(X)$ from step <1>2.
:::

<1>4. If $d\in D$, then $d\notin D$.

::: {.proof}
By the definition of $D$ in step <1>2,
\[
d\in D\quad\Longrightarrow\quad d\notin f(d).
\]
Using $f(d)=D$ from step <1>3 gives $d\notin D$.
:::

<1>5. If $d\notin D$, then $d\in D$.

::: {.proof}
Again by the definition of $D$,
\[
d\notin D\quad\Longrightarrow\quad d\in f(d).
\]
Step <1>3 identifies $f(d)$ with $D$, so $d\in D$.
:::

<1>6. Both possibilities for membership of $d$ in $D$ are contradictory.

::: {.proof}
The law of excluded middle gives either $d\in D$ or $d\notin D$. Step <1>4 contradicts the first alternative and step <1>5 contradicts the second.
:::

<1>7. Therefore no surjection
\[
\boxed{X\to\mathcal P(X)}
\]
exists.

::: {.proof}
The assumed surjection in step <1>1 led to the contradiction in step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is Cantor's theorem in the required form.
:::
:::
