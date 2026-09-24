---
schema: qual/card@1
id: P-BKF05-3A
kind: problem
title: Conformally map a slit half-plane to the disk
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained composition. Squaring maps the slit
    right half-plane exactly to C minus (-infinity,1], so after translation
    the principal square-root branch is globally defined; the final Cayley
    map is biholomorphic onto the disk.
---

::: {.problem}
Let \(U\subseteq\mathbb C\) be the open right half-plane with the interval \((0,1]\subseteq\mathbb R\) deleted.
Find an explicit conformal equivalence from \(U\) onto the open unit disk.
:::

::: {.solution}
Let $\sqrt{\phantom z}$ denote the principal square root on
$\CC\sm(-\infty,0]$.

<1>1. The map
$$
T_1:U\longrightarrow\CC\sm(-\infty,1],
\qquad
T_1(z)=z^2,
$$
is a conformal equivalence.

::: {.proof}
On the open right half-plane, every point has argument in
$(-\pi/2,\pi/2)$, so squaring maps that half-plane bijectively and
holomorphically onto $\CC\sm(-\infty,0]$. Its derivative $2z$ never
vanishes there.

The deleted interval $(0,1]$ is mapped bijectively by squaring onto
$(0,1]$. Since squaring is injective on the whole right half-plane,
deleting that interval deletes exactly its image. Therefore
$$
T_1(U)
=
\bigl(\CC\sm(-\infty,0]\bigr)\sm(0,1]
=
\CC\sm(-\infty,1].
$$
Thus $T_1$ is a conformal equivalence onto the stated slit plane.
:::

<1>2. Translation by $-1$ gives a conformal equivalence
$$
T_2:\CC\sm(-\infty,1]
\longrightarrow
\CC\sm(-\infty,0],
\qquad
T_2(w)=w-1.
$$

::: {.proof}
Translation is biholomorphic on $\CC$, and it sends the deleted ray
$(-\infty,1]$ exactly onto $(-\infty,0]$.
:::

<1>3. The principal square root gives a conformal equivalence
$$
T_3:\CC\sm(-\infty,0]
\longrightarrow
\{w\in\CC:\operatorname{Re}w>0\},
\qquad
T_3(\zeta)=\sqrt{\zeta}.
$$

::: {.proof}
If $\zeta=re^{i\theta}$ with $r>0$ and
$-\pi<\theta<\pi$, then
$$
\sqrt{\zeta}=\sqrt r\,e^{i\theta/2},
$$
whose argument lies in $(-\pi/2,\pi/2)$ and hence whose real part is
positive. Conversely, squaring maps the open right half-plane back
biholomorphically onto $\CC\sm(-\infty,0]$, so it is the inverse of
this branch of the square root.
:::

<1>4. The Möbius transformation
$$
T_4(w)=\frac{w-1}{w+1}
$$
is a conformal equivalence from the open right half-plane onto the open
unit disk.

::: {.proof}
For $\operatorname{Re}w>0$,
$$
\abs{w+1}^2-\abs{w-1}^2
=
4\operatorname{Re}w
>0,
$$
so $\abs{T_4(w)}<1$. Conversely, for $\abs{\zeta}<1$, the inverse
formula
$$
w=\frac{1+\zeta}{1-\zeta}
$$
satisfies
$$
\operatorname{Re}w
=
\frac{1-\abs{\zeta}^2}{\abs{1-\zeta}^2}
>0.
$$
Thus $T_4$ is biholomorphic between the two domains.
:::

<1>5. The map
$$
\boxed{
F(z)=
\frac{\sqrt{z^2-1}-1}{\sqrt{z^2-1}+1}
}
$$
is a conformal equivalence from $U$ onto
$$
\{\,\zeta\in\CC:\abs{\zeta}<1\,\}.
$$

::: {.proof}
By steps <1>1--<1>4,
$$
F=T_4\circ T_3\circ T_2\circ T_1
$$
is a composition of conformal equivalences. For $z\in U$, step <1>1
gives $z^2\notin(-\infty,1]$, hence
$z^2-1\notin(-\infty,0]$, so the principal square root appearing in
the displayed formula is defined. Therefore the composition is exactly
the stated explicit conformal equivalence.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested map and proves that it is a conformal
equivalence.
:::
:::
