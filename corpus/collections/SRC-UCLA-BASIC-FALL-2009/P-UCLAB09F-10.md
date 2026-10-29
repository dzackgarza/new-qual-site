---
schema: qual/card@1
id: P-UCLAB09F-10
kind: problem
title: Integral mean values on an interval and a square
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2009.
---
::: {.problem}
Let $I=[0,2]$.

::: pf

::: pf-step

If $f\colon I\to\RR$ is continuous and
$$
\int_I f(x)\,dx=36,
$$
prove that there exists $x\in I$ such that $f(x)=18$.

:::

::: pf-step

If $g\colon I^2\to\RR$ is continuous and

:::

:::

$$
\int_{I^2}g(x,y)\,dx\,dy=36,
$$
prove that there exists $(x,y)\in I^2$ such that $g(x,y)=9$.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Let
$$
m=\min_{x\in I}f(x),
\qquad
M=\max_{x\in I}f(x).
$$
Then
$$
m\le18\le M.
$$

::: pf-proof

The interval
$$
I=[0,2]
$$
is compact, so continuity of $f$ gives the minimum and maximum.
For every $x\in I$,
$$
m\le f(x)\le M.
$$
Integrating over an interval of length $2$ gives
$$
2m
\le
\int_I f(x)\,dx
\le
2M.
$$
Since the integral equals $36$,
$$
2m\le36\le2M,
$$
and division by $2$ gives
$$
m\le18\le M.
$$

:::

:::

::: {.pf-step #p2-s2}

There exists $x\in I$ such that
$$
\boxed{f(x)=18}.
$$

::: pf-proof

Choose $x_m,x_M\in I$ with
$$
f(x_m)=m,
\qquad
f(x_M)=M.
$$
By step [](#p2-s1){.pf-ref}, the number $18$ lies between $m$ and $M$. The interval joining $x_m$ and $x_M$ lies in $I$, and $f$ is continuous there. The intermediate value theorem therefore gives a point $x$ with
$$
f(x)=18.
$$

:::

:::

::: {.pf-step #p2-s3}

Let
$$
m_g=\min_{(x,y)\in I^2}g(x,y),
\qquad
M_g=\max_{(x,y)\in I^2}g(x,y).
$$
Then
$$
m_g\le9\le M_g.
$$

::: pf-proof

The square
$$
I^2=[0,2]^2
$$
is compact, so the extrema exist.
Since its area is $4$,
$$
4m_g
\le
\int_{I^2}g(x,y)\,dx\,dy
\le
4M_g.
$$
The integral equals $36$, so
$$
4m_g\le36\le4M_g.
$$
Dividing by $4$ gives the claim.

:::

:::

::: {.pf-step #p2-s4}

There exists $(x,y)\in I^2$ such that
$$
\boxed{g(x,y)=9}.
$$

::: pf-proof

Choose points
$$
p,q\in I^2
$$
with
$$
g(p)=m_g,
\qquad
g(q)=M_g.
$$
The square $I^2$ is convex, so the line segment
$$
\gamma(t)=(1-t)p+tq,
\qquad
0\le t\le1,
$$
lies in $I^2$.
The function
$$
t\longmapsto g(\gamma(t))
$$
is continuous and takes the values $m_g$ and $M_g$ at the endpoints. By step [](#p2-s3){.pf-ref}, $9$ lies between them, so the intermediate value theorem gives $t_0$ with
$$
g(\gamma(t_0))=9.
$$

:::

:::

::: pf-qed

Step [](#p2-s2){.pf-ref} proves part step [](#p2-s1){.pf-ref}, and step [](#p2-s4){.pf-ref} proves part step [](#p2-s2){.pf-ref}.

:::

:::

:::
