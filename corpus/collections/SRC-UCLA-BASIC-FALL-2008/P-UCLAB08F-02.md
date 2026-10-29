---
schema: qual/card@1
id: P-UCLAB08F-02
kind: problem
title: Path connectedness of connected subsets of the plane
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2008.
---
::: {.problem}
Let $A\subset\RR^2$ be nonempty and connected.

::: pf

::: {.pf-step #p1-s1}

Prove that if $A$ is open, then $A$ is path connected.

:::

::: pf-step

Is step [](#p1-s1){.pf-ref} still true if $A$ is closed?

:::

:::

Prove your assertion.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

Assume $A$ is open. Fix $p\in A$, and let
$$
C=\{q\in A:\text{there is a path in }A\text{ from }p\text{ to }q\}.
$$
Then $C$ is open in $A$.

::: pf-proof

Let $q\in C$. Since $A$ is open, there is $r>0$ such that
$$
B(q,r)\subseteq A.
$$
Every $z\in B(q,r)$ can be joined to $q$ by the straight-line segment
$$
t\longmapsto (1-t)q+tz,
\qquad
0\le t\le1,
$$
which lies in the convex ball $B(q,r)$. Concatenating this segment with a path from $p$ to $q$ shows that every $z\in B(q,r)$ belongs to $C$. Hence $C$ is open in $A$.

:::

:::

::: {.pf-step #p2-s2}

The complement $A\setminus C$ is open in $A$.

::: pf-proof

Let $q\in A\setminus C$. Since $A$ is open, choose $r>0$ with
$$
B(q,r)\subseteq A.
$$
If some $z\in B(q,r)$ belonged to $C$, then a path from $p$ to $z$, followed by the straight-line segment from $z$ to $q$ inside $B(q,r)$, would give a path from $p$ to $q$. That would put $q$ in $C$, a contradiction. Thus
$$
B(q,r)\subseteq A\setminus C,
$$
so $A\setminus C$ is open in $A$.

:::

:::

::: {.pf-step #p2-s3}

If $A$ is nonempty, open, and connected, then
$$
\boxed{A\text{ is path connected}}.
$$

::: pf-proof

The set $C$ from step [](#p2-s1){.pf-ref} contains the chosen point $p$, so it is nonempty. By steps [](#p2-s1){.pf-ref} and [](#p2-s2){.pf-ref}, both $C$ and its complement are open in $A$. Since $A$ is connected, the only nonempty subset of $A$ that is both open and closed is $A$ itself. Hence
$$
C=A.
$$
Thus every point of $A$ can be joined to $p$ by a path in $A$, and any two points can be joined by concatenating their paths to $p$.

:::

:::

::: {.pf-step #p2-s4}

The conclusion is false for closed connected subsets of $\RR^2$.

::: pf-proof

Consider
$$
G=
\left\{
\left(x,\sin\frac1x\right):0<x\le1
\right\}
$$
and
$$
A=
G\cup\bigl(\{0\}\times[-1,1]\bigr).
$$
Steps [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref} and [](#p2-s7){.pf-ref} show that $A$ is closed and connected but not path connected.

:::

:::

::: {.pf-step #p2-s5}

The set $A$ in step [](#p2-s4){.pf-ref} is the closure of $G$ in $\RR^2$.

::: pf-proof

Every point of $G$ is of course in $\overline G$.

For any $y\in[-1,1]$, choose $\theta\in[-\pi/2,\pi/2]$ with
$$
\sin\theta=y.
$$
For sufficiently large positive integers $m$, set
$$
x_m=\frac1{\theta+2\pi m}.
$$
Then $x_m>0$, $x_m\to0$, and
$$
\sin\frac1{x_m}
=
\sin(\theta+2\pi m)
=y.
$$
Thus
$$
(x_m,y)\in G
\quad\text{and}\quad
(x_m,y)\to(0,y),
$$
so
$$
\{0\}\times[-1,1]\subseteq\overline G.
$$

Conversely, any convergent sequence in $G$ whose first coordinates converge to a positive number has its limit again in $G$ by continuity of $x\mapsto\sin(1/x)$. If its first coordinates converge to $0$, the second coordinate of the limit lies in $[-1,1]$. Hence every limit point of $G$ lies in $A$. Therefore
$$
\overline G=A.
$$

:::

:::

::: {.pf-step #p2-s6}

The set $A$ is closed and connected.

::: pf-proof

By step [](#p2-s5){.pf-ref},
$$
A=\overline G,
$$
so $A$ is closed.

The interval $(0,1]$ is connected, and the map
$$
x\longmapsto\left(x,\sin\frac1x\right)
$$
is continuous. Hence its image $G$ is connected. The closure of a connected set is connected, so
$$
A=\overline G
$$
is connected.

:::

:::

::: {.pf-step #p2-s7}

The set $A$ is not path connected.

::: pf-proof

Suppose there were a path
$$
\gamma:[0,1]\to A,
\qquad
\gamma(t)=(x(t),y(t)),
$$
with
$$
\gamma(0)=(0,0)
$$
and
$$
\gamma(1)\in G.
$$
The continuous function $x(t)$ is nonnegative, with $x(0)=0$ and $x(1)>0$.
Let
$$
t_0=\max\{t\in[0,1]:x(t)=0\}.
$$
The maximum exists because the zero set of $x$ is closed. Since $x(1)>0$, one has $t_0<1$, and
$$
x(t)>0
$$
for every $t>t_0$.

Thus for $t>t_0$,
$$
y(t)=\sin\frac1{x(t)}.
$$
Fix any $t>t_0$. By continuity of $x$ and the intermediate value theorem,
$$
x([t_0,t])
$$
contains every value between $0$ and $x(t)$. Choose $m$ so large that both
$$
r_m^+=\frac1{\pi/2+2\pi m}
\quad\text{and}\quad
r_m^-=\frac1{3\pi/2+2\pi m}
$$
are smaller than $x(t)$. Then there are
$$
s_m^+,s_m^-\in(t_0,t]
$$
such that
$$
x(s_m^\pm)=r_m^\pm.
$$
Consequently
$$
y(s_m^+)=1,
\qquad
y(s_m^-)=-1.
$$

Because this can be done for every $t>t_0$, values $1$ and $-1$ occur arbitrarily close to $t_0$ from the right. This contradicts continuity of the scalar function $y(t)$ at $t_0$. Therefore no such path exists, and $A$ is not path connected.

:::

:::

::: pf-qed

Step [](#p2-s3){.pf-ref} proves part (a), while steps [](#p2-s4){.pf-ref}, [](#p2-s5){.pf-ref}, [](#p2-s6){.pf-ref} and [](#p2-s7){.pf-ref} give a closed connected counterexample for part (b).

:::

:::

:::
