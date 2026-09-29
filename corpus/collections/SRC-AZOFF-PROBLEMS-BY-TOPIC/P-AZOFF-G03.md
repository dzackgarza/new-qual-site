---
schema: qual/card@1
id: P-AZOFF-G03
kind: problem
title: $\int_0^\infty\frac{\sqrt x}{(x+1)^2}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the branch sqrt(z)=r^(1/2)e^(i theta/2), 0<theta<2pi, and a keyhole
    contour about the positive real axis. The two banks contribute twice the
    target integral, both circular arcs vanish, and the only enclosed pole is
    the double pole at -1 with residue -i/2.
---

::: {.problem}
Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sqrt { x } } { ( x + 1 ) ^ { 2 } } } d x$
:::

::: {.solution}
On the slit plane
$$
\CC\sm[0,\infty),
$$
choose the branch
$$
z^{1/2}=r^{1/2}e^{i\theta/2},
\qquad
z=re^{i\theta},
\qquad
0<\theta<2\pi.
$$
Set
$$
F(z)=\frac{z^{1/2}}{(1+z)^2}.
$$
For $0<\varepsilon<1<R$, integrate $F$ around the positively oriented
keyhole contour with outer radius $R$, inner radius $\varepsilon$, and cut
along the positive real axis.

::: pf

::: {.pf-step #s1}

The only pole inside the keyhole contour is the double pole at
$z=-1$, and
$$
\Res(F;-1)=-\frac{i}{2}.
$$

::: pf-proof

The chosen branch is holomorphic away from the positive real axis, and the
only zero of the denominator in the slit plane is $z=-1$. Since
$$
(-1)^{1/2}=e^{i\pi/2}=i
$$
on this branch, the residue at the double pole is
$$
\begin{aligned}
\Res(F;-1)
&=
\left.
\frac{d}{dz}z^{1/2}
\right|_{z=-1}\\
&=
\left.
\frac1{2z^{1/2}}
\right|_{z=-1}\\
&=
\frac1{2i}
=
-\frac{i}{2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The two straight portions of the keyhole contour contribute
$$
2\int_{\varepsilon}^{R}
\frac{\sqrt{x}}{(1+x)^2}\,dx.
$$

::: pf-proof

On the upper bank of the cut, the argument tends to $0$, so
$$
z^{1/2}=\sqrt{x},
$$
and the contribution is
$$
\int_{\varepsilon}^{R}
\frac{\sqrt{x}}{(1+x)^2}\,dx.
$$

On the lower bank, the argument tends to $2\pi$, so
$$
z^{1/2}
=
\sqrt{x}e^{i\pi}
=
-\sqrt{x}.
$$
This bank is traversed from $R$ to $\varepsilon$, hence its contribution is
$$
\int_R^{\varepsilon}
\frac{-\sqrt{x}}{(1+x)^2}\,dx
=
\int_{\varepsilon}^{R}
\frac{\sqrt{x}}{(1+x)^2}\,dx.
$$
Adding the two contributions gives the claim.

:::

:::

::: {.pf-step #s3}

The outer circular contribution tends to zero as $R\to\infty$.

::: pf-proof

On $\abs{z}=R$,
$$
\abs{z^{1/2}}=R^{1/2}
$$
and
$$
\abs{1+z}\geq R-1.
$$
The outer arc has length at most $2\pi R$, so
$$
\abs{
\int_{\text{outer arc}}F(z)\,dz
}
\leq
\frac{2\pi R^{3/2}}{(R-1)^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s4}

The inner circular contribution tends to zero as
$\varepsilon\to0$.

::: pf-proof

On $\abs{z}=\varepsilon$,
$$
\abs{z^{1/2}}=\varepsilon^{1/2}
$$
and
$$
\abs{1+z}\geq1-\varepsilon.
$$
The inner arc has length at most $2\pi\varepsilon$, so
$$
\abs{
\int_{\text{inner arc}}F(z)\,dz
}
\leq
\frac{2\pi\varepsilon^{3/2}}{(1-\varepsilon)^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s5}

The target integral is
$$
\boxed{
\int_0^{\infty}
\frac{\sqrt{x}}{(1+x)^2}\,dx
=
\frac{\pi}{2}.
}
$$

::: pf-proof

By the residue theorem and step [](#s1){.pf-ref}, the keyhole contour integral is
$$
2\pi i\Res(F;-1)
=
2\pi i\left(-\frac{i}{2}\right)
=
\pi.
$$
By step [](#s2){.pf-ref}, its two straight portions contribute twice the truncated
target integral. Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that the circular contributions
vanish as $R\to\infty$ and $\varepsilon\to0$. Hence
$$
2\int_0^{\infty}
\frac{\sqrt{x}}{(1+x)^2}\,dx
=
\pi,
$$
which gives the displayed value.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the requested evaluation.

:::

:::

:::
