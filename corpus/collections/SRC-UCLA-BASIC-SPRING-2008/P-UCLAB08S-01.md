---
schema: qual/card@1
id: P-UCLAB08S-01
kind: problem
title: Fixed points and contraction iteration
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2008.
---
::: {.problem}
Let $g\in C([a,b])$ satisfy $a\le g(x)\le b$ for all $x\in[a,b]$.

::: pf

::: pf-step

Prove that $g$ has a fixed point $p\in[a,b]$.

:::

::: pf-step

Suppose there is $\gamma<1$ such that

:::

:::

$$
|g(x)-g(y)|\le \gamma|x-y|
$$
for all $x,y\in[a,b]$.
Prove that the fixed point is unique and that, for every $x_0\in[a,b]$, the iteration $x_{n+1}=g(x_n)$ converges to $p$.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Define
$$
h(x)=g(x)-x.
$$
Then
$$
h(a)\ge0
\qquad\text{and}\qquad
h(b)\le0.
$$

::: pf-proof

Since
$$
a\le g(a)\le b,
$$
one has
$$
h(a)
=
g(a)-a
\ge0.
$$
Likewise,
$$
a\le g(b)\le b,
$$
so
$$
h(b)
=
g(b)-b
\le0.
$$

:::

:::

::: {.pf-step #p2-s2}

There exists
$$
p\in[a,b]
$$
such that
$$
\boxed{g(p)=p}.
$$

::: pf-proof

The function $h$ is continuous because $g$ is continuous.
By step [](#p2-s1){.pf-ref}, either
$$
h(a)=0,
$$
or
$$
h(b)=0,
$$
or $h(a)$ and $h(b)$ have opposite signs.
In the third case, the intermediate value theorem gives
$$
p\in(a,b)
$$
with
$$
h(p)=0.
$$
Thus in all cases there exists
$$
p\in[a,b]
$$
such that
$$
g(p)-p=0.
$$
This proves part step [](#p2-s1){.pf-ref}.

:::

:::

::: {.pf-step #p2-s3}

Assume now that
$$
|g(x)-g(y)|
\le
\gamma|x-y|
$$
for all $x,y\in[a,b]$, where
$$
0\le\gamma<1.
$$
Then the fixed point is unique.

::: pf-proof

Suppose
$$
p,q\in[a,b]
$$
are both fixed points.
Then
$$
\begin{aligned}
|p-q|
&=
|g(p)-g(q)|\\
&\le
\gamma|p-q|.
\end{aligned}
$$
Hence
$$
(1-\gamma)|p-q|\le0.
$$
Since
$$
1-\gamma>0,
$$
one gets
$$
|p-q|=0,
$$
so
$$
p=q.
$$

:::

:::

::: pf-step

Let
$$
x_0\in[a,b]
$$
and define
$$
x_{n+1}=g(x_n).
$$
Then every $x_n$ belongs to $[a,b]$.

::: pf-proof

The initial point $x_0$ belongs to $[a,b]$ by hypothesis.
If
$$
x_n\in[a,b],
$$
then
$$
x_{n+1}=g(x_n)\in[a,b]
$$
because $g$ maps $[a,b]$ into itself.
The claim follows by induction.

:::

:::

::: {.pf-step #p2-s5}

For every $n\ge0$,
$$
\boxed{
|x_n-p|
\le
\gamma^n|x_0-p|
}.
$$

::: pf-proof

The case $n=0$ is equality.
Assume the estimate holds for some $n$.
Since
$$
g(p)=p,
$$
the contraction estimate gives
$$
\begin{aligned}
|x_{n+1}-p|
&=
|g(x_n)-g(p)|\\
&\le
\gamma|x_n-p|\\
&\le
\gamma^{n+1}|x_0-p|.
\end{aligned}
$$
Thus the estimate holds for all $n$ by induction.

:::

:::

::: {.pf-step #p2-s6}

One has
$$
x_n\to p.
$$

::: pf-proof

Because
$$
0\le\gamma<1,
$$
one has
$$
\gamma^n\to0.
$$
Step [](#p2-s5){.pf-ref} gives
$$
0
\le
|x_n-p|
\le
\gamma^n|x_0-p|
\longrightarrow0.
$$
By the squeeze theorem,
$$
|x_n-p|\to0,
$$
which is exactly
$$
x_n\to p.
$$

:::

:::

::: pf-qed

Step [](#p2-s2){.pf-ref} proves existence of a fixed point.
Step [](#p2-s3){.pf-ref} proves uniqueness under the contraction hypothesis, and step [](#p2-s6){.pf-ref} proves convergence of every iteration to that fixed point.

:::

:::

:::
