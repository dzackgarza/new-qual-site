---
schema: qual/card@1
id: P-BERK84S-05
kind: problem
title: Analytic branch of a square root and a contour integral
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the exterior square-root branch via w=1/z and the contour integral from the Laurent coefficient at infinity.
---

::: {.problem}
1. Show that there is a unique analytic branch outside the unit circle of the function $f ( z ) = { \sqrt { z ^ { 2 } + z + 1 } }$ such that $f ( t )$ is positive when $t > 1$

2. Using the branch determined in Part $^ { 1 , }$ calculate the integral

$$
\frac { 1 } { 2 \pi i } \int _ { C _ { r } } \frac { d z } { \sqrt { z ^ { 2 } + z + 1 } }
$$

where $C _ { r }$ is the positively oriented circle $| z | = r$ and $r > 1$
:::


::: {.solution}
Put
\[
q(w)=1+w+w^2.
\]
The zeros of $q$ are $e^{2\pi i/3}$ and $e^{-2\pi i/3}$, both on the unit circle. Hence $q$ has no zeros in the open unit disk.

<1>1. There is a unique analytic square root $h$ of $q$ on $|w|<1$ satisfying $h(0)=1$.
::: {.proof}
The disk is simply connected and $q$ is holomorphic and nowhere zero there. Therefore $q$ admits a holomorphic logarithm $L$ on the disk. Choose $L$ with $L(0)=0$ and define
\[
h(w)=e^{L(w)/2}.
\]
Then $h^2=q$ and $h(0)=1$.

If $\widetilde h$ is another such square root with $\widetilde h(0)=1$, then $\widetilde h/h$ is holomorphic and satisfies $(\widetilde h/h)^2=1$. Since the disk is connected, $\widetilde h/h$ is constant with value $1$, so $\widetilde h=h$.
:::

<1>2. The required branch on $|z|>1$ is
\[
f(z)=z\,h(1/z).
\]
::: {.proof}
For $|z|>1$ we have $|1/z|<1$, so $h(1/z)$ is analytic. Moreover,
\[
f(z)^2
=z^2h(1/z)^2
=z^2q(1/z)
=z^2+z+1.
\]
Thus $f$ is an analytic square root of $z^2+z+1$ on the exterior of the unit circle.

For real $t>1$, the number
\[
q(1/t)=1+t^{-1}+t^{-2}
\]
is positive. Along the interval $0\le w<1$, the continuous function $h(w)$ cannot change sign because it never vanishes and $h(0)=1$. Hence $h(1/t)>0$, and therefore
\[
f(t)=t\,h(1/t)>0.
\]

If $g$ is any other analytic square root on $|z|>1$, then $g/f$ is holomorphic, never zero, and satisfies $(g/f)^2=1$. Since the exterior domain is connected, $g/f$ is identically $1$ or $-1$. The condition $g(t)>0$ for $t>1$ forces $g=f$. Hence this branch is unique.
:::

<1>3. The normalized contour integral equals $1$.
::: {.proof}
Since $h(0)=1$, its reciprocal is analytic near $0$ and has expansion
\[
\frac1{h(w)}=1+c_1w+c_2w^2+\cdots.
\]
Therefore, for $|z|>1$,
\[
\frac1{f(z)}
=\frac1z\frac1{h(1/z)}
=\frac1z+\frac{c_1}{z^2}+\frac{c_2}{z^3}+\cdots.
\]
The coefficient of $z^{-1}$ in the Laurent series is $1$. Hence for every $r>1$,
\[
\frac1{2\pi i}\int_{C_r}\frac{dz}{\sqrt{z^2+z+1}}
=\frac1{2\pi i}\int_{C_r}\frac{dz}{f(z)}
=1.
\]
Thus
\[
\boxed{\frac1{2\pi i}\int_{C_r}\frac{dz}{\sqrt{z^2+z+1}}=1}.
\]
:::
:::
