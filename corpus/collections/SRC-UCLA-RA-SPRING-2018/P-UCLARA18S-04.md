---
schema: qual/card@1
id: P-UCLARA18S-04
kind: problem
title: Strong maximal function and differentiation along parabolic rectangles
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 4.

(a) Fix $1<p<\infty$. Show that
\[
f\mapsto [Mf](x,y)
=\sup_{r>0,\rho>0}\frac1{4r\rho}
\int_{-r}^{r}\int_{-\rho}^{\rho} f(x+h,y+\ell)\,dh\,d\ell
\]
is bounded on $L^p(\RR^2)$.

(b) Show that
\[
[A_rf](x,y)=\frac1{4r^3}
\int_{-r}^{r}\int_{-r^2}^{r^2}f(x+h,y+\ell)\,dh\,d\ell
\]
converges to $f$ almost everywhere in the plane as $r\to0$.
:::

::: {.solution}

Let \(M_1\) denote the centered one-dimensional Hardy--Littlewood maximal
operator:
\[
[M_1g](x)
=
\sup_{r>0}
\frac1{2r}
\int_{-r}^{r}|g(x+h)|\,dh.
\]

::: pf

::: {.pf-step #s1-1}

For every locally integrable \(f\),
\[
|Mf(x,y)|
\le
M_1^x\!\left(M_1^y|f|\right)(x,y),
\]
where \(M_1^x\) and \(M_1^y\) apply the one-dimensional maximal operator in
the indicated variable.


::: pf-proof

For fixed \(r,\rho>0\),
\[
\begin{aligned}
\left|
\frac1{4r\rho}
\int_{-r}^{r}\int_{-\rho}^{\rho}
f(x+h,y+\ell)\,d\ell\,dh
\right|
&\le
\frac1{2r}
\int_{-r}^{r}
\left[
\frac1{2\rho}
\int_{-\rho}^{\rho}
|f(x+h,y+\ell)|\,d\ell
\right]dh\\
&\le
\frac1{2r}
\int_{-r}^{r}
M_1^y|f|(x+h,y)\,dh\\
&\le
M_1^x(M_1^y|f|)(x,y).
\end{aligned}
\]
Taking the supremum over \(r,\rho\) gives the claim.

:::

:::

::: {.pf-step #s1-2}

For \(1<p<\infty\),
\[
\|M_1^y|f|\|_{L^p(\RR^2)}
\le
C_p\|f\|_{L^p(\RR^2)}.
\]


::: pf-proof

For almost every fixed \(x\), the section
\[
y\longmapsto f(x,y)
\]
belongs to \(L^p(\RR)\) by Fubini--Tonelli. The one-dimensional
Hardy--Littlewood maximal theorem gives
\[
\int_{\RR}
|M_1^y|f|(x,y)|^p\,dy
\le
C_p^p
\int_{\RR}|f(x,y)|^p\,dy.
\]
Integrating in \(x\) yields the stated estimate.

:::

:::

::: {.pf-step #s1-3}

One also has
\[
\|M_1^x(M_1^y|f|)\|_{L^p(\RR^2)}
\le
C_p^2\|f\|_{L^p(\RR^2)}.
\]


::: pf-proof

Apply the same one-dimensional maximal theorem in the \(x\)-variable to the
function
\[
g(x,y)=M_1^y|f|(x,y).
\]
Step [](#s1-2){.pf-ref} guarantees \(g\in L^p(\RR^2)\). Thus
\[
\|M_1^x g\|_p
\le
C_p\|g\|_p
\le
C_p^2\|f\|_p.
\]

:::

:::

::: {.pf-step #s1-4}

Therefore the strong maximal operator in part (a) is bounded on
\(L^p(\RR^2)\):
\[
\boxed{
\|Mf\|_{L^p(\RR^2)}
\le
C_p^2\|f\|_{L^p(\RR^2)}}.
\]


::: pf-proof

Combine the pointwise domination in step [](#s1-1){.pf-ref} with step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For \(r>0\), define the averaging-error operator
\[
T_rf(x,y)
=
\frac1{4r^3}
\int_{-r}^{r}\int_{-r^2}^{r^2}
|f(x+h,y+\ell)-f(x,y)|\,d\ell\,dh
\]
and
\[
Tf(x,y)=\limsup_{r\to0}T_rf(x,y).
\]
Then
\[
|A_rf(x,y)-f(x,y)|
\le
T_rf(x,y).
\]


::: pf-proof

Subtract \(f(x,y)\) from the average defining \(A_rf(x,y)\), move it inside
the integral, and apply the triangle inequality.

:::

:::

::: {.pf-step #s1-6}

If \(g\in C_c(\RR^2)\), then
\[
\boxed{Tg=0\quad\text{everywhere}}.
\]


::: pf-proof

Every compactly supported continuous function on \(\RR^2\) is uniformly
continuous. Given \(\varepsilon>0\), choose \(\delta>0\) such that
\[
|g(x+h,y+\ell)-g(x,y)|<\varepsilon
\]
whenever
\[
\sqrt{h^2+\ell^2}<\delta.
\]
For all sufficiently small \(r\), every point in
\[
[-r,r]\times[-r^2,r^2]
\]
satisfies this bound. Hence
\[
T_rg(x,y)\le\varepsilon
\]
for all \((x,y)\), and \(Tg=0\).

:::

:::

::: {.pf-step #s1-7}

For every \(u\in L^p(\RR^2)\),
\[
\boxed{
Tu(x,y)
\le
|u(x,y)|+M|u|(x,y)}
\]
almost everywhere.


::: pf-proof

For every \(r>0\),
\[
\begin{aligned}
T_ru(x,y)
&\le
\frac1{4r^3}
\int_{-r}^{r}\int_{-r^2}^{r^2}
\bigl(
|u(x+h,y+\ell)|
+
|u(x,y)|
\bigr)\,d\ell\,dh\\
&=
|u(x,y)|
+
\frac1{4r\cdot r^2}
\int_{-r}^{r}\int_{-r^2}^{r^2}
|u(x+h,y+\ell)|\,d\ell\,dh\\
&\le
|u(x,y)|+M|u|(x,y).
\end{aligned}
\]
Take \(\limsup_{r\to0}\).

:::

:::

::: {.pf-step #s1-8}

Fix \(\alpha>0\). For every \(u\in L^p(\RR^2)\),
\[
\left|\{Tu\ge\alpha\}\right|
\le
\frac{2^p}{\alpha^p}
\left(
\|u\|_p^p+\|M|u|\|_p^p
\right).
\]


::: pf-proof

By step [](#s1-7){.pf-ref},
\[
\{Tu\ge\alpha\}
\subseteq
\{|u|\ge\alpha/2\}
\cup
\{M|u|\ge\alpha/2\}.
\]
Apply Chebyshev's inequality to each set and add the resulting bounds.

:::

:::

::: {.pf-step #s1-9}

There is a constant \(C_{p,\alpha}\) such that
\[
\boxed{
\left|\{Tu\ge\alpha\}\right|
\le
C_{p,\alpha}\|u\|_p^p}.
\]


::: pf-proof

By part (a),
\[
\|M|u|\|_p
\le
C_p^2\|u\|_p.
\]
Insert this into step [](#s1-8){.pf-ref}:
\[
\left|\{Tu\ge\alpha\}\right|
\le
\frac{2^p}{\alpha^p}
\left(
1+C_p^{2p}
\right)\|u\|_p^p.
\]

:::

:::

::: {.pf-step #s1-10}

Let \(f\in L^p(\RR^2)\). For every \(\varepsilon>0\), choose
\[
g\in C_c(\RR^2)
\]
such that
\[
\|f-g\|_p<\varepsilon,
\]
and set
\[
u=f-g.
\]
Then
\[
Tf\le Tu
\]
almost everywhere.


::: pf-proof

The operators \(T_r\) are subadditive:
\[
T_r(f)
\le
T_r(g)+T_r(u).
\]
Taking limsups gives
\[
Tf\le Tg+Tu.
\]
Step [](#s1-6){.pf-ref} gives \(Tg=0\).

:::

:::

::: {.pf-step #s1-11}

For every \(\alpha>0\),
\[
\left|\{Tf\ge\alpha\}\right|
=0.
\]


::: pf-proof

By step [](#s1-10){.pf-ref},
\[
\{Tf\ge\alpha\}
\subseteq
\{Tu\ge\alpha\}.
\]
Hence step [](#s1-9){.pf-ref} gives
\[
\left|\{Tf\ge\alpha\}\right|
\le
C_{p,\alpha}\|u\|_p^p
<
C_{p,\alpha}\varepsilon^p.
\]
The left-hand side is independent of \(\varepsilon\). Let
\[
\varepsilon\downarrow0.
\]

:::

:::

::: {.pf-step #s1-12}

Therefore
\[
\boxed{Tf=0\quad\text{almost everywhere}}.
\]


::: pf-proof

Apply step [](#s1-11){.pf-ref} with
\[
\alpha=\frac1m,
\qquad
m=1,2,\dots.
\]
Then
\[
\{Tf>0\}
=
\bigcup_{m=1}^{\infty}
\left\{
Tf\ge\frac1m
\right\}
\]
is a countable union of null sets.

:::

:::

::: {.pf-step #s1-13}

Consequently,
\[
\boxed{
A_rf(x,y)\longrightarrow f(x,y)
\quad\text{for almost every }(x,y)}
\]
as \(r\to0\).


::: pf-proof

By step [](#s1-5){.pf-ref},
\[
\limsup_{r\to0}
|A_rf(x,y)-f(x,y)|
\le
Tf(x,y).
\]
Step [](#s1-12){.pf-ref} makes the right-hand side zero almost everywhere, forcing the
desired convergence.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-13){.pf-ref} proves part (b).

:::

:::

:::
