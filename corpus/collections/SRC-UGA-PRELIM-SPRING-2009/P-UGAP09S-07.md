---
schema: qual/card@1
id: P-UGAP09S-07
kind: problem
title: Continuity at the origin of two rational functions on $\RR^2$
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
Determine, with proof, which of the following functions $\RR^2\to\RR$ are continuous:
\[
f(x,y)=
\begin{cases}
\dfrac{x^3y}{x^4+y^4},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0),
\end{cases}
\]
and
\[
g(x,y)=
\begin{cases}
\dfrac{x^3y^2}{(x^2+y^2)^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f$ is continuous at every point other than the origin.


::: pf-proof

Away from $(0,0)$ one has
\[
x^4+y^4>0,
\]
so $f$ is a quotient of polynomial functions with nonzero denominator and is
therefore continuous there.

:::

:::

::: pf-step

The function $f$ is not continuous at $(0,0)$.


::: pf-proof

Along the line $y=x$, for $x\ne0$,
\[
f(x,x)
=\frac{x^4}{x^4+x^4}
=\frac12.
\]
Thus
\[
\lim_{x\to0}f(x,x)=\frac12,
\]
whereas
\[
f(0,0)=0.
\]
Hence the two-variable limit at the origin cannot equal the function value.

:::

:::

::: pf-step

The function $g$ is continuous at every point other than the origin.


::: pf-proof

Away from $(0,0)$,
\[
(x^2+y^2)^2>0,
\]
so $g$ is again a quotient of polynomial functions with nonzero denominator.

:::

:::

::: {.pf-step #s1-4}

For every $(x,y)\ne(0,0)$,
\[
|g(x,y)|
\le
\sqrt{x^2+y^2}.
\]


::: pf-proof

Set
\[
r=\sqrt{x^2+y^2}.
\]
Then
\[
|x|\le r,
\qquad
|y|\le r.
\]
Therefore
\[
|x^3y^2|
\le r^5,
\]
while
\[
(x^2+y^2)^2=r^4.
\]
Hence
\[
|g(x,y)|
=\frac{|x^3y^2|}{(x^2+y^2)^2}
\le r.
\]

:::

:::

::: {.pf-step #s1-5}

The function $g$ is continuous at $(0,0)$.


::: pf-proof

By step [](#s1-4){.pf-ref},
\[
|g(x,y)-g(0,0)|
=|g(x,y)|
\le
\sqrt{x^2+y^2}.
\]
The right-hand side tends to $0$ as $(x,y)\to(0,0)$, so the squeeze theorem
gives
\[
g(x,y)\to0=g(0,0).
\]

:::

:::

::: {.pf-step #s1-6}

Therefore
\[
\boxed{f\text{ is discontinuous only at }(0,0),\qquad
g\text{ is continuous on }\RR^2}.
\]


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the requested determination.

:::

:::

:::
