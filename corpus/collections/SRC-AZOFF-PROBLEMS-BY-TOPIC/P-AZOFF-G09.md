---
schema: qual/card@1
id: P-AZOFF-G09
kind: problem
title: $\int_{-\infty}^\infty\frac{1+x^2}{1+x^4}\,dx$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Residues, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Integrated (1+z^2)/(1+z^4) over an upper semicircle. The arc integral
    tends to zero and the residues at exp(i pi/4) and exp(3i pi/4) are both
    -i/(2 sqrt(2)), giving the value sqrt(2) pi.
---

::: {.problem}
Evaluate $\textstyle \int _ { - \infty } ^ { \infty } { \frac { 1 + x ^ { 2 } } { 1 + x ^ { 4 } } } d x$
:::

::: {.solution}
Set
$$
F(z)=\frac{1+z^2}{1+z^4}.
$$
For $R>1$, integrate $F$ over the positively oriented upper semicircle with
diameter $[-R,R]$.

<1>1. The poles of $F$ in the upper half-plane are
$$
\zeta_1=e^{i\pi/4}
\qquad\text{and}\qquad
\zeta_2=e^{3i\pi/4}.
$$

::: {.proof}
The poles are the roots of
$$
z^4=-1=e^{i(\pi+2\pi k)}.
$$
Thus
$$
z=e^{i(\pi/4+k\pi/2)},
\qquad
k=0,1,2,3.
$$
Exactly the roots with $k=0,1$ lie in the upper half-plane.
:::

<1>2. The residues at the two upper-half-plane poles are
$$
\Res(F;\zeta_1)
=
-\frac{i}{2\sqrt2},
\qquad
\Res(F;\zeta_2)
=
-\frac{i}{2\sqrt2}.
$$

::: {.proof}
Each pole is simple, so for a root $\zeta$ of $1+z^4$,
$$
\Res(F;\zeta)
=
\frac{1+\zeta^2}{4\zeta^3}.
$$

For $\zeta_1=e^{i\pi/4}$,
$$
\zeta_1^2=i,
\qquad
\zeta_1^3=\zeta_2,
$$
and $\abs{\zeta_2}=1$, so
$$
\begin{aligned}
\Res(F;\zeta_1)
&=
\frac{1+i}{4\zeta_2}\\
&=
\frac{(1+i)(-1-i)}{4\sqrt2}\\
&=
-\frac{i}{2\sqrt2}.
\end{aligned}
$$

For $\zeta_2=e^{3i\pi/4}$,
$$
\zeta_2^2=-i,
\qquad
\zeta_2^3=\zeta_1,
$$
so
$$
\begin{aligned}
\Res(F;\zeta_2)
&=
\frac{1-i}{4\zeta_1}\\
&=
\frac{(1-i)^2}{4\sqrt2}\\
&=
-\frac{i}{2\sqrt2}.
\end{aligned}
$$
:::

<1>3. The integral over the upper semicircular arc tends to zero as
$R\to\infty$.

::: {.proof}
On $\abs{z}=R$,
$$
\abs{1+z^2}\leq1+R^2
$$
and
$$
\abs{1+z^4}\geq R^4-1.
$$
Hence
$$
\abs{F(z)}
\leq
\frac{1+R^2}{R^4-1}.
$$
The arc has length $\pi R$, so
$$
\abs{
\int_{\text{arc}}F(z)\,dz
}
\leq
\frac{\pi R(1+R^2)}{R^4-1}
\longrightarrow0.
$$
:::

<1>4. The requested integral is
$$
\boxed{
\int_{-\infty}^{\infty}
\frac{1+x^2}{1+x^4}\,dx
=
\sqrt2\,\pi.
}
$$

::: {.proof}
By steps <1>1 and <1>2, the sum of the enclosed residues is
$$
-\frac{i}{\sqrt2}.
$$
The residue theorem gives
$$
\int_{C_R}F(z)\,dz
=
2\pi i
\left(-\frac{i}{\sqrt2}\right)
=
\sqrt2\,\pi.
$$
Split the contour into the real segment and the upper arc. Let
$R\to\infty$ and use step <1>3 to obtain the displayed improper integral.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested evaluation.
:::
:::
