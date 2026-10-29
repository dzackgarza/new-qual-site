---
schema: qual/card@1
id: P-WESTOP06-B1
kind: problem
title: Path homotopy and an explicit loop in the punctured plane
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $f,f':I\to X$.

1. Define path homotopy for $f$ and $f'$.
2. Show that path homotopy is an equivalence relation on maps $I\to X$ with fixed endpoints.
3. Let
   $$
   X=\RR^2\setminus\{(0,0)\}
   $$
   and
   $$
   f(t)=\bigl(\cos^2(2\pi t),\sin^2(2\pi t)\bigr).
   $$
   Sketch $f$ and determine for which integers $k$ it is path-homotopic to
   $$
   g_k(t)=\bigl(\cos(2\pi kt),\sin(2\pi kt)\bigr).
   $$
:::

::: {.solution}

Write $I=[0,1]$.

::: pf

::: {.pf-step #s1-1}

Two paths $f,f':I\to X$ with the same endpoints are path-homotopic if there is a continuous map
$$
H:I\times I\to X
$$
such that
$$
H(t,0)=f(t),\qquad H(t,1)=f'(t),
$$
and
$$
H(0,s)=f(0)=f'(0),\qquad
H(1,s)=f(1)=f'(1)
$$
for every $s,t\in I$.


::: pf-proof

This is the definition of a homotopy of paths relative to the endpoint set $\{0,1\}$.

:::

:::

::: {.pf-step #s1-2}

Path homotopy is reflexive on paths with fixed endpoints.


::: pf-proof

For a path $f$, define
$$
H(t,s)=f(t).
$$
This is continuous, has $H(\,\cdot\,,0)=H(\,\cdot\,,1)=f$, and fixes both endpoints for all $s$. Hence $f$ is path-homotopic to itself.

:::

:::

::: {.pf-step #s1-3}

Path homotopy is symmetric.


::: pf-proof

If $H$ is a path homotopy from $f$ to $f'$, define
$$
K(t,s)=H(t,1-s).
$$
Then $K$ is continuous, runs from $f'$ to $f$, and fixes the same endpoints. Hence $f'$ is path-homotopic to $f$.

:::

:::

::: {.pf-step #s1-4}

Path homotopy is transitive.


::: pf-proof

Suppose $H$ is a path homotopy from $f$ to $f'$ and $K$ is a path homotopy from $f'$ to $f''$. Define
$$
L(t,s)=
\begin{cases}
H(t,2s),&0\le s\le\tfrac12,\\
K(t,2s-1),&\tfrac12\le s\le1.
\end{cases}
$$
The two formulas agree at $s=\tfrac12$ because
$$
H(t,1)=f'(t)=K(t,0).
$$
Therefore the pasting lemma gives continuity of $L$. The map $L$ runs from $f$ to $f''$, and both $H$ and $K$ fix the endpoints, so $L$ does as well. Hence path homotopy is transitive.

:::

:::

::: {.pf-step #s1-5}

Consequently, path homotopy is an equivalence relation on the set of paths with any prescribed pair of endpoints.


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-4){.pf-ref} establish reflexivity, symmetry, and transitivity.

:::

:::

::: {.pf-step #s1-6}

The image of
$$
f(t)=\bigl(\cos^2(2\pi t),\sin^2(2\pi t)\bigr)
$$
is the line segment
$$
\{(x,y)\in\RR^2:x\ge0,\ y\ge0,\ x+y=1\},
$$
traversed from $(1,0)$ to $(0,1)$ and back twice.


::: pf-proof

For every $t$,
$$
\cos^2(2\pi t)+\sin^2(2\pi t)=1,
$$
and both coordinates are nonnegative. Conversely, as $t$ varies from $0$ to $1/4$, $\cos^2(2\pi t)$ decreases continuously from $1$ to $0$, so the entire segment is traced. The values at
$$
t=0,\ \tfrac14,\ \tfrac12,\ \tfrac34,\ 1
$$
are respectively
$$
(1,0),\ (0,1),\ (1,0),\ (0,1),\ (1,0),
$$
which gives the stated traversal.

:::

:::

::: {.pf-step #s1-7}

The loop $f$ is path-homotopic in $\RR^2\setminus\{0\}$ to the constant loop $g_0(t)=(1,0)$.


::: pf-proof

Define
$$
H(t,s)=\bigl((1-s)\cos^2(2\pi t)+s,\ (1-s)\sin^2(2\pi t)\bigr).
$$
Then $H(t,0)=f(t)$ and $H(t,1)=(1,0)=g_0(t)$. Moreover
$$
H_1(t,s)+H_2(t,s)
=(1-s)\bigl(\cos^2(2\pi t)+\sin^2(2\pi t)\bigr)+s
=1,
$$
so $H(t,s)\ne(0,0)$ for all $t,s$. Finally, because $f(0)=f(1)=(1,0)$,
$$
H(0,s)=H(1,s)=(1,0)
$$
for every $s$. Thus $H$ is a path homotopy from $f$ to $g_0$.

:::

:::

::: {.pf-step #s1-8}

If $g_k$ and $g_\ell$ are path-homotopic in $\RR^2\setminus\{0\}$, then $k=\ell$.


::: pf-proof

Radially retract $\RR^2\setminus\{0\}$ onto $S^1$. For a based loop $h:I\to S^1$ with $h(0)=h(1)=(1,0)$, lift $h$ through the covering map
$$
p:\RR\to S^1,\qquad
p(u)=(\cos(2\pi u),\sin(2\pi u)),
$$
using the unique lift $\widetilde h$ with $\widetilde h(0)=0$. Since $h(1)=(1,0)$, one has $\widetilde h(1)\in\ZZ$. This endpoint is invariant under based homotopy: a based homotopy lifts starting from $0$, and the endpoint of the lifted path depends continuously on the homotopy parameter while always lying in the discrete set $\ZZ$, so it is constant.

For $g_k$, the lift
$$
\widetilde g_k(t)=kt
$$
starts at $0$ and ends at $k$. Hence based-homotopic loops $g_k$ and $g_\ell$ must satisfy $k=\ell$.

:::

:::

::: {.pf-step #s1-9}

The loop $f$ is path-homotopic to $g_k$ exactly for
$$
\boxed{k=0.}
$$


::: pf-proof

Step [](#s1-7){.pf-ref} proves that $f$ is path-homotopic to $g_0$. If $f$ were path-homotopic to $g_k$, then by symmetry and transitivity from steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, $g_0$ would be path-homotopic to $g_k$. Step [](#s1-8){.pf-ref} then gives $k=0$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part $1$; step [](#s1-5){.pf-ref} answers part $2$; and steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} answer part $3$.

:::

:::

:::
