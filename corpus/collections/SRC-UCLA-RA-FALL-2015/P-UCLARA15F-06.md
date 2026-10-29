---
schema: qual/card@1
id: P-UCLARA15F-06
kind: problem
title: Difference-quotient characterization of $H^{1/2}(\RR^d)$
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 6 on pages 1-2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $u \in L^2(\RR^d)$ and let us say that $u \in H^{1/2}(\RR^d)$ (a Sobolev space) if
\[
\left( 1 + |\xi|^{1/2} \right) \hat{u}(\xi) \in L^2(\RR^d).
\]
Here $\hat{u}$ is the Fourier transform of $u$. Show that $u \in H^{1/2}(\RR^d)$ if and only if
\[
\iint \frac{|u(x+y) - u(x)|^2}{|y|^{d+1}}\,dx\,dy < \infty.
\]
:::

::: {.solution}

Let
\[
[u]_{1/2}^2
=
\iint_{\RR^d\times\RR^d}
\frac{|u(x+y)-u(x)|^2}{|y|^{d+1}}
\,dx\,dy.
\]

Since \(u\in L^2(\RR^d)\), Plancherel's theorem applies.

::: pf

::: {.pf-step #s1-1}

For fixed \(y\in\RR^d\), the Fourier transform of
\[
x\longmapsto u(x+y)-u(x)
\]
is
\[
\boxed{
\left(
e^{i\xi\cdot y}-1
\right)\widehat u(\xi)}
\]
up to the harmless sign convention in the Fourier transform.


::: pf-proof

Translation by \(y\) multiplies the Fourier transform by
\[
e^{i\xi\cdot y}
\]
under the chosen convention. Subtract the transform of \(u(x)\).

:::

:::

::: {.pf-step #s1-2}

Hence, by Plancherel,
\[
\boxed{
\int_{\RR^d}
|u(x+y)-u(x)|^2\,dx
=
\int_{\RR^d}
|e^{i\xi\cdot y}-1|^2
|\widehat u(\xi)|^2\,d\xi}.
\]


::: pf-proof

Apply Plancherel to the difference from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

Therefore
\[
[u]_{1/2}^2
=
\int_{\RR^d}
\int_{\RR^d}
\frac{
|e^{i\xi\cdot y}-1|^2
}{
|y|^{d+1}
}
|\widehat u(\xi)|^2
\,d\xi\,dy.
\]


::: pf-proof

Insert step [](#s1-2){.pf-ref} into the definition of \([u]_{1/2}^2\).

:::

:::

::: {.pf-step #s1-4}

Tonelli's theorem permits interchange of the two integrals:
\[
\boxed{
[u]_{1/2}^2
=
\int_{\RR^d}
|\widehat u(\xi)|^2
\left[
\int_{\RR^d}
\frac{
|e^{i\xi\cdot y}-1|^2
}{
|y|^{d+1}
}
\,dy
\right]
d\xi}.
\]


::: pf-proof

The integrand is nonnegative.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\boxed{I(0)=0}.
\]


::: pf-proof

If \(\xi=0\), then
\[
e^{i\xi\cdot y}-1=0
\]
for every \(y\).

:::

:::

::: pf-step

By rotational invariance,
\[
I(\xi)
=
I(|\xi|e_1),
\]
where \(e_1=(1,0,\dots,0)\).


::: pf-proof

Choose an orthogonal map \(R\) with
\[
R\xi=|\xi|e_1.
\]
In the integral defining \(I(\xi)\), make the change of variables
\[
y=R^{-1}z.
\]
Orthogonal maps preserve Lebesgue measure and Euclidean norm, and
\[
\xi\cdot R^{-1}z
=
(R\xi)\cdot z
=
|\xi|z_1.
\]

:::

:::

::: {.pf-step #s1-7}

Make the scaling change of variables
\[
z=\frac{w}{|\xi|}.
\]
Then
\[
\boxed{
I(\xi)
=
|\xi|
\int_{\RR^d}
\frac{
|e^{iw_1}-1|^2
}{
|w|^{d+1}
}
\,dw}.
\]


::: pf-proof

Under
\[
z=w/|\xi|,
\]
one has
\[
dz=|\xi|^{-d}dw,
\]
\[
|z|^{-(d+1)}
=
|\xi|^{d+1}|w|^{-(d+1)},
\]
and
\[
e^{i|\xi|z_1}
=
e^{iw_1}.
\]
Multiplying the scaling factors gives one remaining factor \(|\xi|\).

:::

:::

::: {.pf-step #s1-8}

Define
\[
\boxed{
C_d
=
\int_{\RR^d}
\frac{
|e^{iw_1}-1|^2
}{
|w|^{d+1}
}
\,dw}.
\]


::: pf-proof

This is the dimension-dependent constant appearing in step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The constant \(C_d\) is finite.


::: pf-proof

Split the integral into
\[
|w|\le1
\qquad\text{and}\qquad
|w|>1.
\]

For \(|w|\le1\),
\[
|e^{iw_1}-1|
\le
|w_1|
\le
|w|,
\]
so
\[
\frac{|e^{iw_1}-1|^2}{|w|^{d+1}}
\le
|w|^{1-d}.
\]
In polar coordinates,
\[
\int_{|w|\le1}|w|^{1-d}\,dw
=
C
\int_0^1 r^{1-d}r^{d-1}\,dr
=
C
\int_0^1dr
<
\infty.
\]

For \(|w|>1\),
\[
|e^{iw_1}-1|\le2,
\]
so
\[
\frac{|e^{iw_1}-1|^2}{|w|^{d+1}}
\le
4|w|^{-d-1}.
\]
Again in polar coordinates,
\[
\int_{|w|>1}|w|^{-d-1}\,dw
=
C
\int_1^\infty r^{-2}\,dr
<
\infty.
\]

:::

:::

::: {.pf-step #s1-10}

The constant \(C_d\) is strictly positive.


::: pf-proof

The integrand is nonnegative and is positive on any set where
\[
w_1\notin2\pi\ZZ.
\]
Such a set has positive Lebesgue measure.

:::

:::

::: {.pf-step #s1-11}

Therefore, for every \(\xi\in\RR^d\),
\[
\boxed{
I(\xi)=C_d|\xi|}.
\]


::: pf-proof

For \(\xi\ne0\), combine steps [](#s1-7){.pf-ref} through [](#s1-10){.pf-ref}. For \(\xi=0\), both sides are zero by step [](#s1-5){.pf-ref}.

:::

:::

::: pf-step

Substituting step [](#s1-11){.pf-ref} into step [](#s1-4){.pf-ref} gives
\[
\boxed{
[u]_{1/2}^2
=
C_d
\int_{\RR^d}
|\xi|
\,|\widehat u(\xi)|^2
\,d\xi}.
\]


::: pf-proof

Replace the inner \(y\)-integral in step [](#s1-4){.pf-ref} by \(C_d|\xi|\).

:::

:::

::: {.pf-step #s1-13}

Since \(C_d\in(0,\infty)\),
\[
\boxed{
[u]_{1/2}<\infty
\iff
\int_{\RR^d}
|\xi|
\,|\widehat u(\xi)|^2
\,d\xi
<
\infty}.
\]


::: pf-proof

Multiplication by a fixed finite positive constant does not affect finiteness.

:::

:::

::: {.pf-step #s1-14}

Since \(u\in L^2(\RR^d)\),
\[
\boxed{
\widehat u\in L^2(\RR^d)}.
\]


::: pf-proof

Apply Plancherel's theorem.

:::

:::

::: {.pf-step #s1-15}

One has the pointwise comparability
\[
\boxed{
(1+|\xi|^{1/2})^2
\asymp
1+|\xi|}.
\]


::: pf-proof

For \(t\ge0\),
\[
(1+\sqrt t)^2
=
1+2\sqrt t+t.
\]
Also,
\[
2\sqrt t
\le
1+t
\]
by
\[
(\sqrt t-1)^2\ge0.
\]
Hence
\[
1+t
\le
(1+\sqrt t)^2
\le
2(1+t).
\]
Set \(t=|\xi|\).

:::

:::

::: {.pf-step #s1-16}

Therefore
\[
(1+|\xi|^{1/2})\widehat u(\xi)\in L^2
\]
if and only if
\[
\int_{\RR^d}
(1+|\xi|)
|\widehat u(\xi)|^2\,d\xi
<
\infty.
\]


::: pf-proof

Square the \(L^2\)-norm and use the two-sided comparison from step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

By step [](#s1-14){.pf-ref}, the condition in step [](#s1-16){.pf-ref} is equivalent to
\[
\boxed{
\int_{\RR^d}
|\xi|
|\widehat u(\xi)|^2\,d\xi
<
\infty}.
\]


::: pf-proof

The term
\[
\int|\widehat u(\xi)|^2\,d\xi
\]
is already finite because \(u\in L^2\).

:::

:::

::: {.pf-step #s1-18}

Combining steps [](#s1-13){.pf-ref} and [](#s1-17){.pf-ref},
\[
\boxed{
u\in H^{1/2}(\RR^d)
\iff
\iint_{\RR^d\times\RR^d}
\frac{|u(x+y)-u(x)|^2}{|y|^{d+1}}
\,dx\,dy
<
\infty}.
\]


::: pf-proof

Both conditions are equivalent to finiteness of
\[
\int|\xi||\widehat u(\xi)|^2\,d\xi.
\]

:::

:::

::: pf-qed

Step [](#s1-18){.pf-ref} is the required equivalence.

:::

:::

:::
