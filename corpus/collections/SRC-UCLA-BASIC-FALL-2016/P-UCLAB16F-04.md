---
schema: qual/card@1
id: P-UCLAB16F-04
kind: problem
title: Lower semicontinuity of matrix rank
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 4 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Let $B$ be a $7 \times 7$ matrix and $A_n$ a sequence of matrices of the same size.
Suppose that

$$
A_n \to B \quad \text{as} \quad n \to \infty,
$$

in the sense that the individual matrix entries converge.
Show that

$$
\rank(B) \leq \liminf_{n \to \infty} \rank(A_n).
$$
:::

::: {.solution}

Let
$$
r=\operatorname{rank}(B).
$$

::: pf

::: {.pf-step #s1-1}

If $r=0$, then the desired inequality is immediate.


::: pf-proof

Every matrix rank is nonnegative, so
$$
0
\le
\liminf_{n\to\infty}\operatorname{rank}(A_n).
$$
Since $r=0$, this is exactly the desired inequality.

:::

:::

::: pf-step

Assume $r>0$.
Then $B$ has an $r\times r$ minor whose determinant is nonzero.


::: pf-proof

By the definition of matrix rank, $r$ is the largest size of a square minor with nonzero determinant.
Hence some $r\times r$ minor of $B$ has nonzero determinant.

:::

:::

::: pf-step

Fix the row and column indices of such a minor, and let
$$
D_n
$$
be the determinant of the corresponding $r\times r$ minor of $A_n$.
Then
$$
D_n\to D,
$$
where
$$
D\ne0
$$
is the determinant of the chosen minor of $B$.


::: pf-proof

The determinant is a polynomial in the entries.
Since the entries of $A_n$ converge to those of $B$, the selected minor converges entrywise to the chosen minor of $B$.
Continuity of the determinant therefore gives
$$
D_n\to D.
$$
By construction, $D\ne0$.

:::

:::

::: {.pf-step #s1-4}

There exists $N$ such that
$$
D_n\ne0
$$
for every $n\ge N$.


::: pf-proof

Since
$$
D_n\to D\ne0,
$$
choose $N$ so that
$$
\abs{D_n-D}<\frac{\abs{D}}{2}
$$
for $n\ge N$.
Then
$$
\abs{D_n}
\ge
\abs{D}-\abs{D_n-D}
>
\frac{\abs{D}}{2}
>
0.
$$

:::

:::

::: {.pf-step #s1-5}

For every $n\ge N$,
$$
\operatorname{rank}(A_n)\ge r.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $A_n$ has a nonzero $r\times r$ minor for every sufficiently large $n$.
Hence its rank is at least $r$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\operatorname{rank}(B)
\le
\liminf_{n\to\infty}\operatorname{rank}(A_n)
}.
$$


::: pf-proof

If $r=0$, use step [](#s1-1){.pf-ref}.
If $r>0$, step [](#s1-5){.pf-ref} shows that the ranks are eventually bounded below by
$$
r=\operatorname{rank}(B).
$$
Hence their lower limit is at least $r$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required inequality.

:::

:::

:::
