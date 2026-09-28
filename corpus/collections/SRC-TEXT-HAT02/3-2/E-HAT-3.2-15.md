---
schema: qual/card@1
id: E-HAT-3.2-15
kind: problem
title: "Poincaré series and products"
classification:
  areas:
  - topology
  topics:
  - Cohomology
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
---

::: {.problem}
For a fixed coefficient field $F$, define the Poincaré series of a space $X$ to be the formal power series $p(t) = \sum_i a_i t^i$ where $a_i$ is the dimension of $H^i(X; F)$ as a vector space over $F$, assuming this dimension is finite for all $i$.
Show that $p(X \times Y) = p(X) p(Y)$.
Compute the Poincaré series for $S^n$, $\mathbb{RP}^n$, $\mathbb{RP}^\infty$, $\mathbb{CP}^n$, $\mathbb{CP}^\infty$, and the spaces in the preceding three exercises.
:::

::: {.solution}
Over the fixed field $F$, the Künneth theorem has no Tor term and gives
\[
H^n(X\times Y;F)\cong\bigoplus_{i+j=n}H^i(X;F)\otimes_F H^j(Y;F).
\]
Taking dimensions therefore yields convolution of the Betti numbers, hence
\[
\boxed{p_{X\times Y}(t)=p_X(t)p_Y(t).}
\]

The basic examples are
\[
p_{S^n}(t)=1+t^n.
\]
For $\mathbb{RP}^n$ the answer depends on $\operatorname{char}F$:
\[
p_{\mathbb{RP}^n}(t)=
\begin{cases}
1+t+\cdots+t^n,&\operatorname{char}F=2,\\
1,&\operatorname{char}F\ne2,\ n\text{ even},\\
1+t^n,&\operatorname{char}F\ne2,\ n\text{ odd},
\end{cases}
\]
and
\[
p_{\mathbb{RP}^\infty}(t)=
\begin{cases}
(1-t)^{-1},&\operatorname{char}F=2,\\
1,&\operatorname{char}F\ne2.
\end{cases}
\]
For complex projective spaces,
\[
p_{\mathbb{CP}^n}(t)=1+t^2+\cdots+t^{2n}
=\frac{1-t^{2n+2}}{1-t^2},
\qquad
p_{\mathbb{CP}^\infty}(t)=\frac1{1-t^2}.
\]

For Exercise 12, both spaces have one copy of $F$ in degree $0$ and in every degree $\ge2$ except degree $1$, with the same ring structure; thus
\[
p(t)=1+\frac{t^2}{1-t}.
\]
For Exercise 13,
\[
\widetilde H^*(\mathbb{CP}^\infty/\mathbb{CP}^1;F)
\]
has one generator in every even degree $\ge4$, so
\[
p(t)=1+\frac{t^4}{1-t^2}.
\]
For Exercise 14, let $X$ be the pushout built from $\mathbb{RP}^\infty$ and $\mathbb{CP}^n$. If $\operatorname{char}F=2$, the ring description
\[
H^*(X;F)\cong F[\alpha,\beta]/(\beta^2-\alpha^{2n+1}),
\qquad |\alpha|=2,\ |\beta|=2n+1,
\]
shows that it is free as an $F[\alpha]$-module on $1,\beta$. Hence
\[
p_X(t)=\frac{1+t^{2n+1}}{1-t^2}.
\]
If $\operatorname{char}F\ne2$, the $\mathbb{RP}^\infty$ tail contributes no positive-dimensional cohomology, so $X$ has the same $F$-cohomology as $\mathbb{CP}^n$ and
\[
p_X(t)=\frac{1-t^{2n+2}}{1-t^2}.
\]

For the analogous pushout $Y$ associated to $\mathbb{CP}^\infty\to\mathbb{HP}^\infty$, the pair $(Y,\mathbb{HP}^n)$ is the same cellular pair as $(\mathbb{CP}^\infty,\mathbb{CP}^{2n+1})$. Thus, over every field,
\[
H^*(Y;F)
\]
has one generator in degrees $0,4,8,\ldots,4n$ and one generator in every even degree $\ge4n+4$, with no other groups. Therefore
\[
\boxed{
p_Y(t)=1+t^4+\cdots+t^{4n}+\frac{t^{4n+4}}{1-t^2}.
}
\]
These formulas complete the Poincaré-series calculation for all spaces in Exercises 12--14.
:::
