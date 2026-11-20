---
schema: qual/card@1
id: E-HAT-3.2-15
kind: problem
title: Poincaré series and products
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 15; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the series: Künneth over a field makes the Betti numbers convolve, and the six basic
    computations are checked against the cellular differentials ($\RP^n$ depending on whether $2=0$
    in $F$); the three spaces of Exercises 12-14 are then read off from their ring descriptions,
    including $1+t^4+\cdots+t^{4n}+t^{4n+2}/(1-t^2)=(1+t^{4n+2})/(1-t^4)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 15 (p.230). Rechecked the multiplicativity from Theorem 3.15 p.216 over a field, and each series against the ring computations: S^n gives 1+t^n; RP^n gives 1+t+...+t^n for char F = 2 by Theorem 3.19 p.220 and 1 or 1+t^n according to the parity of n otherwise; RP^inf gives 1/(1-t) or 1; CP^n and CP^inf give 1+t^2+...+t^{2n} and 1/(1-t^2) by Example 3.12 p.213; the two spaces of Exercise 12 give 1+t^2/(1-t); CP^inf/CP^1 gives the even tail; and the two spaces of Exercise 14 give the stated series. Not covered: the series for the spaces of Exercise 14 are reported from that card.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 15 of §3.2, printed p. 230, with Theorem 3.15 (printed p. 216),
    Theorem 3.19 (p. 220) and Example 3.12 (p. 213). Correct, and every series checked:
    $p(X\times Y)=p(X)p(Y)$ by Künneth over a field; $S^n$ gives $1+t^n$; $\RP^n$ gives
    $1+t+\cdots+t^n$ in characteristic $2$ and $1$ or $1+t^n$ according to the parity of $n$
    otherwise; $\RP^\infty$ gives $(1-t)^{-1}$ or $1$; $\CP^n$ and $\CP^\infty$ give
    $1+t^2+\cdots+t^{2n}$ and $(1-t^2)^{-1}$; the two spaces of Exercise 12 give $1+t^2/(1-t)$,
    since $R[u,v]/(v^2)$ has one class in degree $0$ and one in every degree $\ge2$;
    $\CP^\infty/\CP^1$ gives $1+t^4/(1-t^2)$; and the two pushouts of Exercise 14 give
    $(1+t^{2n+1})/(1-t^2)$ in characteristic $2$ and $(1-t^{2n+2})/(1-t^2)$ otherwise. The final
    closed form was checked by algebra: $1+t^4+\cdots+t^{4n}+t^{4n+2}/(1-t^2)=(1+t^{4n+2})/(1-t^4)$.
    Nothing changed. Not claimed: a certificate, and the series for the Exercise 14 spaces rest on
    that card's ring computation.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with eleven steps — multiplicativity, the six named spaces, and the three exercises — each
    carrying a `pf-proof`; every displayed formula of the prose is kept and no series is
    changed. Cited by number only: Hatcher Theorem 3.15 for Künneth and Theorem 3.19 for the
    cohomology of real projective space, together with the universal coefficient theorem over a
    field. Checked: the dimension count giving convolution, the two characteristics for
    $\RP^n$ and $\RP^\infty$, the geometric sums for $\CP^n$, and the closed form
    $1+t^4+\cdots+t^{4n}+t^{4n+2}/(1-t^2)=(1+t^{4n+2})/(1-t^4)$ by putting the sum over
    $1-t^4$.
---

::: {.problem}
For a fixed coefficient field $F$, define the Poincaré series of a space $X$ to be the formal power series $p(t) = \sum_i a_i t^i$ where $a_i$ is the dimension of $H^i(X; F)$ as a vector space over $F$, assuming this dimension is finite for all $i$.
Show that $p(X \times Y) = p(X) p(Y)$.
Compute the Poincaré series for $S^n$, $\RP^n$, $\RP^\infty$, $\CP^n$, $\CP^\infty$, and the spaces in the preceding three exercises.
:::

::: {.solution}

::: pf

::: pf-step

Over the fixed field $F$, Künneth gives
$$
H^n(X\times Y;F)\cong\bigoplus_{i+j=n}H^i(X;F)\otimes_F H^j(Y;F),
$$
so taking dimensions yields convolution of the Betti numbers and
$$
p_{X\times Y}(t)=p_X(t)p_Y(t).
$$

::: pf-proof

$F$ is a field, so $\operatorname{Tor}^F_1$ vanishes and every $F$-module is free; the Künneth theorem (Hatcher, Theorem 3.15) then reduces to the displayed isomorphism, its exact sequence collapsing to an isomorphism. Writing $a_i=\dim_FH^i(X;F)$ and $b_j=\dim_FH^j(Y;F)$, both finite by hypothesis, gives $\dim_FH^n(X\times Y;F)=\sum_{i+j=n}a_ib_j$ because $\dim(V\otimes_FW)=\dim V\dim W$ for finite-dimensional spaces and dimension is additive over direct sums. The coefficient of $t^n$ in $p_X(t)p_Y(t)=\sum_i a_it^i\sum_jb_jt^j$ is exactly that sum, so the two series agree coefficientwise.

:::

:::

::: pf-step

$p_{S^n}(t)=1+t^n$.

::: pf-proof

$S^n$ has $H^0(S^n;F)\cong F$ and $H^n(S^n;F)\cong F$, all other cohomology vanishing; so $a_0=a_n=1$ and the other $a_i$ are $0$.

:::

:::

::: pf-step

For $\RP^n$ the answer depends on $\operatorname{char}F$:
$$
p_{\RP^n}(t)=
\begin{cases}
1+t+\cdots+t^n,&\operatorname{char}F=2,\\
1,&\operatorname{char}F\ne2,\ n\text{ even},\\
1+t^n,&\operatorname{char}F\ne2,\ n\text{ odd}.
\end{cases}
$$

::: pf-proof

For $\operatorname{char}F=2$, Hatcher's Theorem 3.19 gives $H^*(\RP^n;F)\cong F[\alpha]/(\alpha^{n+1})$ with $\abs{\alpha}=1$, whose classes $1,\alpha,\dots,\alpha^n$ lie in degrees $0,1,\dots,n$; the series is $1+t+\cdots+t^n$. For $\operatorname{char}F\ne2$, the same theorem gives $H^*(\RP^n;\ZZ)\cong\ZZ[\alpha]/(2\alpha,\alpha^{n+1})$ with $\abs\alpha=2$, so $H^k(\RP^n;\ZZ)$ is $\ZZ$ for $k=0$, $\ZZ/2$ for the even $k$ with $2\le k<n$, and $\ZZ$ for $k=n$ when $n$ is odd. The universal coefficient theorem over a field has vanishing $\Ext^1$, so $H^k(\RP^n;F)\cong\Hom(H_k(\RP^n;\ZZ),F)$, which is $F$ when $H_k(\RP^n;\ZZ)$ has a $\ZZ$ summand and $0$ when it is a $2$-torsion group, $2$ being invertible in $F$. Hence only $H^0$ survives for even $n$, and $H^0$ and $H^n$ for odd $n$.

:::

:::

::: pf-step

And
$$
p_{\RP^\infty}(t)=
\begin{cases}
(1-t)^{-1},&\operatorname{char}F=2,\\
1,&\operatorname{char}F\ne2.
\end{cases}
$$

::: pf-proof

$\RP^\infty$ is the union of the $\RP^n$, and $H^*(\RP^\infty;F)\cong F[\alpha]$ with $\abs\alpha=1$ for $\operatorname{char}F=2$ (Theorem 3.19 in the limit), giving one class in every degree and the series $\sum_{i\ge0}t^i=(1-t)^{-1}$. For $\operatorname{char}F\ne2$ the same coefficient argument as in the previous step leaves only $H^0$, since $H_k(\RP^\infty;\ZZ)$ is $\ZZ$ in degree $0$ and $\ZZ/2$ in every even positive degree.

:::

:::

::: pf-step

For complex projective spaces,
$$
p_{\CP^n}(t)=1+t^2+\cdots+t^{2n}
=\frac{1-t^{2n+2}}{1-t^2},
\qquad
p_{\CP^\infty}(t)=\frac1{1-t^2}.
$$

::: pf-proof

$H^*(\CP^n;F)\cong F[\alpha]/(\alpha^{n+1})$ with $\abs\alpha=2$, so there is one class in each of the degrees $0,2,\dots,2n$ and none elsewhere; summing the geometric progression gives $\frac{1-t^{2n+2}}{1-t^2}$. In the limit $H^*(\CP^\infty;F)\cong F[\alpha]$ with $\abs\alpha=2$, one class in every even degree, so the series is $\sum_{k\ge0}t^{2k}=(1-t^2)^{-1}$.

:::

:::

::: pf-step

For Exercise 12, both spaces have one copy of $F$ in degree $0$ and in every degree $\ge2$ except degree $1$, with the same ring structure; thus
$$
p(t)=1+\frac{t^2}{1-t}.
$$

::: pf-proof

By the ring description of the two spaces of Exercise 12, $H^0=F$ and $H^k=F$ for every $k\ge2$, while $H^1=0$; the series is therefore $1+\sum_{k\ge2}t^k=1+t^2(1-t)^{-1}$.

:::

:::

::: pf-step

For Exercise 13,
$$
\widetilde H^*(\CP^\infty/\CP^1;F)
$$
has one generator in every even degree $\ge4$, so
$$
p(t)=1+\frac{t^4}{1-t^2}.
$$

::: pf-proof

$\CP^\infty/\CP^1$ is the Thom space of the tautological line bundle over $\CP^\infty$, and its reduced cohomology is $F$ in the even degrees $4,6,8,\dots$ and $0$ elsewhere (the cell structure of $\CP^\infty$ with the $2$-cell and the $0$-cell collapsed). Adding the degree-$0$ class gives $1+t^4+t^6+\cdots=1+t^4(1-t^2)^{-1}$.

:::

:::

::: pf-step

For Exercise 14 with $\operatorname{char}F=2$: the ring description
$$
H^*(X;F)\cong F[\alpha,\beta]/(\beta^2-\alpha^{2n+1}),
\qquad \gradeddegree{\alpha}=2,\ \gradeddegree{\beta}=2n+1,
$$
shows that $X$ is free as an $F[\alpha]$-module on $1,\beta$, hence
$$
p_X(t)=\frac{1+t^{2n+1}}{1-t^2}.
$$

::: pf-proof

The displayed presentation exhibits $H^*(X;F)$ as a free $F[\alpha]$-module with basis $1,\beta$: every class is a unique combination $f(\alpha)+g(\alpha)\beta$, since $\beta^2=\alpha^{2n+1}$ reduces any higher power of $\beta$. The classes $\alpha^k$ lie in degrees $2k$ and $\beta\alpha^k$ in degrees $2n+1+2k$, so the series is $\sum_{k\ge0}t^{2k}+t^{2n+1}\sum_{k\ge0}t^{2k}=(1+t^{2n+1})(1-t^2)^{-1}$.

:::

:::

::: pf-step

For Exercise 14 with $\operatorname{char}F\ne2$: the $\RP^\infty$ tail contributes no positive-dimensional cohomology, so $X$ has the same $F$-cohomology as $\CP^n$ and
$$
p_X(t)=\frac{1-t^{2n+2}}{1-t^2}.
$$

::: pf-proof

In this characteristic $H^k(\RP^\infty;F)=0$ for $k>0$ by step 4, so the part of the pushout coming from $\RP^\infty$ contributes only in degree $0$; what remains is the cohomology of $\CP^n$, which step 5 computes as $1+t^2+\cdots+t^{2n}=(1-t^{2n+2})(1-t^2)^{-1}$.

:::

:::

::: pf-step

For the analogous pushout $Y$ associated to $\CP^\infty\to\quatprojective^\infty$, the pair $(Y,\quatprojective^n)$ has the cells of $(\CP^\infty,\CP^{2n})$, so over every field $H^*(Y;F)$ has one generator in degrees $0,4,8,\ldots,4n$ and one generator in every even degree $\ge4n+2$, with no other groups. Therefore
$$
p_Y(t)=1+t^4+\cdots+t^{4n}+\frac{t^{4n+2}}{1-t^2}
=\frac{1+t^{4n+2}}{1-t^4}.
$$

::: pf-proof

The quotient $Y/\quatprojective^n$ has the cells of $\CP^\infty/\CP^{2n}$: one cell in each even dimension $2k$ with $k\ge2n+1$. Hence $H^*(Y;F)$ is $F$ in degrees $0,4,\dots,4n$ — the classes coming from $\quatprojective^n$, one in each quaternionic dimension — and in the even degrees $4n+2,4n+4,\dots$ from the quotient, and vanishes otherwise. Summing gives $1+t^4+\cdots+t^{4n}+t^{4n+2}(1-t^2)^{-1}$. For the closed form, put the first sum over the common denominator: $\frac{1-t^{4n+4}}{1-t^4}+\frac{t^{4n+2}}{1-t^2}=\frac{1-t^{4n+4}+t^{4n+2}+t^{4n+4}}{1-t^4}=\frac{1+t^{4n+2}}{1-t^4}$.

:::

:::

::: pf-step

These formulas complete the Poincaré-series calculation for all spaces in Exercises 12--14, and $p(X\times Y)=p(X)p(Y)$ holds for every pair of spaces with finite Betti numbers.

::: pf-proof

The multiplicativity is step 1; the six named spaces are steps 2--5; Exercise 12 is step 6, Exercise 13 step 7, and Exercise 14 steps 8--10, in both characteristics and for both pushouts.

:::

:::

:::
:::
