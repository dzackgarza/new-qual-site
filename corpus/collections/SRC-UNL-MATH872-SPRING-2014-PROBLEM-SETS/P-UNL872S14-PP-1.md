---
schema: qual/card@1
id: P-UNL872S14-PP-1
kind: problem
title: UNL Math 872 Spring 2014 assignment PP.1
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against assignment PP.1 on the retained UNL Math 872 Section 001 Spring 2014 problem-sets page PDF.
---

::: {.problem}
Let \\(A_1,A_2,A_3\\) be solid rectangular blocks in \\(\\RR^3\\).
For \\(q\\in S^2\\) and \\(t\\in\\RR\\), let
\\[
P_{q,t}=\\{x\\in\\RR^3:x\\cdot q=t\\}
\\]
be the plane through \\(tq\\) perpendicular to \\(q\\). Let
\\[
H_{q,t}=\\{x:x\\cdot q>t\\},
\\qquad
J_{q,t}=\\{x:x\\cdot q<t\\}.
\\]

(a) Draw pictures of \\(P_{q,t}\\) and \\(H_{q,t}\\). Using pictures and multivariable calculus, discuss how to compute
\\[
\\operatorname{vol}(A_i\\cap H_{q,t}).
\\]

(b) Discuss why
\\[
(q,t)\\longmapsto \\operatorname{vol}(A_3\\cap H_{q,t})
\\]
is continuous. Prove that for each \\(q\\in S^2\\) there is a unique real number \\(t_q\\) such that
\\[
\\operatorname{vol}(A_3\\cap H_{q,t_q})
=
\\operatorname{vol}(A_3\\cap J_{q,t_q}).
\\]

(c) For \\(i=1,2\\), define
\\[
f_i(q)=\\operatorname{vol}(A_i\\cap H_{q,t_q}).
\\]
Discuss why \\(f_i:S^2\\to\\RR\\) is continuous.

(d) Use the Borsuk--Ulam theorem to prove that there is a plane in \\(\\RR^3\\) that simultaneously divides each block \\(A_i\\) into two pieces of equal volume.
:::

::: {.solution}

Write
\[
V_i=\operatorname{vol}(A_i).
\]

::: pf

::: {.pf-step #s1-1}

The plane and half-spaces are exactly
\[
P_{q,t}=\{x:x\cdot q=t\},
\qquad
H_{q,t}=\{x:x\cdot q>t\},
\qquad
J_{q,t}=\{x:x\cdot q<t\}.
\]


::: pf-proof

The vector $q$ has length $1$, so the affine plane perpendicular to
$q$ through $tq$ consists of the points $x$ satisfying
\[
(x-tq)\cdot q=0,
\]
equivalently $x\cdot q=t$. The point $(t+1)q$ has dot product
$t+1>t$, so the component containing it is $H_{q,t}$; the other
component is $J_{q,t}$.

:::

:::

::: {.pf-step #s1-2}

For a block $A_i$,
\[
\boxed{
\operatorname{vol}(A_i\cap H_{q,t})
=
\int_t^\infty
\operatorname{area}(A_i\cap P_{q,s})\,ds}.
\]


::: pf-proof

Choose an orthogonal coordinate system whose third coordinate is
\[
u=x\cdot q.
\]
Orthogonal changes of variables preserve volume. Fubini's theorem then
expresses the volume above the level $u=t$ as the integral, over
$s>t$, of the cross-sectional areas in the parallel planes $P_{q,s}$.
For a rectangular block these cross-sections are polygons, so their areas
can be computed by elementary multivariable geometry.

:::

:::

::: {.pf-step #s1-3}

For each fixed block $A_i$, the function
\[
F_i:S^2\times\RR\to\RR,
\qquad
F_i(q,t)=\operatorname{vol}(A_i\cap H_{q,t}),
\]
is continuous.


::: pf-proof

Let
\[
(q_n,t_n)\to(q,t).
\]
For almost every $x\in\RR^3$,
\[
\mathbf 1_{A_i}(x)
\mathbf 1_{\{x\cdot q_n>t_n\}}
\longrightarrow
\mathbf 1_{A_i}(x)
\mathbf 1_{\{x\cdot q>t\}}.
\]
The only possible failure occurs on the plane
\[
P_{q,t},
\]
which has three-dimensional Lebesgue measure zero. The integrands are
dominated by the integrable function $\mathbf 1_{A_i}$. Dominated
convergence therefore gives
\[
F_i(q_n,t_n)\to F_i(q,t).
\]

:::

:::

::: {.pf-step #s1-4}

For fixed $q\in S^2$, the function
\[
t\longmapsto F_3(q,t)
\]
is nonincreasing and continuous, with
\[
F_3(q,t)=V_3
\]
for all sufficiently negative $t$, and
\[
F_3(q,t)=0
\]
for all sufficiently positive $t$.


::: pf-proof

If $t_1<t_2$, then
\[
H_{q,t_2}\subset H_{q,t_1},
\]
so the volume is nonincreasing. Continuity follows from step [](#s1-3){.pf-ref}.

Since $A_3$ is compact, the continuous function $x\mapsto x\cdot q$
attains a minimum and maximum on $A_3$. Below the minimum, the whole block
lies in $H_{q,t}$; above the maximum, none of it does.

:::

:::

::: {.pf-step #s1-5}

For each $q\in S^2$, there exists $t_q\in\RR$ such that
\[
\boxed{F_3(q,t_q)=\frac{V_3}{2}}.
\]


::: pf-proof

By step [](#s1-4){.pf-ref}, the continuous function $F_3(q,-)$ takes the values
$V_3$ and $0$. The intermediate value theorem gives a level where it
equals $V_3/2$.

:::

:::

::: {.pf-step #s1-6}

For fixed $q$, the function $F_3(q,t)$ is strictly decreasing
while the plane $P_{q,t}$ passes through the interior of $A_3$.


::: pf-proof

Suppose
\[
t_1<t_2
\]
both lie strictly between
\[
\min_{x\in A_3}x\cdot q
\qquad\text{and}\qquad
\max_{x\in A_3}x\cdot q.
\]
Because $A_3$ is a solid convex block with nonempty interior, the slab
\[
A_3\cap\{x:t_1<x\cdot q<t_2\}
\]
contains an open subset of $\RR^3$, hence has positive volume.
Therefore
\[
F_3(q,t_1)-F_3(q,t_2)>0.
\]

:::

:::

::: {.pf-step #s1-7}

The number $t_q$ from step [](#s1-5){.pf-ref} is unique.


::: pf-proof

The value $V_3/2$ is strictly between $0$ and $V_3$, so any level
where it occurs lies between the minimum and maximum values of
$x\cdot q$ on $A_3$. Step [](#s1-6){.pf-ref} gives strict decrease there, so the
level is unique.

:::

:::

::: {.pf-step #s1-8}

The plane $P_{q,t_q}$ bisects $A_3$:
\[
\boxed{
\operatorname{vol}(A_3\cap H_{q,t_q})
=
\operatorname{vol}(A_3\cap J_{q,t_q})
=
\frac{V_3}{2}}.
\]


::: pf-proof

Step [](#s1-5){.pf-ref} gives the first equality to $V_3/2$. The plane
$P_{q,t_q}$ has three-dimensional volume zero, so the two open
half-spaces partition $A_3$ up to a null set. Hence the other half also
has volume $V_3/2$.

:::

:::

::: {.pf-step #s1-9}

The half-volume level satisfies
\[
\boxed{t_{-q}=-t_q}.
\]


::: pf-proof

One has
\[
H_{-q,-t_q}
=
\{x:-x\cdot q>-t_q\}
=
\{x:x\cdot q<t_q\}
=
J_{q,t_q}.
\]
By step [](#s1-8){.pf-ref}, this half-space contains exactly half the volume of $A_3$.
Thus $-t_q$ is a half-volume level for direction $-q$. Uniqueness from
step [](#s1-7){.pf-ref} gives
\[
t_{-q}=-t_q.
\]

:::

:::

::: {.pf-step #s1-10}

The map
\[
q\longmapsto t_q
\]
is continuous on $S^2$.


::: pf-proof

Let $q_n\to q$, and write $t_n=t_{q_n}$. Since $A_3$ is contained
in some ball $B(0,R)$, every half-volume plane meeting the block has
\[
|t_n|\le R.
\]
Thus every subsequence of $(t_n)$ has a convergent further subsequence;
let
\[
t_{n_j}\to t.
\]
By step [](#s1-3){.pf-ref},
\[
F_3(q,t)
=
\lim_{j\to\infty}
F_3(q_{n_j},t_{n_j})
=
\frac{V_3}{2}.
\]
Uniqueness in step [](#s1-7){.pf-ref} gives $t=t_q$. Therefore every convergent
subsequence of $(t_n)$ converges to $t_q$, forcing
\[
t_n\to t_q.
\]

:::

:::

::: {.pf-step #s1-11}

For $i=1,2$, the function
\[
f_i(q)=F_i(q,t_q)
\]
is continuous.


::: pf-proof

The map
\[
q\longmapsto(q,t_q)
\]
is continuous by step [](#s1-10){.pf-ref}, and $F_i$ is continuous by step [](#s1-3){.pf-ref}.
Their composition is $f_i$.

:::

:::

::: {.pf-step #s1-12}

For $i=1,2$,
\[
\boxed{
f_i(-q)=V_i-f_i(q)}.
\]


::: pf-proof

By step [](#s1-9){.pf-ref},
\[
H_{-q,t_{-q}}
=
H_{-q,-t_q}
=
J_{q,t_q}.
\]
Therefore
\[
f_i(-q)
=
\operatorname{vol}(A_i\cap J_{q,t_q}).
\]
The separating plane has volume zero, so
\[
\operatorname{vol}(A_i\cap J_{q,t_q})
=
V_i-
\operatorname{vol}(A_i\cap H_{q,t_q})
=
V_i-f_i(q).
\]

:::

:::

::: {.pf-step #s1-13}

Define
\[
F:S^2\to\RR^2,
\qquad
F(q)=(f_1(q),f_2(q)).
\]
Then $F$ is continuous.


::: pf-proof

This follows from step [](#s1-11){.pf-ref} componentwise.

:::

:::

::: {.pf-step #s1-14}

By the Borsuk--Ulam theorem, there exists $q\in S^2$ such that
\[
\boxed{F(q)=F(-q)}.
\]


::: pf-proof

The Borsuk--Ulam theorem states that every continuous map
\[
S^2\to\RR^2
\]
takes the same value at some antipodal pair. Apply it to the map in step
[](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

For the $q$ from step [](#s1-14){.pf-ref},
\[
\boxed{
f_i(q)=\frac{V_i}{2}
\qquad(i=1,2)}.
\]


::: pf-proof

By step [](#s1-14){.pf-ref},
\[
f_i(q)=f_i(-q).
\]
Step [](#s1-12){.pf-ref} gives
\[
f_i(-q)=V_i-f_i(q).
\]
Hence
\[
2f_i(q)=V_i.
\]

:::

:::

::: {.pf-step #s1-16}

The plane
\[
\boxed{P_{q,t_q}}
\]
simultaneously bisects all three blocks $(A_1,A_2,A_3)$.


::: pf-proof

Step [](#s1-8){.pf-ref} says this plane bisects $A_3$. Step [](#s1-15){.pf-ref} says its
$H_{q,t_q}$-side contains half the volume of each of $A_1$ and $A_2$;
since the plane itself has zero volume, their other halves also have half
the volume. Thus all three blocks are bisected by the same plane.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} address part (a), steps [](#s1-3){.pf-ref} through [](#s1-10){.pf-ref} prove part (b), step
[](#s1-11){.pf-ref} proves part (c), and steps [](#s1-12){.pf-ref} through [](#s1-16){.pf-ref} prove part (d).

:::

:::

:::
