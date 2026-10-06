---
schema: qual/card@1
id: P-UGAP11F-06
kind: problem
title: Prove the sum-of-cubes identity by induction
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Use induction to show that
\[
1^3+2^3+\cdots+n^3=(1+2+\cdots+n)^2.
\]
:::

::: {.solution}
<1>1. The identity holds for $n=1$.

::: {.proof}
For $n=1$,
$$
1^3=1=(1)^2.
$$
:::

<1>2. Assume for some $n\ge1$ that
$$
1^3+\cdots+n^3
=
\left(1+\cdots+n\right)^2.
$$
Then
$$
1^3+\cdots+n^3+(n+1)^3
=
\left(1+\cdots+n+(n+1)\right)^2.
$$

::: {.proof}
By the induction hypothesis,
$$
1^3+\cdots+n^3
=
\left(\frac{n(n+1)}2\right)^2.
$$
Therefore
$$
\begin{aligned}
1^3+\cdots+n^3+(n+1)^3
&=
\frac{n^2(n+1)^2}{4}
+(n+1)^3\\
&=
(n+1)^2
\left(
\frac{n^2}{4}+n+1
\right)\\
&=
(n+1)^2
\frac{(n+2)^2}{4}\\
&=
\left(
\frac{(n+1)(n+2)}2
\right)^2.
\end{aligned}
$$
But
$$
1+\cdots+n+(n+1)
=
\frac{(n+1)(n+2)}2.
$$
Thus the formula holds for $n+1$.
:::

<1>3. Hence, for every $n\ge1$,
$$
\boxed{
1^3+2^3+\cdots+n^3
=
(1+2+\cdots+n)^2}.
$$

::: {.proof}
Step <1>1 gives the base case and step <1>2 gives the induction step.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required induction result.
:::
:::
