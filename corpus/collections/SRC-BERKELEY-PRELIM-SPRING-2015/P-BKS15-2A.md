---
schema: qual/card@1
id: P-BKS15-2A
kind: problem
title: Cousin's lemma for a positive gauge on $[a,b]$
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the supremum construction of a tagged gauge partition and the final extension to b without assuming continuity of g.
---

::: {.problem}
Suppose that $g$ is a positive real-valued function of a real variable, not necessarily continuous.
If $a<b$ are real numbers, show that there is a finite sequence
$$
a=t_0<t_1<\cdots<t_n=b
$$
such that in each interval $[t_k,t_{k+1}]$ there is a point where the value of $g$ is greater than the length of the interval.
:::

::: {.solution}
Call a finite partition
$$
a=t_0<t_1<\cdots<t_m=c
$$
of $[a,c]$ \dfn{good} if for every $0\leq k<m$ there is a tag
$$
\xi_k\in[t_k,t_{k+1}]
$$
such that
$$
t_{k+1}-t_k<g(\xi_k).
$$
Let
$$
E
\coloneqq
\{c\in[a,b]:[a,c]\text{ has a good partition}\}.
$$

::: pf

::: pf-step

The set $E$ is nonempty.

::: pf-proof

The degenerate interval $[a,a]$ has the empty partition, so $a\in E$.
Alternatively, since $g(a)>0$, every sufficiently small $c>a$ lies in
$E$ by using the one-interval partition $[a,c]$ tagged at $a$.

:::

:::

::: pf-step

Let
$$
c\coloneqq\sup E.
$$
Then
$$
c>a.
$$

::: pf-proof

Since $g(a)>0$ and $b>a$, choose
$$
0<h<\min(g(a),b-a).
$$
The one-interval partition
$$
[a,a+h]
$$
tagged at $a$ is good because
$$
h<g(a).
$$
Thus $a+h\in E$, so $\sup E>a$.

:::

:::

::: {.pf-step #s3}

One has
$$
c=b.
$$

::: pf-proof

Suppose instead that $c<b$. Since $g(c)>0$, choose
$$
0<\eta
<
\min\left(
\frac{b-c}{2},
\frac{g(c)}{4}
\right).
$$
By the definition of supremum, there is some
$$
x\in E
$$
with
$$
c-\eta<x\leq c.
$$
Set
$$
y=c+\eta.
$$
Then
$$
y<b
$$
and
$$
y-x
<
2\eta
<
g(c).
$$
Moreover
$$
c\in[x,y].
$$

Take a good partition of $[a,x]$ and append the interval $[x,y]$ with
tag $c$. The appended interval is good because its length is less than
$g(c)$. Thus
$$
y\in E,
$$
contradicting $y>c=\sup E$. Therefore $c=b$.

:::

:::

::: {.pf-step #s4}

There is some
$$
x\in E
$$
such that
$$
b-x<g(b).
$$

::: pf-proof

By step [](#s3){.pf-ref},
$$
\sup E=b.
$$
Since $g(b)>0$, choose a point of $E$ in the interval
$$
\left(
b-\min(g(b),b-a),
b
\right].
$$
For such an $x$, the displayed inequality holds. If the chosen point is
$b$, the conclusion is already immediate.

:::

:::

::: {.pf-step #s5}

The interval $[a,b]$ has a good partition.

::: pf-proof

Take $x$ from step [](#s4){.pf-ref}. If $x=b$, this is true because $b\in E$.
Otherwise, take a good partition of $[a,x]$ and append the interval
$$
[x,b]
$$
tagged at $b$. Its length satisfies
$$
b-x<g(b),
$$
so the enlarged partition is good.

:::

:::

::: {.pf-step #s6}

Therefore there is a finite sequence
$$
\boxed{
a=t_0<t_1<\cdots<t_n=b
}
$$
such that every interval $[t_k,t_{k+1}]$ contains a point $\xi_k$ with
$$
g(\xi_k)>t_{k+1}-t_k.
$$

::: pf-proof

Unpack the definition of the good partition furnished by step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is exactly the required statement.

:::

:::

:::
