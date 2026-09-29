---
schema: qual/card@1
id: P-BKS11-1A
kind: problem
title: Path-connected spaces are connected; the topologist's sine curve
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 1 of the retained Spring 2011 solution PDF and independently reviewed both topology arguments.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked connectedness via the closure of the oscillating graph and non-path-connectedness via the last zero of a hypothetical path's first coordinate.
---

::: {.problem}
A non-empty metric space X is said to be connected if it is not the union of two non-empty disjoint open subsets, and is said to be path-connected if for every two points a, b there is a continuous map f from the unit interval to X with $f ( 0 ) = a , f ( 1 ) = b$

(a) Prove that every path-connected space is connected.

(b) If X is the subset of the plane consisting of the points $( x , y )$ with $x = 0$ or $x > 0 , y =$ sin(1/x) show that X is connected but not path-connected.
:::

::: {.solution}

::: pf

::: {.pf-step #unit-interval-connected}
The unit interval $[0,1]$ is connected.

::: pf-proof
Suppose, for contradiction, that
$$
[0,1]=U\sqcup V
$$
with $U,V$ nonempty and open in the subspace topology. Choose
$$
u\in U,
\qquad
v\in V,
$$
and, after interchanging the names if necessary, assume $u<v$. Set
$$
c\coloneqq
\sup\bigl(U\cap[u,v]\bigr).
$$
Because $U$ is relatively open, $c$ cannot belong to $U$: if it did, an
interval immediately to the right of $c$ inside $[u,v]$ would also lie in
$U$, contradicting the definition of $c$.

Thus $c\in V$. Since $V$ is relatively open, some interval immediately
to the left of $c$ lies in $V$. But by the definition of supremum there
are points of $U\cap[u,v]$ arbitrarily close to $c$ from the left. This
is a contradiction.
:::

:::

::: {.pf-step #path-connected-implies-connected}
Every path-connected space is connected.

::: pf-proof
Let $Y$ be path-connected and suppose
$$
Y=U\sqcup V
$$
were a separation into nonempty disjoint open subsets. Choose
$$
a\in U,
\qquad
b\in V.
$$
Path-connectedness gives a continuous map
$$
\gamma:[0,1]\longrightarrow Y
$$
with $\gamma(0)=a$ and $\gamma(1)=b$. Then
$$
\gamma^{-1}(U)
\quad\text{and}\quad
\gamma^{-1}(V)
$$
are nonempty disjoint open subsets of $[0,1]$ whose union is the whole
interval, contradicting step [](#unit-interval-connected){.pf-ref}. This proves part (a).
:::

:::

::: {.pf-step #a-and-b-connected}
For part (b), write
$$
A\coloneqq\{(0,y):y\in\RR\}
$$
and
$$
B\coloneqq
\{(x,\sin(1/x)):x>0\}.
$$
Then both $A$ and $B$ are connected.

::: pf-proof
The set $A$ is a line, hence path-connected. The map
$$
(0,\infty)\longrightarrow\RR^2,
\qquad
x\longmapsto(x,\sin(1/x))
$$
is continuous and has image $B$. Since $(0,\infty)$ is an interval and
therefore connected, its continuous image $B$ is connected.
:::

:::

::: {.pf-step #closure-contains-origin}
The closure $\overline B$ is contained in $X=A\cup B$, and
$$
A\cap\overline B\neq\varnothing.
$$

::: pf-proof
Let $(x_j,\sin(1/x_j))\in B$ converge to a point $(x,y)$.
If $x>0$, then continuity of
$$
t\longmapsto\sin(1/t)
$$
at $x$ gives
$$
y=\sin(1/x),
$$
so $(x,y)\in B$. If $x=0$, then $(x,y)\in A$. Thus
$$
\overline B\subseteq A\cup B=X.
$$

Moreover, the sequence
$$
x_j\coloneqq\frac{1}{2\pi j}
$$
satisfies
$$
(x_j,\sin(1/x_j))
=
(x_j,0)
\longrightarrow
(0,0).
$$
Hence $(0,0)\in A\cap\overline B$.
:::

:::

::: {.pf-step #x-connected}
The space $X$ is connected.

::: pf-proof
By step [](#a-and-b-connected){.pf-ref}, $B$ is connected, so its closure $\overline B$ is
connected. The set $A$ is connected by the same step, and step [](#closure-contains-origin){.pf-ref} gives
$$
A\cap\overline B\neq\varnothing.
$$
The union of two connected sets with nonempty intersection is connected.
Therefore
$$
A\cup\overline B
$$
is connected. Since $B\subseteq\overline B$ and
$\overline B\subseteq A\cup B$ by step [](#closure-contains-origin){.pf-ref},
$$
A\cup\overline B
=
A\cup B
=
X.
$$
Thus $X$ is connected.
:::

:::

::: {.pf-step #no-path-to-b}
There is no path in $X$ from $(0,0)$ to a point of $B$.

::: pf-proof
Suppose instead that
$$
\gamma(t)=(r(t),s(t)),
\qquad
0\leq t\leq1,
$$
is continuous, with
$$
\gamma(0)=(0,0)
$$
and
$$
\gamma(1)\in B.
$$
The first coordinate $r$ is continuous and nonnegative. Set
$$
Z\coloneqq\{t\in[0,1]:r(t)=0\}.
$$
This is a nonempty closed subset of $[0,1]$, and $1\notin Z$. Hence
$$
t_0\coloneqq\max Z
$$
is well-defined and satisfies $t_0<1$. For every $t>t_0$,
$$
r(t)>0,
$$
so the defining equation of $X$ gives
$$
s(t)=\sin(1/r(t)).
$$

Choose any sequence $\delta_j>0$ with
$$
\delta_j\longrightarrow0
$$
and
$$
t_0+\delta_j\leq1.
$$
Set
$$
c_j\coloneqq r(t_0+\delta_j)>0.
$$
The positive numbers
$$
u_k^+
\coloneqq
\frac{1}{\pi/2+2\pi k}
$$
and
$$
u_k^-
\coloneqq
\frac{1}{3\pi/2+2\pi k}
$$
tend to $0$, with
$$
\sin(1/u_k^+)=1,
\qquad
\sin(1/u_k^-)=-1.
$$
For each $j$, choose $k$ large enough that both $u_k^+$ and $u_k^-$ are
less than $c_j$. Since the continuous function $r$ takes the values
$0$ and $c_j$ at the endpoints of
$$
[t_0,t_0+\delta_j],
$$
the intermediate value theorem gives points
$$
p_j,q_j\in(t_0,t_0+\delta_j)
$$
such that
$$
r(p_j)=u_k^+,
\qquad
r(q_j)=u_k^-.
$$
Hence
$$
s(p_j)=1,
\qquad
s(q_j)=-1.
$$
But $p_j,q_j\to t_0$, so continuity of $s$ would force both sequences
$s(p_j)$ and $s(q_j)$ to converge to $s(t_0)$. This is impossible.
:::

:::

::: {.pf-step #x-not-path-connected}
The space $X$ is not path-connected.

::: pf-proof
The point $(0,0)$ lies in $X$, and $B$ is nonempty, for example
$$
(1,\sin1)\in B.
$$
Step [](#no-path-to-b){.pf-ref} shows that these points cannot be joined by a path in $X$.
:::

:::

::: pf-qed
Step [](#path-connected-implies-connected){.pf-ref} proves part (a), while steps [](#x-connected){.pf-ref} and [](#x-not-path-connected){.pf-ref} prove respectively
the connectedness and failure of path-connectedness required in part (b).
:::

:::

:::
