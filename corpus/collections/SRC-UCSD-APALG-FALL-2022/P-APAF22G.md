---
schema: qual/card@1
id: P-APAF22G
kind: problem
title: Every bivector in $\mathbb{C}^3 \wedge \mathbb{C}^3$ is decomposable
classification:
  areas:
  - applied-algebra
  topics:
  - Multilinear Algebra
relations: []
review: draft
---

::: {.problem}
Show that any tensor $T \in \mathbb{C}^3 \wedge \mathbb{C}^3$ can be written as $T = v_1 \wedge v_2$ for some $v_1, v_2 \in \mathbb{C}^3$.
:::

::: {.solution}
Fix a basis $e_1,e_2,e_3$ of $\mathbb C^3$. Every element of $\mathbb C^3\wedge\mathbb C^3$ has a unique form
\[
T=a\,e_1\wedge e_2+b\,e_1\wedge e_3+c\,e_2\wedge e_3.
\]
We exhibit $v_1,v_2$ explicitly.

<1>1. If $a\ne0$, then
\[
T=\left(e_1-\frac ca e_3\right)\wedge(ae_2+be_3).
\]
::: {.proof}
Expanding and using $e_i\wedge e_i=0$ and $e_3\wedge e_2=-e_2\wedge e_3$ gives
\[
\begin{aligned}
\left(e_1-\frac ca e_3\right)\wedge(ae_2+be_3)
&=a e_1\wedge e_2+b e_1\wedge e_3-c e_3\wedge e_2\\
&=a e_1\wedge e_2+b e_1\wedge e_3+c e_2\wedge e_3=T.
\end{aligned}
\]
:::

<1>2. If $a=0$ and $b\ne0$, then
\[
T=\left(e_1+\frac cb e_2\right)\wedge(be_3).
\]
::: {.proof}
Directly,
\[
\left(e_1+\frac cb e_2\right)\wedge(be_3)
=b e_1\wedge e_3+c e_2\wedge e_3=T.
\]
:::

<1>3. If $a=b=0$, then
\[
T=e_2\wedge(ce_3).
\]
::: {.proof}
In this case $T=c\,e_2\wedge e_3$, so the displayed equality is immediate. This includes $T=0$ when $c=0$.
:::

<1>4. Hence every bivector in $\mathbb C^3\wedge\mathbb C^3$ is decomposable.
::: {.proof}
The three cases <1>1--<1>3 exhaust all triples $(a,b,c)\in\mathbb C^3$, and each gives an explicit factorization $T=v_1\wedge v_2$.
:::
:::
