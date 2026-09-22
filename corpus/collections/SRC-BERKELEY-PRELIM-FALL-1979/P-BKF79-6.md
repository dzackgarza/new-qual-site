---
schema: qual/card@1
id: P-BKF79-6
kind: problem
title: A single Jordan-chain nilpotent has no square root
classification: {areas: [prelim], topics: []}
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
    If X^2=N, then X is nilpotent. Any nilpotent operator on an
    n-dimensional space has nilpotency index at most n, so X^n=0.
    Since n>1 gives 2n-2>=n, this forces
    N^{n-1}=X^{2n-2}=0, contradicting the hypothesis.
---

::: {.problem}
Let $N$ be an operator on an $n$-dimensional vector space, $n>1$, such that
\[
N^n=0,
\qquad
N^{n-1}\ne0.
\]
Prove that there is no operator $X$ with
\[
X^2=N.
\]
:::

::: {.solution}
<1>1. Every nilpotent operator $T$ on an $n$-dimensional vector space
satisfies
$$
T^n=0.
$$

::: {.proof}
Let $m$ be the nilpotency index of $T$, so
$$
T^m=0,
\qquad
T^{m-1}\neq0.
$$
Choose $v$ with $T^{m-1}v\neq0$. We claim that
$$
v,Tv,T^2v,\ldots,T^{m-1}v
$$
are linearly independent. Indeed, suppose
$$
c_0v+c_1Tv+\cdots+c_{m-1}T^{m-1}v=0.
$$
If $j$ is the least index with $c_j\neq0$, applying
$T^{m-1-j}$ gives
$$
c_jT^{m-1}v=0,
$$
because every term with index larger than $j$ acquires exponent at
least $m$. This contradicts $c_j\neq0$ and $T^{m-1}v\neq0$.
Therefore $m$ linearly independent vectors lie in an $n$-dimensional
space, so $m\leq n$. Hence $T^n=0$.
:::

<1>2. If an operator $X$ satisfied $X^2=N$, then $X$ would be
nilpotent.

::: {.proof}
The hypothesis $N^n=0$ would give
$$
X^{2n}
=(X^2)^n
=N^n
=0.
$$
Thus some positive power of $X$ is zero.
:::

<1>3. Under the assumption in step <1>2,
$$
X^n=0.
$$

::: {.proof}
Apply step <1>1 to the nilpotent operator $X$.
:::

<1>4. Under the assumption $X^2=N$, one would have
$$
N^{n-1}=0.
$$

::: {.proof}
Since $n>1$,
$$
2n-2\geq n.
$$
Therefore step <1>3 gives
$$
N^{n-1}
=(X^2)^{n-1}
=X^{2n-2}
=0.
$$
:::

<1>5. No operator $X$ satisfies $X^2=N$.

::: {.proof}
Step <1>4 contradicts the hypothesis
$$
N^{n-1}\neq0.
$$
Hence no such $X$ exists.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
