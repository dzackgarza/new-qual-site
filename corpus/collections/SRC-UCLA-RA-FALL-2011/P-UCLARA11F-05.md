---
schema: qual/card@1
id: P-UCLARA11F-05
kind: problem
title: Weak type estimate for the Hardy-Littlewood maximal function
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
For $f\in L^1(\RR)$, define
$$
Mf(x):=\sup_{h>0}\frac1{2h}\int_{x-h}^{x+h}\abs{f(y)}\,dy.
$$
Prove that there is a constant $A$ such that for every $\alpha>0$,
$$
\lambda\{x\in\RR:Mf(x)>\alpha\}\le \frac{A}{\alpha}\norm{f}_{L^1}.
$$
If you use a covering lemma, prove it.
:::

::: {.solution}

Fix
$$
\alpha>0
$$
and set
$$
E_\alpha
=
\{x\in\RR:Mf(x)>\alpha\}.
$$

## A finite covering lemma

::: pf

::: {.pf-step #s1-1}

Let
$$
\mathcal I=\{I_1,\dots,I_N\}
$$
be a finite family of bounded intervals in $\RR$. Then there exists a pairwise disjoint subfamily
$$
J_1,\dots,J_m
$$
such that
$$
\boxed{
\bigcup_{I\in\mathcal I}I
\subseteq
\bigcup_{k=1}^{m}3J_k},
$$
where $3J_k$ denotes the interval with the same center as $J_k$ and three times its length.


::: pf-proof

Choose $J_1$ to be an interval of maximal length in $\mathcal I$. Remove $J_1$ and every interval meeting it. From the remaining family choose $J_2$ of maximal length, remove it and every interval meeting it, and continue. Since the original family is finite, the process stops.

The selected intervals are pairwise disjoint by construction.

Every original interval $I$ is either selected or was removed because it met some selected interval $J_k$ with
$$
\setmeasure{I}\le \setmeasure{J_k},
$$
since $J_k$ had maximal length among the intervals remaining at that stage.

Choose
$$
z\in I\cap J_k.
$$
If $c_k$ is the center of $J_k$, then for any $y\in I$,
$$
\abs{y-c_k}
\le
\abs{y-z}+\abs{z-c_k}
\le
\setmeasure{I}+\frac{\setmeasure{J_k}}{2}
\le
\frac{3\setmeasure{J_k}}{2}.
$$
Thus $y\in3J_k$, so
$$
I\subseteq3J_k.
$$
Hence the union of the entire family is contained in the union of the triples of the selected intervals.

:::

:::

::: pf-step

The set $E_\alpha$ is open.


::: pf-proof

Take $x\in E_\alpha$. Then for some $h>0$,
$$
\frac1{2h}
\int_{x-h}^{x+h}\abs{f(y)}\,dy
>
\alpha.
$$
Set
$$
A=
\int_{x-h}^{x+h}\abs{f(y)}\,dy.
$$
Then
$$
A>2h\alpha.
$$
Choose $\delta>0$ so small that
$$
\frac{A}{2(h+\delta)}>\alpha.
$$

If $\abs{x'-x}<\delta$, then
$$
[x-h,x+h]
\subseteq
[x'-(h+\delta),x'+(h+\delta)].
$$
Therefore
$$
\frac1{2(h+\delta)}
\int_{x'-(h+\delta)}^{x'+(h+\delta)}
\abs{f(y)}\,dy
\ge
\frac{A}{2(h+\delta)}
>
\alpha.
$$
Hence $Mf(x')>\alpha$, so a neighborhood of $x$ lies in $E_\alpha$.

:::

:::

::: {.pf-step #s1-3}

For every $x\in K$, choose $h_x>0$ such that
$$
\boxed{
\frac1{2h_x}
\int_{x-h_x}^{x+h_x}\abs{f(y)}\,dy
>
\alpha}.
$$


::: pf-proof

This is the definition of $Mf(x)>\alpha$.

:::

:::

::: pf-step

The family
$$
\{I_x:x\in K\}
$$
is an open cover of $K$.


::: pf-proof

Each $x\in K$ belongs to its interval $I_x$.

:::

:::

::: pf-step

By compactness, choose a finite subcover
$$
I_1,\dots,I_N.
$$


::: pf-proof

Every open cover of a compact set has a finite subcover.

:::

:::

::: pf-step

Apply the covering lemma from step [](#s1-1){.pf-ref} to obtain pairwise disjoint intervals
$$
J_1,\dots,J_m
$$
chosen from the $I_j$ such that
$$
\boxed{
K
\subseteq
\bigcup_{k=1}^{m}3J_k}.
$$


::: pf-proof

The finite subcover satisfies
$$
K\subseteq\bigcup_{j=1}^{N}I_j.
$$
The covering lemma gives
$$
\bigcup_{j=1}^{N}I_j
\subseteq
\bigcup_{k=1}^{m}3J_k.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\lambda(K)
\le
3\sum_{k=1}^{m}\setmeasure{J_k}.
$$


::: pf-proof

By subadditivity,
$$
\lambda(K)
\le
\sum_{k=1}^{m}\setmeasure{3J_k}
=
3\sum_{k=1}^{m}\setmeasure{J_k}.
$$

:::

:::

::: {.pf-step #s1-8}

Every selected interval $J_k$ satisfies
$$
\boxed{
\alpha\setmeasure{J_k}
<
\int_{J_k}\abs{f(y)}\,dy}.
$$


::: pf-proof

Each $J_k$ is one of the intervals chosen in step [](#s1-3){.pf-ref}. Since
$$
\setmeasure{J_k}=2h_x,
$$
the average inequality from step [](#s1-3){.pf-ref} is exactly the displayed inequality.

:::

:::

::: {.pf-step #s1-9}

Hence
$$
3\sum_{k=1}^{m}\setmeasure{J_k}
<
\frac3\alpha
\sum_{k=1}^{m}
\int_{J_k}\abs{f(y)}\,dy.
$$


::: pf-proof

Divide the inequalities in step [](#s1-8){.pf-ref} by $\alpha$ and sum.

:::

:::

::: {.pf-step #s1-10}

Since the $J_k$ are pairwise disjoint,
$$
\sum_{k=1}^{m}
\int_{J_k}\abs{f(y)}\,dy
\le
\norm{f}_{L^1}.
$$


::: pf-proof

The sum of the integrals over pairwise disjoint measurable sets is the integral over their union, which is bounded by the integral over all of $\RR$.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
\lambda(K)
\le
\frac3\alpha
\norm{f}_{L^1}}.
$$


::: pf-proof

Combine steps [](#s1-7){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

Since $E_\alpha$ is open,
$$
\lambda(E_\alpha)
=
\sup\{\lambda(K):K\subseteq E_\alpha,\ K\text{ compact}\}.
$$


::: pf-proof

Lebesgue measure is inner regular on open subsets of $\RR$.

:::

:::

::: {.pf-step #s1-13}

Taking the supremum in step [](#s1-11){.pf-ref} gives
$$
\boxed{
\lambda(E_\alpha)
\le
\frac3\alpha
\norm{f}_{L^1}}.
$$


::: pf-proof

The same upper bound holds for every compact $K\subseteq E_\alpha$, so it also bounds their supremum.

:::

:::

::: {.pf-step #s1-14}

Thus the weak type $(1,1)$ estimate holds with
$$
\boxed{A=3}.
$$


::: pf-proof

Step [](#s1-13){.pf-ref} is precisely
$$
\lambda\{Mf>\alpha\}
\le
\frac{A}{\alpha}\norm{f}_1
$$
with $A=3$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the required covering lemma, and step [](#s1-14){.pf-ref} proves the maximal-function estimate.

:::

:::

:::
