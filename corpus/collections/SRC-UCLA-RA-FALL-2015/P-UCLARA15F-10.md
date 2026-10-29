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
$$
\int_0^\infty e^{\cos x} \sin(\sin x)\,\frac{dx}{x} = \frac{\pi}{2}(e - 1).
$$
Use a large semicircle as part of the contour.
:::

::: {.solution}

Define
$$
\boxed{
F(z)=\frac{e^{e^{iz}}-1}{z}}.
$$

The function $F$ is holomorphic on $\CC\setminus\{0\}$, with a simple pole at $0$.

::: pf

::: pf-step

The residue at $0$ is
$$
\boxed{
\operatorname{Res}_{z=0}F=e-1}.
$$


::: pf-proof

Since the numerator is holomorphic and
$$
e^{e^{i\cdot0}}-1=e-1\ne0,
$$
$$
\operatorname{Res}_{z=0}F
=
\lim_{z\to0}zF(z)
=
e-1.
$$

:::

:::

::: pf-step

The function $F$ is holomorphic in the region enclosed by $\Gamma_{R,\varepsilon}$.


::: pf-proof

The only singularity is $z=0$, and that point lies inside the removed small half-disk.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\int_{\Gamma_{R,\varepsilon}}F(z)\,dz=0}.
$$


::: pf-proof

Apply Cauchy's theorem, equivalently the residue theorem with no poles inside the indented contour.

:::

:::

::: {.pf-step #s1-4}

On the large semicircle,
$$
\boxed{
|e^{iz}|=e^{-R\sin\theta}\le1}.
$$


::: pf-proof

If
$$
z=R(\cos\theta+i\sin\theta),
$$
then
$$
iz=iR\cos\theta-R\sin\theta,
$$
so
$$
|e^{iz}|=e^{-R\sin\theta}.
$$

:::

:::

::: {.pf-step #s1-5}

If $|w|\le1$, then
$$
\boxed{
|e^w-1|\le e|w|}.
$$


::: pf-proof

Using
$$
e^w-1
=
w\int_0^1 e^{tw}\,dt,
$$
one gets
$$
|e^w-1|
\le
|w|
\int_0^1 e^{t|w|}\,dt
\le
e|w|.
$$

:::

:::

::: {.pf-step #s1-6}

Hence on the large semicircle,
$$
|F(z)|
\le
\frac{e}{R}e^{-R\sin\theta}.
$$


::: pf-proof

Apply step [](#s1-5){.pf-ref} with
$$
w=e^{iz},
$$
whose modulus is at most $1$ by step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Therefore the large-arc integral satisfies
$$
\left|
\int_{\text{large arc}}F(z)\,dz
\right|
\le
e\int_0^\pi e^{-R\sin\theta}\,d\theta.
$$


::: pf-proof

On the arc,
$$
|dz|=R\,d\theta.
$$
Combine with step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

For
$$
0\le\theta\le\frac{\pi}{2},
$$
one has
$$
\boxed{
\sin\theta\ge\frac{2\theta}{\pi}}.
$$


::: pf-proof

The sine function is concave on $[0,\pi]$, so on $[0,\pi/2]$ it lies above the chord joining
$$
(0,0)
\quad\text{and}\quad
(\pi/2,1).
$$

:::

:::

::: {.pf-step #s1-9}

Consequently,
$$
\int_0^\pi e^{-R\sin\theta}\,d\theta
\le
\frac{\pi}{R}.
$$


::: pf-proof

By symmetry,
$$
\int_0^\pi e^{-R\sin\theta}\,d\theta
=
2\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta.
$$
Using step [](#s1-8){.pf-ref},
$$
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
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\int_{\text{large arc}}F(z)\,dz
\longrightarrow0}
$$
as $R\to\infty$.


::: pf-proof

Combine steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

As $z\to0$,
$$
\boxed{
F(z)=\frac{e-1}{z}+O(1)}.
$$


::: pf-proof

The numerator has Taylor expansion
$$
e^{e^{iz}}-1
=
(e-1)+O(z).
$$
Divide by $z$.

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\boxed{
\int_{\text{small arc}}F(z)\,dz
\longrightarrow
-i\pi(e-1)}
$$
as $\varepsilon\downarrow0$.


::: pf-proof

Using the principal part from step [](#s1-11){.pf-ref},
$$
\int_{\text{small arc}}
\frac{e-1}{z}\,dz
=
(e-1)
\int_{\pi}^{0}
\frac{1}{\varepsilon e^{i\theta}}
i\varepsilon e^{i\theta}\,d\theta
=
-i\pi(e-1).
$$
The $O(1)$ remainder contributes $O(\varepsilon)$, which tends to $0$.

:::

:::

::: {.pf-step #s1-13}

One has
$$
\boxed{
F(-x)=-\overline{F(x)}}.
$$


::: pf-proof

Since
$$
e^{-ix}=\overline{e^{ix}},
$$
$$
e^{e^{-ix}}
=
\overline{e^{e^{ix}}}.
$$
Therefore
$$
F(-x)
=
\frac{e^{e^{-ix}}-1}{-x}
=
-\overline{
\frac{e^{e^{ix}}-1}{x}
}.
$$

:::

:::

::: {.pf-step #s1-14}

Hence
$$
F(x)+F(-x)
=
2i\,\operatorname{Im}F(x).
$$


::: pf-proof

For any complex number $w$,
$$
w-\overline w=2i\,\operatorname{Im}w.
$$
Use step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

The imaginary part of $F(x)$ is
$$
\boxed{
\operatorname{Im}F(x)
=
e^{\cos x}\sin(\sin x)\frac1x}.
$$


::: pf-proof

Since
$$
e^{e^{ix}}
=
e^{\cos x+i\sin x}
=
e^{\cos x}
\left(
\cos(\sin x)+i\sin(\sin x)
\right),
$$
subtracting $1$ changes only the real part. Divide by the real number $x$.

:::

:::

::: {.pf-step #s1-16}

Therefore
$$
\int_{-R}^{-\varepsilon}F(x)\,dx
+
\int_{\varepsilon}^{R}F(x)\,dx
=
2i
\int_{\varepsilon}^{R}
e^{\cos x}\sin(\sin x)\frac{dx}{x}.
$$


::: pf-proof

Change variables $x=-t$ in the negative real integral:
$$
\int_{-R}^{-\varepsilon}F(x)\,dx
=
\int_{\varepsilon}^{R}F(-t)\,dt.
$$
Add the positive integral and use steps [](#s1-14){.pf-ref} through [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

The integrand
$$
e^{\cos x}\sin(\sin x)\frac1x
$$
has a finite limit $e$ as $x\to0$.


::: pf-proof

As $x\to0$,
$$
\cos x\to1,
\qquad
\frac{\sin(\sin x)}{x}
=
\frac{\sin(\sin x)}{\sin x}
\frac{\sin x}{x}
\to1.
$$
Thus the product tends to $e$.

:::

:::

::: {.pf-step #s1-18}

Hence the improper integral near $0$ is ordinary convergent.


::: pf-proof

Step [](#s1-17){.pf-ref} shows the singularity at $0$ is removable.

:::

:::

::: {.pf-step #s1-19}

Letting first $R\to\infty$ and then $\varepsilon\downarrow0$,
$$
2i
\int_0^\infty
e^{\cos x}\sin(\sin x)\frac{dx}{x}
-i\pi(e-1)
=
0.
$$


::: pf-proof

The contour integral is zero by step [](#s1-3){.pf-ref}. The large arc tends to zero by step [](#s1-10){.pf-ref}. The small arc tends to
$$
-i\pi(e-1)
$$
by step [](#s1-12){.pf-ref}. The two real segments combine as in step [](#s1-16){.pf-ref}, and step [](#s1-18){.pf-ref} permits passage to the limit $\varepsilon\downarrow0$.

:::

:::

::: {.pf-step #s1-20}

Therefore
$$
2i
\int_0^\infty
e^{\cos x}\sin(\sin x)\frac{dx}{x}
=
i\pi(e-1).
$$


::: pf-proof

Rearrange step [](#s1-19){.pf-ref}.

:::

:::

::: {.pf-step #s1-21}

Dividing by $2i$,
$$
\boxed{
\int_0^\infty
e^{\cos x}\sin(\sin x)\frac{dx}{x}
=
\frac{\pi}{2}(e-1)}.
$$


::: pf-proof

This is immediate from step [](#s1-20){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-21){.pf-ref} is the required identity.

:::

:::

:::
