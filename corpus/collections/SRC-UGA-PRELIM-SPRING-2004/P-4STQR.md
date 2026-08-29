---
schema: qual/card@1
id: P-4STQR
kind: problem
title: A spanning set with no proper spanning subset is linearly independent
classification:
  areas:
  - prelim
  topics:
  - Vector Spaces
  - Bases
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
a) Define what it means for vectors $v_1, \ldots, v_n$ in a vector space $V$ to be linearly independent.

b) Suppose that vectors $v_1, \ldots, v_n$ in a vector space $V$ span $V$ and that no proper subset of $\{v_1, \ldots, v_n\}$ spans $V$.
Prove that $v_1, \ldots, v_n$ are linearly independent.
:::

::: {.solution}
**(a).**

<1>1. The vectors $v_1, \ldots, v_n$ are linearly independent if the only scalars $c_1, \ldots, c_n$ with $c_1 v_1 + \cdots + c_n v_n = 0$ are $c_1 = \cdots = c_n = 0$.
Proof: definition of linear independence.

**(b).**

<1>1. Suppose for contradiction that $v_1, \ldots, v_n$ are linearly dependent.
Proof: assume the conclusion fails.

<1>2. Then there is a nontrivial relation $c_1 v_1 + \cdots + c_n v_n = 0$ with some $c_j \neq 0$.
Proof: <1>1 (a).

<1>3. Hence $v_j = -\sum_{i \neq j} \frac{c_i}{c_j} v_i$, so $v_j$ is a linear combination of the other vectors.
Proof: <1>2, solving for $v_j$.

<1>4. Therefore $\{v_1, \ldots, v_n\} \setminus \{v_j\}$ still spans $V$ (any linear combination using $v_j$ can be rewritten using the other vectors).
Proof: <1>3.

<1>5. This contradicts the hypothesis that no proper subset spans $V$.
Proof: <1>4.

<1>6. Hence $v_1, \ldots, v_n$ are linearly independent.
Proof: <1>5.

<1>7. Q.E.D.
Proof: <1>1 (a) and <1>6 (b).
:::
