---
schema: qual/card@1
id: P-PZO5Y
kind: problem
title: Newtonian and Cauchy potentials of a compactly supported measure
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 6 of the UCLA Analysis Qualifying Exam, Spring 2010, from the collection provenance PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Reworked the earlier proof to make the quantifier in part (b) simultaneous for every compact subset of almost every line, using a countable exhaustion by squares. In part (c), justified the exchange of the boundary and measure integrals by absolute integrability of the kernel over the boundary-product space before applying the winding-number formula.
---

::: {.problem}
Let $\mu$ be a finite, positive, regular Borel measure supported on a compact subset of $\mathbb{C}$ and define the Newtonian potential $$U_\mu(z) = \int_\mathbb{C} \left|\frac{1}{z-w}\right| d\mu(w).$$

a. Prove that $U_\mu$ exists at Lebesgue almost all $z\in\mathbb{C}$ and that $$\iint_K U_\mu(z)\,dx\,dy < \infty$$ for every compact $K\subseteq\mathbb{C}$.

b. Prove that for almost every horizontal or vertical line $L\subseteq\mathbb{C}$, $\mu(L)=0$ and $\int_K U_\mu(z)\,ds < \infty$ for every compact subset $K\subseteq L$, where $ds$ denotes Lebesgue linear measure on $L$.

c. Define the Cauchy potential of $\mu$ to be $$S_\mu(z) = \int_\mathbb{C} \frac{1}{z-w}\,d\mu(w).$$ Let $R$ be a rectangle in $\mathbb{C}$ whose four sides are contained in lines $L$ having the conclusions of (b). Prove that $$\frac{1}{2\pi i}\int_{\partial R} S_\mu(z)\,dz = \mu(R).$$
:::

::: {.solution}
Let $dA=dx\,dy$ denote planar Lebesgue measure.

<1>1. For every compact $K\subseteq\mathbb C$,
\[
\int_K U_\mu(z)\,dA(z)<\infty.
\]
::: {.proof}
Because both $K$ and $\operatorname{supp}\mu$ are compact, choose $R>0$ such that
\[
K\cup\operatorname{supp}\mu\subseteq B(0,R).
\]
For every $w\in\operatorname{supp}\mu$ and every $z\in K$,
\[
|z-w|\le |z|+|w|<2R,
\]
so
\[
K\subseteq B(w,2R).
\]
Consequently, using polar coordinates centered at $w$,
\[
\begin{aligned}
\int_K\frac{dA(z)}{|z-w|}
&\le
\int_{B(w,2R)}\frac{dA(z)}{|z-w|}\\
&=\int_0^{2R}\int_0^{2\pi}\frac1r\,r\,d\theta\,dr\\
&=4\pi R.
\end{aligned}
\]
The integrand $(z,w)\mapsto |z-w|^{-1}$ is nonnegative and measurable, so Tonelli's theorem gives
\[
\begin{aligned}
\int_K U_\mu(z)\,dA(z)
&=
\int_K\int_{\mathbb C}\frac1{|z-w|}\,d\mu(w)\,dA(z)\\
&=
\int_{\operatorname{supp}\mu}
\left(\int_K\frac{dA(z)}{|z-w|}\right)d\mu(w)\\
&\le 4\pi R\,\mu(\mathbb C)<\infty.
\end{aligned}
\]
:::

<1>2. The potential $U_\mu(z)$ is finite for Lebesgue-almost every $z\in\mathbb C$.
::: {.proof}
For every $N\ge1$, apply <1>1 to the compact square
\[
Q_N=[-N,N]+i[-N,N].
\]
Since $U_\mu\ge0$ and
\[
\int_{Q_N}U_\mu\,dA<\infty,
\]
the function $U_\mu$ is finite almost everywhere on $Q_N$.
Because
\[
\mathbb C=\bigcup_{N=1}^{\infty}Q_N,
\]
the union of the corresponding exceptional null sets is still null.
This proves part (a).
:::

For $y\in\mathbb R$, write
\[
L_y^h=\{x+iy:x\in\mathbb R\},
\]
and for $x\in\mathbb R$ write
\[
L_x^v=\{x+iy:y\in\mathbb R\}.
\]

<1>3. Only countably many horizontal lines have positive $\mu$-measure, and only countably many vertical lines have positive $\mu$-measure.
::: {.proof}
For $m\ge1$, let
\[
H_m=\left\{y\in\mathbb R:\mu(L_y^h)\ge\frac1m\right\}.
\]
Distinct horizontal lines are disjoint.
If $H_m$ contained more than $m\mu(\mathbb C)$ elements, a sufficiently large finite subfamily would have total measure greater than $\mu(\mathbb C)$, which is impossible.
Thus each $H_m$ is finite.
If $\mu(L_y^h)>0$, then $y\in H_m$ for some $m$, so
\[
\{y:\mu(L_y^h)>0\}=\bigcup_{m=1}^{\infty}H_m
\]
is countable.
The same argument applies to vertical lines.
:::

<1>4. For almost every horizontal line $L$, one has $\mu(L)=0$ and
\[
\int_K U_\mu\,ds<\infty
\]
for every compact $K\subseteq L$.
::: {.proof}
Fix $N\ge1$.
By <1>1,
\[
\int_{Q_N}U_\mu(x+iy)\,dx\,dy<\infty.
\]
Tonelli's theorem therefore gives
\[
\int_{-N}^{N}
\left(
\int_{-N}^{N}U_\mu(x+iy)\,dx
\right)dy<\infty.
\]
Hence there is a null set $E_N^h\subseteq[-N,N]$ such that
\[
\int_{-N}^{N}U_\mu(x+iy)\,dx<\infty
\qquad
(y\in[-N,N]\setminus E_N^h).
\]
Let
\[
E^h=
\left(\bigcup_{N=1}^{\infty}E_N^h\right)
\cup
\{y:\mu(L_y^h)>0\}.
\]
By <1>3, $E^h$ has Lebesgue measure zero.

Take $y\notin E^h$ and a compact set $K\subseteq L_y^h$.
For sufficiently large $N$, one has $|y|\le N$ and
\[
K\subseteq [-N,N]+iy.
\]
Therefore
\[
\int_KU_\mu\,ds
\le
\int_{-N}^{N}U_\mu(x+iy)\,dx
<\infty,
\]
and, by the definition of $E^h$,
\[
\mu(L_y^h)=0.
\]
Thus every horizontal line outside a null family has both required properties.
:::

<1>5. The analogous conclusion holds for almost every vertical line.
::: {.proof}
Repeat <1>4 with the order of the $x$- and $y$-integrations reversed.
For each $N$, Tonelli gives a null set $E_N^v$ outside which
\[
\int_{-N}^{N}U_\mu(x+iy)\,dy<\infty.
\]
Intersecting the resulting countably many full-measure parameter sets and removing the countable family of vertical lines with positive $\mu$-measure from <1>3 proves the claim.
This completes part (b).
:::

Now let $R$ be a rectangle whose four sides lie on lines having the conclusions of part (b), and orient $\partial R$ positively.

<1>6. One has
\[
\mu(\partial R)=0
\qquad\text{and}\qquad
\int_{\partial R}U_\mu(z)\,ds<\infty.
\]
::: {.proof}
Each side of $R$ is contained in one of the four good horizontal or vertical lines.
Each such line has $\mu$-measure zero, so the finite union $\partial R$ also has $\mu$-measure zero.
Each side is compact, and part (b) gives finite line integral of $U_\mu$ over that side.
Summing over the four sides gives the second assertion.
:::

<1>7. The boundary integral of $S_\mu$ is absolutely convergent, and one may interchange the boundary integral with the $\mu$-integral:
\[
\int_{\partial R}S_\mu(z)\,dz
=
\int_{\mathbb C}
\left(
\int_{\partial R}\frac{dz}{z-w}
\right)d\mu(w).
\]
::: {.proof}
By Tonelli's theorem and <1>6,
\[
\begin{aligned}
\int_{\mathbb C}
\left(
\int_{\partial R}\frac{ds(z)}{|z-w|}
\right)d\mu(w)
&=
\int_{\partial R}
\left(
\int_{\mathbb C}\frac{d\mu(w)}{|z-w|}
\right)ds(z)\\
&=
\int_{\partial R}U_\mu(z)\,ds(z)\\
&<\infty.
\end{aligned}
\]
Thus the kernel $(z,w)\mapsto(z-w)^{-1}$ is absolutely integrable on the product of $\partial R$ with $(\mathbb C,\mu)$, where the boundary is parametrized side by side by arclength.
Fubini's theorem therefore permits exchanging the two integrals.
It also shows that $S_\mu(z)$ exists for arclength-almost every $z\in\partial R$ and
\[
|S_\mu(z)|\le U_\mu(z),
\]
so its contour integral is absolutely convergent.
:::

<1>8. For every $w\notin\partial R$,
\[
\frac1{2\pi i}
\int_{\partial R}\frac{dz}{z-w}
=
\begin{cases}
1,&w\in R^\circ,\\
0,&w\notin R.
\end{cases}
\]
::: {.proof}
This is the winding-number form of Cauchy's integral theorem: the positively oriented boundary of a rectangle has winding number $1$ about every point of its interior and $0$ about every point outside the rectangle.
:::

<1>9. Therefore
\[
\frac1{2\pi i}\int_{\partial R}S_\mu(z)\,dz=\mu(R).
\]
::: {.proof}
By <1>7 and <1>8, and because <1>6 gives $\mu(\partial R)=0$,
\[
\begin{aligned}
\frac1{2\pi i}\int_{\partial R}S_\mu(z)\,dz
&=
\int_{\mathbb C}
\left(
\frac1{2\pi i}\int_{\partial R}\frac{dz}{z-w}
\right)d\mu(w)\\
&=\int_{\mathbb C}\mathbf 1_{R^\circ}(w)\,d\mu(w)\\
&=\mu(R^\circ)\\
&=\mu(R).
\end{aligned}
\]
The last equality again uses $\mu(\partial R)=0$.
This proves part (c).
:::
:::
