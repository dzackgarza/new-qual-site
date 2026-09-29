---
schema: qual/card@1
id: P-BKS11-1B
kind: problem
title: An open set containing the unit square contains a thickened rectangle
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
  note: Compared the authored statement with pages 3--4 of the retained Spring 2011 solution PDF and independently reviewed the compactness argument along the top edge of the square.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the finite subcover and the uniform Euclidean-ball estimate yielding the thickened rectangle.
---

::: {.problem}
Let D be an open subset of $\mathbb { R } ^ { 2 }$ (with the topology induced by the euclidean metric), and assume that it contains the closed unit square

$$
[ 0 , 1 ] \times [ 0 , 1 ] = \{ ( x , y ) : 0 \leq x \leq 1 , 0 \leq y \leq 1 \} .
$$

Show that D contains the partially-open rectangle

$$
[ 0 , 1 ] \times [ 0 , 1 + \epsilon ) = \{ ( x , y ) : 0 \leq x \leq 1 , 0 \leq y < 1 + \epsilon \}
$$

for some $\epsilon > 0$
:::

::: {.solution}

::: pf

::: {.pf-step #radius-exists}
For every $x\in[0,1]$, there is a radius $r_x>0$ such that
$$
B((x,1),r_x)\subseteq D.
$$

::: pf-proof
The point $(x,1)$ belongs to the closed unit square, hence to $D$. Since
$D$ is open, some Euclidean open ball centered at $(x,1)$ lies inside
$D$.
:::

:::

::: {.pf-step #intervals-cover}
The intervals
$$
I_x
\coloneqq
\left(x-\frac{r_x}{2},x+\frac{r_x}{2}\right),
\qquad
x\in[0,1],
$$
form an open cover of $[0,1]$.

::: pf-proof
For each $x\in[0,1]$, one has
$$
x\in I_x.
$$
Thus every point of $[0,1]$ is contained in at least one of the displayed
open intervals.
:::

:::

::: {.pf-step #finite-subcover}
There are points $x_1,\ldots,x_m\in[0,1]$ such that
$$
[0,1]
\subseteq
I_{x_1}\cup\cdots\cup I_{x_m}.
$$

::: pf-proof
The interval $[0,1]$ is compact, and step [](#intervals-cover){.pf-ref} gives an open cover.
Compactness therefore supplies a finite subcover.
:::

:::

::: {.pf-step #epsilon-positive}
Define
$$
\varepsilon
\coloneqq
\frac12
\min_{1\leq j\leq m}r_{x_j}.
$$
Then $\varepsilon>0$.

::: pf-proof
Every $r_{x_j}$ is positive by step [](#radius-exists){.pf-ref}. The minimum of finitely many
positive numbers is positive, so the displayed $\varepsilon$ is positive.
:::

:::

::: {.pf-step #strip-in-d}
One has
$$
[0,1]\times[1,1+\varepsilon)
\subseteq
D.
$$

::: pf-proof
Take
$$
(u,v)\in[0,1]\times[1,1+\varepsilon).
$$
By step [](#finite-subcover){.pf-ref}, choose $j$ such that $u\in I_{x_j}$. Then
$$
\abs{u-x_j}
<
\frac{r_{x_j}}{2}.
$$
Also, by step [](#epsilon-positive){.pf-ref},
$$
0\leq v-1
<
\varepsilon
\leq
\frac{r_{x_j}}{2}.
$$
Hence
$$
\begin{aligned}
\norm{(u,v)-(x_j,1)}^2
&=
(u-x_j)^2+(v-1)^2\\
&<
\frac{r_{x_j}^2}{4}
+
\frac{r_{x_j}^2}{4}\\
&<
r_{x_j}^2.
\end{aligned}
$$
Therefore
$$
(u,v)\in B((x_j,1),r_{x_j})\subseteq D
$$
by step [](#radius-exists){.pf-ref}.
:::

:::

::: {.pf-step #rectangle-in-d}
The partially open rectangle
$$
\boxed{
[0,1]\times[0,1+\varepsilon)
}
$$
is contained in $D$.

::: pf-proof
By hypothesis,
$$
[0,1]\times[0,1]\subseteq D.
$$
Step [](#strip-in-d){.pf-ref} gives
$$
[0,1]\times[1,1+\varepsilon)\subseteq D.
$$
The union of these two sets is exactly
$$
[0,1]\times[0,1+\varepsilon).
$$
:::

:::

::: pf-qed
Step [](#rectangle-in-d){.pf-ref} is the required inclusion.
:::

:::

:::
