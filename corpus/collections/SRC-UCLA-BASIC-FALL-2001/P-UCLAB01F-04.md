---
schema: qual/card@1
id: P-UCLAB01F-04
kind: problem
title: Binary sequences are uncountable
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Let $S$ be the set of all sequences $(x_1,x_2,\ldots)$ such that
\[
x_n\in\{0,1\}
\]
for every $n$.
Prove that there is no bijection from $\NN=\{1,2,\ldots\}$ onto $S$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that there is a surjection
\[
\phi:\NN\to S.
\]


::: pf-proof

If a bijection from $\NN$ onto $S$ existed, then in particular a surjection would exist. It is therefore enough to contradict surjectivity.

:::

:::

::: pf-step

Write
\[
\phi(n)=\bigl(x^{(n)}_1,x^{(n)}_2,\ldots\bigr)
\]
for each $n\in\NN$, where every $x^{(n)}_j\in\{0,1\}$.


::: pf-proof

This merely records the coordinates of the binary sequence $\phi(n)$.

:::

:::

::: {.pf-step #s1-3}

Define a sequence $y=(y_1,y_2,\ldots)$ by
\[
y_n=
\begin{cases}
1,&x^{(n)}_n=0,\\
0,&x^{(n)}_n=1.
\end{cases}
\]
Then $y\in S$.


::: pf-proof

For every $n$, the value $y_n$ is either $0$ or $1$. Hence $y$ is a binary sequence and therefore belongs to $S$.

:::

:::

::: {.pf-step #s1-4}

For every $n\in\NN$,
\[
y\ne \phi(n).
\]


::: pf-proof

By construction,
\[
y_n\ne x^{(n)}_n.
\]
Thus $y$ and $\phi(n)$ differ in their $n$th coordinate, so they are distinct sequences.

:::

:::

::: {.pf-step #s1-5}

No surjection from $\NN$ onto $S$ exists.


::: pf-proof

Step [](#s1-3){.pf-ref} gives $y\in S$, while step [](#s1-4){.pf-ref} shows that $y$ is not equal to $\phi(n)$ for any $n\in\NN$. Hence $y$ is not in the image of $\phi$, contradicting the surjectivity assumed in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore there is no bijection from $\NN$ onto $S$.


::: pf-proof

Every bijection is surjective, and step [](#s1-5){.pf-ref} rules out every surjection.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
