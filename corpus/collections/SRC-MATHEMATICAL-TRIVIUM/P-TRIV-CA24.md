---
schema: qual/card@1
id: P-TRIV-CA24
kind: problem
title: $\int_0^\infty \frac{\log^2 x}{1+x^2}\,dx$ by contour integration
classification:
  areas: [complex-analysis]
  topics:
  - Contour Integration
  - Complex Logarithm
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Quoted problems 23 and 34 and described the Figure 3 contour referenced by the hint, against Complex Analysis pages 15-18 of the source PDF.
---

::: {.problem}
Compute $\displaystyle\int_0^\infty \frac{\log^2 x}{1 + x^2}\,\mathrm{d}x$ (**hint:** solve problem 23 first.
Use the function $\frac{\log^3 x}{1 + x^2}$ integrated over some smart choice of contour);

Problem 23 of the source reads: Compute $\int_0^\infty \frac{\log x}{1 + x^\alpha}\,\mathrm{d}x$ for $\alpha \in \NN$, $\alpha > 1$ (hint: solve problem 34 first. Now, as a contour, use a circular wegde of the complex plane that makes a $2\pi/\alpha$ angle with the positive real axis).

Problem 34 of the source reads: Solve the integral $\int_0^\infty \frac{1}{1 + x^\alpha}\,dx$ for $\alpha \in \NN$, $\alpha > 1$ by integrating the function $\frac{\log z}{1 + z^\alpha}$ along the contour of figure 3.

Figure 3 of the source shows the contour $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$: $L_+$ runs just above the positive real axis from the small circle $\gamma_\epsilon$ around $0$ out to the large circle $C_R$ of radius $R$ centered at $0$, $C_R$ is traversed counterclockwise, $L_-$ returns just below the positive real axis, and $\gamma_\epsilon$ is traversed clockwise around $0$.
:::

::: {.solution}

Use the branch
$$
\Log z=\log\abs{z}+i\arg z,
\qquad
0<\arg z<2\pi,
$$
on the slit plane $\CC\setminus[0,\infty)$.

::: pf

::: pf-step

Let
$$
F(z)=\frac{(\Log z)^3}{1+z^2}.
$$
Inside the standard keyhole contour about the positive real axis, the poles of
$F$ are $z=i$ and $z=-i$.


::: pf-proof

The only poles of $1/(1+z^2)$ are at $\pm i$, and both lie away from the
branch cut.

:::

:::

::: pf-step

The residues are
$$
\operatorname{Res}_{z=i}F(z)
=
-\frac{\pi^3}{16}
$$
and
$$
\operatorname{Res}_{z=-i}F(z)
=
\frac{27\pi^3}{16}.
$$


::: pf-proof

On the chosen branch,
$$
\Log i=i\frac\pi2,
\qquad
\Log(-i)=i\frac{3\pi}{2}.
$$
Since the poles are simple,
$$
\operatorname{Res}_{z=i}F
=
\frac{(i\pi/2)^3}{2i}
=
-\frac{\pi^3}{16},
$$
and
$$
\operatorname{Res}_{z=-i}F
=
\frac{(3i\pi/2)^3}{-2i}
=
\frac{27\pi^3}{16}.
$$

:::

:::

::: {.pf-step #s1-3}

Hence the keyhole contour integral tends to
$$
\frac{13\pi^4 i}{4}.
$$


::: pf-proof

The sum of the residues is
$$
\frac{26\pi^3}{16}
=
\frac{13\pi^3}{8}.
$$
The residue theorem therefore gives
$$
2\pi i\cdot\frac{13\pi^3}{8}
=
\frac{13\pi^4 i}{4}.
$$
The outer circular arc tends to zero because
$$
\frac{R(\log R+2\pi)^3}{R^2-1}
\longrightarrow0,
$$
and the inner circular arc tends to zero because
$$
\varepsilon(\abs{\log\varepsilon}+2\pi)^3
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-4}

Set
$$
I_j
=
\int_0^\infty
\frac{(\log x)^j}{1+x^2}\,dx
$$
for $j=0,1,2$. Then the two radial sides of the keyhole contour contribute,
in the limit,
$$
-6\pi i,I_2
+
12\pi^2 I_1
+
8\pi^3 i,I_0.
$$


::: pf-proof

On the upper side of the positive real axis,
$$
\Log x=\log x,
$$
and the contour runs from $\varepsilon$ to $R$. Thus this side contributes
$$
\int_\varepsilon^R
\frac{(\log x)^3}{1+x^2}\,dx.
$$

On the lower side, the chosen branch has
$$
\Log x=\log x+2\pi i,
$$
and the contour runs from $R$ back to $\varepsilon$. Hence that side
contributes
$$
-\int_\varepsilon^R
\frac{(\log x+2\pi i)^3}{1+x^2}\,dx.
$$
Subtracting the cubic expansions gives
$$
(\log x)^3
-
(\log x+2\pi i)^3
=
-6\pi i(\log x)^2
+
12\pi^2\log x
+
8\pi^3 i.
$$
Letting $\varepsilon\to0^+$ and $R\to\infty$ yields the displayed
combination of $I_0,I_1,I_2$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
I_0=\frac\pi2
$$
and
$$
I_1=0.
$$


::: pf-proof

The first identity is
$$
\int_0^\infty\frac{dx}{1+x^2}
=
\frac\pi2.
$$
For the second, Problem 23 with $\alpha=2$ gives
$$
I_1
=
-\frac{\pi^2}{4}
\csc\left(\frac\pi2\right)
\cot\left(\frac\pi2\right)
=0.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
-6\pi i,I_2
+
4\pi^4 i
=
\frac{13\pi^4 i}{4}.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, the limiting contour integral is
$$
-6\pi i,I_2
+
12\pi^2 I_1
+
8\pi^3 i,I_0.
$$
Substitute the values from step [](#s1-5){.pf-ref}:
$$
12\pi^2I_1=0,
$$
and
$$
8\pi^3 i I_0
=
8\pi^3 i\cdot\frac\pi2
=
4\pi^4i.
$$
Step [](#s1-3){.pf-ref} gives the value of the same contour integral.

:::

:::

::: {.pf-step #s1-7}

Solving the equation in step [](#s1-6){.pf-ref} gives
$$
\boxed{
\int_0^\infty
\frac{\log^2 x}{1+x^2}\,dx
=
\frac{\pi^3}{8}.
}
$$


::: pf-proof

From step [](#s1-6){.pf-ref},
$$
-6\pi i,I_2
=
\left(
\frac{13}{4}-4
\right)\pi^4 i
=
-\frac{3\pi^4 i}{4}.
$$
Divide by $-6\pi i$:
$$
I_2
=
\frac{3\pi^4/4}{6\pi}
=
\frac{\pi^3}{8}.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required value.

:::

:::

:::
