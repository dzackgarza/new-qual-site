---
schema: qual/card@1
id: P-AGH72ARITHGENUS
kind: problem
title: Arithmetic genus $p_a(Y) = (-1)^r(P_Y(0) - 1)$ of hypersurfaces and products
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomials
  - Arithmetic Genus
  - Complete Intersections
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.2 in the Hartshorne source and the preceding Hilbert-polynomial definition of degree. The proof computes Hilbert polynomials from the hypersurface and complete-intersection exact sequences, and uses the Segre graded ring to multiply Hilbert polynomials for products.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a variety of dimension $r$ in $\PP^n$, with Hilbert polynomial $P_Y$.
Define the *arithmetic genus* of $Y$ to be
$$
p_a(Y) = (-1)^r \left( P_Y(0) - 1 \right).
$$
This is an important invariant which (as we will see later in (III, Ex. 5.3)) is independent of the projective embedding of $Y$.

(a) Show that $p_a(\PP^n) = 0$.

(b) If $Y$ is a plane curve of degree $d$, show that $p_a(Y) = \frac{1}{2}(d-1)(d-2)$.

(c) More generally, if $H$ is a hypersurface of degree $d$ in $\PP^n$, show that $p_a(H) = \binom{d-1}{n}$.

(d) If $Y$ is a complete intersection of surfaces of degrees $a, b$ in $\PP^3$, show that $p_a(Y) = \frac{1}{2}ab(a + b - 4) + 1$.

(e) Let $Y^r \subseteq \PP^n$ and $Z^s \subseteq \PP^m$ be projective varieties, and embed $Y \times Z \subseteq \PP^n \times \PP^m \to \PP^N$ by the Segre embedding.
   Show that
$$
p_a(Y \times Z) = p_a(Y) p_a(Z) + (-1)^s p_a(Y) + (-1)^r p_a(Z).
$$
:::

::: {.solution}
For an integer-valued polynomial we use
$$
\binom{t}{m}=\frac{t(t-1)\cdots(t-m+1)}{m!}
$$
as a polynomial in $t$; in particular
$$
\binom{-q}{m}=(-1)^m\binom{q+m-1}{m}.
$$

::: pf

::: {.pf-step #pn-genus-zero}
The arithmetic genus of projective space is zero.

::: pf-proof
The Hilbert polynomial of $\PP^n$ is
$$
P_{\PP^n}(t)=\binom{t+n}{n}.
$$
Hence $P_{\PP^n}(0)=1$, and therefore
$$
\boxed{p_a(\PP^n)=(-1)^n(1-1)=0}.
$$
This proves part (a).
:::

:::

::: {.pf-step #hypersurface-hilbert-poly}
If $H\subseteq\PP^n$ is a hypersurface of degree $d$, then
$$
P_H(t)=\binom{t+n}{n}-\binom{t-d+n}{n}.
$$

::: pf-proof
Let $S=k[x_0,\ldots,x_n]$ and let $F\in S_d$ be an irreducible homogeneous equation for $H$.
Multiplication by $F$ gives an exact sequence of graded $S$-modules
$$
0\longrightarrow S(-d)\xrightarrow{\cdot F}S\longrightarrow S/(F)\longrightarrow0.
$$
Taking degree-$t$ dimensions for $t\gg0$ gives
$$
P_H(t)=P_S(t)-P_S(t-d)
=\binom{t+n}{n}-\binom{t-d+n}{n}.
$$
:::

:::

::: {.pf-step #hypersurface-genus}
A degree-$d$ hypersurface in $\PP^n$ has
$$
\boxed{p_a(H)=\binom{d-1}{n}}.
$$

::: pf-proof
The hypersurface has dimension $n-1$.
By step [](#hypersurface-hilbert-poly){.pf-ref},
$$
P_H(0)-1=-\binom{n-d}{n}.
$$
Using
$$
\binom{n-d}{n}=(-1)^n\binom{d-1}{n},
$$
we obtain
$$
p_a(H)
=(-1)^{n-1}(P_H(0)-1)
=(-1)^n\binom{n-d}{n}
=\binom{d-1}{n}.
$$
This proves part (c).
:::

:::

::: {.pf-step #plane-curve-genus}
A plane curve of degree $d$ has
$$
\boxed{p_a(Y)=\frac{(d-1)(d-2)}2}.
$$

::: pf-proof
A plane curve is a degree-$d$ hypersurface in $\PP^2$.
Apply step [](#hypersurface-genus){.pf-ref} with $n=2$:
$$
p_a(Y)=\binom{d-1}{2}=\frac{(d-1)(d-2)}2.
$$
This proves part (b).
:::

:::

::: {.pf-step #complete-intersection-hilbert-poly}
If $Y\subseteq\PP^3$ is the complete intersection of surfaces $F=0$ and $G=0$ of degrees $a$ and $b$, then
$$
P_Y(t)
=\binom{t+3}{3}
-\binom{t-a+3}{3}
-\binom{t-b+3}{3}
+\binom{t-a-b+3}{3}.
$$

::: pf-proof
Because $F,G$ define a complete intersection, they form a homogeneous regular sequence in $S=k[x_0,x_1,x_2,x_3]$.
The Koszul resolution of $S/(F,G)$ is
$$
0\longrightarrow S(-a-b)
\longrightarrow S(-a)\oplus S(-b)
\longrightarrow S
\longrightarrow S/(F,G)
\longrightarrow0.
$$
Taking Hilbert polynomials and using $P_S(t)=\binom{t+3}{3}$ gives the displayed formula.
:::

:::

::: {.pf-step #complete-intersection-genus}
The complete-intersection curve of step [](#complete-intersection-hilbert-poly){.pf-ref} has
$$
\boxed{p_a(Y)=1+\frac12ab(a+b-4)}.
$$

::: pf-proof
Since $Y$ has dimension one,
$$
p_a(Y)=1-P_Y(0).
$$
Substitute $t=0$ into step [](#complete-intersection-hilbert-poly){.pf-ref}:
$$
P_Y(0)
=1-\binom{3-a}{3}-\binom{3-b}{3}+\binom{3-a-b}{3}.
$$
For every integer $c$,
$$
\binom{3-c}{3}=-\frac{(c-1)(c-2)(c-3)}6.
$$
Hence
$$
\begin{aligned}
p_a(Y)
&=\binom{3-a}{3}+\binom{3-b}{3}-\binom{3-a-b}{3}\\
&=1+\frac12ab(a+b-4),
\end{aligned}
$$
where the last equality follows by expanding the three cubic polynomials and cancelling the pure $a$- and $b$-terms.
This proves part (d).
:::

:::

::: {.pf-step #segre-hilbert-poly-product}
For the Segre embedding of $Y\times Z$, the Hilbert polynomial is
$$
P_{Y\times Z}(t)=P_Y(t)P_Z(t).
$$

::: pf-proof
Let $R_Y$ and $R_Z$ be the homogeneous coordinate rings of the given embeddings.
The Segre coordinate ring has degree-$q$ piece
$$
(R_Y)_q\otimes_k(R_Z)_q.
$$
Therefore, for all sufficiently large $q$,
$$
H_{Y\times Z}(q)
=H_Y(q)H_Z(q)
=P_Y(q)P_Z(q).
$$
Two polynomials agreeing for all sufficiently large integers are equal, so the Hilbert polynomial is the product as claimed.
:::

:::

::: {.pf-step #product-genus-formula}
The arithmetic genus of the product satisfies
$$
\boxed{
p_a(Y\times Z)
=p_a(Y)p_a(Z)+(-1)^s p_a(Y)+(-1)^r p_a(Z)}.
$$

::: pf-proof
Put $A=p_a(Y)$ and $B=p_a(Z)$.
By definition,
$$
P_Y(0)=1+(-1)^rA,
\qquad
P_Z(0)=1+(-1)^sB.
$$
Step [](#segre-hilbert-poly-product){.pf-ref} and $\dim(Y\times Z)=r+s$ give
$$
\begin{aligned}
p_a(Y\times Z)
&=(-1)^{r+s}\bigl(P_Y(0)P_Z(0)-1\bigr)\\
&=(-1)^{r+s}\bigl((-1)^rA+(-1)^sB+(-1)^{r+s}AB\bigr)\\
&=AB+(-1)^sA+(-1)^rB.
\end{aligned}
$$
This proves part (e).
:::

:::

::: pf-qed
Step [](#pn-genus-zero){.pf-ref} proves part (a), step [](#plane-curve-genus){.pf-ref} proves part (b), step [](#hypersurface-genus){.pf-ref} proves part (c), steps [](#complete-intersection-hilbert-poly){.pf-ref} and [](#complete-intersection-genus){.pf-ref} prove part (d), and steps [](#segre-hilbert-poly-product){.pf-ref} and [](#product-genus-formula){.pf-ref} prove part (e).
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 7.2, PDF p. 9: (a) the Hilbert polynomial $\binom{n+k}{n}$ has constant term $1$; (b) and (c) "by 7.6c, $P_H(k)=\binom{k+n}{n}-\binom{k-d+n}{n}$, whose value at $0$ is $1-\binom{n-d}{n}=1-(-1)^n\binom{d-1}{n}$"; (d) the four-term polynomial $\binom{k+3}{3}-\binom{k-a+3}{3}-\binom{k-b+3}{3}+\binom{k-a-b+3}{3}$, "whose constant term is $1-\binom{3-a}{3}-\binom{3-b}{3}+\binom{3-a-b}{3}$ which is $1-\left(ab(a+b-4)/2+1\right)$"; (e) the product of the two Hilbert polynomials.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), stops at §I.5 and gives no solution to 7.2.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.7.2, PDF p. 56: (a) the Hilbert polynomial of $\PP^n$; (b) "$P_H(0)=\binom{0+2}{2}-\binom{0-d+2}{2}=1-\binom{2-d}{2}$" under the cross-reference "I.7.6.d", although I.7.6 has no part (d), and the displayed binomial is the plane-curve case $n=2$; (c) "as in I.7.6.d we get $\chi(l)=\binom{n+l}{n}-\binom{n+l-d}{n}$, then $p_a(X)=(-1)^{n-1}(1-\chi(0))$ and computing this gives the result" — the sign is inverted, since $p_a=(-1)^{n-1}(\chi(0)-1)$, and the displayed formula yields $-\binom{d-1}{n}$; with the sign corrected and $\binom{n-d}{n}=(-1)^n\binom{d-1}{n}$ it gives $\binom{d-1}{n}$; (d) the same four-term sequence, its binomial coefficients garbled in the text layer; (e) the Hilbert polynomial of the product is the product.
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.7.2, PDF p. 26: (a) $p_a(\PP^n)=0$; (b) $\dim k[x,y]/(f)_l=\binom{l+2}{2}-\binom{l-d+2}{2}$, hence $P_Y(0)=1-\frac{(d-1)(d-2)}{2}$ and $p_a(Y)=\frac{(d-1)(d-2)}{2}$; (c) with the correct signs, $\binom{d-1}{n}$; (d) "$X_1\cup X_2=Z(f_1f_2)$, so $\deg X_1\cup X_2=a+b$", and from $0\to S/(f_1f_2)\to S/(f_1)\oplus S/(f_2)\to S/(f_1,f_2)\to 0$, $p_a(Y)=\frac12ab(a+b-4)+1$; (e) the product of the Hilbert polynomials, expanded as $p_a(Y)p_a(Z)+(-1)^sp_a(Y)+(-1)^rp_a(Z)$.
All three agree on (a), (b), (c) and (e); Egbert's sign and cross-reference above are published defects that the card does not inherit. The four-term expansion of (d) is left as "expanding and solving" or "computing this" by all three sets, and step [](#complete-intersection-genus){.pf-ref} states it in closed form: $\binom{3-a}{3}+\binom{3-b}{3}-\binom{3-a-b}{3}=1+\frac12ab(a+b-4)$ is an identity of cubic polynomials in $a$ and $b$. Matches.
:::
