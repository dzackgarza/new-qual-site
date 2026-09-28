---
schema: qual/card@1
id: P-BKF14-8A
kind: problem
title: Cardinality of the set of down-sets of a countable total order
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet. Its
    constructions Z and Q give the minimum and maximum cardinalities; the
    packet's final reference to X=R is a typo for X=Q.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the classification of down-sets of Z, the injection from any
    countable order into its principal down-sets, and the continuum lower
    and upper bounds for L(Q).
---

::: {.problem}
Let $X$ be a totally ordered set, (i.e. equipped with a non-reflexive, transitive binary relation $<$ such that for every $x\neq y$, either $x<y$ or $y<x$). Let $L(X)$ denote the set of subsets $S\subseteq X$ with the property that for all $y\in S$ and $x<y$, $x\in S$. Find, with proof:

(a) a countably infinite totally ordered set $X$ for which $L(X)$ has the smallest possible cardinality;

(b) a countably infinite totally ordered set $X$ for which $L(X)$ has the largest possible cardinality.
:::

::: {.solution}
For $x\in X$, write
$$
\downarrow x\coloneqq\{y\in X:y\le x\}.
$$

<1>1. For every countably infinite totally ordered set $X$, the set
$L(X)$ is infinite.

::: {.proof}
For every $x\in X$, the principal down-set $\downarrow x$ belongs to
$L(X)$. If $x<y$, then $y\in\downarrow y$ but
$y\notin\downarrow x$, so $\downarrow x\ne\downarrow y$. Thus
$$
x\longmapsto\downarrow x
$$
is an injection from $X$ into $L(X)$. Since $X$ is countably infinite,
$L(X)$ has cardinality at least $\aleph_0$.
:::

<1>2. For $X=\ZZ$ with its usual order, every down-set is either
$$
\varnothing,\qquad
\ZZ,\qquad\text{or}\qquad
\{m\in\ZZ:m\le k\}
$$
for a unique $k\in\ZZ$.

::: {.proof}
Let $S\in L(\ZZ)$ be nonempty and proper. Choose $s\in S$ and
$t\notin S$. The down-set property forces $s<t$: if $t<s$, then
$s\in S$ would imply $t\in S$.

The nonempty set $\ZZ\setminus S$ therefore has elements above $s$.
Its subset in $\{s+1,s+2,\ldots\}$ has a least element; call it $m$.
No integer less than $m$ can lie outside $S$, since otherwise there
would be a smaller element of the complement above or equal to $s+1$,
while every integer at most $s$ lies in $S$ by downward closure.
Conversely no integer at least $m$ can lie in $S$, because then
downward closure would force $m\in S$. Hence
$$
S=\{j\in\ZZ:j\le m-1\}.
$$
Uniqueness of $m-1$ is immediate.
:::

<1>3. The smallest possible cardinality of $L(X)$ is
$$
\boxed{\aleph_0},
$$
attained by $X=\ZZ$.

::: {.proof}
Step <1>2 gives only countably many down-sets of $\ZZ$, while step
<1>1 shows that no countably infinite total order can have fewer than
countably many. Thus $\aleph_0$ is the minimum.
:::

<1>4. For $X=\QQ$ with its usual order, there is an injection
$$
\RR\hookrightarrow L(\QQ).
$$

::: {.proof}
For $r\in\RR$, define
$$
S_r\coloneqq\{q\in\QQ:q<r\}.
$$
This is a down-set. If $r<s$, density of $\QQ$ in $\RR$ gives
$q\in\QQ$ with
$$
r<q<s.
$$
Then $q\in S_s$ but $q\notin S_r$, so $S_r\ne S_s$. Therefore
$r\mapsto S_r$ is injective.
:::

<1>5. One has
$$
|L(\QQ)|=2^{\aleph_0}=|\RR|.
$$

::: {.proof}
Step <1>4 gives
$$
|\RR|\le|L(\QQ)|.
$$
On the other hand,
$$
L(\QQ)\subseteq\mathcal P(\QQ),
$$
and because $\QQ$ is countably infinite,
$$
|\mathcal P(\QQ)|=2^{\aleph_0}=|\RR|.
$$
Hence equality holds.
:::

<1>6. The largest possible cardinality of $L(X)$ is
$$
\boxed{2^{\aleph_0}},
$$
attained by $X=\QQ$.

::: {.proof}
For every countably infinite $X$,
$$
L(X)\subseteq\mathcal P(X),
$$
so
$$
|L(X)|\le2^{\aleph_0}.
$$
Step <1>5 shows that equality is attained for $\QQ$.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>3 and <1>6 answer parts (a) and (b), respectively.
:::
:::
