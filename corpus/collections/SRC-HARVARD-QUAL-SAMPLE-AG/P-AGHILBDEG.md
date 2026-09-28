---
schema: qual/card@1
id: P-AGHILBDEG
kind: problem
title: The leading term of $P_X(r)$ against line bundles on $\PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomial
  - Degree
  - Line Bundles
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's question connecting the leading Hilbert-polynomial term with the embedding line bundle, specifically $\OO_{\PP^1}(3)$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What does the degree — the leading term of the Hilbert polynomial $P_X(r)$ — have to do with line bundles on $\PP^1$, namely with $\OO(3)$?
:::

::: {.solution}
<1>1. If
\[
i:C\hookrightarrow\mathbb P^N
\]
is a projective embedding of a smooth projective curve, then the embedding is encoded by the very ample line bundle
\[
L=i^*\mathcal O_{\mathbb P^N}(1).
\]
::: {.proof}
Hyperplane sections of the embedded curve pull back to divisors in the complete linear system of $L$.  Conversely, a very ample line bundle and a basis of its global sections give a projective embedding.  Thus the hyperplane bundle restricted to $C$ is exactly the line bundle measuring the embedding.
:::

<1>2. The Hilbert polynomial of the embedded curve is
\[
\boxed{
P_C(r)=\chi(C,L^{\otimes r})
=r\deg L+1-g(C).
}
\]
::: {.proof}
By definition,
\[
\mathcal O_C(r)=i^*\mathcal O_{\mathbb P^N}(r)=L^{\otimes r},
\]
so
\[
P_C(r)=\chi(C,L^{\otimes r}).
\]
Riemann--Roch for a line bundle $M$ on a smooth projective curve gives
\[
\chi(M)=\deg M+1-g(C).
\]
Taking $M=L^{\otimes r}$ and using
\[
\deg L^{\otimes r}=r\deg L
\]
gives the formula.
:::

<1>3. Therefore the degree of the embedded curve is
\[
\boxed{\deg i(C)=\deg L.}
\]
::: {.proof}
For a projective curve the coefficient of $r$ in its Hilbert polynomial is its degree.  Step <1>2 shows that this coefficient is $\deg L$.

Geometrically, this is the same statement: a general hyperplane cuts the curve in the zero divisor of a section of $L$, and that divisor has degree $\deg L$.
:::

<1>4. On $\mathbb P^1$,
\[
L=\mathcal O_{\mathbb P^1}(3)
\]
has four global sections
\[
s^3,\ s^2t,\ st^2,\ t^3
\]
and defines the cubic Veronese embedding
\[
\nu_3:\mathbb P^1\hookrightarrow\mathbb P^3,
\qquad
[s:t]\longmapsto[s^3:s^2t:st^2:t^3].
\]
Its image is the twisted cubic.
::: {.proof}
One has
\[
h^0(\mathbb P^1,\mathcal O(3))=4,
\]
and the displayed monomials form a basis.  The complete linear system $|\mathcal O(3)|$ is very ample, so the associated map is an embedding.  By definition its image is the degree-three rational normal curve in $\mathbb P^3$, i.e. the twisted cubic.
:::

<1>5. Its Hilbert polynomial is
\[
\boxed{P_{\nu_3(\mathbb P^1)}(r)=3r+1.}
\]
::: {.proof}
By <1>2,
\[
P(r)
=\chi\bigl(\mathbb P^1,\mathcal O(3r)\bigr)
=3r+1-g(\mathbb P^1)
=3r+1.
\]
Thus the leading coefficient is $3$, exactly the degree of $\mathcal O(3)$ and of the twisted cubic.
:::

<1>6. This also explains why degree can change when the same abstract curve is embedded differently.
::: {.proof}
The identity embedding of $\mathbb P^1$ uses $\mathcal O(1)$ and has degree $1$, while the cubic Veronese uses $\mathcal O(3)$ and has degree $3$.  The abstract curve and its genus have not changed; only the embedding line bundle has.
:::

<1>7. Q.E.D.
::: {.proof}
Steps <1>2--<1>5 give the requested connection between the leading Hilbert-polynomial term and $\mathcal O(3)$ on $\mathbb P^1$.
:::
:::
