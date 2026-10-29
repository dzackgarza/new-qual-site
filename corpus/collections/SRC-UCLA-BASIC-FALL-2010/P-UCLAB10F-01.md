---
schema: qual/card@1
id: P-UCLAB10F-01
kind: problem
title: Positive distance between a compact set and a disjoint closed set
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Let $F$ be a closed subset of a metric space $(X,\rho)$.

(a) Show that if $K\subset X$ is compact, then $K\cap F=\varnothing$ if and only if
$$
\inf_{x\in K,\,y\in F}\rho(x,y)>0.
$$

(b) Is the statement in (a) true if $K$ is assumed only to be closed rather than compact?
Give a proof if it is true and a counterexample if it is false.
:::

::: {.solution}

Assume first that $K$ and $F$ are nonempty.

::: pf

::: {.pf-step #s1-1}

If
$$
\inf_{x\in K,\ y\in F}\rho(x,y)>0,
$$
then
$$
K\cap F=\varnothing.
$$


::: pf-proof

If some point $z$ belonged to $K\cap F$, then
$$
\rho(z,z)=0
$$
would be one of the distances occurring in the infimum. Hence the infimum would be $0$, contradicting the assumed positivity.

:::

:::

::: {.pf-step #s1-2}

Suppose
$$
K\cap F=\varnothing.
$$
For every $x\in K$, there is $r_x>0$ such that
$$
B(x,r_x)\cap F=\varnothing.
$$


::: pf-proof

Since $x\notin F$ and $F$ is closed, the complement
$$
X\setminus F
$$
is open and contains $x$. Hence some metric ball $B(x,r_x)$ is contained in the complement.

:::

:::

::: {.pf-step #s1-3}

There are points $x_1,\ldots,x_m\in K$ such that
$$
K\subseteq
\bigcup_{i=1}^m
B\left(x_i,\frac{r_{x_i}}2\right).
$$


::: pf-proof

The balls
$$
B\left(x,\frac{r_x}{2}\right),
\qquad x\in K,
$$
form an open cover of the compact set $K$. Hence a finite subcover exists.

:::

:::

::: {.pf-step #s1-4}

With
$$
\delta=
\min_{1\le i\le m}\frac{r_{x_i}}2,
$$
one has
$$
\rho(x,y)\ge\delta
$$
for every $x\in K$ and $y\in F$.


::: pf-proof

The number $\delta$ is positive.
Fix $x\in K$ and $y\in F$. Choose $i$ as in step [](#s1-3){.pf-ref}, so
$$
\rho(x,x_i)<\frac{r_{x_i}}2.
$$
By step [](#s1-2){.pf-ref},
$$
\rho(x_i,y)\ge r_{x_i}.
$$
The triangle inequality gives
$$
\begin{aligned}
\rho(x,y)
&\ge
\rho(x_i,y)-\rho(x_i,x)\\
&>
r_{x_i}-\frac{r_{x_i}}2\\
&=
\frac{r_{x_i}}2\\
&\ge
\delta.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

If $K$ is compact, then
$$
\boxed{
K\cap F=\varnothing
\iff
\inf_{x\in K,\ y\in F}\rho(x,y)>0
}.
$$


::: pf-proof

The forward implication follows from step [](#s1-4){.pf-ref}, and the reverse implication is step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Part (a) is false if $K$ is assumed only closed.


::: pf-proof

Take
$$
X=\RR^2,
$$
$$
K=\{(x,0):x\in\RR\},
$$
and
$$
F=\left\{
\left(x,\frac1x\right):x>0
\right\}.
$$
The set $K$ is closed.

To see that $F$ is closed, suppose
$$
\left(x_n,\frac1{x_n}\right)\to(a,b)
$$
in $\RR^2$. Then $x_n\to a$. If $a=0$, the second coordinates would be unbounded, contradicting convergence. Hence $a>0$, and then
$$
\frac1{x_n}\to\frac1a,
$$
so $(a,b)\in F$.

The sets are disjoint, but
$$
\left\|
(n,0)-\left(n,\frac1n\right)
\right\|
=
\frac1n\to0.
$$
Thus
$$
\inf_{x\in K,\ y\in F}\rho(x,y)=0.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} gives the counterexample required in part (b).

:::

:::

:::
