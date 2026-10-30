---
schema: qual/card@1
id: P-TRIV-CA11
kind: problem
title: Image of the sector $\operatorname{Re} z>\operatorname{Im} z>0$ under $e^{z^2}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
What is the image of $\{z \st \Re(z) > \Im(z) > 0\}$ under the mapping $e^{z^2}$?
:::

::: {.solution}

Let
$$
S=
\{z=x+iy\in\CC:x>y>0\}.
$$

::: pf

::: pf-step

The sector $S$ can be written as
$$
S=
\{re^{i\theta}:r>0,\ 0<\theta<\pi/4\}.
$$


::: pf-proof

The inequalities $x>y>0$ place $z$ in the first quadrant and give
$$
0<\frac yx<1.
$$
Thus
$$
0<\arg z<\frac\pi4.
$$
Conversely, every point with argument strictly between $0$ and $\pi/4$
satisfies $x>y>0$.

:::

:::

::: {.pf-step #s1-2}

Squaring maps $S$ bijectively onto the open first quadrant
$$
Q=
\{u+iv:u>0,\ v>0\}.
$$


::: pf-proof

If
$$
z=re^{i\theta}\in S,
$$
then
$$
z^2=r^2e^{2i\theta},
$$
with
$$
0<2\theta<\frac\pi2.
$$
Hence $z^2\in Q$.

Conversely, if
$$
w=\rho e^{i\phi}\in Q,
$$
then
$$
\rho>0,
\qquad
0<\phi<\frac\pi2.
$$
The square root
$$
z=\sqrt\rho\,e^{i\phi/2}
$$
belongs to $S$ and satisfies $z^2=w$. Uniqueness follows because the other
square root has argument differing by $\pi$ and does not lie in $S$.

:::

:::

::: {.pf-step #s1-3}

If $w=u+iv\in Q$, then
$$
\abs{e^w}>1.
$$


::: pf-proof

One has
$$
e^w=e^u e^{iv},
$$
so
$$
\abs{e^w}=e^u.
$$
Since $u>0$, one has $e^u>1$.

:::

:::

::: {.pf-step #s1-4}

Every complex number $\zeta$ with
$$
\abs{\zeta}>1
$$
equals $e^w$ for some $w\in Q$.


::: pf-proof

Write
$$
\zeta=\rho e^{i\psi},
\qquad
\rho>1.
$$
Set
$$
u=\log\rho>0.
$$
Choose an integer $k$ so large that
$$
v=\psi+2\pi k>0.
$$
Then
$$
w=u+iv\in Q,
$$
and
$$
e^w
=
e^u e^{iv}
=
\rho e^{i\psi}
=
\zeta.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore the image of $S$ under $z\mapsto e^{z^2}$ is
$$
\boxed{
\{\zeta\in\CC:\abs{\zeta}>1\}.
}
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $z^2$ ranges over all of $Q$. Step [](#s1-3){.pf-ref} shows that exponentiating
$Q$ produces only points outside the closed unit disk, while step [](#s1-4){.pf-ref} shows
that every such point occurs.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required image.

:::

:::

:::
