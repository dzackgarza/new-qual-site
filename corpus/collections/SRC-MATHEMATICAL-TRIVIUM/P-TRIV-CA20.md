---
schema: qual/card@1
id: P-TRIV-CA20
kind: problem
title: $\int_0^\infty \frac{dx}{(x+i)\sqrt x}$ by a keyhole contour
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 20, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source also supplies Figure 3; Flash has only its image placeholder/caption. The contour is nevertheless specified textually as $L_+\cup C_R\cup L_-\cup\gamma_\epsilon$.
---

::: {.problem}
(a) Compute the integral $I _ { 1 } = \int _ { C } \frac { \mathrm { d } z } { ( z + i ) \sqrt { z } }$ , where the contour C is shown in figure 3, $C = L _ { + } \cup C _ { R } \cup L _ { - } \cup \gamma _ { \epsilon }$ , and we send the radius of $\gamma _ { \epsilon }$ to zero and the radius of $C _ { R }$ to infinity.
Note that, because of the square root, $z = 0$ is a branch point.
We choose to have a branch cut on the positive real axis.

(b) Find a relation between the integral $I _ { 1 }$ and $I _ { 2 } = \int _ { 0 } ^ { \infty } \frac { 1 } { ( x + i ) \sqrt { x } } \mathrm { d } x$ ,then use the result from the previous point to find the value of $I _ { 2 }$ .
:::

::: {.solution}

Use the branch
$$
\sqrt z
=
\sqrt r\,e^{i\theta/2},
\qquad
z=re^{i\theta},
\qquad
0<\theta<2\pi.
$$
This places the branch cut on the positive real axis.

::: pf

::: {.pf-step #s1-1}

The integrand
$$
F(z)
=
\frac1{(z+i)\sqrt z}
$$
has a single pole inside the keyhole contour, at
$$
z=-i.
$$


::: pf-proof

The factor $z+i$ vanishes only at $-i$. The square root has a branch point at
$0$ rather than a pole, and the contour excludes $0$ by the inner circle.
With the chosen branch, $-i$ has argument $3\pi/2$ and lies in the branch
domain.

:::

:::

::: {.pf-step #s1-2}

On the chosen branch,
$$
\sqrt{-i}
=
e^{3\pi i/4},
$$
and therefore
$$
\operatorname{Res}_{z=-i}F(z)
=
e^{-3\pi i/4}.
$$


::: pf-proof

Since
$$
-i=e^{3\pi i/2}
$$
with argument in $(0,2\pi)$,
$$
\sqrt{-i}
=
e^{3\pi i/4}.
$$
The pole is simple, so its residue is
$$
\frac1{\sqrt{-i}}
=
e^{-3\pi i/4}.
$$

:::

:::

::: {.pf-step #s1-3}

The outer-circle contribution tends to zero as $R\to\infty$.


::: pf-proof

On $\abs{z}=R>1$,
$$
\abs{z+i}
\geq
R-1
$$
and
$$
\abs{\sqrt z}=\sqrt R.
$$
The outer circle has length $2\pi R$, so the $ML$ estimate gives
$$
\abs{
\int_{C_R}F(z)\,dz
}
\leq
\frac{2\pi R}{(R-1)\sqrt R}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-4}

The inner-circle contribution tends to zero as
$\varepsilon\to0^+$.


::: pf-proof

On $\abs{z}=\varepsilon<1$,
$$
\abs{z+i}
\geq
1-\varepsilon
$$
and
$$
\abs{\sqrt z}=\sqrt\varepsilon.
$$
The inner circle has length $2\pi\varepsilon$. Hence
$$
\abs{
\int_{\gamma_\varepsilon}F(z)\,dz
}
\leq
\frac{2\pi\varepsilon}
{(1-\varepsilon)\sqrt\varepsilon}
=
\frac{2\pi\sqrt\varepsilon}{1-\varepsilon}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-5}

In the limit
$$
R\to\infty,
\qquad
\varepsilon\to0^+,
$$
the upper-ray contribution tends to
$$
I_2
=
\int_0^\infty
\frac{dx}{(x+i)\sqrt x}.
$$


::: pf-proof

On the upper side of the positive real axis,
$$
\arg z=0,
$$
so
$$
\sqrt z=\sqrt x.
$$
The ray is traversed from $\varepsilon$ to $R$, giving exactly the truncated
version of $I_2$.

:::

:::

::: {.pf-step #s1-6}

The lower-ray contribution also tends to $I_2$.


::: pf-proof

On the lower side of the cut,
$$
\arg z=2\pi,
$$
so
$$
\sqrt z
=
\sqrt x,e^{i\pi}
=
-\sqrt x.
$$
The lower ray is traversed from $R$ back to $\varepsilon$. Hence its
contribution is
$$
\int_R^\varepsilon
\frac{dx}{(x+i)(-\sqrt x)}
=
\int_\varepsilon^R
\frac{dx}{(x+i)\sqrt x}.
$$
Taking the limits gives $I_2$.

:::

:::

::: {.pf-step #s1-7}

Therefore the limiting keyhole integral satisfies
$$
I_1=2I_2.
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} show that both circular arcs vanish in the limit, while
steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} show that the two ray contributions both tend to $I_2$.

:::

:::

::: {.pf-step #s1-8}

The residue theorem gives
$$
I_1
=
2\pi i,e^{-3\pi i/4}
=
\sqrt2\pi(1-i).
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, the contour encloses exactly one pole with residue
$$
e^{-3\pi i/4}
=
-\frac{1+i}{\sqrt2}.
$$
Thus
$$
2\pi i e^{-3\pi i/4}
=
2\pi i
\left(
-\frac{1+i}{\sqrt2}
\right)
=
\sqrt2\pi(1-i).
$$

:::

:::

::: {.pf-step #s1-9}

Consequently
$$
\boxed{
I_2
=
\int_0^\infty
\frac{dx}{(x+i)\sqrt x}
=
\frac{\pi}{\sqrt2}(1-i).
}
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
I_2=\frac{I_1}{2}.
$$
Substitute the value of $I_1$ from step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} solves part (a), and steps [](#s1-7){.pf-ref} and [](#s1-9){.pf-ref} solve part (b).

:::

:::

:::
