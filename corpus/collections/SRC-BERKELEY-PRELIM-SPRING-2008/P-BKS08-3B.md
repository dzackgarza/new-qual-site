---
schema: qual/card@1
id: P-BKS08-3B
kind: problem
title: A finite-index subgroup contains a bounded-index normal subgroup
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
  note: >-
    Checked against the vendored UC Berkeley Spring 2008 preliminary-exam
    solution packet. The packet reproduces the problem statement but does not
    print a solution for Problem 3B.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Independently checked via the action of G on the left cosets of H.
---

::: {.problem}
Let $G$ be a group and $H\le G$ a subgroup of finite index $n$. Show that $G$ contains a normal subgroup $N$ such that
$$
N\subseteq H
\qquad\text{and}\qquad
[G:N]\le n!.
$$
:::

::: {.solution}
Let
$$
X\coloneqq G/H
$$
be the set of left cosets of $H$ in $G$. By hypothesis,
$\abs{X}=n$.

::: pf

::: {.pf-step #phi-homomorphism}
Left multiplication defines a homomorphism
$$
\varphi:G\longrightarrow\operatorname{Sym}(X)\cong S_n.
$$

::: pf-proof
For $g\in G$, define
$$
\varphi(g)(xH)=gxH.
$$
This is well defined on cosets and is a permutation of $X$, with
inverse $\varphi(g^{-1})$. Moreover,
$$
\varphi(g_1g_2)(xH)
=g_1g_2xH
=\varphi(g_1)\bigl(\varphi(g_2)(xH)\bigr),
$$
so $\varphi$ is a homomorphism.
:::

:::

::: {.pf-step #n-normal}
Set
$$
N\coloneqq\ker\varphi.
$$
Then $N\trianglelefteq G$.

::: pf-proof
The kernel of a group homomorphism is normal.
:::

:::

::: {.pf-step #n-subset-h}
One has
$$
N\subseteq H.
$$

::: pf-proof
If $g\in N$, then $\varphi(g)$ fixes every coset in $X$, in
particular the coset $H$. Thus
$$
gH=H,
$$
which is equivalent to $g\in H$.
:::

:::

::: {.pf-step #index-bound}
The index of $N$ satisfies
$$
[G:N]\le n!.
$$

::: pf-proof
By the first isomorphism theorem,
$$
G/N\cong\operatorname{im}\varphi.
$$
Since $\operatorname{im}\varphi$ is a subgroup of
$\operatorname{Sym}(X)$ and $\abs{X}=n$,
$$
[G:N]
=\abs{\operatorname{im}\varphi}
\le\abs{S_n}
=n!.
$$
:::

:::

::: {.pf-step #conclusion}
Therefore $G$ contains a normal subgroup $N$ with
$$
\boxed{N\subseteq H\quad\text{and}\quad[G:N]\le n!}.
$$

::: pf-proof
Steps [](#n-normal){.pf-ref}, [](#n-subset-h){.pf-ref} and [](#index-bound){.pf-ref} establish all three required properties.
:::

:::

::: pf-qed
Step [](#conclusion){.pf-ref} is the desired conclusion.
:::

:::

:::
