---
schema: qual/card@1
id: P-AZOFF-G08
kind: problem
title: $\int_0^\infty\frac{\sqrt x}{1+x^2}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the branch sqrt(z)=r^(1/2)e^(i theta/2), 0<theta<2pi, and a keyhole
    contour about the positive real axis. The two banks contribute twice the
    target integral, both circular arcs vanish, and the residues at i and -i
    sum to -i/sqrt(2), giving pi/sqrt(2).
---

::: {.problem}
Evaluate $\textstyle \int _ { 0 } ^ { \infty } { \frac { \sqrt { x } } { 1 + x ^ { 2 } } } d x$
:::

::: {.solution}
On
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
F(z)=\frac{z^{1/2}}{1+z^2}.
$$
For $0<\varepsilon<1<R$, integrate $F$ around the positively oriented
keyhole contour with cut along the positive real axis.

::: pf

::: {.pf-step #s1}

The poles inside the contour are $i$ and $-i$, with
$$
\Res(F;i)
=
\frac{1-i}{2\sqrt2},
\qquad
\Res(F;-i)
=
-\frac{1+i}{2\sqrt2}.
$$

::: pf-proof

The poles are the simple zeros of $1+z^2$. On the chosen branch,
$$
i^{1/2}=e^{i\pi/4}
=
\frac{1+i}{\sqrt2},
$$
while $-i$ has argument $3\pi/2$, so
$$
(-i)^{1/2}
=
e^{3\pi i/4}
=
\frac{-1+i}{\sqrt2}.
$$
Therefore
$$
\begin{aligned}
\Res(F;i)
&=
\frac{i^{1/2}}{2i}
=
\frac{1-i}{2\sqrt2},
\\
\Res(F;-i)
&=
\frac{(-i)^{1/2}}{-2i}
=
-\frac{1+i}{2\sqrt2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The sum of the enclosed residues is
$$
-\frac{i}{\sqrt2}.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
\frac{1-i}{2\sqrt2}
-\frac{1+i}{2\sqrt2}
=
-\frac{i}{\sqrt2}.
$$

:::

:::

::: {.pf-step #s3}

The two straight portions of the keyhole contour contribute
$$
2\int_{\varepsilon}^{R}
\frac{\sqrt{x}}{1+x^2}\,dx.
$$

::: pf-proof

On the upper bank,
$$
z^{1/2}=\sqrt{x},
$$
so the contribution is the truncated target integral.

On the lower bank,
$$
z^{1/2}
=
\sqrt{x}e^{i\pi}
=
-\sqrt{x},
$$
and the orientation is from $R$ to $\varepsilon$. Thus the lower-bank
contribution is again
$$
\int_{\varepsilon}^{R}
\frac{\sqrt{x}}{1+x^2}\,dx.
$$

:::

:::

::: {.pf-step #s4}

The outer circular contribution tends to zero as $R\to\infty$.

::: pf-proof

On $\abs{z}=R$,
$$
\abs{z^{1/2}}=R^{1/2},
\qquad
\abs{1+z^2}\geq R^2-1.
$$
The outer arc has length at most $2\pi R$, so
$$
\abs{
\int_{\text{outer arc}}F(z)\,dz
}
\leq
\frac{2\pi R^{3/2}}{R^2-1}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s5}

The inner circular contribution tends to zero as
$\varepsilon\to0$.

::: pf-proof

On $\abs{z}=\varepsilon$,
$$
\abs{z^{1/2}}=\varepsilon^{1/2},
\qquad
\abs{1+z^2}\geq1-\varepsilon^2.
$$
The inner arc has length at most $2\pi\varepsilon$, so
$$
\abs{
\int_{\text{inner arc}}F(z)\,dz
}
\leq
\frac{2\pi\varepsilon^{3/2}}{1-\varepsilon^2}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s6}

The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{\sqrt{x}}{1+x^2}\,dx
=
\frac{\pi}{\sqrt2}.
}
$$

::: pf-proof

By the residue theorem and step [](#s2){.pf-ref}, the keyhole contour integral is
$$
2\pi i
\left(-\frac{i}{\sqrt2}\right)
=
\sqrt2\,\pi.
$$
By step [](#s3){.pf-ref}, the two straight portions contribute twice the truncated
target integral. Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} show that both circular contributions
vanish. Hence
$$
2\int_0^{\infty}
\frac{\sqrt{x}}{1+x^2}\,dx
=
\sqrt2\,\pi,
$$
which yields the displayed value.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the requested evaluation.

:::

:::

:::
