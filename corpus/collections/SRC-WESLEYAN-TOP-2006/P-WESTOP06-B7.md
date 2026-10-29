---
schema: qual/card@1
id: P-WESTOP06-B7
kind: problem
title: Local nullhomotopy near a contraction point and a rational comb retraction example
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Suppose a space $X$ deformation retracts to a point $x\in X$. Prove that for every neighborhood $U$ of $x$ there is a neighborhood $V\subset U$ of $x$ such that the inclusion
   \[
   V\hookrightarrow U
   \]
   is null-homotopic.
2. Let $X\subset\RR^2$ be the union of the horizontal segment
   \[
   [0,1]\times\{0\}
   \]
   and all vertical segments
   \[
   \{r\}\times[0,1-r]
   \]
   for rational $r\in[0,1]$. Show that $X$ deformation retracts to every point of $[0,1]\times\{0\}$, but to no other point.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If \(X\) deformation retracts to \(x\), then for every neighborhood \(U\) of \(x\) there is a neighborhood \(V\subseteq U\) of \(x\) such that the inclusion \(V\hookrightarrow U\) is null-homotopic.


::: pf-proof

Let
\[
H:X\times I\to X
\]
be a deformation retraction to \(x\). Thus
\[
H(y,0)=y,\qquad H(y,1)=x,\qquad H(x,t)=x.
\]
Choose an open neighborhood \(U_0\) of \(x\) with \(U_0\subseteq U\). The set
\[
H^{-1}(U_0)
\]
is open in \(X\times I\) and contains the compact set \(\{x\}\times I\). By the tube lemma, there is a neighborhood \(V_0\) of \(x\) in \(X\) such that
\[
V_0\times I\subseteq H^{-1}(U_0).
\]
Set \(V=V_0\cap U_0\). Then \(V\) is a neighborhood of \(x\) with \(V\subseteq U\), and
\[
H|_{V\times I}:V\times I\to U_0\subseteq U
\]
is a homotopy from the inclusion \(V\hookrightarrow U\) to the constant map with value \(x\). Hence the inclusion is null-homotopic.

:::

:::

::: {.pf-step #s1-2}

For every \(a\in[0,1]\), the space \(X\) deformation retracts to the point \((a,0)\).


::: pf-proof

Define
\[
H_a:X\times I\to X
\]
by
\[
H_a((r,y),t)=
\begin{cases}
\bigl(r,(1-2t)y\bigr),&0\le t\le\tfrac12,\\[2mm]
\bigl((2-2t)r+(2t-1)a,0\bigr),&\tfrac12\le t\le1.
\end{cases}
\]
For \(0\le t\le\tfrac12\), the first coordinate stays fixed, so a point on a vertical tooth remains on that same tooth while moving downward; a point on the horizontal segment remains there. Thus the first formula takes values in \(X\). For \(\tfrac12\le t\le1\), the second coordinate is \(0\), so the image lies in the horizontal segment and therefore in \(X\).

At \(t=\tfrac12\), both formulas give \((r,0)\), so the pasting lemma gives continuity. Moreover,
\[
H_a((r,y),0)=(r,y),
\qquad
H_a((r,y),1)=(a,0).
\]
If \((r,y)=(a,0)\), both formulas give \((a,0)\) for every \(t\). Hence \(H_a\) is a deformation retraction of \(X\) to \((a,0)\).

:::

:::

::: {.pf-step #s1-3}

Let \(p=(r_0,y_0)\in X\) with \(y_0>0\). There is a neighborhood \(U\) of \(p\) such that every path in \(U\) has constant first coordinate.


::: pf-proof

Choose
\[
0<\varepsilon<\frac{y_0}{2}
\]
and set
\[
U=X\cap B_\varepsilon(p).
\]
Then every point of \(U\) has positive second coordinate, so every point of \(U\) lies on one of the vertical teeth. Therefore the first-coordinate projection
\[
\pi_1:U\to\RR
\]
has image contained in \(\QQ\cap[0,1]\).

If \(\gamma:I\to U\) is a path, then \(\pi_1\circ\gamma:I\to\QQ\) has connected image. The only connected subsets of \(\QQ\) are singletons. Hence \(\pi_1\circ\gamma\) is constant, so \(\gamma\) has constant first coordinate.

:::

:::

::: {.pf-step #s1-4}

Every neighborhood \(V\subseteq U\) of \(p\) contains a point \(q\) that cannot be joined to \(p\) by a path in \(U\).


::: pf-proof

Because \(V\) is a neighborhood of \(p\) in the subspace \(X\), there is \(\delta>0\) such that
\[
X\cap B_\delta(p)\subseteq V,
\]
after decreasing \(\delta\) if necessary so that \(B_\delta(p)\subseteq B_\varepsilon(p)\).

If \(y_0<1-r_0\), choose a rational number \(r\ne r_0\) sufficiently close to \(r_0\) that
\[
|r-r_0|<\delta
\qquad\text{and}\qquad
y_0<1-r.
\]
Then
\[
q=(r,y_0)\in X\cap B_\delta(p)\subseteq V.
\]

If \(y_0=1-r_0\), choose instead a rational \(r<r_0\) with \(|r-r_0|<\delta\). Then \(1-r>1-r_0=y_0\), so again \(q=(r,y_0)\in V\).

In either case, \(q\) and \(p\) have different first coordinates. By step [](#s1-3){.pf-ref}, no path in \(U\) can join them.

:::

:::

::: {.pf-step #s1-5}

No point \(p=(r_0,y_0)\in X\) with \(y_0>0\) can be a deformation-retraction point of \(X\).


::: pf-proof

Assume that \(X\) deformation retracts to such a point \(p\), and choose the neighborhood \(U\) from step [](#s1-3){.pf-ref}. By step [](#s1-1){.pf-ref}, there must be a neighborhood \(V\subseteq U\) of \(p\) for which the inclusion
\[
i:V\hookrightarrow U
\]
is null-homotopic. Let
\[
K:V\times I\to U
\]
be a homotopy from \(i\) to a constant map with value \(c\in U\). For every \(v\in V\), the path \(t\mapsto K(v,t)\) joins \(v\) to \(c\) in \(U\). Hence every two points of \(V\) lie in the same path component of \(U\).

This contradicts step [](#s1-4){.pf-ref}, which gives a point \(q\in V\) not path-connected to \(p\) in \(U\). Therefore \(X\) cannot deformation retract to \(p\).

:::

:::

::: {.pf-step #s1-6}

The deformation-retraction points of \(X\) are exactly
\[
\boxed{[0,1]\times\{0\}.}
\]


::: pf-proof

Step [](#s1-2){.pf-ref} shows that every point on the horizontal segment is a deformation-retraction point. Every point of \(X\) outside that segment has positive second coordinate, so step [](#s1-5){.pf-ref} excludes all remaining points.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part \(1\), and step [](#s1-6){.pf-ref} proves part \(2\).

:::

:::

:::
