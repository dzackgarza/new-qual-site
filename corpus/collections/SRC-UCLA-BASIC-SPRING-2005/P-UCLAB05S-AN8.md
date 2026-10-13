---
schema: qual/card@1
id: P-UCLAB05S-AN8
kind: problem
title: Separability and second countability of metric spaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 8 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Let $(X,d)$ be a metric space.
Prove that the following are equivalent:

(a) $X$ has a countable dense subset.

(b) The topology of $X$ has a countable basis.

Recall that a collection of open sets is a basis if every open set can be written as a union of elements of the collection.
:::

::: {.solution}
<1>1. Assume that $X$ has a countable dense subset
$$
D=\{d_1,d_2,\ldots\}.
$$
Then the collection
$$
\mathcal B\coloneqq
\left\{B(d_j,1/m):j,m\in\NN\right\}
$$
is countable.

::: {.proof}
The set $\NN\times\NN$ is countable, and each pair $(j,m)$ determines one ball $B(d_j,1/m)$. Hence $\mathcal B$ is countable.
:::

<1>2. The collection $\mathcal B$ from step <1>1 is a basis for the topology of $X$.

::: {.proof}
Let $U\subseteq X$ be open and let $x\in U$. Choose $\varepsilon>0$ such that
$$
B(x,\varepsilon)\subseteq U.
$$
Choose $m\in\NN$ with $2/m<\varepsilon$. Since $D$ is dense, there is some $d_j\in D$ satisfying
$$
d(x,d_j)<\frac1m.
$$
Then $x\in B(d_j,1/m)$. If $y\in B(d_j,1/m)$, the triangle inequality gives
$$
d(x,y)
\le d(x,d_j)+d(d_j,y)
<\frac2m
<\varepsilon.
$$
Thus
$$
x\in B(d_j,1/m)\subseteq B(x,\varepsilon)\subseteq U.
$$
Therefore every point of every open set lies in a member of $\mathcal B$ contained in that open set, so $\mathcal B$ is a basis.
:::

<1>3. Conversely, suppose the topology of $X$ has a countable basis
$$
\mathcal B=\{U_1,U_2,\ldots\}.
$$
Choose one point $x_n\in U_n$ for each nonempty $U_n$, and let
$$
D\coloneqq\{x_n:U_n\ne\varnothing\}.
$$
Then $D$ is countable.

::: {.proof}
There is at most one chosen point for each basis element $U_n$, and the basis is countable. Hence $D$ is countable.
:::

<1>4. The set $D$ from step <1>3 is dense in $X$.

::: {.proof}
Let $U\subseteq X$ be nonempty and open. Choose $x\in U$. Since $\mathcal B$ is a basis, there is some basis element $U_n$ such that
$$
x\in U_n\subseteq U.
$$
In particular $U_n$ is nonempty, so the chosen point $x_n$ belongs to $D\cap U$. Thus every nonempty open set meets $D$, which is equivalent to density of $D$.
:::

<1>5. Therefore, for a metric space $(X,d)$,
$$
\boxed{
X\text{ has a countable dense subset}
\iff
X\text{ has a countable basis}.}
$$

::: {.proof}
Steps <1>1--<1>2 prove (a)$\Rightarrow$(b), and steps <1>3--<1>4 prove (b)$\Rightarrow$(a).
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required equivalence.
:::
:::
