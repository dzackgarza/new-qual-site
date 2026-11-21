---
schema: qual/card@1
id: E-SS4.EX-4
kind: problem
title: The Fourier transform of $1/Q(x)$ in terms of the roots of $Q$
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 notation and exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The arc estimate, the
    residue at a simple root, the three cases of the sign of xi with the orientation
    of the reversed contour, and the multiplicity case are now separate steps. The
    exponent in the decay is written out in the variable z = x + iy so that which
    half-plane decays for which sign of xi is not asserted but computed, and the
    polynomial-in-xi statement for a higher-order pole is derived from the
    differentiation formula for the residue rather than named. Not checked: the
    book's own text of the exercise, which is not retained in this checkout; the
    statement is as transcribed on the card. No retained solution set covers the
    exercise (the collection's provenance is a Google Books record), so the argument
    is the card's own. No statement repair.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card carried two solution blocks: the answer, and a separate block holding only the provenance
    note that no retained solution set covers the exercise. Both rendered as solutions. The note was
    moved to the head of the single solution block; its wording and the answer were not changed.

---

::: {.exercise}
Suppose $Q$ is a polynomial of degree $\geq 2$ with distinct roots, none lying on the real axis.
   Calculate

$$
\int_ {- \infty} ^ {\infty} \frac {e ^ {- 2 \pi i x \xi}}{Q (x)} d x, \quad \xi \in \RR
$$

in terms of the roots of $Q$ . What happens when several roots coincide?
[Hint: Consider separately the cases $\xi < 0 , \xi = 0$ , and $\xi > 0$ . Use residues.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Let $Q$ be a polynomial of degree $d\ge2$ with distinct roots $\alpha_1,\dots,\alpha_d$, none real, and set
$$
I(\xi)=\int_{-\infty}^{\infty}\frac{e^{-2\pi ix\xi}}{Q(x)}\,dx,\qquad \xi\in\RR .
$$

::: pf

::: {.pf-step #decay}
For $z=x+iy$ one has $\abs{e^{-2\pi iz\xi}}=e^{2\pi y\xi}$, and $\abs{Q(z)}\ge c\abs{z}^d$ for $\abs{z}$ large, with $d\ge2$.

::: pf-proof
$e^{-2\pi iz\xi}=e^{-2\pi i(x+iy)\xi}=e^{-2\pi ix\xi}e^{2\pi y\xi}$ and $\abs{e^{-2\pi ix\xi}}=1$, since $x,\xi\in\RR$; so the modulus is $e^{2\pi y\xi}$. If $\xi<0$ this is $\le1$ in the closed upper half-plane $y\ge0$, and if $\xi>0$ it is $\le1$ in the closed lower half-plane.
For the polynomial: $Q(z)=c_dz^d\bigl(1+O(1/z)\bigr)$ as $\abs{z}\to\infty$ with $c_d\ne0$, so for $\abs{z}\ge R$ with $R$ large one has $\abs{Q(z)}\ge\tfrac{\abs{c_d}}{2}\abs{z}^d$, hence $\abs{1/Q(z)}\le\frac{2}{\abs{c_d}}\abs{z}^{-d}\le\frac{2}{\abs{c_d}}\abs{z}^{-2}$ because $d\ge2$ and $\abs{z}\ge1$; in particular $\abs{1/Q(z)}=O(\abs{z}^{-2})$.
:::

:::

::: {.pf-step #arc}
For every $\xi$, the integral of $e^{-2\pi iz\xi}/Q(z)$ over the semicircle of radius $R$ in the closed half-plane where $\abs{e^{-2\pi iz\xi}}\le1$ tends to $0$ as $R\to\infty$.

::: pf-proof
On that semicircle $\abs{e^{-2\pi iz\xi}}\le1$, so the integrand is bounded by $\abs{1/Q(z)}\le C R^{-2}$ for $R$ large by step [](#decay){.pf-ref}, and the semicircle has length $\pi R$; hence the modulus of the arc integral is at most $\pi C R^{-1}\to0$.
:::

:::

::: {.pf-step #simple}
At a simple root $\alpha_j$,
$$
\operatorname{Res}_{z=\alpha_j}\frac{e^{-2\pi iz\xi}}{Q(z)}=\frac{e^{-2\pi i\alpha_j\xi}}{Q'(\alpha_j)} .
$$

::: pf-proof
Write $Q(z)=(z-\alpha_j)Q_j(z)$ with $Q_j$ holomorphic near $\alpha_j$ and $Q_j(\alpha_j)=Q'(\alpha_j)\ne0$: the product rule at $\alpha_j$ gives $Q'(z)=Q_j(z)+(z-\alpha_j)Q_j'(z)$, so $Q'(\alpha_j)=Q_j(\alpha_j)$, and $Q'(\alpha_j)\ne0$ because the roots are distinct. Then $e^{-2\pi iz\xi}/Q(z)=\bigl(e^{-2\pi iz\xi}/Q_j(z)\bigr)/(z-\alpha_j)$ exhibits a simple pole with residue $e^{-2\pi i\alpha_j\xi}/Q_j(\alpha_j)$, which is the displayed value.
:::

:::

::: {.pf-step #negative}
For $\xi<0$,
$$
I(\xi)=2\pi i\sum_{\operatorname{Im}\alpha_j>0}\frac{e^{-2\pi i\alpha_j\xi}}{Q'(\alpha_j)} .
$$

::: pf-proof
For $\xi<0$ the exponential is bounded by $1$ in the closed upper half-plane by step [](#decay){.pf-ref}, and no root is real, so the closed contour given by $[-R,R]$ followed by the upper semicircle encloses exactly the roots with $\operatorname{Im}\alpha_j>0$ and no pole lies on it. The residue theorem gives $I_R(\xi)+(\text{upper arc})=2\pi i\sum_{\operatorname{Im}\alpha_j>0}\operatorname{Res}_{\alpha_j}$, the arc term tends to $0$ by step [](#arc){.pf-ref}, and the residues are those of step [](#simple){.pf-ref}; now let $R\to\infty$. The improper integral converges because $\abs{1/Q(x)}=O(\abs{x}^{-2})$ is absolutely integrable.
:::

:::

::: {.pf-step #positive}
For $\xi>0$,
$$
I(\xi)=-2\pi i\sum_{\operatorname{Im}\alpha_j<0}\frac{e^{-2\pi i\alpha_j\xi}}{Q'(\alpha_j)} .
$$

::: pf-proof
This time step [](#decay){.pf-ref} bounds the exponential by $1$ in the closed lower half-plane, so the contour is $[-R,R]$ followed by the lower semicircle, traversed clockwise; the residue theorem for a clockwise contour carries a minus sign, and the enclosed poles are the roots with $\operatorname{Im}\alpha_j<0$. The arc term vanishes by step [](#arc){.pf-ref}, the residues are again those of step [](#simple){.pf-ref}, and $R\to\infty$ gives the displayed formula.
:::

:::

::: {.pf-step #zero}
For $\xi=0$,
$$
I(0)=2\pi i\sum_{\operatorname{Im}\alpha_j>0}\frac{1}{Q'(\alpha_j)} .
$$

::: pf-proof
At $\xi=0$ the numerator is $1$ and either half-plane may be used; take the upper one. The integrand is $1/Q$, the contour is the closed upper contour of step [](#negative){.pf-ref} with $\xi=0$, the residue at $\alpha_j$ is $1/Q'(\alpha_j)$ for the same reason as in step [](#simple){.pf-ref}, and the arc term is the same vanishing one by step [](#arc){.pf-ref}. As $\deg Q\ge2$, $\abs{1/Q(x)}=O(\abs{x}^{-2})$ and the integral converges. (The value agrees with the lower half-plane computation because the sum of all residues of $1/Q$ is $0$ for $\deg Q\ge2$.)
:::

:::

::: {.pf-step #coincide}
If a root $\alpha$ has multiplicity $r\ge2$, the residue of $e^{-2\pi iz\xi}/Q(z)$ at $\alpha$ is $e^{-2\pi i\alpha\xi}P_\alpha(\xi)$ with $P_\alpha$ a polynomial of degree at most $r-1$; the formulas of steps [](#negative){.pf-ref} to [](#zero){.pf-ref} then hold with these residues in place of the simple ones.

::: pf-proof
Write $Q(z)=(z-\alpha)^rR(z)$ with $R$ holomorphic and nonzero near $\alpha$. Then $e^{-2\pi iz\xi}/Q(z)=G(z)/(z-\alpha)^r$ with $G(z)=e^{-2\pi iz\xi}/R(z)$ holomorphic near $\alpha$, and the residue at a pole of order $r$ is
$$
\operatorname{Res}_{z=\alpha}=\frac{1}{(r-1)!}\evaluated{\frac{d^{r-1}}{dz^{r-1}}G(z)}_{z=\alpha}.
$$
Each derivative of $G$ at $\alpha$ is a finite sum of terms $c\,(2\pi i\xi)^{s}e^{-2\pi i\alpha\xi}$ with $s\le r-1$, by the product rule and $\frac{d}{dz}e^{-2\pi iz\xi}=-2\pi i\xi\,e^{-2\pi iz\xi}$; so the residue is $e^{-2\pi i\alpha\xi}$ times a polynomial in $\xi$ of degree at most $r-1$. The contour arguments of steps [](#negative){.pf-ref} to [](#zero){.pf-ref} use only that the poles are off the real axis and the arc estimate, so they go through unchanged, with the residue theorem now summing these higher-order residues.
:::

:::

::: {.pf-step}
The integral is given by steps [](#negative){.pf-ref}, [](#positive){.pf-ref} and [](#zero){.pf-ref} according as $\xi<0$, $\xi>0$ or $\xi=0$, and by step [](#coincide){.pf-ref} when roots coincide.

::: pf-proof
The three cases of the sign of $\xi$ cover every $\xi\in\RR$, and each has its formula; the hypothesis $\deg Q\ge2$ was used exactly in the estimate $\abs{1/Q(z)}=O(\abs{z}^{-2})$ of step [](#decay){.pf-ref} that makes both the integral converge and the arc tend to $0$, and the hypothesis that no root is real was used to put no pole on the contour. If several roots coincide the formulas are replaced by finite sums $P_\alpha(\xi)e^{-2\pi i\alpha\xi}$ with $\deg P_\alpha<r$, as step [](#coincide){.pf-ref} shows.
:::

:::

:::

Let the distinct roots of $Q$ be $\alpha_1,\ldots,\alpha_m$, none real, and set
$$
I(\xi)=\int_{-\infty}^{\infty}\frac{e^{-2\pi i x\xi}}{Q(x)}\,dx.
$$
Because $\deg Q\ge2$, the semicircular arc contribution tends to $0$ in every case below.

If $\xi<0$, close in the upper half-plane, where the exponential decays. The residue theorem gives
$$
I(\xi)=2\pi i\sum_{\Im\alpha_j>0}
\frac{e^{-2\pi i\alpha_j\xi}}{Q'(\alpha_j)}.
\tag{1}
$$
If $\xi>0$, close in the lower half-plane. The contour is clockwise, hence
$$
I(\xi)=-2\pi i\sum_{\Im\alpha_j<0}
\frac{e^{-2\pi i\alpha_j\xi}}{Q'(\alpha_j)}.
\tag{2}
$$
For $\xi=0$ one may close in either half-plane; for example
$$
I(0)=2\pi i\sum_{\Im\alpha_j>0}\frac1{Q'(\alpha_j)}.
\tag{3}
$$

If roots coincide, the same contour argument holds but the poles are of higher order. A root $\alpha$ of multiplicity $r$ contributes its higher-order residue
$$
\operatorname{Res}_{z=\alpha}
\frac{e^{-2\pi i z\xi}}{Q(z)},
$$
which is $e^{-2\pi i\alpha\xi}$ times a polynomial in $\xi$ of degree at most $r-1$. Thus (1)--(2) are replaced by finite sums of terms
$$
P_\alpha(\xi)e^{-2\pi i\alpha\xi},
\qquad \deg P_\alpha<r.
$$
:::

