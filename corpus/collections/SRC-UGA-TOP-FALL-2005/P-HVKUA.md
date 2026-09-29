---
schema: qual/card@1
id: P-HVKUA
kind: problem
title: The closed topologist's sine curve is connected but not path-connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 1 of the official UGA Fall 2005 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Corrected the graph transcription and replaced the invalid retained proof by
    the closure argument for connectedness and an oscillation argument excluding
    paths from the graph to the limiting vertical segment.
---

::: {.problem}
Let
\[
X
=
\{(0,y):-1\le y\le1\}
\cup
\{(x,\sin(1/x)):0<x\le1\}.
\]

Prove that $X$ is connected but not path connected.
:::

::: {.solution}
Write
\[
G=\{(x,\sin(1/x)):0<x\le1\},
\qquad
L=\{0\}\times[-1,1],
\]
so that $X=G\cup L$.

::: pf

::: {.pf-step #graph-connected}
The graph $G$ is connected.

::: pf-proof
The interval $(0,1]$ is connected, and the map
\[
\phi:(0,1]\longrightarrow\RR^2,
\qquad
\phi(x)=(x,\sin(1/x)),
\]
is continuous.
Hence its image
\[
G=\phi((0,1])
\]
is connected.
:::

:::

::: {.pf-step #x-is-closure-of-g}
One has $X=\overline G$.

::: pf-proof
First let $y\in[-1,1]$.
Choose $\alpha\in\RR$ with
\[
\sin\alpha=y.
\]
For all sufficiently large integers $n$, put
\[
x_n=\frac1{2\pi n+\alpha}>0.
\]
Then $x_n\to0$ and
\[
(x_n,\sin(1/x_n))
=
(x_n,y)
\longrightarrow
(0,y).
\]
Thus every point of $L$ belongs to $\overline G$, so
\[
X=G\cup L\subseteq\overline G.
\]

Conversely, because $\RR^2$ is metric, closure is detected by convergent sequences.
Suppose
\[
(x_m,\sin(1/x_m))\longrightarrow(a,b)
\]
with $0<x_m\le1$.
If $a>0$, then $x_m\to a$ and continuity of $x\mapsto\sin(1/x)$ at $a$ gives
\[
b=\sin(1/a),
\]
so $(a,b)\in G$.
If $a=0$, then each second coordinate lies in $[-1,1]$, hence $b\in[-1,1]$ and $(a,b)\in L$.
Therefore
\[
\overline G\subseteq X.
\]
Hence $X=\overline G$.
:::

:::

::: {.pf-step #x-connected}
The space $X$ is connected.

::: pf-proof
By step [](#graph-connected){.pf-ref}, $G$ is connected.
The closure of a connected subspace is connected, and by step [](#x-is-closure-of-g){.pf-ref} that closure is $X$.
Therefore $X$ is connected.
:::

:::

::: {.pf-step #no-path-joins}
No path in $X$ joins a point of $L$ to a point of $G$.

::: pf-proof
Suppose to the contrary that
\[
\gamma:[0,1]\longrightarrow X
\]
is a path with $\gamma(0)\in L$ and $\gamma(1)\in G$.
Write
\[
\gamma(t)=(u(t),v(t)).
\]
Then $u,v:[0,1]\to\RR$ are continuous,
\[
u(0)=0,
\qquad
u(1)>0,
\qquad
u(t)\ge0.
\]

Let
\[
t_0=\max\{t\in[0,1]:u(t)=0\}.
\]
This maximum exists because the zero set of $u$ is a nonempty closed subset of $[0,1]$, and $t_0<1$ because $u(1)>0$.
By maximality,
\[
u(t)>0
\qquad
(t_0<t\le1).
\]
Hence, for every such $t$, the point $\gamma(t)$ lies in $G$ and therefore
\[
v(t)=\sin(1/u(t)).
\]

Choose any sequence $r_n\downarrow t_0$ with $r_n>t_0$.
Since $u(r_n)>0$ and $u(t_0)=0$, the intermediate value theorem shows that
\[
[0,u(r_n)]\subseteq u([t_0,r_n]).
\]
For each $n$, choose integers $k_n$ large enough that
\[
a_n=\frac1{\pi/2+2\pi k_n}<u(r_n),
\qquad
b_n=\frac1{3\pi/2+2\pi k_n}<u(r_n).
\]
Then there are $s_n,t_n\in[t_0,r_n]$ such that
\[
u(s_n)=a_n,
\qquad
u(t_n)=b_n.
\]
Because $r_n\downarrow t_0$, both $s_n$ and $t_n$ tend to $t_0$.
But
\[
v(s_n)
=
\sin(1/a_n)
=1,
\qquad
v(t_n)
=
\sin(1/b_n)
=-1.
\]
Thus $v$ takes the values $1$ and $-1$ along two sequences tending to $t_0$, contradicting continuity of $v$ at $t_0$.

Therefore no such path exists.
:::

:::

::: {.pf-step #x-not-path-connected}
Hence $X$ is not path connected.

::: pf-proof
Both $L$ and $G$ are nonempty.
By step [](#no-path-joins){.pf-ref}, no point of $L$ can be joined by a path in $X$ to a point of $G$.
Therefore $X$ is not path connected.
:::

:::

::: pf-qed
Step [](#x-connected){.pf-ref} and step [](#x-not-path-connected){.pf-ref} show that $X$ is connected but not path connected.
:::

:::

:::
