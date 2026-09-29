---
schema: qual/card@1
id: P-BKF16-2B
kind: problem
title: Volume of a compact set as a limit of integrals of powers of a distance cutoff
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: the
    distance function is 1-Lipschitz, while the cutoff powers converge
    pointwise to the indicator of K and have common bounded support.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked existence of nearest points, the zero set of the distance
    function, boundedness of the closed unit neighborhood of K, and the
    dominated-convergence argument.
---

::: {.problem}
Let K be a compact subset of $\mathbb { R } ^ { n }$ and $\boldsymbol { f } ( \boldsymbol { x } ) = \boldsymbol { d } ( \boldsymbol { x } , K )$ be the Euclidean distance from x to the nearest point of K.

(a) Show that f is continuous and $f ( x ) = 0 { \mathrm { ~ i f ~ } } x \in K$

(b) Let $g ( x ) = \operatorname* { m a x } ( 1 - f ( x ) , 0 )$ . Show that $\int g ^ { m }$ converges to the n-dimensional volume of K as $m \to \infty$

(The n-dimensional volume of K is defined to be $\textstyle \int 1 _ { K }$ , if the integral exists, where $1 _ { K } ( x ) = 1$ for $x \in K$ , and $1 _ { K } ( x ) = 0$ for $x \notin K . )$ )
:::

::: {.solution}
Write
$$
f(x)=d(x,K)
\coloneqq
\inf_{y\in K}\norm{x-y}.
$$

::: pf

::: {.pf-step #s1}

For every $x\in\RR^n$, there is a point
$$
y_x\in K
$$
such that
$$
f(x)=\norm{x-y_x}.
$$

::: pf-proof

For fixed $x$, the function
$$
y\longmapsto\norm{x-y}
$$
is continuous on the compact set $K$. It therefore attains its
minimum.

:::

:::

::: {.pf-step #s2}

For all $x,y\in\RR^n$,
$$
\abs{f(x)-f(y)}
\le
\norm{x-y}.
$$

::: pf-proof

Let $y_0\in K$ realize the distance from $y$ to $K$, as in step [](#s1){.pf-ref}.
Then
$$
\begin{aligned}
f(x)
&\le
\norm{x-y_0}\\
&\le
\norm{x-y}+\norm{y-y_0}\\
&=
\norm{x-y}+f(y).
\end{aligned}
$$
Thus
$$
f(x)-f(y)\le\norm{x-y}.
$$
Interchanging $x$ and $y$ gives the opposite inequality, and the two
together yield the claim.

:::

:::

::: {.pf-step #s3}

The function $f$ is continuous and
$$
\boxed{f(x)=0\iff x\in K}.
$$

::: pf-proof

Step [](#s2){.pf-ref} shows that $f$ is $1$-Lipschitz, hence continuous.

If $x\in K$, then
$$
f(x)\le\norm{x-x}=0,
$$
so $f(x)=0$. Conversely, if $f(x)=0$, step [](#s1){.pf-ref} gives
$y_x\in K$ with
$$
\norm{x-y_x}=0.
$$
Hence $x=y_x\in K$. This proves part (a).

:::

:::

::: {.pf-step #s4}

The function
$$
g(x)\coloneqq\max\{1-f(x),0\}
$$
is continuous and satisfies
$$
0\le g(x)\le1.
$$

::: pf-proof

Continuity follows from step [](#s3){.pf-ref} and continuity of the maximum of two
real-valued continuous functions. Since $f\ge0$, one has
$$
1-f(x)\le1,
$$
and taking the maximum with $0$ gives the displayed bounds.

:::

:::

::: {.pf-step #s5}

The functions $g^m$ are supported in the bounded set
$$
K_1
\coloneqq
\{x\in\RR^n:d(x,K)\le1\}.
$$

::: pf-proof

If $d(x,K)>1$, then
$$
1-f(x)<0
$$
and hence $g(x)=0$. Thus the support of every positive power of $g$ is
contained in $K_1$.

Because $K$ is compact, it is contained in some ball
$$
B(0,R).
$$
If $x\in K_1$, choose $y\in K$ with
$$
\norm{x-y}\le1.
$$
Then
$$
\norm x
\le
\norm{x-y}+\norm y
\le
R+1.
$$
Thus $K_1$ is bounded. It is also closed by continuity of $f$, hence
compact.

:::

:::

::: {.pf-step #s6}

Pointwise on $\RR^n$,
$$
g(x)^m
\longrightarrow
1_K(x)
$$
as $m\to\infty$.

::: pf-proof

If $x\in K$, step [](#s3){.pf-ref} gives $f(x)=0$, so
$$
g(x)=1
$$
and every power equals $1$.

If $x\notin K$, then step [](#s3){.pf-ref} gives $f(x)>0$. Hence
$$
0\le g(x)<1,
$$
so
$$
g(x)^m\to0.
$$
These are exactly the two values of $1_K$.

:::

:::

::: {.pf-step #s7}

For every $m\ge1$,
$$
0\le g(x)^m\le1_{K_1}(x).
$$

::: pf-proof

Step [](#s4){.pf-ref} gives $0\le g^m\le1$. Step [](#s5){.pf-ref} shows that $g^m$ vanishes
outside $K_1$. Combining the two statements gives the displayed
domination.

:::

:::

::: {.pf-step #s8}

One has
$$
\boxed{
\lim_{m\to\infty}
\int_{\RR^n}g(x)^m\,dx
=
\int_{\RR^n}1_K(x)\,dx.
}
$$

::: pf-proof

The compact set $K_1$ is bounded and Borel measurable, so
$1_{K_1}$ is integrable. Steps [](#s6){.pf-ref} and [](#s7){.pf-ref} therefore satisfy the
hypotheses of the dominated convergence theorem, which gives the
displayed limit. Since compact $K$ is Borel measurable, the right-hand
side is its $n$-dimensional volume. This proves part (b).

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (a), and step [](#s8){.pf-ref} proves part (b).

:::

:::

:::
