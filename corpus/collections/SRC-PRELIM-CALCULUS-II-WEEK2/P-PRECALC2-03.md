---
schema: qual/card@1
id: P-PRECALC2-03
kind: problem
title: The integral $\int_0^\infty x^ne^{-x}\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
For $n \in \mathbb { N } ,$ evaluate $\int _ { 0 } ^ { \infty } x ^ { n } e ^ { - x } d x .$
:::

::: {.solution}
For \(n\ge0\), define
\[
I_n
=
\int_0^\infty x^n e^{-x}\,dx.
\]

<1>1. The base case is
\[
\boxed{I_0=1}.
\]

::: {.proof}
\[
I_0
=
\int_0^\infty e^{-x}\,dx
=
\left[-e^{-x}\right]_0^\infty
=
0-(-1)
=
1.
\]
:::

<1>2. For every integer \(n\ge1\),
\[
\lim_{x\to\infty}x^ne^{-x}=0.
\]

::: {.proof}
Using the exponential series,
\[
e^x
=
\sum_{k=0}^{\infty}\frac{x^k}{k!}
\ge
\frac{x^{n+1}}{(n+1)!}
\qquad(x>0).
\]
Hence
\[
0
\le
x^ne^{-x}
\le
\frac{(n+1)!}{x}
\longrightarrow0.
\]
:::

<1>3. For \(n\ge1\), integration by parts gives
\[
I_n
=
\left[-x^ne^{-x}\right]_0^\infty
+
n\int_0^\infty x^{n-1}e^{-x}\,dx.
\]

::: {.proof}
Take
\[
u=x^n,
\qquad
dv=e^{-x}\,dx.
\]
Then
\[
du=nx^{n-1}\,dx,
\qquad
v=-e^{-x}.
\]
Apply integration by parts to the improper integral, understood as the limit
over \([0,R]\).
:::

<1>4. The boundary term in step <1>3 is zero:
\[
\boxed{
\left[-x^ne^{-x}\right]_0^\infty=0}.
\]

::: {.proof}
At \(x=\infty\), step <1>2 gives
\[
x^ne^{-x}\to0.
\]
At \(x=0\), since \(n\ge1\),
\[
x^ne^{-x}=0.
\]
:::

<1>5. Therefore
\[
\boxed{I_n=nI_{n-1}}
\qquad(n\ge1).
\]

::: {.proof}
Combine steps <1>3 and <1>4.
:::

<1>6. Iterating the recurrence gives
\[
I_n
=
n(n-1)\cdots2\cdot1\,I_0.
\]

::: {.proof}
Repeatedly apply step <1>5:
\[
I_n=nI_{n-1}
=n(n-1)I_{n-2}
=\cdots
=n!I_0.
\]
:::

<1>7. Hence
\[
\boxed{
\int_0^\infty x^ne^{-x}\,dx
=
n!}.
\]

::: {.proof}
By step <1>6 and the base value \(I_0=1\) from step <1>1,
\[
I_n=n!.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the requested value.
:::
:::
