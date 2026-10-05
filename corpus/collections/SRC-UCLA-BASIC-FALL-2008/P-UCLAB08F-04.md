---
schema: qual/card@1
id: P-UCLAB08F-04
kind: problem
title: Positive distance between disjoint compact and closed sets
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
<1>1. Let $K,F\subset\mathbb R^2$, with $K$ closed and bounded and $F$ closed.
Prove that if $K\cap F=\varnothing$, then
\[
d(K,F):=\inf\{d(x,y):x\in K,\ y\in F\}>0.
\]

<1>2. Is <1>1 still true if $K$ is only assumed closed?
Prove your assertion.
:::

::: {.solution}
Assume first that both $K$ and $F$ are nonempty; if one is empty, the distance set is empty and the conclusion is interpreted separately according to the convention for $\inf\varnothing$.

<1>1. Under the hypotheses of part <1>1, the set $K$ is compact.

::: {.proof}
The set $K\subseteq\mathbb R^2$ is closed and bounded. By the Heine--Borel theorem, it is compact.
:::

<1>2. For every $x\in K$, there exists $r_x>0$ such that
\[
B(x,r_x)\cap F=\varnothing.
\]

::: {.proof}
Since
\[
K\cap F=\varnothing,
\]
one has $x\notin F$. The set $F$ is closed, so $\mathbb R^2\setminus F$ is open. Hence some Euclidean ball
\[
B(x,r_x)
\]
is contained in $\mathbb R^2\setminus F$.
:::

<1>3. There are points $x_1,\ldots,x_m\in K$ such that
\[
K\subseteq
\bigcup_{i=1}^m
B\left(x_i,\frac{r_{x_i}}2\right).
\]

::: {.proof}
The balls
\[
B\left(x,\frac{r_x}{2}\right),
\qquad x\in K,
\]
form an open cover of $K$. By compactness from step <1>1, a finite subcover exists.
:::

<1>4. If
\[
\delta=
\min_{1\le i\le m}\frac{r_{x_i}}2,
\]
then
\[
d(x,y)\ge\delta
\]
for every $x\in K$ and $y\in F$.

::: {.proof}
The number $\delta$ is positive because it is the minimum of finitely many positive numbers.

Fix $x\in K$ and $y\in F$. By step <1>3, choose $i$ with
\[
d(x,x_i)<\frac{r_{x_i}}2.
\]
By step <1>2,
\[
d(x_i,y)\ge r_{x_i}.
\]
Hence the triangle inequality gives
\[
\begin{aligned}
d(x,y)
&\ge
d(x_i,y)-d(x,x_i)\\
&>
r_{x_i}-\frac{r_{x_i}}2\\
&=
\frac{r_{x_i}}2\\
&\ge
\delta.
\end{aligned}
\]
:::

<1>5. Therefore
\[
\boxed{d(K,F)>0}.
\]

::: {.proof}
Step <1>4 gives the positive lower bound $\delta$ for every distance
\[
d(x,y),
\qquad
x\in K,\ y\in F.
\]
Thus
\[
d(K,F)\ge\delta>0.
\]
:::

<1>6. Part <1>1 is false if $K$ is assumed only closed.

::: {.proof}
Take
\[
K=\{(x,0):x\in\mathbb R\}
\]
and
\[
F=\left\{\left(x,\frac1x\right):x>0\right\}.
\]
The set $K$ is closed.

To see that $F$ is closed, suppose
\[
\left(x_n,\frac1{x_n}\right)\to(a,b)
\]
in $\mathbb R^2$. Then $x_n\to a$. If $a=0$, the second coordinates $1/x_n$ would be unbounded, contradicting convergence. Hence $a>0$, and then
\[
\frac1{x_n}\to\frac1a,
\]
so $b=1/a$ and $(a,b)\in F$. Thus $F$ is closed.

The two sets are disjoint because every point of $F$ has positive second coordinate. However,
\[
d\left((n,0),\left(n,\frac1n\right)\right)=\frac1n\to0.
\]
Therefore
\[
d(K,F)=0.
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 proves part <1>1, and step <1>6 gives a counterexample to part <1>2.
:::
:::
