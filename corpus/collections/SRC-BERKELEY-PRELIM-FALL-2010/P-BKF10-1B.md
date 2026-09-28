---
schema: qual/card@1
id: P-BKF10-1B
kind: problem
title: Proper continuous functions $\mathbb R^2\to\mathbb R$ attain a minimum or a maximum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked compactness of a bounded level preimage, connectedness of the
    disk exterior, and the promotion of a disk extremum to a global one.
---

::: {.problem}
Let $f:\RR^2\to\RR$ be continuous and suppose the inverse image of every bounded set is bounded.
Show that $f$ achieves either a minimum value or a maximum value.
:::

::: {.solution}
<1>1. There is a positive integer $n$ such that
$$
K\coloneqq f^{-1}([-n,n])
$$
is nonempty and compact.

::: {.proof}
Choose any $x_0\in\RR^2$. Since $f(x_0)$ is real, choose a positive
integer $n>\abs{f(x_0)}$. Then $x_0\in K$, so $K$ is nonempty.

The interval $[-n,n]$ is closed, so continuity of $f$ implies that $K$
is closed. It is bounded by the hypothesis on inverse images of bounded
sets. Hence $K$ is compact by the Heine--Borel theorem.
:::

<1>2. There exists $R>0$ such that
$$
K\subseteq D_R\coloneqq\{x\in\RR^2:\abs{x}\le R\}.
$$

::: {.proof}
The compact set $K$ from step <1>1 is bounded, so it lies in some closed
ball about the origin. Enlarge its radius if necessary to make $R>0$.
:::

<1>3. On the connected set
$$
E_R\coloneqq\RR^2\setminus D_R,
$$
either
$$
f(E_R)\subset(-\infty,-n)
$$
or
$$
f(E_R)\subset(n,\infty).
$$

::: {.proof}
By step <1>2, no point of $E_R$ lies in $K=f^{-1}([-n,n])$. Thus
$$
f(E_R)\subset\RR\setminus[-n,n]
=(-\infty,-n)\cup(n,\infty).
$$

The exterior $E_R=\{x:\abs{x}>R\}$ of a closed disk in $\RR^2$ is path
connected, hence connected. Since $f$ is continuous, $f(E_R)$ is
connected. A connected subset of the disjoint union
$(-\infty,-n)\cup(n,\infty)$ must lie wholly in one of its two
components, proving the dichotomy.
:::

<1>4. If
$$
f(E_R)\subset(n,\infty),
$$
then $f$ attains a global minimum.

::: {.proof}
The closed disk $D_R$ is compact, so by the extreme value theorem there
exists $x_{\min}\in D_R$ such that
$$
f(x_{\min})=\min_{D_R}f.
$$
Because $K$ is nonempty and $K\subseteq D_R$, choose $x_0\in K$; then
$f(x_0)\le n$. Hence
$$
f(x_{\min})\le n.
$$
Every point of $E_R$ has value strictly greater than $n$, so no point
outside $D_R$ has smaller value than $f(x_{\min})$. Thus $x_{\min}$ is a
global minimizer of $f$ on $\RR^2$.
:::

<1>5. If
$$
f(E_R)\subset(-\infty,-n),
$$
then $f$ attains a global maximum.

::: {.proof}
By compactness of $D_R$, choose $x_{\max}\in D_R$ with
$$
f(x_{\max})=\max_{D_R}f.
$$
Since $K\ne\varnothing$, there is $x_0\in K\subseteq D_R$ with
$f(x_0)\ge-n$, and therefore
$$
f(x_{\max})\ge-n.
$$
Every value on $E_R$ is strictly less than $-n$, so no exterior point
has larger value than $f(x_{\max})$. Hence $x_{\max}$ is a global
maximizer.
:::

<1>6. Therefore $f$ attains either a minimum or a maximum value.

::: {.proof}
Step <1>3 gives exactly the two alternatives treated in steps <1>4 and
<1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
