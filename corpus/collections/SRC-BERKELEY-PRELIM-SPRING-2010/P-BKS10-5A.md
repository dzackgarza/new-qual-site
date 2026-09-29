---
schema: qual/card@1
id: P-BKS10-5A
kind: problem
title: Solutions of $y'=2^y-1/x$ with $y(1)\ge0$ increase on $[1,b)$
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution. The packet prints y=y(t) once but then uses x consistently; this card normalizes that evident variable typo to y=y(x).
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the first-zero contradiction in both cases and the second-derivative start when y(1)=0.
---

::: {.problem}
Let $I=(a,b)$ be an interval containing $1$, and let $y=y(x)$ be a $C^\infty$ function on $I$ satisfying
$$
y'=2^y-\frac1x.
$$
Prove rigorously that:

(a) if $y(1)>0$, then $y$ is strictly increasing on $[1,b)$;

(b) the same conclusion holds if $y(1)=0$.
:::

::: {.solution}

::: pf

::: {.pf-step #derivative-at-zero}
If $c>1$ and $y(c)=0$, then
$$
y'(c)=1-\frac1c>0.
$$

::: pf-proof
Substituting $y(c)=0$ into the differential equation gives
$$
y'(c)
=
2^0-\frac1c
=
1-\frac1c.
$$
Since $c>1$, this quantity is positive.
:::

:::

::: {.pf-step #positivity-case-a}
Suppose $y(1)>0$. Then
$$
y(x)>0
$$
for every $x\in[1,b)$.

::: pf-proof
Assume otherwise. By continuity, there is some $x_0>1$ with
$y(x_0)\leq0$, and the set
$$
Z
\coloneqq
\{x\in[1,x_0]:y(x)=0\}
$$
is nonempty and closed. Let
$$
c\coloneqq\min Z.
$$
Then $c>1$ and
$$
y(x)>0
$$
for $1\leq x<c$.

For every sufficiently small $h<0$,
$$
\frac{y(c+h)-y(c)}{h}
<0,
$$
because the numerator is positive and the denominator is negative. Since
$y'(c)$ exists, passage to the limit $h\to0^-$ gives
$$
y'(c)\leq0.
$$
This contradicts step [](#derivative-at-zero){.pf-ref}.
:::

:::

::: {.pf-step #part-a}
If $y(1)>0$, then $y$ is strictly increasing on $[1,b)$.

::: pf-proof
By step [](#positivity-case-a){.pf-ref}, $y(x)>0$ for every $x>1$. Hence
$$
y'(x)
=
2^{y(x)}-\frac1x
>
1-\frac1x
>
0
$$
for every $x>1$. For any
$$
1\leq x_1<x_2<b,
$$
the mean value theorem gives some $c\in(x_1,x_2)$ with
$$
y(x_2)-y(x_1)
=
y'(c)(x_2-x_1)
>
0.
$$
This proves part (a).
:::

:::

::: {.pf-step #initial-derivatives}
Suppose $y(1)=0$. Then
$$
y'(1)=0
$$
and
$$
y''(1)=1.
$$

::: pf-proof
The differential equation gives
$$
y'(1)
=
2^0-1
=
0.
$$
Differentiating the differential equation yields
$$
y''
=
(\log 2)2^y y'
+
\frac1{x^2}.
$$
Evaluating at $x=1$ gives
$$
y''(1)
=
(\log 2)2^0y'(1)+1
=
1.
$$
:::

:::

::: {.pf-step #positivity-near-one}
If $y(1)=0$, then there is $\delta>0$ such that
$$
y(x)>0
$$
for every $x\in(1,1+\delta]$.

::: pf-proof
Since $y''(1)=1$ and $y''$ is continuous, there is $\delta>0$ such that
$$
y''(x)>0
$$
for $1\leq x\leq1+\delta$, after shrinking $\delta$ so that this
interval lies in $I$. Hence $y'$ is strictly increasing there. By step
[](#initial-derivatives){.pf-ref},
$$
y'(1)=0,
$$
so
$$
y'(x)>0
$$
for $1<x\leq1+\delta$. Therefore $y$ is strictly increasing on this
interval, and since $y(1)=0$, one has $y(x)>0$ for every
$x\in(1,1+\delta]$.
:::

:::

::: {.pf-step #positivity-case-b}
If $y(1)=0$, then
$$
y(x)>0
$$
for every $x\in(1,b)$.

::: pf-proof
Step [](#positivity-near-one){.pf-ref} gives positivity immediately to the right of $1$. If $y$ vanished
again at some point, choose its first zero $c>1$ after this initial positive
interval. Then $y(x)>0$ for $x<c$ sufficiently close to $c$. Exactly as in
step [](#positivity-case-a){.pf-ref}, the left derivative at $c$ would satisfy
$$
y'(c)\leq0,
$$
contradicting step [](#derivative-at-zero){.pf-ref}.
:::

:::

::: {.pf-step #part-b}
If $y(1)=0$, then $y$ is strictly increasing on $[1,b)$.

::: pf-proof
By step [](#positivity-case-b){.pf-ref}, $y(x)>0$ for every $x>1$. The same calculation as in step
[](#part-a){.pf-ref} gives
$$
y'(x)>0
$$
for every $x>1$. The mean value theorem then shows that
$$
y(x_2)>y(x_1)
$$
whenever $1\leq x_1<x_2<b$. This proves part (b).
:::

:::

::: pf-qed
Step [](#part-a){.pf-ref} proves part (a), and step [](#part-b){.pf-ref} proves part (b).
:::

:::

:::
