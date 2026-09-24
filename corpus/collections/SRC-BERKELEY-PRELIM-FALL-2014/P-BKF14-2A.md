---
schema: qual/card@1
id: P-BKF14-2A
kind: problem
title: Counterexamples to interchanging $\limsup$ and $\liminf$ with integrals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: shrinking
    unit-mass spikes disprove the first and third inequalities, while
    alternating x and 1-x disproves the second.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked continuity and unit integral of the explicit triangular spikes,
    their pointwise limit, and the limsup integral for the alternating
    sequence.
---

::: {.problem}
Suppose that $f _ { n }$ is a sequence of non-negative continuous functions on the unit interval.
Find counterexamples to three of the following four inequalities:

$$
\operatorname* { l i m } _ { n } \operatorname* { s u p } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \leq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { s u p } f _ { n } ( x ) d x
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { s u p } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \geq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { s u p } f _ { n } ( x ) d x
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { i n f } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \leq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { i n f } f _ { n } ( x ) d x
$$

$$
\operatorname* { l i m } _ { n } \operatorname* { i n f } \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \geq \int _ { 0 } ^ { 1 } \operatorname* { l i m } _ { n } \operatorname* { i n f } f _ { n } ( x ) d x
$$

(The remaining inequality always holds; you do not need to prove this.)
:::

::: {.solution}
Number the four displayed inequalities in the order in which they occur in
the problem.

<1>1. Inequality 1 is false.

::: {.proof}
For $n\ge1$, define
$$
f_n(x)\coloneqq
\begin{cases}
4n^2x,&0\le x\le\frac1{2n},\\
4n-4n^2x,&\frac1{2n}\le x\le\frac1n,\\
0,&\frac1n\le x\le1.
\end{cases}
$$
Each $f_n$ is nonnegative and continuous. Its graph is a triangle with
base $1/n$ and height $2n$, so
$$
\int_0^1 f_n(x)\,dx=1.
$$
For every fixed $x>0$, one has $f_n(x)=0$ for all sufficiently large
$n$, while $f_n(0)=0$ for every $n$. Hence $f_n(x)\to0$ at every point
of $[0,1]$. Therefore
$$
\limsup_{n\to\infty}\int_0^1f_n(x)\,dx=1
>
0
=
\int_0^1\limsup_{n\to\infty}f_n(x)\,dx,
$$
contradicting inequality 1.
:::

<1>2. Inequality 3 is false.

::: {.proof}
Use the same sequence as in step <1>1. Since every integral is $1$ and
$f_n(x)\to0$ pointwise,
$$
\liminf_{n\to\infty}\int_0^1f_n(x)\,dx=1
>
0
=
\int_0^1\liminf_{n\to\infty}f_n(x)\,dx.
$$
Thus the asserted inequality
$$
\liminf_n\int_0^1f_n
\le
\int_0^1\liminf_n f_n
$$
fails.
:::

<1>3. Inequality 2 is false.

::: {.proof}
Define
$$
f_n(x)\coloneqq
\begin{cases}
x,&n\text{ even},\\
1-x,&n\text{ odd}.
\end{cases}
$$
These functions are nonnegative and continuous, and
$$
\int_0^1f_n(x)\,dx=\frac12
$$
for every $n$. Thus
$$
\limsup_{n\to\infty}\int_0^1f_n(x)\,dx=\frac12.
$$
At each $x$,
$$
\limsup_{n\to\infty}f_n(x)=\max\{x,1-x\}.
$$
Consequently
$$
\begin{aligned}
\int_0^1\limsup_{n\to\infty}f_n(x)\,dx
&=
\int_0^{1/2}(1-x)\,dx
+
\int_{1/2}^1x\,dx\\
&=
\frac38+\frac38\\
&=
\frac34.
\end{aligned}
$$
Hence
$$
\frac12
=
\limsup_{n\to\infty}\int_0^1f_n(x)\,dx
<
\int_0^1\limsup_{n\to\infty}f_n(x)\,dx
=
\frac34,
$$
contradicting inequality 2.
:::

<1>4. The first three inequalities therefore admit counterexamples.

::: {.proof}
Steps <1>1, <1>2, and <1>3 provide counterexamples to inequalities 1,
3, and 2, respectively, which are three of the four displayed
inequalities.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 supplies the three requested counterexamples.
:::
:::
