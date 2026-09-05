---
schema: qual/card@1
id: P-VPACG
kind: problem
title: The quotient $\RR^n/U$ by a bounded open set is not Hausdorff
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 2 of the official UGA Spring 2018 topology exam; as written, the source omits the necessary nonempty hypothesis on U.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the empty-set counterexample and the boundary-point separation obstruction for every nonempty bounded open U in positive-dimensional Euclidean space.
---

::: {.problem}
Let $U\subset\RR^n$ be an open set which is bounded in the standard Euclidean metric.
Prove that the quotient space $\RR^n/U$ is not Hausdorff.
:::

::: {.solution}
<1>1. As written, the statement has an exceptional case: if $U=\varnothing$, then the quotient is Hausdorff.
::: {.proof}
Collapsing the empty subset makes no identifications, so
\[
\RR^n/\varnothing\cong\RR^n,
\]
which is Hausdorff.
Thus the intended assertion requires $U\neq\varnothing$.
:::

Assume henceforth that $n\ge1$ and that $U$ is nonempty.
Let
\[
q:\RR^n\longrightarrow\RR^n/U
\]
be the quotient map, and write $p=q(U)$ for the point obtained by collapsing $U$.

<1>2. The boundary $\partial U$ is nonempty.
::: {.proof}
Because $U$ is bounded and $n\ge1$, it is a proper subset of $\RR^n$.
If $\partial U$ were empty, then, since $U$ is open,
\[
\overline U=U\cup\partial U=U,
\]
so $U$ would also be closed.
This would make $U$ a nonempty proper clopen subset of the connected space $\RR^n$, a contradiction.
:::

<1>3. For any $x\in\partial U$, the two distinct quotient points $p$ and $q(x)$ cannot be separated by disjoint open neighborhoods.
::: {.proof}
Since $U$ is open, no boundary point lies in $U$, so
\[
x\notin U
\qquad\text{and hence}\qquad
q(x)\neq p.
\]
Suppose there were disjoint open sets $O_p,O_x\subseteq\RR^n/U$ with
\[
p\in O_p,
\qquad
q(x)\in O_x.
\]
Their inverse images
\[
V=q^{-1}(O_p),
\qquad
W=q^{-1}(O_x)
\]
are disjoint open subsets of $\RR^n$.
Because $p=q(U)$ lies in $O_p$, one has
\[
U\subseteq V.
\]
Because $x\in W$ and $x\in\partial U$, every open neighborhood of $x$ meets $U$; in particular,
\[
W\cap U\neq\varnothing.
\]
Since $U\subseteq V$, this gives
\[
W\cap V\neq\varnothing,
\]
contradicting the disjointness of $O_p$ and $O_x$.
:::

<1>4. Therefore, for every nonempty bounded open set $U\subset\RR^n$ with $n\ge1$, the quotient $\RR^n/U$ is not Hausdorff.
::: {.proof}
By <1>2 choose $x\in\partial U$.
Then <1>3 exhibits two distinct points of the quotient that admit no disjoint open neighborhoods, which is exactly the failure of the Hausdorff property.
:::
:::
