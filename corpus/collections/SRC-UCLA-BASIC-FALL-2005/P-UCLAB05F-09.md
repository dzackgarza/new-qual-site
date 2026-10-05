---
schema: qual/card@1
id: P-UCLAB05F-09
kind: problem
title: Dimension of intersections of subspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
Suppose $V_1$ and $V_2$ are subspaces of a finite-dimensional vector space $V$.

(a) Show that
\[
\dim(V_1\cap V_2)
=
\dim(V_1)+\dim(V_2)-\dim\bigl(\operatorname{span}(V_1,V_2)\bigr),
\]
where $\operatorname{span}(V_1,V_2)$ is the smallest subspace containing both $V_1$ and $V_2$.

(b) Let $n=\dim V$.
Use part (a) to show that, if $k<n$, an intersection of $k$ subspaces of dimension $n-1$ always has dimension at least $n-k$.

Suggestion: use induction on $k$.
:::

::: {.solution}
<1>1. Define
\[
\Phi:V_1\oplus V_2\to \operatorname{span}(V_1,V_2)
\]
by
\[
\Phi(v_1,v_2)=v_1+v_2.
\]
Then $\Phi$ is surjective.

::: {.proof}
The map is linear. By definition,
\[
\operatorname{span}(V_1,V_2)=V_1+V_2,
\]
so every vector in the target has the form $v_1+v_2$ with $v_i\in V_i$. Hence it lies in the image of $\Phi$.
:::

<1>2. The kernel of $\Phi$ is
\[
\ker\Phi=\{(w,-w):w\in V_1\cap V_2\}.
\]

::: {.proof}
One has
\[
(v_1,v_2)\in\ker\Phi
\]
if and only if
\[
v_1+v_2=0.
\]
Then $v_1=-v_2$ belongs to both $V_1$ and $V_2$. Writing $w=v_1$ gives
\[
(v_1,v_2)=(w,-w)
\]
with $w\in V_1\cap V_2$. Conversely, every such pair plainly lies in the kernel.
:::

<1>3. One has
\[
\boxed{
\dim(V_1\cap V_2)
=
\dim V_1+\dim V_2-\dim\operatorname{span}(V_1,V_2)
}.
\]

::: {.proof}
By step <1>2, the map
\[
V_1\cap V_2\to\ker\Phi,
\qquad
w\mapsto(w,-w),
\]
is an isomorphism, so
\[
\dim\ker\Phi=\dim(V_1\cap V_2).
\]
By rank-nullity for the surjective map $\Phi$ from step <1>1,
\[
\dim V_1+\dim V_2
=
\dim\ker\Phi+\dim\operatorname{span}(V_1,V_2).
\]
Rearranging gives the displayed formula.
:::

<1>4. Let $H_1,\ldots,H_k\subseteq V$ each have dimension $n-1$, and put
\[
W_j=H_1\cap\cdots\cap H_j.
\]
Then
\[
\dim W_1=n-1.
\]

::: {.proof}
By definition,
\[
W_1=H_1,
\]
and $\dim H_1=n-1$.
:::

<1>5. If
\[
\dim W_j\ge n-j
\]
for some $j<k$, then
\[
\dim W_{j+1}\ge n-(j+1).
\]

::: {.proof}
Since
\[
W_{j+1}=W_j\cap H_{j+1},
\]
part (a), proved in step <1>3, gives
\[
\dim W_{j+1}
=
\dim W_j+\dim H_{j+1}
-
\dim\operatorname{span}(W_j,H_{j+1}).
\]
The span is a subspace of $V$, so its dimension is at most $n$. Hence
\[
\begin{aligned}
\dim W_{j+1}
&\ge
\dim W_j+(n-1)-n\\
&=
\dim W_j-1\\
&\ge
n-j-1\\
&=
n-(j+1).
\end{aligned}
\]
:::

<1>6. For every $k<n$,
\[
\boxed{
\dim(H_1\cap\cdots\cap H_k)\ge n-k
}.
\]

::: {.proof}
Step <1>4 is the base case $k=1$. Step <1>5 is the induction step. Therefore the inequality holds for every positive integer $k$, in particular for every $k<n$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>6 proves part (b).
:::
:::
