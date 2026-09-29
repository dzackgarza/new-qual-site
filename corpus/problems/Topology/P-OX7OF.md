---
schema: qual/card@1
id: P-OX7OF
kind: problem
title: Induced maps on $\pi_1(S^1)$ of $z\mapsto z^n$, antipodal, and $\sin$ maps
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
8. Here we go:

9. Let $\alpha(t) = e^{2\pi it}$ where $t \in [0, 1]$, be a loop in $S^1$ parameterized by $t$, which goes around $S^1$ exactly once.
   Then under the map $f: z \mapsto z^n$, we obtain $f(\alpha(t)) = e^{2\pi n i t}$ where $t \in [0,1]$.
   This resulting loop then goes around $S^1$ $n$ times, so the induced homomorphism on $\pi_1(S^1) = \ZZ$ is the map $f^*: \ZZ \into \ZZ$ given by $f^*(a) = na$.

10. Define $\alpha$ as above, and define $f: S^1 \into S^1$ to be the antipodal map, so $f(z) = -z$ for $z \in S^1 \subset \CC$.
    We then left $\alpha$ to the fundamental group, and define $f_*([\alpha]) = [f \circ \alpha]$.
    Computing, we have $(f\circ \alpha)(t) = f(\alpha(t)) = -e^{2\pi i t}$.
    Where $\alpha(0) = \alpha(1) = 1 + 0i$, we have $(f\circ \alpha)(0) = (f\circ \alpha)(1) = -1 + 0i$.
    But note that $\alpha$ was a counter-clockwise loop in $S^1$, and the image of $\alpha$ is also a counter-clockwise loop.
    So this maps the generator $[\alpha] \in \pi_1(S^1, 1)$ to the generator $[\alpha'] \in \pi_1(S^1, -1)$.
    But since $S^1$ is path-connected, the fundamental groups at these two base points are isomorphic.
    Alternatively: the antipodal map on $S^1$ is homotopic to the identity map (since $n=1$ is odd), so $[f\circ \alpha] = [f][\alpha] = [\id][\alpha] = [\alpha]$, so the induced homomorphism on $\pi_1(S^1)$ is the identity map.

11. Let $\alpha(t) = e^{it}$ where $t\in [0, 2\pi]$ be a counter-clockwise loop in $S^1$; then $[\alpha]$ generates the fundamental group.
    Then $f^*([\alpha]) = [(f\circ \alpha) (t)] = [e^{it} \mapsto e^{2\pi i \sin t}]$.
    Then just consider how $\sin$ behaves in each quadrant.
    In quadrant 1, as $t$ ranges from $0, \pi/2$ then $\sin t$ ranges from 0 to 1, so $\alpha$ is exactly traced out.
    In quadrant two, $\bar\alpha$ is traced out, since $\sin t$ decreases from 1 to 0. This happens again in the bottom quadrants, so we have $f^*([\alpha]) = [\alpha\bar\alpha\alpha\bar\alpha] = [\alpha][\alpha]^{-1}[\alpha][\alpha]^{-1} = [\id]$.
    But the identity element in $\ZZ$ is  0, so the induced homomorphism on $\ZZ$ is $f^*(a) = 0$, the homomorphism sending everything to 0.
:::

::: {.solution}
**Goal.** Compute the induced maps on $\pi_1(S^1) \cong \ZZ$ for the three maps $z \mapsto z^n$, the antipodal map, and $z \mapsto e^{2\pi i \sin(\arg z)}$.

::: pf

::: {.pf-step #s1}
$f(z) = z^n$ induces $f_*: \ZZ \to \ZZ$, $a \mapsto na$.

::: pf-proof

::: pf-step
The generator $[\alpha]$ of $\pi_1(S^1)$ is the loop $\alpha(t) = e^{2\pi i t}$.

::: pf-proof
this loop winds once around $S^1$.
:::

:::

::: pf-step
$f \circ \alpha$ is the loop $t \mapsto e^{2\pi i n t}$, which winds $n$ times.

::: pf-proof
$f(\alpha(t)) = (e^{2\pi i t})^n = e^{2\pi i n t}$.
:::

:::

::: pf-step
Hence $f_*([\alpha]) = n[\alpha]$, so $f_*(a) = na$.

::: pf-proof
the winding number of $f \circ \alpha$ is $n$.
:::

:::

:::

:::

::: {.pf-step #s2}
The antipodal map $f(z) = -z$ induces the identity on $\pi_1(S^1)$.

::: pf-proof

::: pf-step
$f(z) = -z = e^{i\pi} z$ is rotation by $\pi$.

::: pf-proof
multiplication by $-1$ on the unit circle is rotation through angle $\pi$.
:::

:::

::: pf-step
Rotation by $\pi$ is homotopic to the identity.

::: pf-proof
rotate continuously from angle $\pi$ back to angle $0$ (the family $z \mapsto e^{i(1-s)\pi} z$).
:::

:::

::: pf-step
Hence $f_* = \id$, i.e. $f_*(a) = a$.

::: pf-proof
homotopic maps induce the same homomorphism on $\pi_1$.
:::

:::

:::

:::

::: {.pf-step #s3}
$f(e^{it}) = e^{2\pi i \sin t}$ induces the zero map on $\pi_1(S^1)$.

::: pf-proof

::: pf-step
As $t$ runs $0 \to \pi/2$, $\sin t$ runs $0 \to 1$, so $f \circ \alpha$ traces the generator $\alpha$ once.

::: pf-proof
$e^{2\pi i \sin t}$ winds once counterclockwise.
:::

:::

::: pf-step
As $t$ runs $\pi/2 \to \pi$, $\sin t$ runs $1 \to 0$, so $f \circ \alpha$ traces $\bar\alpha$ (the reverse loop).

::: pf-proof
the argument decreases from $2\pi$ to $0$.
:::

:::

::: pf-step
On $[\pi,3\pi/2]$, $\sin t$ decreases from $0$ to $-1$, so the image again winds once clockwise; on $[3\pi/2,2\pi]$, $\sin t$ increases from $-1$ to $0$, so the image winds once counterclockwise. Thus the four quadrants contribute winding numbers $+1,-1,-1,+1$.

::: pf-proof
The argument $2\pi\sin t$ changes respectively by $+2\pi,-2\pi,-2\pi,+2\pi$ on the four quarter-intervals.
:::

:::

::: pf-step
Hence the total winding number is
$$
1-1-1+1=0,
$$
so $f\circ\alpha$ is null-homotopic.

::: pf-proof
Homotopy classes of loops in $S^1$ are classified by winding number.
:::

:::

::: pf-step
Hence $f_*([\alpha]) = 0$, so $f_*(a) = 0$ for all $a$.

::: pf-proof
the generator maps to the identity element $0 \in \ZZ$.
:::

:::

:::

:::

::: pf-qed
step [](#s1){.pf-ref}, step [](#s2){.pf-ref}, and step [](#s3){.pf-ref} give the three induced maps.
:::

:::

:::
