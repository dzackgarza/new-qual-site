---
schema: qual/card@1
id: P-BKF94-1
kind: problem
title: Convergence of a series built from $1/n-\sin(1/n)$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used the cubic Taylor asymptotic
    1/n-sin(1/n)~1/(6n^3) and limit comparison with the p-series
    sum n^{-3a}.
---

::: {.problem}
For which real values of $a$ does
\[
\sum_{n=1}^{\infty}\left(\frac1n-\sin\frac1n\right)^a
\]
converge?
:::

::: {.solution}
Set
$$
b_n\coloneqq
\frac1n-\sin\frac1n.
$$

<1>1. One has
$$
b_n>0
$$
for every $n\geq1$.

::: {.proof}
For every $t>0$,
$$
\sin t<t.
$$
Applying this with $t=1/n$ gives the claim.
:::

<1>2. One has
$$
\lim_{n\to\infty}6n^3b_n=1.
$$

::: {.proof}
Taylor's formula at the origin gives
$$
\sin t
=
t-\frac{t^3}{6}+O(t^5)
\qquad(t\to0).
$$
Hence
$$
t-\sin t
=
\frac{t^3}{6}+O(t^5).
$$
Substituting $t=1/n$ yields
$$
b_n
=
\frac1{6n^3}+O(n^{-5}),
$$
and multiplication by $6n^3$ gives the asserted limit.
:::

<1>3. For every fixed real $a$,
$$
\lim_{n\to\infty}
\frac{b_n^a}{6^{-a}n^{-3a}}
=1.
$$

::: {.proof}
By step <1>1 the terms are positive, so the real powers are defined. Step
<1>2 gives
$$
\frac{b_n}{1/(6n^3)}
\longrightarrow1.
$$
The function $x\mapsto x^a$ is continuous on $(0,\infty)$, so raising this
ratio to the fixed power $a$ preserves the limit:
$$
\left(
\frac{b_n}{1/(6n^3)}
\right)^a
\longrightarrow1.
$$
This is exactly the displayed quotient.
:::

<1>4. The series
$$
\sum_{n=1}^{\infty}b_n^a
$$
converges if and only if
$$
3a>1.
$$

::: {.proof}
By step <1>3, limit comparison reduces the question to
$$
\sum_{n=1}^{\infty}n^{-3a}.
$$
This is a $p$-series, which converges exactly when its exponent is greater
than $1$. Thus convergence is equivalent to $3a>1$.
:::

<1>5. The complete range is
$$
\boxed{a>\frac13}.
$$

::: {.proof}
The inequality $3a>1$ from step <1>4 is equivalent to
$a>1/3$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives all real values of $a$ for which the series converges.
:::
:::
