---
schema: qual/card@1
id: E-70TGS
kind: problem
title: Shrinking maps and contractions on compact metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §28 Exercise 7, printed p. 181, with Theorem
    26.9, Theorem 27.4 and Theorem 28.2; the four parts and the two hints are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.7, PDF pp. 20-21. (b) the intersection of the
    iterated images is a single fixed point, by the extreme value theorem on the diameter;
    (c) x - x^2/2 on [0,1] is shrinking but not a contraction; (d) (x + sqrt(x^2+1))/2 on R
    is shrinking with no fixed point, its difference quotient being 1/2 plus a term of
    modulus below 1/2. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked all four parts against Munkres §28 Exercise
    7, printed p. 181: (b) the nested compact sets A_n = f^n(X) with nonempty intersection
    (Theorem 26.9), f(A) = A by sequential compactness, and A a point through the maximum of
    d on A x A (Theorem 27.4); (c) that x - x^2/2 maps [0,1] into itself, is shrinking, and
    has ratios 1 - x/2 tending to 1; (d) the ratio formula, the bound giving shrinking, the
    ratios tending to 1, and the absence of a fixed point. Part (a) is added on the card: a
    contraction is a shrinking map, so (b) gives its unique fixed point. positron0802,
    Exercise 28.7, PDF pp. 20-21, for (b), (c), (d).
---

::: {.exercise}

Let $(X, d)$ be a nonempty metric space.
If $f$ satisfies the condition

$$
d(f(x), f(y)) < d(x, y)
$$

for all $x, y \in X$ with $x \neq y$, then $f$ is called a shrinking map.
If there is a number $\alpha < 1$ such that

$$
d(f(x), f(y)) \leq \alpha d(x, y)
$$

for all $x, y \in X$, then $f$ is called a contraction.
A fixed point of $f$ is a point $x$ such that $f(x) = x$.

(a) If $f$ is a contraction and $X$ is compact, show $f$ has a unique fixed point.
[Hint: Define $f^1 = f$ and $f^{n+1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$.]

(b) Show more generally that if $f$ is a shrinking map and $X$ is compact, then $f$ has a unique fixed point.
[Hint: Let $A$ be as before. Given $x \in A$, choose $x_n$ so that $x = f^{n+1}(x_n)$. If $a$ is the limit of some subsequence of the sequence $y_n = f^n(x_n)$, show that $a \in A$ and $f(a) = x$. Conclude that $A = f(A)$, so that $\operatorname{diam} A = 0$.]

(c) Let $X = [0, 1]$.
Show that $f(x) = x - x^2/2$ maps $X$ into $X$ and is a shrinking map that is not a contraction.
[Hint: Use the mean-value theorem of calculus.]

(d) The result in (a) holds if $X$ is a complete metric space, such as $\RR$; see the exercises of §43. The result in (b) does not: show that the map $f: \RR \to \RR$ given by $f(x) = [x + (x^2 + 1)^{1/2}]/2$ is a shrinking map that is not a contraction and has no fixed point.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.7, PDF pp. 20--21** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); parts (b), (c) and (d) are theirs, and part (a), which their sheet leaves implicit as the special case, is proved here from (b).

Throughout, $(X,d)$ is a nonempty compact metric space and $f^{1}=f$, $f^{n+1}=f\circ f^{n}$.

::: pf

::: {.pf-step #part-b}
(b) A shrinking map of a compact metric space has a unique fixed point.

:::: pf-proof

::: {.pf-step #nested}
With $A_{n}=f^{n}(X)$ and $A=\bigcap_{n\in\ZZ_{+}}A_{n}$, each $A_{n}$ is compact and closed, $A_{n+1}\subset A_{n}$, and $A$ is nonempty and compact.

::: pf-proof
$f^{n}$ is continuous, being an iterate of the continuous map $f$, so $A_{n}=f^{n}(X)$ is compact, being a continuous image of the compact space $X$; a compact subspace of a metric space is closed (Theorem 26.3 does it for Hausdorff, and a metric space is Hausdorff). Also $A_{n+1}=f^{n+1}(X)=f^{n}\big(f(X)\big)\subset f^{n}(X)=A_{n}$ because $f(X)\subset X$. The sets $A_{n}$ are nonempty closed subsets of the compact space $X$ with the finite intersection property, since $A_{1}\cap\dots\cap A_{N}=A_{N}\ne\varnothing$; so their intersection is nonempty (Theorem 26.9). Finally $A$ is closed, being an intersection of closed sets, and a closed subset of a compact space is compact.
:::

:::

::: {.pf-step #forward}
$f(A)\subset A$.

::: pf-proof
Let $y=f(x)$ with $x\in A$. For each $n$, $x\in A_{n}$ gives $y\in f(A_{n})=f^{n+1}(X)=A_{n+1}\subset A_{n}$; so $y$ lies in every $A_{n}$, that is $y\in A$.
:::

:::

::: {.pf-step #backward}
$A\subset f(A)$.

::: pf-proof
Let $x\in A$. Since $x\in A_{n+1}=f^{n+1}(X)=f\big(f^{n}(X)\big)$, there is $x_{n}\in X$ with $f^{n+1}(x_{n})=x$; put $y_{n}=f^{n}(x_{n})\in A_{n}$. Then $f(y_{n})=x$ for every $n$. A compact metric space is sequentially compact, so the sequence $(y_{n})$ has a subsequence converging to a point $a$; that point lies in $A$ because $A$ is closed and every $y_{n}$ lies in $A$. Continuity of $f$ gives $f(a)=\lim_{k}f(y_{n_{k}})=x$, so $x\in f(A)$.
:::

:::

::: {.pf-step #diameter}
$A$ consists of a single point.

::: pf-proof
Suppose $A$ has two distinct points. The function $(x,y)\mapsto d(x,y)$ is continuous on $A\times A$ (Munkres §20 Exercise 3(a)) and $A\times A$ is compact, being a product of compact spaces, so it attains a maximum at some pair $(x_{0},y_{0})\in A\times A$ (Theorem 27.4). Since $A$ has two distinct points $p,q$, the maximum is at least $d(p,q)>0$, so $x_{0}\ne y_{0}$. By step [](#backward){.pf-ref} write $x_{0}=f(a)$ and $y_{0}=f(b)$ with $a,b\in A$. Then
$$
d(x_{0},y_{0})=d\big(f(a),f(b)\big)<d(a,b)\le d(x_{0},y_{0}),
$$
the strict inequality because $f$ is shrinking and $a\ne b$ — they are distinct since $d(x_{0},y_{0})>0=d(a,a)$ — and the last inequality because $(x_{0},y_{0})$ maximizes $d$ on $A\times A$. This is a contradiction.
:::

:::

::: {.pf-step #fixed}
$f$ has exactly one fixed point.

::: pf-proof
Let $A=\{p\}$. By steps [](#forward){.pf-ref} and [](#backward){.pf-ref}, $f(A)\subset A$ and $A\subset f(A)$, so $f(A)=A=\{p\}$ and $f(p)=p$. If $q$ were another fixed point, $q\ne p$, then $d(p,q)=d\big(f(p),f(q)\big)<d(p,q)$, which is impossible; so $p$ is the unique fixed point.
:::

:::

::: {.pf-step}
(b) holds.

::: pf-proof
Steps [](#nested){.pf-ref} to [](#fixed){.pf-ref} prove that a shrinking map of a compact metric space has exactly one fixed point.
:::

:::

:::

:::

::: {.pf-step #part-a}
(a) A contraction of a compact metric space has a unique fixed point.

::: pf-proof
Let $f$ satisfy $d\big(f(x),f(y)\big)\le\alpha d(x,y)$ with $\alpha<1$. For $x\ne y$ one has $d(x,y)>0$, so $d\big(f(x),f(y)\big)\le\alpha d(x,y)<d(x,y)$; hence $f$ is a shrinking map, and step [](#part-b){.pf-ref} gives it a unique fixed point.
:::

:::

::: {.pf-step #part-c}
(c) On $X=[0,1]$ the map $f(x)=x-x^{2}/2$ carries $X$ into $X$, is a shrinking map, and is not a contraction.

::: pf-proof
For $x\in[0,1]$ one has $f(x)=x(1-x/2)\ge x/2\ge0$ and $f(x)\le x\le1$, so $f$ maps $X$ into $X$. For $x\ne y$,
$$
f(x)-f(y)=(x-y)\Big(1-\frac{x+y}{2}\Big),
$$
and $0<x+y\le2$ gives $0\le1-(x+y)/2<1$; hence $\abs{f(x)-f(y)}<\abs{x-y}$ and $f$ is shrinking. It is not a contraction: for $x\ne0$,
$$
\frac{\abs{f(x)-f(0)}}{\abs{x-0}}=1-\frac x2,
$$
which tends to $1$ as $x\to0^{+}$, so for every $\alpha<1$ there is $x$ with $\abs{f(x)-f(0)}>\alpha\abs{x-0}$.
:::

:::

::: {.pf-step #part-d}
(d) On $\RR$ the map $f(x)=\big(x+(x^{2}+1)^{1/2}\big)/2$ is a shrinking map that is not a contraction and has no fixed point.

:::: pf-proof

::: {.pf-step #d-shrinking}
$f$ is shrinking.

::: pf-proof
For $x\ne y$,
$$
\frac{f(x)-f(y)}{x-y}=\frac12+\frac{x+y}{2\big((x^{2}+1)^{1/2}+(y^{2}+1)^{1/2}\big)},
$$
because $(x^{2}+1)^{1/2}-(y^{2}+1)^{1/2}=(x^{2}-y^{2})/\big((x^{2}+1)^{1/2}+(y^{2}+1)^{1/2}\big)$. Since $\abs{x}<(x^{2}+1)^{1/2}$ and $\abs{y}<(y^{2}+1)^{1/2}$,
$$
\abs{x+y}\le\abs{x}+\abs{y}<(x^{2}+1)^{1/2}+(y^{2}+1)^{1/2},
$$
so the fraction has modulus less than $\tfrac12$ and the whole ratio has modulus less than $1$. Hence $\abs{f(x)-f(y)}<\abs{x-y}$.
:::

:::

::: {.pf-step #d-not-contraction}
$f$ is not a contraction.

::: pf-proof
The ratio displayed in step [](#d-shrinking){.pf-ref} tends to $\tfrac12+\tfrac12=1$ as $x,y\to+\infty$ with $x\ne y$ fixed in difference: taking $y=x+1$ gives $x+y=2x+1$ and denominators $2\big((x^{2}+1)^{1/2}+((x+1)^{2}+1)^{1/2}\big)\sim4x$, so the fraction tends to $\tfrac12$ and the ratio to $1$. So no $\alpha<1$ bounds all the ratios.
:::

:::

::: {.pf-step #d-no-fixed}
$f$ has no fixed point.

::: pf-proof
If $f(x)=x$ then $\big(x+(x^{2}+1)^{1/2}\big)/2=x$, that is $(x^{2}+1)^{1/2}=x$; squaring gives $x^{2}+1=x^{2}$, which is impossible.
:::

:::

::: {.pf-step}
(d) holds.

::: pf-proof
Steps [](#d-shrinking){.pf-ref}, [](#d-not-contraction){.pf-ref} and [](#d-no-fixed){.pf-ref} are the three assertions about the example.
:::

:::

:::

:::

::: {.pf-step}
All four parts hold.

::: pf-proof
Steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref}, [](#part-c){.pf-ref} and [](#part-d){.pf-ref} are the four assertions of the exercise.
:::

:::

:::
:::
