---
schema: qual/card@1
id: P-TIE-F09-18
kind: problem
title: Uniform continuity of $z^2$ on disks but not on $\mathbb C$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 18.
---

::: {.problem}
Show that $f ( z ) = z ^ { 2 }$ is uniformly continuous in any open disk $| z | < R$ , where $R > 0$ is fixed, but it is not uniformly continuous on C.
:::

::: {.solution}

Let
$$
f(z)=z^2.
$$

::: pf

::: {.pf-step #s1-1}

If $|z|<R$ and $|w|<R$, then
$$
|f(z)-f(w)|
<
2R|z-w|.
$$


::: pf-proof

Factor the difference:
$$
|z^2-w^2|
=
|z-w|\,|z+w|.
$$
Since
$$
|z+w|
\le
|z|+|w|
<
2R,
$$
the claimed estimate follows.

:::

:::

::: {.pf-step #s1-2}

The function $f$ is uniformly continuous on the open disk
$$
D_R=\{z\in\CC:|z|<R\}.
$$


::: pf-proof

Given $\varepsilon>0$, choose
$$
\delta=\frac{\varepsilon}{2R}.
$$
If $z,w\in D_R$ and $|z-w|<\delta$, then step [](#s1-1){.pf-ref} gives
$$
|f(z)-f(w)|
<
2R\delta
=
\varepsilon.
$$
The same $\delta$ works for every pair of points in $D_R$, so the continuity is uniform.

:::

:::

::: {.pf-step #s1-3}

There are sequences $z_n,w_n\in\CC$ such that
$$
|z_n-w_n|\longrightarrow0
$$
but
$$
|f(z_n)-f(w_n)|\not\longrightarrow0.
$$


::: pf-proof

Take
$$
z_n=n,
\qquad
w_n=n+\frac1n.
$$
Then
$$
|z_n-w_n|=\frac1n\longrightarrow0.
$$
On the other hand,
$$
\begin{aligned}
|f(w_n)-f(z_n)|
&=
\left|
\left(n+\frac1n\right)^2-n^2
\right|\\
&=
2+\frac1{n^2},
\end{aligned}
$$
which tends to $2$.

:::

:::

::: {.pf-step #s1-4}

The function $f(z)=z^2$ is not uniformly continuous on $\CC$.


::: pf-proof

If $f$ were uniformly continuous, then for every two sequences with
$|z_n-w_n|\to0$ one would have
$$
|f(z_n)-f(w_n)|\to0.
$$
Step [](#s1-3){.pf-ref} provides a contradiction.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves uniform continuity on every fixed open disk, and step [](#s1-4){.pf-ref} proves failure
of uniform continuity on the whole plane.

:::

:::

:::
