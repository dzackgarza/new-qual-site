---
schema: qual/card@1
id: P-WESTOP03-09
kind: problem
title: Point-set properties of the Sorgenfrey line and its square
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $S$ be the Sorgenfrey line, the real numbers with basis
$$
\{[a,b):a<b\}.
$$

1. Explain why $S$ is completely regular, separable, Lindelöf, and not metrizable.
2. Explain why $S\times S$ is separable, not normal, and not Lindelöf.
:::

::: {.solution}

::: pf

::: pf-step

The Sorgenfrey line $S$ is Hausdorff and has a basis of clopen sets.


::: pf-proof

If $x<y$, then
$$
[x,y)\quad\text{and}\quad[y,y+1)
$$
are disjoint neighborhoods. Thus $S$ is Hausdorff. A basic interval $[a,b)$ is open by definition, and its complement
$$
(-\infty,a)\cup[b,\infty)
$$
is open in the Sorgenfrey topology: each point $x<a$ has some basic interval $[x,c)$ contained in $(-\infty,a)$, while each $x\geq b$ has $[x,x+1)\subset[b,\infty)$. Hence $[a,b)$ is also closed.

:::

:::

::: {.pf-step #s1-2}

Therefore $S$ is completely regular.


::: pf-proof

Let $F\subset S$ be closed and $x\notin F$. Since $S\setminus F$ is open, choose a clopen basic neighborhood $U=[x,b)$ with
$$
x\in U\subseteq S\setminus F.
$$
The characteristic function
$$
\varphi(y)=\begin{cases}0,&y\in U,\\1,&y\notin U\end{cases}
$$
is continuous because $U$ is clopen, satisfies $\varphi(x)=0$, and equals $1$ on $F$. Together with Hausdorffness, this is complete regularity.

:::

:::

::: {.pf-step #s1-3}

The set $\QQ$ is dense in $S$, so $S$ is separable.


::: pf-proof

Every nonempty basic interval $[a,b)$ contains a rational number because $a<b$ and $\QQ$ is dense in the ordinary real line. Thus every nonempty open set meets $\QQ$.

:::

:::

::: {.pf-step #s1-4}

The Sorgenfrey line is Lindelöf.


::: pf-proof

Let $\mathcal U$ be an open cover of $S$. For each $x\in\RR$, choose $U_x\in\mathcal U$ and $b_x>x$ such that
$$
[x,b_x)\subseteq U_x.
$$
Let
$$
V=\bigcup_{x\in\RR}(x,b_x)
$$
in the ordinary Euclidean topology. This is an open subset of the second-countable real line, so choose countably many points $x_n$ such that
$$
V=\bigcup_n(x_n,b_{x_n}).
$$
The corresponding countable family $\{U_{x_n}\}$ covers $V$. The complement $C=\RR\setminus V$ has the property that each $x\in C$ is the left endpoint of an interval $[x,b_x)$ and no distinct point of $C$ lies in $(x,b_x)$. Thus the intervals $(x,b_x)$, $x\in C$, contain pairwise distinct rational witnesses, so $C$ is countable. Add one $U_x$ for each $x\in C$. The resulting countable subfamily covers $S$.

:::

:::

::: {.pf-step #s1-5}

The Sorgenfrey line is not second countable.


::: pf-proof

Suppose $\mathcal B$ were a countable basis. For each $x\in\RR$, choose $B_x\in\mathcal B$ with
$$
x\in B_x\subseteq[x,x+1).
$$
If $x<y$, then $x\in B_x$ but $x\notin[y,y+1)$, so $B_x\ne B_y$. Thus $x\mapsto B_x$ injects the uncountable set $\RR$ into the countable set $\mathcal B$, a contradiction.

:::

:::

::: {.pf-step #s1-6}

Hence $S$ is not metrizable.


::: pf-proof

Every separable metric space is second countable: a countable dense set together with balls of positive rational radii forms a countable basis. Step [](#s1-3){.pf-ref} says $S$ is separable, while step [](#s1-5){.pf-ref} says it is not second countable. Therefore it cannot be metrizable.

:::

:::

::: {.pf-step #s1-7}

The product $S\times S$ is separable.


::: pf-proof

The countable set $\QQ\times\QQ$ is dense. Indeed, every nonempty basic rectangle
$$
[a,b)\times[c,d)
$$
contains a pair of rationals.

:::

:::

::: {.pf-step #s1-8}

The anti-diagonal
$$
D=\{(x,-x):x\in\RR\}
$$
is an uncountable closed discrete subspace of $S\times S$.


::: pf-proof

For $(x,-x)\in D$, the basic rectangle
$$
[x,x+\varepsilon)\times[-x,-x+\varepsilon)
$$
meets $D$ only at $(x,-x)$: if $(y,-y)$ lies in it, then $y\geq x$ and $-y\geq-x$, hence $y=x$. Thus $D$ is discrete. If $(a,b)\notin D$, then $a+b\ne0$. If $a+b>0$, choose $\varepsilon<(a+b)/2$; every $(u,v)$ in
$$
[a,a+\varepsilon)\times[b,b+\varepsilon)
$$
satisfies $u+v>0$, so the rectangle misses $D$. If $a+b<0$, choose $\varepsilon<-(a+b)/2$ and use the basic rectangle
$$
[a,a+\varepsilon)\times[b,b+\varepsilon),
$$
whose points still have negative sum for sufficiently small $\varepsilon$. Hence the complement of $D$ is open and $D$ is closed.

:::

:::

::: {.pf-step #s1-9}

The product $S\times S$ is not Lindelöf.


::: pf-proof

A closed subspace of a Lindelöf space is Lindelöf. But an uncountable discrete space is not Lindelöf: its cover by singleton open sets has no countable subcover. Step [](#s1-8){.pf-ref} gives an uncountable closed discrete subspace $D$, so $S\times S$ cannot be Lindelöf.

:::

:::

::: {.pf-step #s1-10}

The product $S\times S$ is not normal.


::: pf-proof

Suppose it were normal. It is separable by step [](#s1-7){.pf-ref}. In any separable normal space, every closed discrete subspace has cardinality at most continuum, which alone is insufficient here; use instead the standard Jones lemma: in a separable normal space, every closed discrete subspace $D$ satisfies
$$
2^{|D|}\leq2^{\aleph_0}.
$$
Indeed, for each subset $A\subseteq D$, normality separates the disjoint closed sets $A$ and $D\setminus A$ and Urysohn's lemma gives a continuous $f_A:X\to[0,1]$ with values $0$ and $1$ on them. Distinct $A$ give distinct continuous functions. A continuous real-valued function on a separable space is determined by its values on a countable dense set, so there are at most
$$
|\RR|^{\aleph_0}=2^{\aleph_0}
$$
such functions. For the anti-diagonal $D$ of step [](#s1-8){.pf-ref}, $|D|=2^{\aleph_0}$, so Cantor's theorem gives
$$
2^{|D|}=2^{2^{\aleph_0}}>2^{\aleph_0},
$$
a contradiction. Thus $S\times S$ is not normal.

:::

:::

::: {.pf-step #s1-11}

Therefore $S$ is completely regular, separable, Lindelöf, and nonmetrizable, whereas $S\times S$ is separable, nonnormal, and non-Lindelöf.


::: pf-proof

The assertions for $S$ are steps [](#s1-2){.pf-ref} through [](#s1-6){.pf-ref}, and those for $S\times S$ are steps [](#s1-7){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} collects all requested properties.

:::

:::

:::
