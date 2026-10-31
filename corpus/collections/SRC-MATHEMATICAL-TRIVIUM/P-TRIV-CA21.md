---
schema: qual/card@1
id: P-TRIV-CA21
kind: problem
title: $\int_0^\infty \frac{x^p}{x^2+1}\,dx$ for $0<p<1$ by a keyhole contour
classification:
  areas: [complex-analysis]
  topics:
  - Contour Integration
  - Branch Cuts
  - Keyhole Contours
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source prints $dz$ at the end of the real integral $I_2$; this source/extraction discrepancy is retained rather than silently changed to $dx$.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the setup of exercise 20 and the Figure 3 contour and removed extraction residue, against Complex Analysis Problems 20-21 on page 15 of the source PDF.
---

::: {.problem}
Repeat exercise 20 this time with $I_1 = \int_C \frac{z^p}{z^2+1}\,\mathrm{d}z$ and $I_2 = \int_0^\infty \frac{x^p}{x^2+1}\,\mathrm{d}x$ with $0 < p < 1$; the contour is the same as before.

Exercise 20 of the source reads:
(a) Compute the integral $I_1 = \int_C \frac{\mathrm{d}z}{(z+i)\sqrt{z}}$, where the contour $C$ is shown in figure 3, $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$, and we send the radius of $\gamma_\epsilon$ to zero and the radius of $C_R$ to infinity.
Note that, because of the square root, $z = 0$ is a branch point.
We choose to have a branch cut on the positive real axis.
(b) Find a relation between the integral $I_1$ and $I_2 = \int_0^\infty \frac{1}{(x+i)\sqrt{x}}\,\mathrm{d}x$, then use the result from the previous point to find the value of $I_2$.

Figure 3 of the source shows the contour $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$: $L_+$ runs just above the positive real axis from the small circle $\gamma_\epsilon$ around $0$ out to the large circle $C_R$ of radius $R$ centered at $0$, $C_R$ is traversed counterclockwise, $L_-$ returns just below the positive real axis, and $\gamma_\epsilon$ is traversed clockwise around $0$.
:::

::: {.solution}

Use the branch
$$
z^p
=
r^p e^{ip\theta},
\qquad
z=re^{i\theta},
\qquad
0<\theta<2\pi.
$$

::: pf

::: pf-step

The function
$$
F(z)
=
\frac{z^p}{z^2+1}
$$
has two simple poles inside the keyhole contour:
$$
z=i
\qquad\text{and}\qquad
z=-i.
$$


::: pf-proof

The denominator vanishes exactly at $\pm i$. Both points lie in the branch
domain
$$
0<\arg z<2\pi.
$$

:::

:::

::: pf-step

The residue at $z=i$ is
$$
\operatorname{Res}_{z=i}F(z)
=
\frac{e^{i\pi p/2}}{2i}.
$$


::: pf-proof

On the chosen branch,
$$
i^p
=
e^{i\pi p/2}.
$$
Since the derivative of $z^2+1$ at $i$ is $2i$,
$$
\operatorname{Res}_{z=i}F(z)
=
\frac{i^p}{2i}.
$$

:::

:::

::: pf-step

The residue at $z=-i$ is
$$
\operatorname{Res}_{z=-i}F(z)
=
-\frac{e^{3\pi i p/2}}{2i}.
$$


::: pf-proof

On the branch $0<\arg z<2\pi$,
$$
\arg(-i)=\frac{3\pi}{2},
$$
so
$$
(-i)^p
=
e^{3\pi i p/2}.
$$
The derivative of $z^2+1$ at $-i$ is $-2i$, giving the result.

:::

:::

::: {.pf-step #s1-4}

Hence the limiting contour integral is
$$
I_1
=
\pi
\left(
e^{i\pi p/2}
-
e^{3\pi i p/2}
\right).
$$


::: pf-proof

The residue theorem gives
$$
I_1
=
2\pi i
\left(
\frac{e^{i\pi p/2}}{2i}
-
\frac{e^{3\pi i p/2}}{2i}
\right),
$$
provided the two circular arcs vanish. That vanishing is verified in
steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The outer-circle contribution tends to zero as $R\to\infty$.


::: pf-proof

On $\abs{z}=R>1$,
$$
\abs{z^p}=R^p
$$
and
$$
\abs{z^2+1}
\geq
R^2-1.
$$
The outer circle has length $2\pi R$. Hence
$$
\abs{
\int_{C_R}F(z)\,dz
}
\leq
\frac{2\pi R^{p+1}}{R^2-1}.
$$
Since $p<1$, the right-hand side tends to zero.

:::

:::

::: {.pf-step #s1-6}

The inner-circle contribution tends to zero as
$\varepsilon\to0^+$.


::: pf-proof

On $\abs{z}=\varepsilon<1$,
$$
\abs{z^p}=\varepsilon^p
$$
and
$$
\abs{z^2+1}
\geq
1-\varepsilon^2.
$$
The inner circle has length $2\pi\varepsilon$, so
$$
\abs{
\int_{\gamma_\varepsilon}F(z)\,dz
}
\leq
\frac{2\pi\varepsilon^{p+1}}
{1-\varepsilon^2}
\longrightarrow0
$$
because $p>0$.

:::

:::

::: {.pf-step #s1-7}

The upper-ray contribution tends to
$$
I_2
=
\int_0^\infty
\frac{x^p}{1+x^2}\,dx.
$$


::: pf-proof

On the upper side of the positive axis,
$$
\arg z=0,
$$
so
$$
z^p=x^p.
$$
The ray is traversed from $\varepsilon$ to $R$, producing the truncated
integral for $I_2$.

:::

:::

::: {.pf-step #s1-8}

The lower-ray contribution tends to
$$
-e^{2\pi ip}I_2.
$$


::: pf-proof

On the lower side of the positive-axis cut,
$$
\arg z=2\pi,
$$
so
$$
z^p
=
x^p e^{2\pi ip}.
$$
The lower ray is traversed from $R$ to $\varepsilon$, hence its contribution
is
$$
\int_R^\varepsilon
\frac{x^p e^{2\pi ip}}{1+x^2}\,dx
=
-e^{2\pi ip}
\int_\varepsilon^R
\frac{x^p}{1+x^2}\,dx.
$$
Take the limits.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
I_1
=
(1-e^{2\pi ip})I_2.
$$


::: pf-proof

By steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} the circular arcs vanish, and by steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} the
two ray contributions sum to the displayed expression.

:::

:::

::: {.pf-step #s1-10}

One has
$$
\boxed{
I_2
=
\int_0^\infty
\frac{x^p}{1+x^2}\,dx
=
\frac\pi2
\sec\left(\frac{\pi p}{2}\right).
}
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} and [](#s1-9){.pf-ref},
$$
I_2
=
\pi
\frac{
e^{i\pi p/2}
-
e^{3\pi i p/2}
}{
1-e^{2\pi ip}
}.
$$
Factor
$$
e^{i\pi p/2}
-
e^{3\pi i p/2}
=
e^{i\pi p/2}(1-e^{i\pi p})
$$
and
$$
1-e^{2\pi ip}
=
(1-e^{i\pi p})(1+e^{i\pi p}).
$$
Because $0<p<1$,
$$
1-e^{i\pi p}\neq0.
$$
Cancel it to obtain
$$
I_2
=
\pi
\frac{e^{i\pi p/2}}
{1+e^{i\pi p}}.
$$
Finally,
$$
1+e^{i\pi p}
=
2e^{i\pi p/2}
\cos\left(\frac{\pi p}{2}\right),
$$
which yields the stated formula.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} evaluates the contour integral $I_1$, step [](#s1-9){.pf-ref} gives its relation
to $I_2$, and step [](#s1-10){.pf-ref} gives the requested real integral.

:::

:::

:::
