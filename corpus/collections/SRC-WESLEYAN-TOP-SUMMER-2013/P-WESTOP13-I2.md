---
schema: qual/card@1
id: P-WESTOP13-I2
kind: problem
title: Compact finer topologies and a noncompact mixed product of $K$- and lower-limit intervals
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. Let $X$ be a set with two topologies $T_1$ and $T_2$, and suppose $T_1$ is finer than $T_2$. If $(X,T_1)$ is compact and $(X,T_2)$ is Hausdorff, prove that $T_1=T_2$.

2. Let $I=[0,1]$. Let $(I,K)$ be $I$ with the subspace topology inherited from the $K$-topology on $\RR$, and let $(I,L)$ be $I$ with the subspace topology inherited from the lower-limit topology. Let
   \[
   X=\prod_{\alpha\in J}Y_\alpha,
   \]
   where each $Y_\alpha$ is either $(I,K)$ or $(I,L)$. Use part 1 to prove that $X$ is not compact.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Under the hypotheses of part 1, the identity map
$$
\operatorname{id}:(X,T_1)\longrightarrow(X,T_2)
$$
is a continuous bijection.


::: pf-proof

The map is bijective because it is the identity on the underlying set. Since $T_1$ is finer than $T_2$, every $T_2$-open set is $T_1$-open. This is exactly continuity of the identity map from $(X,T_1)$ to $(X,T_2)$.

:::

:::

::: {.pf-step #s1-2}

If $(X,T_1)$ is compact and $(X,T_2)$ is Hausdorff, then
$$
\boxed{T_1=T_2}.
$$


::: pf-proof

Let $C$ be closed in $(X,T_1)$. Since $(X,T_1)$ is compact, $C$ is compact. By continuity of the identity map from step [](#s1-1){.pf-ref}, the same set $C$ is compact in $(X,T_2)$. Compact subsets of a Hausdorff space are closed, so $C$ is $T_2$-closed.

Thus every $T_1$-closed set is $T_2$-closed, equivalently every $T_1$-open set is $T_2$-open. Hence
$$
T_1\subseteq T_2.
$$
The assumed fineness gives $T_2\subseteq T_1$, so equality follows.

:::

:::

::: {.pf-step #s1-3}

As literally written, part 2 has one degenerate exception: if $J=\varnothing$, then $X$ is a one-point space and is compact. Hence the asserted noncompactness requires $J\ne\varnothing$.


::: pf-proof

The empty product of topological spaces is, by definition, a singleton. Every singleton is compact. Thus the source conclusion cannot hold for $J=\varnothing$.

:::

:::

::: {.pf-step #s1-4}

Assume henceforth that $J\ne\varnothing$. Let $T$ be the given product topology on
$$
X=\prod_{\alpha\in J}Y_\alpha,
$$
and let $T_0$ be the ordinary product topology on the same underlying set $I^J$, where every factor $I=[0,1]$ has its usual Euclidean topology. Then
$$
T\text{ is finer than }T_0.
$$


::: pf-proof

Both the $K$-topology and the lower-limit topology on $\RR$ are finer than the usual topology. Therefore their subspace topologies on $I$ are finer than the usual topology on $I$. Every ordinary basic product-open set is consequently open in the product topology $T$.

:::

:::

::: {.pf-step #s1-5}

The space $(I^J,T_0)$ is Hausdorff.


::: pf-proof

The ordinary interval $I$ is Hausdorff, and an arbitrary product of Hausdorff spaces is Hausdorff in the product topology.

:::

:::

::: {.pf-step #s1-6}

For every $\alpha_0\in J$, the topology on the factor $Y_{\alpha_0}$ is strictly finer than the ordinary topology on $I$.


::: pf-proof

If $Y_{\alpha_0}=(I,L)$, then
$$
[1/2,3/4)
$$
is open in the lower-limit subspace topology but is not open in the ordinary topology on $I$.

If $Y_{\alpha_0}=(I,K)$, use the standard
$$
K=\{1/n:n\in\ZZ_{>0}\}.
$$
The set
$$
U=\bigl((-1,1)\setminus K\bigr)\cap I
=[0,1)\setminus K
$$
is open in the $K$-subspace topology. It is not open in the ordinary topology on $I$: it contains $0$, but every ordinary neighborhood of $0$ in $I$ contains $1/n$ for all sufficiently large $n$, and those points are excluded from $U$.

:::

:::

::: {.pf-step #s1-7}

If $J\ne\varnothing$, then
$$
T\ne T_0.
$$


::: pf-proof

Choose $\alpha_0\in J$ and choose a set $U\subseteq I$ that is open in $Y_{\alpha_0}$ but not ordinary-open, as supplied by step [](#s1-6){.pf-ref}. The cylinder
$$
W=\pi_{\alpha_0}^{-1}(U)
$$
is open in $T$.

Define
$$
s:I\longrightarrow I^J
$$
by
$$
s(t)_{\alpha_0}=t,
\qquad
s(t)_\alpha=0\quad(\alpha\ne\alpha_0).
$$
The map $s$ is continuous from ordinary $I$ to $(I^J,T_0)$ because all of its coordinate maps are continuous. If $W$ were $T_0$-open, then
$$
s^{-1}(W)=U
$$
would be ordinary-open in $I$, contrary to the choice of $U$. Thus $W$ is not $T_0$-open and $T\ne T_0$.

:::

:::

::: {.pf-step #s1-8}

If $J\ne\varnothing$, then the product space $(X,T)$ is not compact.


::: pf-proof

Suppose $(X,T)$ were compact. By step [](#s1-4){.pf-ref}, $T$ is finer than $T_0$, and by step [](#s1-5){.pf-ref}, $(X,T_0)$ is Hausdorff. Part 1, proved in step [](#s1-2){.pf-ref}, would then imply
$$
T=T_0.
$$
This contradicts step [](#s1-7){.pf-ref}. Hence $(X,T)$ is not compact.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part 1. Step [](#s1-8){.pf-ref} proves the intended statement of part 2 for every nonempty index set $J$, while step [](#s1-3){.pf-ref} records the empty-product exception in the literal wording.

:::

:::

:::
