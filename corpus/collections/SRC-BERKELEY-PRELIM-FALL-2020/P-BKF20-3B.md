---
schema: qual/card@1
id: P-BKF20-3B
kind: problem
title: Every closed subset of $\mathbb R$ is the closure of a countable set
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 rational-interval
    construction. Choosing one point of C from each rational closed interval
    that meets C gives an at-most-countable subset dense in C.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked countability of the rational intervals, containment of the chosen
    set in C, use of closedness for one closure inclusion, and density via
    rational endpoints for the reverse inclusion.
---

::: {.problem}
Prove that every closed subset $C\subseteq\mathbb R$ is the closure of a finite or countable set.
:::

::: {.solution}
<1>1. Let
$$
\mathcal I
\coloneqq
\{[p,q]:p,q\in\QQ,\ p<q\}.
$$
Then $\mathcal I$ is countable.

::: {.proof}
The set $\QQ$ is countable, so $\QQ\times\QQ$ is countable.
The family $\mathcal I$ is indexed by the subset
$$
\{(p,q)\in\QQ^2:p<q\},
$$
and is therefore countable.
:::

<1>2. For every $I\in\mathcal I$ with
$$
C\cap I\ne\varnothing,
$$
choose one point
$$
x_I\in C\cap I,
$$
and let
$$
D
\coloneqq
\{x_I:I\in\mathcal I,\ C\cap I\ne\varnothing\}.
$$
Then $D$ is finite or countable and
$$
D\subseteq C.
$$

::: {.proof}
There is at most one chosen point for each interval in the countable
family $\mathcal I$, so $D$ is at most countable. Every chosen point
belongs to $C$ by construction.
:::

<1>3. One has
$$
\overline D\subseteq C.
$$

::: {.proof}
By step <1>2,
$$
D\subseteq C.
$$
Since $C$ is closed, it contains the closure of each of its subsets.
Hence
$$
\overline D\subseteq C.
$$
:::

<1>4. Every point of $C$ lies in $\overline D$.

::: {.proof}
Fix $x\in C$ and let $\varepsilon>0$. By density of $\QQ$ in $\RR$,
choose rational numbers $p,q$ such that
$$
x-\varepsilon<p<x<q<x+\varepsilon.
$$
Then
$$
I=[p,q]\in\mathcal I,
\qquad
x\in C\cap I,
$$
so $C\cap I$ is nonempty and the construction in step <1>2 supplies
$$
x_I\in D\cap[p,q].
$$
Because
$$
[p,q]\subseteq(x-\varepsilon,x+\varepsilon),
$$
the $\varepsilon$-neighborhood of $x$ meets $D$. Since
$\varepsilon>0$ was arbitrary,
$$
x\in\overline D.
$$
:::

<1>5. Therefore
$$
\boxed{\overline D=C}.
$$

::: {.proof}
Step <1>3 gives
$$
\overline D\subseteq C,
$$
while step <1>4 gives
$$
C\subseteq\overline D.
$$
Thus equality holds.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 shows that $D$ is finite or countable, and step <1>5 shows
that its closure is $C$.
:::
:::
