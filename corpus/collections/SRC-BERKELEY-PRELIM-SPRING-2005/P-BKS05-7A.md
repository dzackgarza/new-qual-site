---
schema: qual/card@1
id: P-BKS05-7A
kind: problem
title: Continuity of the radius of convergence of a meromorphic function
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained argument: Taylor radii are locally
    1-Lipschitz away from poles by recentering the same holomorphic germ;
    near an isolated pole p the exact radius is |c-p|, so assigning radius
    zero at p gives continuity.
---

::: {.problem}
Let U be a connected open subset of $\mathbb { C }$, and let $f ( z )$ be a meromorphic function on U having at least one pole.
For each $c \in U$ that is not a pole of $f ,$ let $R ( c )$ be the radius of convergence of the Taylor series of f centered at c. Prove that $R ( c )$ extends to a continuous function defined on all of U.
:::

::: {.solution}
Let $P\subseteq U$ be the set of poles of $f$, and write
$$
D(c,s)\coloneqq\{z\in\CC:|z-c|<s\}.
$$
For $c\in U\setminus P$, let $g_c$ denote the holomorphic function
defined on $D(c,R(c))$ by the Taylor series of $f$ at $c$.

::: pf

::: pf-step
For every $c\in U\setminus P$, one has
$$
0<R(c)<\infty.
$$

::: pf-proof
Since $f$ is holomorphic near $c$, its Taylor series has positive
radius, so $R(c)>0$.

If $R(c)=\infty$, then $g_c$ is entire and agrees with $f$ on a
neighborhood of $c$. The meromorphic function $f-g_c$ on the connected
set $U$ then vanishes on a nonempty open set, so the identity theorem
for meromorphic functions gives
$$
f=g_c|_U.
$$
This would make every pole of $f$ removable, contradicting the
hypothesis that $f$ has at least one pole. Hence $R(c)<\infty$.
:::

:::

::: {.pf-step #locally-lipschitz}
The function $R$ is locally $1$-Lipschitz on $U\setminus P$.

::: pf-proof
Fix $c\in U\setminus P$. Choose $\varepsilon>0$ such that
$$
D(c,\varepsilon)\subseteq U\setminus P.
$$
Then $R(c)\geq\varepsilon$. Let
$$
c'\in D(c,\varepsilon/2).
$$
Since
$$
D(c',\varepsilon/2)\subseteq D(c,\varepsilon)\subseteq U\setminus P,
$$
one also has $R(c')\geq\varepsilon/2>|c-c'|$.

The functions $g_c$ and $f$ agree near $c'$. Hence the Taylor series of
$f$ at $c'$ is the Taylor series of $g_c$ at $c'$. The disk
$$
D\bigl(c',R(c)-|c-c'|\bigr)
$$
is contained in $D(c,R(c))$, so
$$
R(c')\geq R(c)-|c-c'|.
$$
Interchanging $c$ and $c'$ gives
$$
R(c)\geq R(c')-|c-c'|.
$$
Therefore
$$
|R(c)-R(c')|\leq|c-c'|
$$
for every $c'$ sufficiently close to $c$.
:::

:::

::: {.pf-step #radius-equals-distance-to-pole}
If $p\in P$, then for all nonpoles $c$ sufficiently close to
$p$,
$$
R(c)=|c-p|.
$$

::: pf-proof
Because poles are isolated and $U$ is open, choose $\varepsilon>0$
such that
$$
D(p,\varepsilon)\subseteq U
$$
and $p$ is the only pole of $f$ in this disk. Let
$$
0<|c-p|<\frac{\varepsilon}{2}
$$
and set $d\coloneqq|c-p|$.

The disk $D(c,d)$ lies in $D(p,\varepsilon)\setminus\{p\}$, so
$f$ is holomorphic on $D(c,d)$. Therefore its Taylor series at $c$
converges throughout that disk, and
$$
R(c)\geq d.
$$

Suppose $R(c)>d$. Then $p\in D(c,R(c))$, so $g_c$ is holomorphic in a
neighborhood of $p$. Set
$$
\Omega\coloneqq D(c,R(c))\cap D(p,\varepsilon).
$$
The set $\Omega$ is an open convex neighborhood of $p$, so
$\Omega\setminus\{p\}$ is connected. Both $g_c$ and $f$ are
holomorphic there, and they agree on the nonempty open subset
$D(c,d)\subseteq\Omega\setminus\{p\}$. The identity theorem
therefore gives
$$
g_c=f
$$
on $\Omega\setminus\{p\}$. Since $g_c$ is holomorphic at $p$, this
makes the singularity of $f$ at $p$ removable, contradicting that $p$
is a pole. Hence
$$
R(c)\leq d.
$$
Together with the opposite inequality, this gives $R(c)=|c-p|$.
:::

:::

::: {.pf-step #continuous-at-poles}
Define
$$
\widetilde R(c)
\coloneqq
\begin{cases}
R(c),&c\in U\setminus P,\\
0,&c\in P.
\end{cases}
$$
Then $\widetilde R$ is continuous at every pole.

::: pf-proof
Fix $p\in P$. By step [](#radius-equals-distance-to-pole){.pf-ref}, for all $c\in U\setminus P$ sufficiently
close to $p$,
$$
\widetilde R(c)=R(c)=|c-p|\longrightarrow0=\widetilde R(p).
$$
The poles are isolated, so this also controls every approach to $p$
inside $U$.
:::

:::

::: {.pf-step #continuous-extension}
The function $\widetilde R$ is a continuous extension of $R$ to
all of $U$.

::: pf-proof
Step [](#locally-lipschitz){.pf-ref} gives continuity at every point of $U\setminus P$, and step
[](#continuous-at-poles){.pf-ref} gives continuity at every point of $P$. By definition,
$\widetilde R=R$ on $U\setminus P$.
:::

:::

::: pf-qed
Step [](#continuous-extension){.pf-ref} is exactly the required extension.
:::

:::

:::
