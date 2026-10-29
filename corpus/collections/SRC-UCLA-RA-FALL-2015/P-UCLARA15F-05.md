---
schema: qual/card@1
id: P-UCLARA15F-05
kind: problem
title: Hölder continuous functions are meager in $C[0,1]$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 5 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
A function $f \in C([0,1])$ is called Hölder continuous of order $\delta > 0$ if there is a constant $C > 0$ such that $|f(x) - f(y)| \leq C|x-y|^\delta$, $x, y \in [0,1]$. Show that the Hölder continuous functions form a set of the first category (a meager set) in $C([0,1])$.
:::

::: {.solution}

Equip
$$
C([0,1])
$$
with the sup norm
$$
\|f\|_\infty
=
\sup_{x\in[0,1]}|f(x)|.
$$

For integers
$$
m,k\ge1,
$$
define
$$
\boxed{
A_{m,k}
=
\left\{
f\in C([0,1]):
|f(x)-f(y)|
\le
k|x-y|^{1/m}
\text{ for all }x,y\in[0,1]
\right\}.}
$$

::: pf

::: {.pf-step #s1-1}

Every Hölder continuous function of positive order belongs to some
$$
A_{m,k}.
$$


::: pf-proof

Let $f$ be Hölder continuous of order $\delta>0$. Then there exists $C>0$ such that
$$
|f(x)-f(y)|
\le
C|x-y|^\delta.
$$

Choose $m$ so large that
$$
\frac1m\le\delta,
$$
and choose an integer $k\ge C$.

Since
$$
0\le|x-y|\le1,
$$
and $\delta\ge1/m$,
$$
|x-y|^\delta
\le
|x-y|^{1/m}.
$$
Therefore
$$
|f(x)-f(y)|
\le
C|x-y|^\delta
\le
k|x-y|^{1/m},
$$
so $f\in A_{m,k}$.

:::

:::

::: {.pf-step #s1-2}

Hence the set $\mathcal H$ of all Hölder continuous functions satisfies
$$
\boxed{
\mathcal H
\subseteq
\bigcup_{m=1}^{\infty}
\bigcup_{k=1}^{\infty}
A_{m,k}}.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} to each Hölder function.

:::

:::

::: pf-step

Each $A_{m,k}$ is closed in $C([0,1])$.


::: pf-proof

Let
$$
f_j\in A_{m,k}
$$
and suppose
$$
f_j\to f
$$
uniformly.

For fixed $x,y\in[0,1]$,
$$
|f_j(x)-f_j(y)|
\le
k|x-y|^{1/m}.
$$
Uniform convergence implies pointwise convergence, so
$$
f_j(x)\to f(x),
\qquad
f_j(y)\to f(y).
$$
Passing to the limit gives
$$
|f(x)-f(y)|
\le
k|x-y|^{1/m}.
$$
Since $x,y$ were arbitrary,
$$
f\in A_{m,k}.
$$

:::

:::

::: {.pf-step #s1-4}

By uniform continuity of $f$, there exists $\eta>0$ such that
$$
|x-y|<\eta
\Longrightarrow
|f(x)-f(y)|<\frac{\varepsilon}{4}.
$$


::: pf-proof

Every continuous function on the compact interval $[0,1]$ is uniformly continuous.

:::

:::

::: {.pf-step #s1-5}

Choose $h>0$ such that
$$
\boxed{
h<\eta,
\qquad
h<\frac14,
\qquad
k h^{1/m}<\frac{\varepsilon}{4}.}
$$


::: pf-proof

Since
$$
h^{1/m}\to0
$$
as $h\downarrow0$, all three inequalities hold for sufficiently small $h>0$.

:::

:::

::: {.pf-step #s1-6}

Choose
$$
x_0\in(0,1-h)
$$
and set
$$
x_1=x_0+h.
$$


::: pf-proof

The condition $h<1/4$ ensures that such an $x_0$ exists.

:::

:::

::: {.pf-step #s1-7}

There exists a continuous function
$$
\varphi:[0,1]\to[0,\varepsilon/2]
$$
such that
$$
\boxed{
\varphi(x_0)=0,
\qquad
\varphi(x_1)=\frac{\varepsilon}{2}.}
$$


::: pf-proof

For example, define $\varphi$ to be $0$ on $[0,x_0]$, linear from $0$ to $\varepsilon/2$ on $[x_0,x_1]$, and constant $\varepsilon/2$ on $[x_1,1]$.

:::

:::

::: {.pf-step #s1-8}

Define
$$
\boxed{
g=f+\varphi}.
$$


::: pf-proof

The sum of continuous functions is continuous.

:::

:::

::: {.pf-step #s1-9}

One has
$$
\boxed{
\|g-f\|_\infty
\le
\frac{\varepsilon}{2}
<
\varepsilon.}
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
0\le\varphi\le\frac{\varepsilon}{2}.
$$
Thus
$$
\|g-f\|_\infty
=
\|\varphi\|_\infty
\le
\frac{\varepsilon}{2}.
$$

:::

:::

::: {.pf-step #s1-10}

The oscillation of $f$ between $x_0$ and $x_1$ satisfies
$$
\boxed{
|f(x_1)-f(x_0)|
<
\frac{\varepsilon}{4}.}
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
|x_1-x_0|=h<\eta.
$$
Apply step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
|g(x_1)-g(x_0)|
\ge
\frac{\varepsilon}{2}
-
|f(x_1)-f(x_0)|.
$$


::: pf-proof

By steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref},
$$
g(x_1)-g(x_0)
=
f(x_1)-f(x_0)+\frac{\varepsilon}{2}.
$$
Apply the reverse triangle inequality.

:::

:::

::: {.pf-step #s1-12}

Hence
$$
\boxed{
|g(x_1)-g(x_0)|
>
\frac{\varepsilon}{4}.}
$$


::: pf-proof

Use step [](#s1-10){.pf-ref} in step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

But
$$
\boxed{
k|x_1-x_0|^{1/m}
=
k h^{1/m}
<
\frac{\varepsilon}{4}.}
$$


::: pf-proof

Use steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
|g(x_1)-g(x_0)|
>
k|x_1-x_0|^{1/m}.
$$


::: pf-proof

Combine steps [](#s1-12){.pf-ref} through [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

Hence
$$
\boxed{
g\notin A_{m,k}}.
$$


::: pf-proof

Step [](#s1-14){.pf-ref} violates the defining Hölder estimate for the pair $x_0,x_1$.

:::

:::

::: {.pf-step #s1-16}

Thus every open ball around every $f\in A_{m,k}$ contains a point outside $A_{m,k}$.


::: pf-proof

Given any $\varepsilon>0$, steps [](#s1-8){.pf-ref} through [](#s1-15){.pf-ref} construct $g$ with
$$
\|g-f\|_\infty<\varepsilon
$$
but
$$
g\notin A_{m,k}.
$$

:::

:::

::: {.pf-step #s1-17}

Therefore
$$
\boxed{
\operatorname{int}(A_{m,k})=\varnothing.}
$$


::: pf-proof

Step [](#s1-16){.pf-ref} is exactly the statement that $A_{m,k}$ has empty interior.

:::

:::

::: {.pf-step #s1-18}

Since $A_{m,k}$ is closed and has empty interior, it is nowhere dense.


::: pf-proof

For a closed set,
$$
\overline{A_{m,k}}=A_{m,k}.
$$
Thus
$$
\operatorname{int}\overline{A_{m,k}}
=
\operatorname{int}(A_{m,k})
=
\varnothing
$$
by step [](#s1-17){.pf-ref}.

:::

:::

::: {.pf-step #s1-19}

The countable union
$$
\bigcup_{m,k\ge1}A_{m,k}
$$
is meager.


::: pf-proof

It is a countable union of nowhere-dense sets by step [](#s1-18){.pf-ref}.

:::

:::

::: {.pf-step #s1-20}

Therefore the set of all Hölder continuous functions is meager in $C([0,1])$.


::: pf-proof

By step [](#s1-2){.pf-ref}, the Hölder functions form a subset of the meager set from step [](#s1-19){.pf-ref}. Every subset of a meager set is meager.

:::

:::

::: pf-qed

Step [](#s1-20){.pf-ref} is the required conclusion.

:::

:::

:::
