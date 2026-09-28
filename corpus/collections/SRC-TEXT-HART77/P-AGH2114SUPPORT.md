---
schema: qual/card@1
id: P-AGH2114SUPPORT
kind: problem
title: The support of a section is closed, but the support of a sheaf need not be
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Support
  - Stalks
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.14 statement and source-order placement after II.1.13.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $\mcf$ be a sheaf on $X$ and let $s \in \mcf(U)$ be a section over an open set $U$.
The **support of $s$**, denoted $\supp s$, is defined to be $\ts{P \in U \st s_P \neq 0}$, where $s_P$ denotes the germ of $s$ in the stalk $\mcf_P$.
Show that $\supp s$ is a closed subset of $U$.

Define the support of $\mcf$ to be $\supp \mcf \da \ts{P \in X \st \mcf_P \neq 0}$.
Show that this need not be a closed subset.
:::

::: {.solution}
<1>1. The complement of the support of a section is open:
\[
U\setminus\operatorname{supp}s
=\{P\in U:s_P=0\}.
\]
::: {.proof}
Let $P\in U$ satisfy
\[
s_P=0
\]
in the stalk $\mcf_P$.  By the definition of a stalk, equality of the germ $s_P$ with the zero germ means that there exists an open neighborhood
\[
P\in V\subseteq U
\]
such that
\[
s|_V=0.
\]
For every $Q\in V$, therefore,
\[
s_Q=0.
\]
Thus
\[
V\subseteq U\setminus\operatorname{supp}s.
\]
Every point of the complement has an open neighborhood contained in the complement, so the complement is open.
:::

<1>2. Hence
\[
\boxed{\operatorname{supp}s\text{ is closed in }U.}
\]
::: {.proof}
This is exactly the conclusion of <1>1.
:::

<1>3. The support of a sheaf need not be closed.
::: {.proof}
Take
\[
X=\mathbb A^1_{\mathbb C}
=\operatorname{Spec}\mathbb C[x].
\]
For each positive integer $n$, let
\[
i_n:\{n\}\hookrightarrow X
\]
be the closed-point inclusion and let
\[
\mathcal K_n=i_{n*}\mathbb C
\]
be the corresponding skyscraper sheaf.  Define
\[
\mcf=\bigoplus_{n\ge1}\mathcal K_n
\]
in the category of sheaves of abelian groups.

The stalk functor commutes with direct sums, so for every $P\in X$,
\[
\mcf_P
\cong
\bigoplus_{n\ge1}(\mathcal K_n)_P.
\]
For a skyscraper sheaf,
\[
(\mathcal K_n)_P
\cong
\begin{cases}
\mathbb C,&P=n,\\
0,&P\ne n.
\end{cases}
\]
Therefore
\[
\operatorname{supp}\mcf
=\{1,2,3,\ldots\}
\subseteq\mathbb A^1_{\mathbb C}.
\]

This subset is infinite.  Every proper Zariski-closed subset of $\mathbb A^1_{\mathbb C}$ is finite, because it is the zero set of a nonzero polynomial in one variable.  Hence
\[
\{1,2,3,\ldots\}
\]
is Zariski dense but is not all of $X$.  It is therefore not closed.
:::

<1>4. Thus there is a genuine distinction:
\[
\boxed{
\operatorname{supp}s\text{ is always closed, whereas }
\operatorname{supp}\mcf\text{ need not be closed}.
}
\]
::: {.proof}
The first assertion is <1>2 and the second is the example in <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>4 is exactly the pair of assertions requested.
:::
:::
