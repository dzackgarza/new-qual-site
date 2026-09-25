---
schema: qual/card@1
id: P-BKF80-4
kind: problem
title: Stabilizers and a coset of half-turns in $SO(3)$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $G=SO(3)$. Fix a unit vector $v\in\RR^3$ and set
$$
H_v=\{T\in G:T v=v\}.
$$

1. Show that $H_v$ is a subgroup of $G$.
2. Let $S_v$ be the set of rotations through $180^\circ$ about lines orthogonal to $v$. Show that $S_v$ is a coset of $H_v$ in $G$.
:::

::: {.solution}
Choose a unit vector $w\in v^\perp$, and let $R\in SO(3)$ be the rotation through $180^\circ$ about the line $\RR w$.

<1>1. $H_v$ is a subgroup of $G$.

::: {.proof}
The identity fixes $v$, so $I\in H_v$. If $T,U\in H_v$, then
$$
(TU)v=T(Uv)=Tv=v,
$$
so $TU\in H_v$. Finally, if $T\in H_v$, then applying $T^{-1}$ to $Tv=v$ gives
$$
T^{-1}v=v,
$$
so $T^{-1}\in H_v$. Hence $H_v\leq G$.
:::

<1>2. One has
$$
S_v=\{T\in SO(3):Tv=-v\}.
$$

::: {.proof}
If $T\in S_v$, its rotation axis is a line $L\subset v^\perp$. A half-turn fixes $L$ pointwise and acts as $-I$ on $L^\perp$. Since $v\perp L$, one has $Tv=-v$.

Conversely, suppose $T\in SO(3)$ and $Tv=-v$. Because $T$ is orthogonal, the plane $v^\perp$ is $T$-invariant. Moreover,
$$
\det(T|_{v^\perp})=\frac{\det T}{-1}=-1.
$$
An orthogonal operator on a two-dimensional real inner-product space with determinant $-1$ has eigenvalues $1$ and $-1$. Hence there is a unit vector $u\in v^\perp$ with $Tu=u$. If $z\in v^\perp$ is a unit vector orthogonal to $u$, then the determinant condition forces $Tz=-z$. Together with $Tv=-v$, this shows that $T$ fixes the axis $\RR u$ and negates its orthogonal complement. Thus $T$ is the rotation through $180^\circ$ about the line $\RR u\subset v^\perp$, so $T\in S_v$.
:::

<1>3. $S_v=\boxed{R H_v}$.

::: {.proof}
Since the axis of $R$ lies in $v^\perp$, step <1>2 gives $Rv=-v$.

If $H\in H_v$, then
$$
(RH)v=R(Hv)=Rv=-v,
$$
so step <1>2 gives $RH\in S_v$. Hence $RH_v\subseteq S_v$.

Conversely, let $T\in S_v$. Since a half-turn satisfies $R^{-1}=R$, step <1>2 gives
$$
(R^{-1}T)v=R(-v)=v.
$$
Thus $R^{-1}T\in H_v$, so $T\in RH_v$. Therefore $S_v=RH_v$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 proves part 1, and step <1>3 proves that $S_v$ is a left coset of $H_v$ in $G$.
:::
:::
