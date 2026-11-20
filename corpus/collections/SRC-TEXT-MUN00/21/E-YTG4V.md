---
schema: qual/card@1
id: E-YTG4V
kind: problem
title: Continuity of the field operations on $\RR$
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 12, printed p. 135, with Lemma 21.4;
    the four parts and the three hints are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.12, PDF pp. 26-27. Delta = epsilon over two for
    addition, the three-term expansion for multiplication, the five cases of the preimage of
    an interval under the reciprocal, and subtraction and quotient as composites with
    negation and the reciprocal. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same four parts, and the table of preimages in (c) repaired:
    its case a = 0 < b carried a superfluous " = f^{-1}((a,b))", and the five cases now compute their
    preimages from the inequalities one at a time, with the openness of each trace stated and the
    passage from basis intervals to arbitrary open sets written out. Nothing else was changed: the
    epsilons, the three-term expansion and the use of Exercise 18.10 for the product of continuous maps
    are the source's. The statement was checked against Munkres, Topology (2000), Section 21 Exercise
    12, printed p. 135.
---

::: {.exercise}

Prove continuity of the algebraic operations on $\RR$, as follows.
Use the metric $d(a, b) = \abs{a - b}$ on $\RR$ and the metric on $\RR^2$ given by the equation

$$
\rho((x, y), (x_0, y_0)) = \max\theset{\abs{x - x_0}, \abs{y - y_0}}.
$$

(a) Show that addition is continuous.
Hint: Given $\epsilon$, let $\delta = \epsilon/2$ and note that

$$
d(x + y, x_0 + y_0) \leq \abs{x - x_0} + \abs{y - y_0}.
$$

(b) Show that multiplication is continuous.
Hint: Given $(x_0, y_0)$ and $0 < \epsilon < 1$, let

$$
3\delta = \epsilon/(\abs{x_0} + \abs{y_0} + 1)
$$

and note that

$$
d(xy, x_0y_0) \leq \abs{x_0}\abs{y - y_0} + \abs{y_0}\abs{x - x_0} + \abs{x - x_0}\abs{y - y_0}.
$$

(c) Show that the operation of taking reciprocals is a continuous map from $\RR - \theset{0}$ to $\RR$.
[Hint: Show the inverse image of the interval $(a, b)$ is open. Consider five cases, according as $a$ and $b$ are positive, negative, or zero.]

(d) Show that the subtraction and quotient operations are continuous.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.12** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the four parts, the $\delta=\varepsilon/2$ of (a), the three-term expansion of (b) and the five cases of (c) are that solution's, and Whitman, printed pp. 249--250, gives the same four. One slip is repaired: the table of preimages in (c) listed the case $a=0<b$ with a superfluous " $=f^{-1}((a,b))$" and left the five cases unseparated from their justifications, so the cases are now computed one by one, each from the inequalities.

The statement was checked against Munkres, *Topology* (2000), §21 Exercise 12, with Lemma 21.4 on printed p. 131, Theorem 18.2 on printed p. 107, Theorem 18.4 on printed p. 110 and Exercises 18.10 and 18.11 on printed p. 112. Throughout $d(a,b)=\abs{a-b}$ on $\RR$ and
$$
\rho\big((x,y),(x_{0},y_{0})\big)\coloneqq\max\theset{\abs{x-x_{0}},\ \abs{y-y_{0}}}
$$
on $\RR^{2}$, which is a metric inducing the product topology (Exercise 21.3(a)); so continuity of a map on $\RR^{2}$ is to be checked in $\rho$-balls, and continuity on the subspace $\RR\times(\RR-\theset{0})$ is checked in the traces of those balls.

::: pf

::: {.pf-step #addition}

(a) Addition is continuous as a map $\RR^{2}\to\RR$.

::: pf-proof

Let $(x_{0},y_{0})\in\RR^{2}$ and $\varepsilon>0$, and take $\delta\coloneqq\varepsilon/2$. If $\rho((x,y),(x_{0},y_{0}))<\delta$ then $\abs{x-x_{0}}<\delta$ and $\abs{y-y_{0}}<\delta$, so
$$
d(x+y,x_{0}+y_{0})\leq\abs{x-x_{0}}+\abs{y-y_{0}}<2\delta=\varepsilon .
$$
Since $(x_{0},y_{0})$ and $\varepsilon$ were arbitrary, addition is continuous.

:::

:::

::: {.pf-step #multiplication}

(b) Multiplication is continuous as a map $\RR^{2}\to\RR$.

::: pf-proof

Let $(x_{0},y_{0})\in\RR^{2}$ and $\varepsilon>0$, and take
$$
\delta\coloneqq\min\theset{\frac{\varepsilon}{\abs{x_{0}}+\abs{y_{0}}+1},\ 1}.
$$
If $\rho((x,y),(x_{0},y_{0}))<\delta$ then
$$
d(xy,x_{0}y_{0})=\abs{x_{0}(y-y_{0})+y_{0}(x-x_{0})+(x-x_{0})(y-y_{0})}
\leq\abs{x_{0}}\abs{y-y_{0}}+\abs{y_{0}}\abs{x-x_{0}}+\abs{x-x_{0}}\abs{y-y_{0}}
<\delta\big(\abs{x_{0}}+\abs{y_{0}}+\delta\big),
$$
and $\delta<1$ gives $\abs{x_{0}}+\abs{y_{0}}+\delta<\abs{x_{0}}+\abs{y_{0}}+1$, while $\delta\leq\varepsilon/(\abs{x_{0}}+\abs{y_{0}}+1)$; so the last expression is less than $\varepsilon$. Hence multiplication is continuous.

:::

:::

::: {.pf-step #reciprocal}

(c) The map $f\colon\RR-\theset{0}\to\RR$, $f(x)\coloneqq 1/x$, is continuous.

:::: pf-proof

By the definition of continuity it suffices to show that the preimage of each basis element of $\RR$ is open in $\RR-\theset{0}$, the open intervals $(a,b)$ with $a<b$ being a basis. Fix $a<b$ and consider the five cases the hint lists.

::: {.pf-step #both-positive}

If $0<a<b$ then $f^{-1}\big((a,b)\big)=(1/b,1/a)$.

::: pf-proof

For $x>0$ the inequalities $a<1/x<b$ are equivalent to $ax<1$ and $1<bx$, that is to $x<1/a$ and $x>1/b$; and $1/b<1/a$ because $0<a<b$. Points with $1/x\in(a,b)\subset(0,+\infty)$ are positive automatically, so the preimage is exactly $(1/b,1/a)$.

:::

:::

::: {.pf-step #both-negative}

If $a<b<0$ then $f^{-1}\big((a,b)\big)=(1/b,1/a)$.

::: pf-proof

Here $1/x\in(a,b)$ forces $x<0$. For $x<0$ the inequality $a<1/x$ is equivalent, on multiplying by the negative number $x$ and reversing, to $ax>1$, that is to $x<1/a$; and $1/x<b$ is equivalent in the same way to $1>bx$, that is to $x>1/b$. So the preimage is $(1/b,1/a)$, and $1/b<1/a$ because $a<b<0$.

:::

:::

::: {.pf-step #straddling}

If $a<0<b$ then $f^{-1}\big((a,b)\big)=(-\infty,1/a)\cup(1/b,+\infty)$.

::: pf-proof

Split according to the sign of $x$. If $x>0$ then $1/x>0>a$, so $a<1/x<b$ reduces to $1/x<b$, that is to $x>1/b$. If $x<0$ then $1/x<0<b$, so it reduces to $a<1/x$, that is to $x<1/a$. The two pieces are disjoint and their union is the preimage.

:::

:::

::: {.pf-step #zero-end}

If $a=0<b$ then $f^{-1}\big((a,b)\big)=(1/b,+\infty)$, and if $a<b=0$ then $f^{-1}\big((a,b)\big)=(-\infty,1/a)$.

::: pf-proof

In the first case $0<1/x<b$ forces $x>0$ and is equivalent to $1<bx$, that is to $x>1/b$. In the second $a<1/x<0$ forces $x<0$ and is equivalent, on multiplying by $x<0$, to $ax>1$, that is to $x<1/a$.

:::

:::

::: {.pf-step #open-preimages}

In each of the five cases $f^{-1}\big((a,b)\big)$ is open in $\RR-\theset{0}$, so $f$ is continuous.

::: pf-proof

An interval $(1/b,1/a)$ and a ray $(-\infty,1/a)$ or $(1/b,+\infty)$ are open in $\RR$; each of the five preimages is therefore the trace on $\RR-\theset{0}$ of an open set of $\RR$ — none of them contains $0$, since $1/a$ and $1/b$ are nonzero with the signs computed above — and so is open in the subspace $\RR-\theset{0}$. The open intervals $(a,b)$ with $a<b$ form a basis for the topology of $\RR$ (§13), so an arbitrary open $U\subset\RR$ is a union of them and $f^{-1}(U)$ is a union of sets open in $\RR-\theset{0}$, hence open there. That is the definition of continuity of $f$.

:::

:::

::::

:::

::: pf-step

(d) Subtraction and quotient are continuous.

::: pf-proof

For subtraction, let $\nu\colon\RR\to\RR$, $\nu(y)\coloneqq-y$, which is an isometry of $\RR$ and hence continuous, since $\abs{\nu(y)-\nu(y_{0})}=\abs{(-y)-(-y_{0})}=\abs{y-y_{0}}$, so that $\delta=\varepsilon$ serves in the definition. By Exercise 18.10 the product map $\mathrm{id}_{\RR}\times\nu\colon\RR^{2}\to\RR^{2}$ is continuous, and $x-y$ is the composite of it with the continuous addition of step [](#addition){.pf-ref}; a composite of continuous maps is continuous (Theorem 18.2(c)).

For the quotient, let $Z\coloneqq\RR\times(\RR-\theset{0})$, a subspace of $\RR^{2}$. The map $\Phi\colon Z\to\RR^{2}$, $\Phi(x,y)\coloneqq(x,1/y)$, is continuous: its first coordinate is the restriction to $Z$ of the projection $\pi_{1}$, and its second is $f\circ\pi_{2}$ with $f$ the continuous map of step [](#reciprocal){.pf-ref}, both continuous by Theorem 18.4 and Theorem 18.2(d). Since $x/y$ is the composite of $\Phi$ with the continuous multiplication of step [](#multiplication){.pf-ref}, it too is continuous on $Z$, and that is the quotient operation with its stated domain. So (d) holds.

:::

:::

:::

:::
