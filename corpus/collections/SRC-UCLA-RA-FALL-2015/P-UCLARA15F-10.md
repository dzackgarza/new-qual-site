---
schema: qual/card@1
id: P-UCLARA15F-10
kind: problem
title: Residue computation of $\int_0^\infty e^{\cos x}\sin(\sin x)\,\frac{dx}{x}$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 10 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Use the Residue Theorem to prove that
\[
\int_0^\infty e^{\cos x} \sin(\sin x)\,\frac{dx}{x} = \frac{\pi}{2}(e - 1).
\]
Use a large semicircle as part of the contour.
:::

::: {.solution}
Define
\[
\boxed{
F(z)=\frac{e^{e^{iz}}-1}{z}}.
\]

The function \(F\) is holomorphic on \(\mathbb C\setminus\{0\}\), with a simple pole at \(0\).

<1>1. The residue at \(0\) is
\[
\boxed{
\operatorname{Res}_{z=0}F=e-1}.
\]

::: {.proof}
Since the numerator is holomorphic and
\[
e^{e^{i\cdot0}}-1=e-1\ne0,
\]
\[
\operatorname{Res}_{z=0}F
=
\lim_{z\to0}zF(z)
=
e-1.
\]
:::

For \(R>1\) and \(0<\varepsilon<1\), let \(\Gamma_{R,\varepsilon}\) be the positively oriented boundary of the upper half-disk
\[
\{z:|z|<R,\ \operatorname{Im}z>0\}
\]
with the upper half-disk \(|z|<\varepsilon\) removed. Thus the contour consists of:
- the real segment \([-R,-\varepsilon]\),
- the small upper semicircle from \(-\varepsilon\) to \(\varepsilon\), traversed clockwise,
- the real segment \([\varepsilon,R]\),
- the large upper semicircle from \(R\) to \(-R\), traversed counterclockwise.

<1>2. The function \(F\) is holomorphic in the region enclosed by \(\Gamma_{R,\varepsilon}\).

::: {.proof}
The only singularity is \(z=0\), and that point lies inside the removed small half-disk.
:::

<1>3. Therefore
\[
\boxed{
\int_{\Gamma_{R,\varepsilon}}F(z)\,dz=0}.
\]

::: {.proof}
Apply Cauchy's theorem, equivalently the residue theorem with no poles inside the indented contour.
:::

## The large semicircle

Let
\[
z=Re^{i\theta},
\qquad
0\le\theta\le\pi.
\]

<1>4. On the large semicircle,
\[
\boxed{
|e^{iz}|=e^{-R\sin\theta}\le1}.
\]

::: {.proof}
If
\[
z=R(\cos\theta+i\sin\theta),
\]
then
\[
iz=iR\cos\theta-R\sin\theta,
\]
so
\[
|e^{iz}|=e^{-R\sin\theta}.
\]
:::

<1>5. If \(|w|\le1\), then
\[
\boxed{
|e^w-1|\le e|w|}.
\]

::: {.proof}
Using
\[
e^w-1
=
w\int_0^1 e^{tw}\,dt,
\]
one gets
\[
|e^w-1|
\le
|w|
\int_0^1 e^{t|w|}\,dt
\le
e|w|.
\]
:::

<1>6. Hence on the large semicircle,
\[
|F(z)|
\le
\frac{e}{R}e^{-R\sin\theta}.
\]

::: {.proof}
Apply step <1>5 with
\[
w=e^{iz},
\]
whose modulus is at most \(1\) by step <1>4.
:::

<1>7. Therefore the large-arc integral satisfies
\[
\left|
\int_{\text{large arc}}F(z)\,dz
\right|
\le
e\int_0^\pi e^{-R\sin\theta}\,d\theta.
\]

::: {.proof}
On the arc,
\[
|dz|=R\,d\theta.
\]
Combine with step <1>6.
:::

<1>8. For
\[
0\le\theta\le\frac{\pi}{2},
\]
one has
\[
\boxed{
\sin\theta\ge\frac{2\theta}{\pi}}.
\]

::: {.proof}
The sine function is concave on \([0,\pi]\), so on \([0,\pi/2]\) it lies above the chord joining
\[
(0,0)
\quad\text{and}\quad
(\pi/2,1).
\]
:::

<1>9. Consequently,
\[
\int_0^\pi e^{-R\sin\theta}\,d\theta
\le
\frac{\pi}{R}.
\]

::: {.proof}
By symmetry,
\[
\int_0^\pi e^{-R\sin\theta}\,d\theta
=
2\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta.
\]
Using step <1>8,
\[
\begin{aligned}
2\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta
&\le
2\int_0^{\pi/2}
e^{-2R\theta/\pi}\,d\theta\\
&=
\frac{\pi}{R}(1-e^{-R})\\
&\le
\frac{\pi}{R}.
\end{aligned}
\]
:::

<1>10. Hence
\[
\boxed{
\int_{\text{large arc}}F(z)\,dz
\longrightarrow0}
\]
as \(R\to\infty\).

::: {.proof}
Combine steps <1>7--<1>9.
:::

## The small indentation

Parameterize the small upper semicircle clockwise by
\[
z=\varepsilon e^{i\theta},
\qquad
\pi\ge\theta\ge0.
\]

<1>11. As \(z\to0\),
\[
\boxed{
F(z)=\frac{e-1}{z}+O(1)}.
\]

::: {.proof}
The numerator has Taylor expansion
\[
e^{e^{iz}}-1
=
(e-1)+O(z).
\]
Divide by \(z\).
:::

<1>12. Therefore
\[
\boxed{
\int_{\text{small arc}}F(z)\,dz
\longrightarrow
-i\pi(e-1)}
\]
as \(\varepsilon\downarrow0\).

::: {.proof}
Using the principal part from step <1>11,
\[
\int_{\text{small arc}}
\frac{e-1}{z}\,dz
=
(e-1)
\int_{\pi}^{0}
\frac{1}{\varepsilon e^{i\theta}}
i\varepsilon e^{i\theta}\,d\theta
=
-i\pi(e-1).
\]
The \(O(1)\) remainder contributes \(O(\varepsilon)\), which tends to \(0\).
:::

## The real-axis contribution

For real \(x\ne0\),
\[
F(x)
=
\frac{e^{e^{ix}}-1}{x}.
\]

<1>13. One has
\[
\boxed{
F(-x)=-\overline{F(x)}}.
\]

::: {.proof}
Since
\[
e^{-ix}=\overline{e^{ix}},
\]
\[
e^{e^{-ix}}
=
\overline{e^{e^{ix}}}.
\]
Therefore
\[
F(-x)
=
\frac{e^{e^{-ix}}-1}{-x}
=
-\overline{
\frac{e^{e^{ix}}-1}{x}
}.
\]
:::

<1>14. Hence
\[
F(x)+F(-x)
=
2i\,\operatorname{Im}F(x).
\]

::: {.proof}
For any complex number \(w\),
\[
w-\overline w=2i\,\operatorname{Im}w.
\]
Use step <1>13.
:::

<1>15. The imaginary part of \(F(x)\) is
\[
\boxed{
\operatorname{Im}F(x)
=
e^{\cos x}\sin(\sin x)\frac1x}.
\]

::: {.proof}
Since
\[
e^{e^{ix}}
=
e^{\cos x+i\sin x}
=
e^{\cos x}
\left(
\cos(\sin x)+i\sin(\sin x)
\right),
\]
subtracting \(1\) changes only the real part. Divide by the real number \(x\).
:::

<1>16. Therefore
\[
\int_{-R}^{-\varepsilon}F(x)\,dx
+
\int_{\varepsilon}^{R}F(x)\,dx
=
2i
\int_{\varepsilon}^{R}
e^{\cos x}\sin(\sin x)\frac{dx}{x}.
\]

::: {.proof}
Change variables \(x=-t\) in the negative real integral:
\[
\int_{-R}^{-\varepsilon}F(x)\,dx
=
\int_{\varepsilon}^{R}F(-t)\,dt.
\]
Add the positive integral and use steps <1>14--<1>15.
:::

<1>17. The integrand
\[
e^{\cos x}\sin(\sin x)\frac1x
\]
has a finite limit \(e\) as \(x\to0\).

::: {.proof}
As \(x\to0\),
\[
\cos x\to1,
\qquad
\frac{\sin(\sin x)}{x}
=
\frac{\sin(\sin x)}{\sin x}
\frac{\sin x}{x}
\to1.
\]
Thus the product tends to \(e\).
:::

<1>18. Hence the improper integral near \(0\) is ordinary convergent.

::: {.proof}
Step <1>17 shows the singularity at \(0\) is removable.
:::

Now return to the contour identity in step <1>3.

<1>19. Letting first \(R\to\infty\) and then \(\varepsilon\downarrow0\),
\[
2i
\int_0^\infty
e^{\cos x}\sin(\sin x)\frac{dx}{x}
-i\pi(e-1)
=
0.
\]

::: {.proof}
The contour integral is zero by step <1>3. The large arc tends to zero by step <1>10. The small arc tends to
\[
-i\pi(e-1)
\]
by step <1>12. The two real segments combine as in step <1>16, and step <1>18 permits passage to the limit \(\varepsilon\downarrow0\).
:::

<1>20. Therefore
\[
2i
\int_0^\infty
e^{\cos x}\sin(\sin x)\frac{dx}{x}
=
i\pi(e-1).
\]

::: {.proof}
Rearrange step <1>19.
:::

<1>21. Dividing by \(2i\),
\[
\boxed{
\int_0^\infty
e^{\cos x}\sin(\sin x)\frac{dx}{x}
=
\frac{\pi}{2}(e-1)}.
\]

::: {.proof}
This is immediate from step <1>20.
:::

<1>22. Q.E.D.

::: {.proof}
Step <1>21 is the required identity.
:::
:::
