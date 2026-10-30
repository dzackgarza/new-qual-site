---
schema: qual/card@1
id: P-UCLARA17S-03
kind: problem
title: $\sigma$-algebras on $C([0,1])$ making point evaluations measurable contain the Borel sets
classification:
  areas:
  - real-analysis
  topics:
  - Borel Measures
  - Function Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $C([0,1])$ denote the Banach space of continuous functions on $[0,1]$ endowed with the sup-norm. Let $\mathcal F$ be a $\sigma$-algebra on $C([0,1])$ such that for all $x\in[0,1]$ the map
$$
L_x(f)=f(x)
$$
is $\mathcal F$-measurable. Show that $\mathcal F$ contains all open sets.
:::

::: {.solution}

Enumerate the dense set $\QQ\cap[0,1]$ as $q_1,q_2,\ldots$.

::: pf

::: {.pf-step #s1-1}

For every $h\in C([0,1])$,
$$
\norm{h}_\infty=\sup_{j\ge1}\abs{h(q_j)}.
$$


::: pf-proof

The right-hand side is at most $\norm{h}_\infty$. Conversely, continuity on the compact interval implies that $\abs{h}$ attains its maximum at some $x_0\in[0,1]$. Choose rationals $q_{j_k}\to x_0$. By continuity,
$$
\abs{h(q_{j_k})}\to \abs{h(x_0)}=\norm{h}_\infty.
$$
Hence the supremum over the rational points is at least $\norm{h}_\infty$.

:::

:::

::: {.pf-step #s1-2}

For each fixed $g\in C([0,1])$, the map
$$
N_g(f)\coloneqq\norm{f-g}_\infty
$$
is $\mathcal F$-measurable.


::: pf-proof

For every $j$, the function
$$
f\longmapsto \abs{L_{q_j}(f)-g(q_j)}
$$
is $\mathcal F$-measurable because $L_{q_j}$ is measurable and absolute value is continuous. By step [](#s1-1){.pf-ref},
$$
N_g(f)=\sup_{j\ge1}\abs{L_{q_j}(f)-g(q_j)}.
$$
A countable supremum of measurable real-valued functions is measurable. Explicitly, for every $a\in\RR$,
$$
\{f:N_g(f)\le a\}
=\bigcap_{j=1}^{\infty}
\{f:\abs{L_{q_j}(f)-g(q_j)}\le a\}
\in\mathcal F.
$$

:::

:::

::: {.pf-step #s1-3}

Every open ball in $C([0,1])$ belongs to $\mathcal F$.


::: pf-proof

For $g\in C([0,1])$ and $r>0$,
$$
B(g,r)=\{f:N_g(f)<r\}.
$$
This set is $\mathcal F$-measurable by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The space $C([0,1])$ has a countable dense subset.


::: pf-proof

Let $\mathcal P_{\QQ}$ be the set of polynomials with rational coefficients. It is countable. To see that it is dense, let $f\in C([0,1])$ and $\varepsilon>0$. By the Weierstrass approximation theorem there is a real-coefficient polynomial
$$
p(x)=\sum_{k=0}^d a_kx^k
$$
with $\norm{f-p}_\infty<\varepsilon/2$. Choose rational numbers $b_k$ so close to $a_k$ that
$$
\sum_{k=0}^d\abs{a_k-b_k}<\frac\varepsilon2.
$$
For
$$
q(x)=\sum_{k=0}^d b_kx^k\in\mathcal P_{\QQ},
$$
one has, since $0\le x\le1$,
$$
\norm{p-q}_\infty
\le\sum_{k=0}^d\abs{a_k-b_k}
<\frac\varepsilon2.
$$
Thus $\norm{f-q}_\infty<\varepsilon$.

:::

:::

::: {.pf-step #s1-5}

The topology of $C([0,1])$ has a countable basis consisting of $\mathcal F$-measurable sets.


::: pf-proof

Let $D\subseteq C([0,1])$ be the countable dense set from step [](#s1-4){.pf-ref}. The collection
$$
\mathcal B\coloneqq\{B(g,r):g\in D,\ r\in\QQ_{>0}\}
$$
is countable. It is a basis for the metric topology: if $O$ is open and $f\in O$, choose $\varepsilon>0$ with $B(f,\varepsilon)\subseteq O$. Choose $g\in D$ with
$$
\norm{f-g}_\infty<\frac\varepsilon3,
$$
and then choose a positive rational $r$ satisfying
$$
\norm{f-g}_\infty<r<\varepsilon-\norm{f-g}_\infty.
$$
Such an $r$ exists because $\norm{f-g}_\infty<\varepsilon/3$. Then
$$
f\in B(g,r)\subseteq B(f,\varepsilon)\subseteq O.
$$
Every element of $\mathcal B$ belongs to $\mathcal F$ by step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Every open set in $C([0,1])$ belongs to $\mathcal F$.


::: pf-proof

Let $O$ be open. Since $\mathcal B$ is a countable basis,
$$
O=\bigcup\{B\in\mathcal B:B\subseteq O\}.
$$
The union is countable, and every member belongs to $\mathcal F$ by step [](#s1-5){.pf-ref}. Since $\mathcal F$ is a $\sigma$-algebra, $O\in\mathcal F$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
