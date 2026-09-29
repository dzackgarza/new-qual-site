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
This is an important invariant which is independent of the projective embedding of $Y$.

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
