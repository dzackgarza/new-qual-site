---
schema: qual/card@1
id: P-BERK89S-14
kind: problem
title: A proper $C^1$ plane map with finitely many critical points is surjective
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Proved the image is closed from the bounded-preimage hypothesis, showed its
    boundary consists only of finitely many critical values, and used
    connectedness of the plane minus finitely many points to force surjectivity.
---

::: {.problem}
Let $f:\mathbb R^2\to\mathbb R^2$ be continuously differentiable. Suppose $f$ has only finitely many singular points and, for every $M>0$, the set
\[
\{z\in\mathbb R^2:\|f(z)\|\le M\}
\]
is bounded. Prove that $f$ is onto $\mathbb R^2$.
:::

::: {.solution}
Let
$$
A=f(\RR^2),
$$
and let $S\subset\RR^2$ be the finite set of singular points of $f$.

::: pf

::: {.pf-step #a-is-closed}
The image $A$ is closed in $\RR^2$.

::: pf-proof
Let $y_j\in A$ and suppose $y_j\to y$. Choose $x_j\in\RR^2$ with
$f(x_j)=y_j$. Since the convergent sequence $(y_j)$ is bounded, there is
$M>0$ such that
$$
\norm{f(x_j)}=\norm{y_j}\leq M
$$
for every $j$. Hence all $x_j$ lie in
$$
K_M=\{x\in\RR^2:\norm{f(x)}\leq M\}.
$$
The set $K_M$ is closed by continuity of $f$ and bounded by hypothesis, so it
is compact. Thus some subsequence $x_{j_k}$ converges to a point $x\in K_M$.
Continuity gives
$$
f(x)=\lim_{k\to\infty}f(x_{j_k})
=\lim_{k\to\infty}y_{j_k}
=y.
$$
Therefore $y\in A$, so $A$ is closed.
:::

:::

::: {.pf-step #boundary-finite}
The boundary of $A$ satisfies
$$
\partial A\subseteq f(S),
$$
and is therefore finite.

::: pf-proof
Let $y\in\partial A$. By step [](#a-is-closed){.pf-ref}, $A$ is closed, so $y\in A$ and there
is $x\in\RR^2$ with $f(x)=y$.

If $x\notin S$, then $Df_x$ is invertible. The inverse function theorem gives
an open neighborhood $U$ of $x$ such that $f(U)$ is an open neighborhood of
$y$. Since $f(U)\subseteq A$, this would make $y$ an interior point of $A$,
contrary to $y\in\partial A$. Hence $x\in S$, so $y\in f(S)$. Because $S$
is finite, $f(S)$ and therefore $\partial A$ are finite.
:::

:::

::: {.pf-step #a-has-interior}
The image $A$ has nonempty interior.

::: pf-proof
The singular set $S$ is finite, whereas $\RR^2$ is infinite, so choose
$x_0\in\RR^2\setminus S$. The inverse function theorem gives a neighborhood
$U$ of $x_0$ for which $f(U)$ is open in $\RR^2$. Since
$f(U)\subseteq A$, the set $A$ has nonempty interior.
:::

:::

::: {.pf-step #a-equals-plane}
One has $A=\RR^2$.

::: pf-proof
Suppose instead that $A\neq\RR^2$. Since $A$ is closed by step [](#a-is-closed){.pf-ref},
$\RR^2\setminus A$ is a nonempty open set. Step [](#a-has-interior){.pf-ref} gives
$\operatorname{int}(A)\neq\varnothing$. Moreover,
$$
\RR^2\setminus\partial A
=\operatorname{int}(A)\,\sqcup\,(\RR^2\setminus A).
$$
The two sets on the right are nonempty, disjoint, and open in
$\RR^2\setminus\partial A$. Thus they disconnect $\RR^2\setminus\partial A$.

But step [](#boundary-finite){.pf-ref} says that $\partial A$ is finite, and the plane with finitely
many points removed is path connected: two points can be joined by a polygonal
path whose finitely many line segments are chosen to avoid the deleted points.
This contradiction proves $A=\RR^2$.
:::

:::

::: {.pf-step #f-onto}
The map $f$ is onto $\RR^2$.

::: pf-proof
By definition, $A=f(\RR^2)$. Step [](#a-equals-plane){.pf-ref} gives $A=\RR^2$.
:::

:::

::: pf-qed
Step [](#f-onto){.pf-ref} is the required surjectivity.
:::

:::
:::
