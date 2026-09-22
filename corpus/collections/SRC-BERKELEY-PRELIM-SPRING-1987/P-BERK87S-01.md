---
schema: qual/card@1
id: P-BERK87S-01
kind: problem
title: If every continuous real-valued function on $K\subset\mathbb R^n$ is bounded, then $K$ is compact
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Applied Heine--Borel. The norm function forces K to be bounded, while any
    missing limit point p would make the reciprocal-distance function from p
    a continuous unbounded real-valued function on K.
---

::: {.problem}
Let $K\subset\mathbb R^n$. Suppose every continuous real-valued function on $K$ is bounded. Prove that $K$ is compact.
:::

::: {.solution}
<1>1. The set $K$ is bounded.

::: {.proof}
The function
$$
f:K\to\RR,
\qquad
f(x)=\norm{x},
$$
is continuous. By hypothesis it is bounded, so there is an $M\geq 0$ such
that
$$
\norm{x}\leq M
$$
for every $x\in K$. Hence $K$ is bounded.
:::

<1>2. The set $K$ is closed in $\RR^n$.

::: {.proof}
Suppose instead that $K$ is not closed. Then there is a point
$$
p\in\overline K\setminus K.
$$
Because $p\notin K$, the function
$$
g:K\to\RR,
\qquad
g(x)=\frac{1}{\norm{x-p}},
$$
is well-defined and continuous.

For every positive integer $m$, the condition $p\in\overline K$ gives a
point $x_m\in K$ with
$$
\norm{x_m-p}<\frac1m.
$$
Therefore
$$
g(x_m)>m.
$$
Thus $g$ is unbounded on $K$, contradicting the hypothesis. Hence $K$ is
closed.
:::

<1>3. The set $K$ is compact.

::: {.proof}
By steps <1>1 and <1>2, $K$ is a closed and bounded subset of $\RR^n$.
The Heine--Borel theorem therefore implies that $K$ is compact.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
