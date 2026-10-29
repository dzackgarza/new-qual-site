---
schema: qual/card@1
id: P-UCLARA16S-04
kind: problem
title: Finite-dimensional subspaces of Banach spaces are complemented
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $V_1$ be a finite-dimensional subspace of the Banach space $V$. Show that there exists a continuous projection $P:V\to V_1$, i.e. a continuous linear map $P:V\to V$ such that $P^2=P$ and the range of $P$ is equal to $V_1$.
:::

::: {.solution}

Choose a basis
\[
e_1,\dots,e_n
\]
of $V_1$.

::: pf

::: pf-step

For each $j=1,\dots,n$, the coordinate functional
\[
\lambda_j:V_1\to\FF,
\qquad
\lambda_j\!\left(\sum_{k=1}^n a_ke_k\right)=a_j,
\]
is continuous.


::: pf-proof

Every linear map from a finite-dimensional normed space to a normed space is continuous. Since $V_1$ is finite dimensional, each coordinate functional $\lambda_j$ is continuous.

:::

:::

::: {.pf-step #s1-2}

For each $j$, there exists a continuous linear functional
\[
\widetilde\lambda_j:V\to\FF
\]
whose restriction to $V_1$ is $\lambda_j$.


::: pf-proof

Apply the Hahn--Banach theorem to the bounded linear functional $\lambda_j$ on the subspace $V_1\subset V$.

:::

:::

::: {.pf-step #s1-3}

Define
\[
P:V\to V_1,
\qquad
P(x)
\coloneqq
\sum_{j=1}^n
\widetilde\lambda_j(x)e_j.
\]
Then $P$ is linear and continuous.


::: pf-proof

Linearity follows from linearity of the functionals $\widetilde\lambda_j$. Moreover,
\[
\begin{aligned}
\|P(x)\|
&\le
\sum_{j=1}^n
|\widetilde\lambda_j(x)|\,\|e_j\|\\
&\le
\left(
\sum_{j=1}^n
\|\widetilde\lambda_j\|\,\|e_j\|
\right)
\|x\|.
\end{aligned}
\]
Thus $P$ is bounded, hence continuous.

:::

:::

::: {.pf-step #s1-4}

The restriction of $P$ to $V_1$ is the identity map.


::: pf-proof

If
\[
v=\sum_{k=1}^n a_ke_k\in V_1,
\]
then step [](#s1-2){.pf-ref} gives
\[
\widetilde\lambda_j(v)
=
\lambda_j(v)
=
a_j.
\]
Therefore
\[
P(v)
=
\sum_{j=1}^n a_je_j
=v.
\]

:::

:::

::: {.pf-step #s1-5}

The map $P$ satisfies
\[
\boxed{
P^2=P,
\qquad
\operatorname{range}(P)=V_1
}.
\]


::: pf-proof

By definition, $P(x)\in V_1$ for every $x\in V$. Applying step [](#s1-4){.pf-ref} to $P(x)$ gives
\[
P^2(x)
=
P(P(x))
=
P(x),
\]
so $P^2=P$.

Also,
\[
\operatorname{range}(P)\subseteq V_1.
\]
Conversely, step [](#s1-4){.pf-ref} says that every $v\in V_1$ satisfies $P(v)=v$, so every element of $V_1$ lies in the range of $P$. Hence
\[
\operatorname{range}(P)=V_1.
\]

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref} show that $P$ is a continuous projection of $V$ onto $V_1$.

:::

:::

:::
