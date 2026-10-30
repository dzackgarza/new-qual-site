---
schema: qual/card@1
id: P-UCLARA18S-04
kind: problem
title: Strong maximal function and differentiation along parabolic rectangles
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - Differentiation
  - Lp Spaces
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
$$
f\mapsto [Mf](x,y)
=\sup_{r>0,\rho>0}\frac1{4r\rho}
\int_{-r}^{r}\int_{-\rho}^{\rho} f(x+h,y+\ell)\,dh\,d\ell
$$
is bounded on $L^p(\RR^2)$.

(b) Show that
$$
[A_rf](x,y)=\frac1{4r^3}
\int_{-r}^{r}\int_{-r^2}^{r^2}f(x+h,y+\ell)\,dh\,d\ell
$$
converges to $f$ almost everywhere in the plane as $r\to0$.
:::

::: {.solution}

Let $M_1$ denote the centered one-dimensional Hardy--Littlewood maximal
operator:
$$
[M_1g](x)
=
\sup_{r>0}
\frac1{2r}
\int_{-r}^{r}\abs{g(x+h)}\,dh.
$$

::: pf

::: {.pf-step #s1-1}

For every locally integrable $f$,
$$
\abs{Mf(x,y)}
\le
M_1^x\!\left(M_1^y\abs{f}\right)(x,y),
$$
where $M_1^x$ and $M_1^y$ apply the one-dimensional maximal operator in
the indicated variable.


::: pf-proof

For fixed $r,\rho>0$,
$$
\begin{aligned}
\abs{
\frac1{4r\rho}
\int_{-r}^{r}\int_{-\rho}^{\rho}
f(x+h,y+\ell)\,d\ell\,dh
}
&\le
\frac1{2r}
\int_{-r}^{r}
\left[
\frac1{2\rho}
\int_{-\rho}^{\rho}
\abs{f(x+h,y+\ell)}\,d\ell
\right]dh\\
&\le
\frac1{2r}
\int_{-r}^{r}
M_1^y\abs{f}(x+h,y)\,dh\\
&\le
M_1^x(M_1^y\abs{f})(x,y).
\end{aligned}
$$
Taking the supremum over $r,\rho$ gives the claim.

:::

:::

::: {.pf-step #s1-2}

For $1<p<\infty$,
$$
\norm{M_1^y\abs{f}}_{L^p(\RR^2)}
\le
C_p\norm{f}_{L^p(\RR^2)}.
$$


::: pf-proof

For almost every fixed $x$, the section
$$
y\longmapsto f(x,y)
$$
belongs to $L^p(\RR)$ by Fubini--Tonelli. The one-dimensional
Hardy--Littlewood maximal theorem gives
$$
\int_{\RR}
\abs{M_1^y\abs{f}(x,y)}^p\,dy
\le
C_p^p
\int_{\RR}\abs{f(x,y)}^p\,dy.
$$
Integrating in $x$ yields the stated estimate.

:::

:::

::: {.pf-step #s1-3}

One also has
$$
\norm{M_1^x(M_1^y\abs{f})}_{L^p(\RR^2)}
\le
C_p^2\norm{f}_{L^p(\RR^2)}.
$$


::: pf-proof

Apply the same one-dimensional maximal theorem in the $x$-variable to the
function
$$
g(x,y)=M_1^y\abs{f}(x,y).
$$
Step [](#s1-2){.pf-ref} guarantees $g\in L^p(\RR^2)$. Thus
$$
\norm{M_1^x g}_p
\le
C_p\norm{g}_p
\le
C_p^2\norm{f}_p.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the strong maximal operator in part (a) is bounded on
$L^p(\RR^2)$:
$$
\boxed{
\norm{Mf}_{L^p(\RR^2)}
\le
C_p^2\norm{f}_{L^p(\RR^2)}}.
$$


::: pf-proof

Combine the pointwise domination in step [](#s1-1){.pf-ref} with step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For $r>0$, define the averaging-error operator
$$
T_rf(x,y)
=
\frac1{4r^3}
\int_{-r}^{r}\int_{-r^2}^{r^2}
\abs{f(x+h,y+\ell)-f(x,y)}\,d\ell\,dh
$$
and
$$
Tf(x,y)=\limsup_{r\to0}T_rf(x,y).
$$
Then
$$
\abs{A_rf(x,y)-f(x,y)}
\le
T_rf(x,y).
$$


::: pf-proof

Subtract $f(x,y)$ from the average defining $A_rf(x,y)$, move it inside
the integral, and apply the triangle inequality.

:::

:::

::: {.pf-step #s1-6}

If $g\in C_c(\RR^2)$, then
$$
\boxed{Tg=0\quad\text{everywhere}}.
$$


::: pf-proof

Every compactly supported continuous function on $\RR^2$ is uniformly
continuous. Given $\varepsilon>0$, choose $\delta>0$ such that
$$
\abs{g(x+h,y+\ell)-g(x,y)}<\varepsilon
$$
whenever
$$
\sqrt{h^2+\ell^2}<\delta.
$$
For all sufficiently small $r$, every point in
$$
[-r,r]\times[-r^2,r^2]
$$
satisfies this bound. Hence
$$
T_rg(x,y)\le\varepsilon
$$
for all $(x,y)$, and $Tg=0$.

:::

:::

::: {.pf-step #s1-7}

For every $u\in L^p(\RR^2)$,
$$
\boxed{
Tu(x,y)
\le
\abs{u(x,y)}+M\abs{u}(x,y)}
$$
almost everywhere.


::: pf-proof

For every $r>0$,
$$
\begin{aligned}
T_ru(x,y)
&\le
\frac1{4r^3}
\int_{-r}^{r}\int_{-r^2}^{r^2}
\bigl(
\abs{u(x+h,y+\ell)}
+
\abs{u(x,y)}
\bigr)\,d\ell\,dh\\
&=
\abs{u(x,y)}
+
\frac1{4r\cdot r^2}
\int_{-r}^{r}\int_{-r^2}^{r^2}
\abs{u(x+h,y+\ell)}\,d\ell\,dh\\
&\le
\abs{u(x,y)}+M\abs{u}(x,y).
\end{aligned}
$$
Take $\limsup_{r\to0}$.

:::

:::

::: {.pf-step #s1-8}

Fix $\alpha>0$. For every $u\in L^p(\RR^2)$,
$$
\setmeasure{\{Tu\ge\alpha\}}
\le
\frac{2^p}{\alpha^p}
\left(
\norm{u}_p^p+\norm{M\abs{u}}_p^p
\right).
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
\{Tu\ge\alpha\}
\subseteq
\{\abs{u}\ge\alpha/2\}
\cup
\{M\abs{u}\ge\alpha/2\}.
$$
Apply Chebyshev's inequality to each set and add the resulting bounds.

:::

:::

::: {.pf-step #s1-9}

There is a constant $C_{p,\alpha}$ such that
$$
\boxed{
\setmeasure{\{Tu\ge\alpha\}}
\le
C_{p,\alpha}\norm{u}_p^p}.
$$


::: pf-proof

By part (a),
$$
\norm{M\abs{u}}_p
\le
C_p^2\norm{u}_p.
$$
Insert this into step [](#s1-8){.pf-ref}:
$$
\setmeasure{\{Tu\ge\alpha\}}
\le
\frac{2^p}{\alpha^p}
\left(
1+C_p^{2p}
\right)\norm{u}_p^p.
$$

:::

:::

::: {.pf-step #s1-10}

Let $f\in L^p(\RR^2)$. For every $\varepsilon>0$, choose
$$
g\in C_c(\RR^2)
$$
such that
$$
\norm{f-g}_p<\varepsilon,
$$
and set
$$
u=f-g.
$$
Then
$$
Tf\le Tu
$$
almost everywhere.


::: pf-proof

The operators $T_r$ are subadditive:
$$
T_r(f)
\le
T_r(g)+T_r(u).
$$
Taking limsups gives
$$
Tf\le Tg+Tu.
$$
Step [](#s1-6){.pf-ref} gives $Tg=0$.

:::

:::

::: {.pf-step #s1-11}

For every $\alpha>0$,
$$
\setmeasure{\{Tf\ge\alpha\}}
=0.
$$


::: pf-proof

By step [](#s1-10){.pf-ref},
$$
\{Tf\ge\alpha\}
\subseteq
\{Tu\ge\alpha\}.
$$
Hence step [](#s1-9){.pf-ref} gives
$$
\setmeasure{\{Tf\ge\alpha\}}
\le
C_{p,\alpha}\norm{u}_p^p
<
C_{p,\alpha}\varepsilon^p.
$$
The left-hand side is independent of $\varepsilon$. Let
$$
\varepsilon\downarrow0.
$$

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
\boxed{Tf=0\quad\text{almost everywhere}}.
$$


::: pf-proof

Apply step [](#s1-11){.pf-ref} with
$$
\alpha=\frac1m,
\qquad
m=1,2,\dots.
$$
Then
$$
\{Tf>0\}
=
\bigcup_{m=1}^{\infty}
\left\{
Tf\ge\frac1m
\right\}
$$
is a countable union of null sets.

:::

:::

::: {.pf-step #s1-13}

Consequently,
$$
\boxed{
A_rf(x,y)\longrightarrow f(x,y)
\quad\text{for almost every }(x,y)}
$$
as $r\to0$.


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
\limsup_{r\to0}
\abs{A_rf(x,y)-f(x,y)}
\le
Tf(x,y).
$$
Step [](#s1-12){.pf-ref} makes the right-hand side zero almost everywhere, forcing the
desired convergence.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-13){.pf-ref} proves part (b).

:::

:::

:::
