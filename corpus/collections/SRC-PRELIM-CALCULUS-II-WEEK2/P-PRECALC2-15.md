---
schema: qual/card@1
id: P-PRECALC2-15
kind: problem
title: Telescoping sum $\sum_{n\ge1}\frac{m}{n(n+m)}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Fix an integer $m > 0$ . Evaluate the infinite sum

$$
\sum _ { n = 1 } ^ { \infty } { \frac { m } { n ( n + m ) } } .
$$
:::

::: {.solution}
<1>1. The summand has the partial-fraction decomposition
\[
\boxed{
\frac{m}{n(n+m)}
=
\frac1n-\frac1{n+m}}.
\]

::: {.proof}
\[
\frac1n-\frac1{n+m}
=
\frac{n+m-n}{n(n+m)}
=
\frac{m}{n(n+m)}.
\]
:::

<1>2. Let
\[
S_N
=
\sum_{n=1}^{N}
\frac{m}{n(n+m)}.
\]
Then
\[
S_N
=
\sum_{n=1}^{N}\frac1n
-
\sum_{n=1}^{N}\frac1{n+m}.
\]

::: {.proof}
Sum the identity from step <1>1 for \(1\le n\le N\).
:::

<1>3. Reindex the second sum:
\[
\boxed{
\sum_{n=1}^{N}\frac1{n+m}
=
\sum_{k=m+1}^{N+m}\frac1k}.
\]

::: {.proof}
Set
\[
k=n+m.
\]
Then \(n=1\) corresponds to \(k=m+1\), and \(n=N\) corresponds to
\(k=N+m\).
:::

<1>4. Therefore
\[
S_N
=
\sum_{k=1}^{N}\frac1k
-
\sum_{k=m+1}^{N+m}\frac1k.
\]

::: {.proof}
Combine steps <1>2--<1>3.
:::

<1>5. For \(N\ge m\),
\[
\boxed{
S_N
=
\sum_{k=1}^{m}\frac1k
-
\sum_{k=N+1}^{N+m}\frac1k}.
\]

::: {.proof}
In step <1>4, the terms
\[
\frac1{m+1},\dots,\frac1N
\]
cancel. The first sum leaves \(1,\dots,m\), while the second sum leaves
\(N+1,\dots,N+m\) with a minus sign.
:::

<1>6. The tail term satisfies
\[
0
\le
\sum_{k=N+1}^{N+m}\frac1k
\le
\frac{m}{N+1}.
\]

::: {.proof}
There are \(m\) terms, and each satisfies
\[
\frac1k
\le
\frac1{N+1}.
\]
:::

<1>7. Hence
\[
\boxed{
\sum_{k=N+1}^{N+m}\frac1k
\longrightarrow0}.
\]

::: {.proof}
By step <1>6,
\[
0
\le
\sum_{k=N+1}^{N+m}\frac1k
\le
\frac{m}{N+1}
\longrightarrow0.
\]
Apply the squeeze theorem.
:::

<1>8. Therefore
\[
\boxed{
\sum_{n=1}^{\infty}
\frac{m}{n(n+m)}
=
\sum_{k=1}^{m}\frac1k}.
\]

::: {.proof}
Take \(N\to\infty\) in step <1>5 and use step <1>7.
:::

<1>9. Equivalently,
\[
\boxed{
\sum_{n=1}^{\infty}
\frac{m}{n(n+m)}
=
H_m},
\]
the \(m\)th harmonic number.

::: {.proof}
By definition,
\[
H_m
=
1+\frac12+\cdots+\frac1m.
\]
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the requested value.
:::
:::
