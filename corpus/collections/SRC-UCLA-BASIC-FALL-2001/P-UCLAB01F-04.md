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
Prove that there is no bijection from $\mathbb N=\{1,2,\ldots\}$ onto $S$.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that there is a surjection
\[
\phi:\mathbb N\to S.
\]

::: {.proof}
If a bijection from $\mathbb N$ onto $S$ existed, then in particular a surjection would exist. It is therefore enough to contradict surjectivity.
:::

<1>2. Write
\[
\phi(n)=\bigl(x^{(n)}_1,x^{(n)}_2,\ldots\bigr)
\]
for each $n\in\mathbb N$, where every $x^{(n)}_j\in\{0,1\}$.

::: {.proof}
This merely records the coordinates of the binary sequence $\phi(n)$.
:::

<1>3. Define a sequence $y=(y_1,y_2,\ldots)$ by
\[
y_n=
\begin{cases}
1,&x^{(n)}_n=0,\\
0,&x^{(n)}_n=1.
\end{cases}
\]
Then $y\in S$.

::: {.proof}
For every $n$, the value $y_n$ is either $0$ or $1$. Hence $y$ is a binary sequence and therefore belongs to $S$.
:::

<1>4. For every $n\in\mathbb N$,
\[
y\ne \phi(n).
\]

::: {.proof}
By construction,
\[
y_n\ne x^{(n)}_n.
\]
Thus $y$ and $\phi(n)$ differ in their $n$th coordinate, so they are distinct sequences.
:::

<1>5. No surjection from $\mathbb N$ onto $S$ exists.

::: {.proof}
Step <1>3 gives $y\in S$, while step <1>4 shows that $y$ is not equal to $\phi(n)$ for any $n\in\mathbb N$. Hence $y$ is not in the image of $\phi$, contradicting the surjectivity assumed in step <1>1.
:::

<1>6. Therefore there is no bijection from $\mathbb N$ onto $S$.

::: {.proof}
Every bijection is surjective, and step <1>5 rules out every surjection.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
