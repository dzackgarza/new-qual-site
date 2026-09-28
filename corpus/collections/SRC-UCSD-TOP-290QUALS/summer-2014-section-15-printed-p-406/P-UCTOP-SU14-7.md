---
schema: qual/card@1
id: P-UCTOP-SU14-7
kind: problem
title: Degree ±1 map induces surjection on fundamental group
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Suppose $f : M \to N$ is a map between two closed connected oriented $n$-manifolds which induces an isomorphism $H_*(M) \cong H_*(N)$ (that is, it is a map of degree $\pm 1$). Prove that the induced map $\pi_1(M) \to \pi_1(N)$ must be surjective.
:::

::: {.solution}
**Goal.** Let $f:M\to N$ have degree $\pm1$, where $M,N$ are closed connected oriented $n$-manifolds. Prove that $f_*:\pi_1(M)\to\pi_1(N)$ is surjective.

<1>1. Let
$$H=f_*(\pi_1(M))\le \pi_1(N),$$
and let $p:\widehat N\to N$ be the connected covering corresponding to $H$.
::: {.proof}
Closed manifolds are locally path connected and semilocally simply connected, so the subgroup-covering correspondence applies after choosing compatible basepoints.
:::

<1>2. The map $f$ lifts to a map $\widehat f:M\to\widehat N$ satisfying $f=p\circ\widehat f$.
::: {.proof}
The covering-space lifting criterion applies because
$$f_*(\pi_1(M))=H=p_*(\pi_1(\widehat N)).$$
:::

<1>3. The covering $p$ cannot have infinitely many sheets.
::: {.proof}
If it had infinitely many sheets, then $\widehat N$ would be a connected noncompact $n$-manifold: an infinite-sheeted cover of the compact manifold $N$ cannot itself be compact. A connected noncompact $n$-manifold has $H_n(\widehat N;\mathbb Z)=0$. Hence
$$
\widehat f_*[M]=0,
$$
so
$$
f_*[M]=p_*\widehat f_*[M]=0,
$$
which says $\deg f=0$, contradicting $\deg f=\pm1$.
:::

<1>4. Let $d=[\pi_1(N):H]$ be the finite number of sheets of $p$. Then
$$\deg f=d\,\deg\widehat f.$$
::: {.proof}
The orientation of $N$ lifts to $\widehat N$, and a connected $d$-sheeted covering of oriented closed manifolds has degree $d$. Since $f=p\circ\widehat f$, multiplicativity of degree gives
$$
\deg f=(\deg p)(\deg\widehat f)=d\,\deg\widehat f.
$$
:::

<1>5. Since $|\deg f|=1$, one has $d=1$.
::: {.proof}
The integer $d\ge1$ divides $\deg f=\pm1$ by <1>4, hence $d=1$.
:::

<1>6. Therefore $H=\pi_1(N)$, so
$$\boxed{f_*:\pi_1(M)\twoheadrightarrow\pi_1(N).}$$
::: {.proof}
A subgroup has index $1$ exactly when it is the whole group. By definition $H=f_*(\pi_1(M))$.
:::
:::
