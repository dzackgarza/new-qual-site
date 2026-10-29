---
schema: qual/card@1
id: P-WESTOP06-A3
kind: problem
title: Preservation of six topological properties by products and sums
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Consider the six topological properties
\[
\text{finite, countable, connected, locally connected, metrizable, normal}.
\]
For each property $P$ determine, with explanation:

1. exactly for which cardinalities $|A|$ it is always true that
   \[
   X_a\in P\text{ for all }a\in A
   \quad\Longrightarrow\quad
   \prod_{a\in A}X_a\in P;
   \]
2. exactly for which cardinalities $|A|$ it is always true that
   \[
   X_a\in P\text{ for all }a\in A
   \quad\Longrightarrow\quad
   \sum_{a\in A}X_a\in P.
   \]
:::

::: {.solution}

Write \(\kappa=|A|\), and interpret “countable” as “at most countable.”

::: pf

::: {.pf-step #s1-1}

For the property “finite,” both products and sums preserve the property for every family indexed by \(A\) exactly when \(\kappa\) is finite.


::: pf-proof

If \(A\) is finite, a finite product and a finite disjoint union of finite sets are finite. If \(A\) is infinite, take every \(X_a=\{0,1\}\) for products: then \(\prod_{a\in A}X_a\) contains at least one point for every subset of \(A\), so it is infinite. For sums, take every \(X_a\) to be a singleton; then \(\sum_{a\in A}X_a\) has cardinality \(\kappa\), hence is infinite.

:::

:::

::: pf-step

For the property “countable,” products preserve the property exactly when \(\kappa\) is finite, while sums preserve it exactly when \(\kappa\le\aleph_0\).


::: pf-proof

A finite product of countable sets is countable. If \(A\) is infinite, taking every \(X_a=\{0,1\}\) gives \(\prod_{a\in A}X_a=\{0,1\}^A\), whose cardinality is \(2^\kappa>\kappa\ge\aleph_0\), so the product is uncountable. A disjoint union of countably many countable sets is countable, whereas for uncountable \(A\), the disjoint union of one singleton for each \(a\in A\) has cardinality \(\kappa\) and is uncountable.

:::

:::

::: pf-step

For the property “connected,” products preserve the property for every cardinality \(\kappa\), while sums preserve it exactly when \(\kappa\le 1\).


::: pf-proof

Arbitrary products of connected spaces are connected. If some factor is empty, then the product is empty and hence connected. Otherwise fix \(p=(p_a)_{a\in A}\) in the product. For each finite \(F\subseteq A\), let
\[
Y_F=\prod_{a\in F}X_a\times\prod_{a\notin F}\{p_a\}.
\]
Each \(Y_F\) is connected because it is homeomorphic to a finite product of connected spaces, all \(Y_F\) contain \(p\), and their union is dense because every basic open set restricts only finitely many coordinates. Hence the closure of \(\bigcup_FY_F\), namely the full product, is connected.

For sums, the empty sum and a one-summand sum are connected whenever the summands are connected. If \(\kappa\ge2\), choose every \(X_a\) to be a singleton. Any two distinct summands are disjoint nonempty open-and-closed subsets of the sum, so the sum is disconnected.

:::

:::

::: pf-step

For the property “locally connected,” products preserve the property exactly when \(\kappa\) is finite, while sums preserve it for every cardinality \(\kappa\).


::: pf-proof

Finite products of locally connected spaces are locally connected: given a point and a basic open neighborhood, choose a connected open neighborhood in each factor and take their product.

If \(A\) is infinite, let every \(X_a=\{0,1\}\) with the discrete topology. Each factor is locally connected. Any connected subset of \(\{0,1\}^A\) is a singleton, since its projection to every factor must be connected and therefore constant. No singleton is open when \(A\) is infinite, so no point has a connected open neighborhood. Thus the product is not locally connected.

For sums, each summand is open in the topological sum. A connected open neighborhood of a point inside its summand is therefore also a connected open neighborhood in the whole sum. Hence arbitrary sums of locally connected spaces are locally connected.

:::

:::

::: pf-step

For the property “metrizable,” products preserve the property exactly when \(\kappa\le\aleph_0\), while sums preserve it for every cardinality \(\kappa\).


::: pf-proof

Finite products are metrizable. For a countable product, choose metrics \(d_n\) on the factors and replace them by \(\min\{1,d_n\}\). Then
\[
D(x,y)=\sum_{n=1}^\infty 2^{-n}\min\{1,d_n(x_n,y_n)\}
\]
is a metric inducing the product topology.

If \(A\) is uncountable, let every factor be the discrete two-point space. The product \(\{0,1\}^A\) is not first countable. Indeed, if \(U_1,U_2,\ldots\) were a countable local base at a point \(x\), choose for each \(n\) a basic neighborhood \(B_n\subseteq U_n\). Only countably many coordinates are restricted among all the \(B_n\), so choose \(a\in A\) outside that union. The basic neighborhood requiring the \(a\)-coordinate to equal \(x_a\) contains none of the \(B_n\), contradicting that the \(U_n\) form a local base. Since every metrizable space is first countable, the product is not metrizable.

For an arbitrary topological sum of metrizable spaces, choose a metric \(d_a\) on each summand and set
\[
D(x,y)=
\begin{cases}
\min\{1,d_a(x,y)\},&x,y\in X_a,\\
2,&x\in X_a,\ y\in X_b,\ a\ne b.
\end{cases}
\]
This is a metric, and its open balls of radius less than \(1\) give exactly the original topology on each open summand. Thus every such sum is metrizable.

:::

:::

::: {.pf-step #s1-6}

For the property “normal,” products preserve the property exactly when \(\kappa\le1\), while sums preserve it for every cardinality \(\kappa\).


::: pf-proof

For \(\kappa=0\), the product is a one-point space, and for \(\kappa=1\) it is just the single normal factor. For \(\kappa\ge2\), let \(\sorgenfrey\) be the Sorgenfrey line. It is normal: its basic intervals \([a,b)\) are clopen, so it is regular, it is Lindelöf, and every regular Lindelöf space is normal.

The Sorgenfrey plane \(\sorgenfrey^2\) is not normal. The countable set \(\QQ^2\) is dense in \(\sorgenfrey^2\), while
\[
D=\{(x,-x):x\in\RR\}
\]
is a closed discrete subspace of cardinality \(2^{\aleph_0}\). Indeed, a sufficiently small basic rectangle about \((x,-x)\) meets \(D\) only there, and if \((u,v)\notin D\), then a sufficiently small basic rectangle about \((u,v)\) has all coordinate sums of the same nonzero sign as \(u+v\), so it misses \(D\).

If \(\sorgenfrey^2\) were normal, then for every subset \(E\subseteq D\), Urysohn's lemma would give a continuous \(f_E:\sorgenfrey^2\to[0,1]\) with \(f_E=0\) on \(E\) and \(f_E=1\) on \(D\setminus E\). Distinct subsets give distinct functions. But a continuous real-valued function is determined by its values on the dense countable set \(\QQ^2\), so there are at most
\[
|\RR|^{\aleph_0}=2^{\aleph_0}
\]
such functions, whereas \(D\) has \(2^{2^{\aleph_0}}\) subsets. This contradicts Cantor's theorem. Hence \(\sorgenfrey^2\) is not normal. Taking two factors equal to \(\sorgenfrey\) and every remaining factor to be a singleton gives a product homeomorphic to \(\sorgenfrey^2\), so normality is not always preserved.

For sums, let \(E,F\) be disjoint closed subsets of \(\sum_{a\in A}X_a\). Then \(E\cap X_a\) and \(F\cap X_a\) are disjoint closed subsets of the normal space \(X_a\), so there are disjoint open sets \(U_a,V_a\subseteq X_a\) containing them. The unions \(\bigcup_aU_a\) and \(\bigcup_aV_a\) are disjoint open subsets of the topological sum containing \(E\) and \(F\), respectively. Hence arbitrary sums of normal spaces are normal.

:::

:::

::: {.pf-step #s1-7}

The complete classification is
\[
\boxed{
\begin{array}{c|c|c}
P & \prod_{a\in A}X_a & \sum_{a\in A}X_a\\
\hline
\text{finite} & \kappa<\aleph_0 & \kappa<\aleph_0\\
\text{countable} & \kappa<\aleph_0 & \kappa\le\aleph_0\\
\text{connected} & \text{all }\kappa & \kappa\le1\\
\text{locally connected} & \kappa<\aleph_0 & \text{all }\kappa\\
\text{metrizable} & \kappa\le\aleph_0 & \text{all }\kappa\\
\text{normal} & \kappa\le1 & \text{all }\kappa
\end{array}}
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} establish every entry in the table and show that every excluded cardinality has a counterexample.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the requested classification for all six properties, for both products and sums.

:::

:::

:::
