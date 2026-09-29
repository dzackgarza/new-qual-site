---
schema: qual/card@1
id: P-AGH431GENUSTWOVERYAMPLE
kind: problem
title: On a curve of genus $2$, a divisor is very ample iff $\deg D \geq 5$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Very Ample Divisors
  - Genus
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.1 together with Corollary IV.3.2 and Example IV.3.3.4.
    The forward direction uses Riemann-Roch to exclude degrees 2 and 3 and
    the plane-curve genus formula to exclude degree 4; degree 1 is excluded
    because a complete linear system with at most two sections cannot embed a
    genus-2 curve.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $X$ is a curve of genus 2, show that a divisor $D$ is very ample $\iff \deg D \geq 5$.
This strengthens (3.3.4).
:::

::: {.solution}
Write
$$
\ell(D)=h^0\bigl(X,\mcl(D)\bigr).
$$
Since $g(X)=2$, a canonical divisor $K$ has degree
$$
\deg K=2g-2=2.
$$

::: pf

::: {.pf-step #s1}

If $\deg D\geq5$, then $D$ is very ample.

::: pf-proof

Corollary IV.3.2(b) states that on a curve of genus $g$, every divisor of
degree at least $2g+1$ is very ample.  Here
$$
2g+1=5,
$$
so every divisor of degree at least $5$ is very ample.

:::

:::

::: {.pf-step #s2}

If $D$ is very ample, then $\deg D>0$ and $\ell(D)\geq3$.

::: pf-proof

A very ample divisor is ample, so Corollary IV.3.3 gives
$$
\deg D>0.
$$

The complete linear system $|D|$ gives a closed immersion
$$
X\longrightarrow\PP^{\ell(D)-1}.
$$
If $\ell(D)=1$, there is no nonconstant morphism.  If $\ell(D)=2$, the target
is $\PP^1$; a closed irreducible one-dimensional subscheme of $\PP^1$ is
$\PP^1$ itself, which has genus $0$.  Since $g(X)=2$, neither case can occur.
Thus
$$
\ell(D)\geq3.
$$

:::

:::

::: {.pf-step #s3}

A very ample divisor on $X$ cannot have degree $1$.

::: pf-proof

A very ample divisor has a nonzero global section, so after replacing $D$ by a
linearly equivalent effective divisor we may write
$$
D=P
$$
for some point $P\in X$.  The exact sequence
$$
0\longrightarrow\OO_X
\longrightarrow\mcl(P)
\longrightarrow\mcl(P)|_P
\longrightarrow0
$$
has a one-dimensional quotient on global sections at most.  Since
$h^0(X,\OO_X)=1$, it follows that
$$
\ell(D)\leq2,
$$
contradicting step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

A very ample divisor on $X$ cannot have degree $2$.

::: pf-proof

Riemann-Roch gives
$$
\ell(D)-\ell(K-D)=\deg D+1-g=1.
$$
Now
$$
\deg(K-D)=0.
$$
A degree-$0$ line bundle has at most one nonzero global section: if it has one,
the corresponding effective divisor has degree $0$ and is therefore zero, so
the line bundle is trivial.  Hence
$$
\ell(K-D)\leq1
$$
and therefore
$$
\ell(D)\leq2,
$$
again contradicting step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s5}

A very ample divisor on $X$ cannot have degree $3$.

::: pf-proof

Here
$$
\deg(K-D)=-1,
$$
so
$$
\ell(K-D)=0.
$$
Riemann-Roch yields
$$
\ell(D)=\deg D+1-g=3+1-2=2,
$$
contradicting step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s6}

A very ample divisor on $X$ cannot have degree $4$.

::: pf-proof

Again
$$
\deg(K-D)=-2,
$$
so $\ell(K-D)=0$.  Riemann-Roch gives
$$
\ell(D)=4+1-2=3.
$$
Thus, if $D$ were very ample, its complete linear system would give a closed
immersion
$$
X\hookrightarrow\PP^2.
$$
For this embedding,
$$
\mcl(D)\cong\iota^*\OO_{\PP^2}(1),
$$
so the degree of the image is $\deg D=4$.  Hence $X$ would be isomorphic to
a nonsingular plane quartic.

By [[P-AGH72ARITHGENUS|Exercise I.7.2]], the genus formula for a nonsingular
plane curve of degree $4$ gives
$$
g=\frac{(4-1)(4-2)}2=3,
$$
contradicting $g(X)=2$.

:::

:::

::: {.pf-step #s7}

If $D$ is very ample, then
$$
\boxed{\deg D\geq5}.
$$

::: pf-proof

Step [](#s2){.pf-ref} gives $\deg D>0$, and steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} exclude the four possible
positive degrees below $5$.

:::

:::

::: {.pf-step #s8}

Therefore
$$
\boxed{D\text{ is very ample}\iff\deg D\geq5}.
$$

::: pf-proof

Step [](#s1){.pf-ref} proves the reverse implication, and step [](#s7){.pf-ref} proves the forward
implication.

:::

:::

::: pf-qed

Step [](#s8){.pf-ref} is exactly the required equivalence.

:::

:::

:::
