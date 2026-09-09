---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-02
kind: problem
title: Cartesian products of locally compact spaces (closure formulation)
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against problem (2) in assets/attachments/Day_1_-_Compactness_Problems.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
A topological space $X$ is called *locally compact* if every point in $X$ has an open neighborhood whose closure is compact.
Show that the Cartesian product of two locally compact spaces, with the product topology, is also locally compact.
:::

::: {.solution}
Let $X$ and $Y$ be locally compact.

<1>1. Fix $(x,y)\in X\times Y$ and choose open neighborhoods $U\ni x$ and $V\ni y$ such that $\overline U$ and $\overline V$ are compact.
::: {.proof}
This is the assumed local compactness of $X$ at $x$ and of $Y$ at $y$.
:::

<1>2. The set $U\times V$ is an open neighborhood of $(x,y)$ in $X\times Y$.
::: {.proof}
Products of open sets form a basis for the product topology.
:::

<1>3. One has
\[
\overline{U\times V}=\overline U\times\overline V.
\]
::: {.proof}
The set $\overline U\times\overline V$ is closed in $X\times Y$ and contains $U\times V$, so
\[
\overline{U\times V}\subseteq\overline U\times\overline V.
\]

Conversely, let $(u,v)\in\overline U\times\overline V$ and let $O$ be any open neighborhood of $(u,v)$.
Choose a basic open set $O_X\times O_Y$ with
\[
(u,v)\in O_X\times O_Y\subseteq O.
\]
Since $u\in\overline U$, the set $O_X$ meets $U$; since $v\in\overline V$, the set $O_Y$ meets $V$.
Hence $(O_X\times O_Y)\cap(U\times V)$ is nonempty.
Thus every neighborhood of $(u,v)$ meets $U\times V$, proving $(u,v)\in\overline{U\times V}$.
:::

<1>4. The closure $\overline{U\times V}$ is compact.
::: {.proof}
By <1>1, both $\overline U$ and $\overline V$ are compact.
We verify directly that their product is compact.
Let $\mathcal W$ be an open cover of $\overline U\times\overline V$.
Fix $u\in\overline U$.
For each $v\in\overline V$, choose $W_v\in\mathcal W$ containing $(u,v)$ and a basic open rectangle
\[
N_v\times M_v\subseteq W_v
\]
with $u\in N_v$ and $v\in M_v$.
Compactness of $\overline V$ gives finitely many points $v_1,\dots,v_r$ such that
\[
\overline V\subseteq M_{v_1}\cup\cdots\cup M_{v_r}.
\]
Then
\[
N_u:=N_{v_1}\cap\cdots\cap N_{v_r}
\]
is an open neighborhood of $u$, and $N_u\times\overline V$ is covered by the finitely many sets $W_{v_1},\dots,W_{v_r}$.

As $u$ varies, the sets $N_u$ cover $\overline U$.
Compactness of $\overline U$ yields $u_1,\dots,u_s$ with
\[
\overline U\subseteq N_{u_1}\cup\cdots\cup N_{u_s}.
\]
The finitely many members of $\mathcal W$ chosen for these $s$ neighborhoods cover all of $\overline U\times\overline V$.
Thus $\overline U\times\overline V$ is compact, and <1>3 gives compactness of
\[
\overline{U\times V}=\overline U\times\overline V.
\]
:::

<1>5. Therefore $X\times Y$ is locally compact.
::: {.proof}
For the arbitrary point $(x,y)$, <1>2 gives an open neighborhood whose closure is compact by <1>4.
This is precisely the stated definition of local compactness.
:::
:::
