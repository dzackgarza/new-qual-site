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
$$
X\longrightarrow\mathcal P(X),
$$
where $\mathcal P(X)$ is the power set of $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that there is a surjection
$$
f:X\to\mathcal P(X).
$$


::: pf-proof

This assumes the negation of the desired conclusion.

:::

:::

::: {.pf-step #s1-2}

Define the diagonal subset
$$
D=\{x\in X:x\notin f(x)\}.
$$
Then
$$
D\in\mathcal P(X).
$$


::: pf-proof

The defining condition selects some elements of $X$, so $D$ is a subset of $X$. By definition, every subset of $X$ is an element of its power set.

:::

:::

::: {.pf-step #s1-3}

Since $f$ is surjective, there exists $d\in X$ such that
$$
f(d)=D.
$$


::: pf-proof

Apply surjectivity of $f$ to the element $D\in\mathcal P(X)$ from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

If $d\in D$, then $d\notin D$.


::: pf-proof

By the definition of $D$ in step [](#s1-2){.pf-ref},
$$
d\in D\quad\Longrightarrow\quad d\notin f(d).
$$
Using $f(d)=D$ from step [](#s1-3){.pf-ref} gives $d\notin D$.

:::

:::

::: {.pf-step #s1-5}

If $d\notin D$, then $d\in D$.


::: pf-proof

Again by the definition of $D$,
$$
d\notin D\quad\Longrightarrow\quad d\in f(d).
$$
Step [](#s1-3){.pf-ref} identifies $f(d)$ with $D$, so $d\in D$.

:::

:::

::: {.pf-step #s1-6}

Both possibilities for membership of $d$ in $D$ are contradictory.


::: pf-proof

The law of excluded middle gives either $d\in D$ or $d\notin D$. Step [](#s1-4){.pf-ref} contradicts the first alternative and step [](#s1-5){.pf-ref} contradicts the second.

:::

:::

::: {.pf-step #s1-7}

Therefore no surjection
$$
\boxed{X\to\mathcal P(X)}
$$
exists.


::: pf-proof

The assumed surjection in step [](#s1-1){.pf-ref} led to the contradiction in step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is Cantor's theorem in the required form.

:::

:::

:::
