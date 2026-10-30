---
schema: qual/card@1
id: P-UCLARA15S-06
kind: problem
title: Compact operators have separable range
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
When $B_1$ and $B_2$ are Banach spaces, call a linear operator $T:B_1\to B_2$ compact if for any bounded sequence $(x_n)$ in $B_1$, the sequence $(Tx_n)$ has a convergent subsequence.
Show that if $T$ is compact then $\operatorname{Im}T$ has a dense countable subset.
:::

::: {.solution}

For each integer $N\ge1$, let
$$
A_N
\coloneqq
\{x\in B_1:\norm{x}_{B_1}\le N\}.
$$

::: pf

::: {.pf-step #s1-1}

For every $N\ge1$, the set $T(A_N)$ is relatively compact in $B_2$.


::: pf-proof

Let $(y_j)$ be any sequence in $T(A_N)$. Choose $x_j\in A_N$ with
$$
Tx_j=y_j.
$$
The sequence $(x_j)$ is bounded in $B_1$. Since $T$ is compact, $(Tx_j)=(y_j)$ has a convergent subsequence in $B_2$. Thus every sequence in $T(A_N)$ has a convergent subsequence.

Because $B_2$ is complete, this sequential precompactness is equivalent to relative compactness. Hence the closure
$$
K_N
\coloneqq
\overline{T(A_N)}
$$
is compact.

:::

:::

::: {.pf-step #s1-2}

For every $N,m\ge1$, there is a finite set
$$
F_{N,m}\subset T(A_N)
$$
such that every point of $T(A_N)$ lies within distance $2/m$ of some point of $F_{N,m}$.


::: pf-proof

By step [](#s1-1){.pf-ref}, the compact set $K_N$ is totally bounded. Hence there are points
$$
z_1,\dots,z_q\in K_N
$$
such that
$$
K_N
\subset
\bigcup_{j=1}^q
B_{B_2}(z_j,1/m).
$$
Discard any ball that does not meet $T(A_N)$. For each remaining ball choose one point
$$
y_j\in
T(A_N)\cap B_{B_2}(z_j,1/m).
$$
Let $F_{N,m}$ be the finite set of chosen points.

If $y\in T(A_N)$, choose $j$ with
$$
\norm{y-z_j}<1/m.
$$
Then
$$
\norm{y-y_j}
\le
\norm{y-z_j}+\norm{z_j-y_j}
<
\frac2m.
$$
Thus $F_{N,m}$ is a finite $2/m$-net for $T(A_N)$.

:::

:::

::: {.pf-step #s1-3}

For each $N\ge1$, the set
$$
D_N
\coloneqq
\bigcup_{m=1}^{\infty}F_{N,m}
$$
is countable and dense in $T(A_N)$.


::: pf-proof

Each $F_{N,m}$ is finite, so the countable union $D_N$ is countable.

Fix $y\in T(A_N)$ and $\varepsilon>0$. Choose $m$ so large that
$$
\frac2m<\varepsilon.
$$
By step [](#s1-2){.pf-ref}, some point $d\in F_{N,m}\subset D_N$ satisfies
$$
\norm{y-d}<\frac2m<\varepsilon.
$$
Hence $D_N$ is dense in $T(A_N)$.

:::

:::

::: {.pf-step #s1-4}

The set
$$
D
\coloneqq
\bigcup_{N=1}^{\infty}D_N
$$
is countable and dense in $\operatorname{Im}T$.


::: pf-proof

Each $D_N$ is countable by step [](#s1-3){.pf-ref}, so $D$ is countable.

Moreover,
$$
B_1
=
\bigcup_{N=1}^{\infty}A_N,
$$
hence
$$
\operatorname{Im}T
=
\bigcup_{N=1}^{\infty}T(A_N).
$$
If $y\in\operatorname{Im}T$, then $y\in T(A_N)$ for some $N$. Step [](#s1-3){.pf-ref} says that $D_N\subset D$ is dense in that set, so every neighborhood of $y$ meets $D$. Thus $D$ is dense in $\operatorname{Im}T$.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{\operatorname{Im}T\text{ is separable}.}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} constructs an explicit dense countable subset of $\operatorname{Im}T$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
