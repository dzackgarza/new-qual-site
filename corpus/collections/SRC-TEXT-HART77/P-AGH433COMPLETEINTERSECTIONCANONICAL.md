---
schema: qual/card@1
id: P-AGH433COMPLETEINTERSECTIONCANONICAL
kind: problem
title: The canonical divisor of a complete intersection curve is very ample
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Divisor
  - Very Ample Divisors
  - Embeddings
  - Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.3 together with the complete-intersection adjunction
    formula from II.8.4. The proof identifies the canonical bundle as a
    positive tensor power of the hyperplane bundle and then invokes IV.3.1 for
    the genus-two contradiction.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.3.3, printed pp. 88,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF pages are the printed
    pages. Checked against the book: Hartshorne IV.3.3, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed $m=\sum_i d_i-N-1$ against $g=\frac12(m\deg X)+1$ on a line in $\PP^3$ ($m=-2$, $g=0$), a plane conic ($m=-1$, $g=0$) and a plane quartic ($m=1$, $g=3$), and checked that $\deg K=2g-2>0$ forces $m>0$ for $g\geq2$.
    Not checked: Yang's Solutions outside printed pp. 88; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.3.3 at printed
    pp. 88 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
If $X$ is a curve of genus $\geq 2$ which is a complete intersection (II, Ex.
8.4) in some $\PP^n$, show that the canonical divisor $K$ is very ample.
Conclude that a curve of genus 2 can never be a complete intersection in any $\PP^n$.
Cf.
(Ex.
5.1).
:::

::: {.solution}
Suppose
$$
X=H_1\cap\cdots\cap H_{n-1}\subset\PP^n
$$
is a nonsingular complete-intersection curve, where
$$
\deg H_i=d_i.
$$

::: pf

::: {.pf-step #s1}

The canonical sheaf of $X$ is
$$
\omega_X
\cong
\OO_X(m),
\qquad
m=\sum_{i=1}^{n-1}d_i-n-1.
$$

::: pf-proof

Part (e) of [[P-AGH284COMPINT|Exercise II.8.4]] gives
$$
\omega_X
\cong
\left(
\omega_{\PP^n}
\tensor
\OO_{\PP^n}\!\left(\sum_i d_i\right)
\right)\restrict_X.
$$
Since
$$
\omega_{\PP^n}\cong\OO_{\PP^n}(-n-1),
$$
this becomes
$$
\omega_X
\cong
\OO_X\!\left(\sum_i d_i-n-1\right)
=\OO_X(m).
$$

:::

:::

::: {.pf-step #s2}

If $g(X)\ge2$, then
$$
m>0.
$$

::: pf-proof

The hyperplane bundle $\OO_X(1)$ has positive degree
$$
\deg X=\prod_i d_i>0.
$$
By step [](#s1){.pf-ref},
$$
2g-2
=
\deg\omega_X
=
m\deg\OO_X(1).
$$
The left-hand side is positive because $g\ge2$, and
$\deg\OO_X(1)>0$.  Hence $m>0$.

:::

:::

::: {.pf-step #s3}

The canonical divisor of $X$ is very ample.

::: pf-proof

The line bundle $\OO_X(1)$ is very ample because it is the restriction of
the hyperplane bundle for the given closed immersion
$$
X\hookrightarrow\PP^n.
$$
By step [](#s2){.pf-ref}, $m\ge1$.  Every positive tensor power of a very ample line
bundle is very ample: the corresponding morphism is the given embedding
followed by the $m$-uple Veronese embedding.  Thus
$$
\omega_X\cong\OO_X(1)^{\tensor m}
$$
is very ample.

:::

:::

::: {.pf-step #s4}

A curve of genus $2$ cannot be a complete intersection in any
$\PP^n$.

::: pf-proof

If $g(X)=2$, then every canonical divisor has degree
$$
\deg K_X=2g-2=2.
$$
If $X$ were a complete intersection, step [](#s3){.pf-ref} would make $K_X$ very ample.
But [[P-AGH431GENUSTWOVERYAMPLE|Exercise IV.3.1]] proves that on a genus-$2$
curve every very ample divisor has degree at least $5$.  This contradicts
$\deg K_X=2$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove that the canonical divisor of a complete-intersection
curve of genus at least $2$ is very ample, and step [](#s4){.pf-ref} proves the genus-$2$
conclusion.

:::

:::

:::

::: {.remark title="Published solution"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.3.3, printed p. 219, text version `tmp/sources/hartshorne-solutions-egbert.md`, computes $\omega_X=\OO_X(\sum d_i-n-1)$ for a complete intersection and observes that for $g\ge2$ the canonical sheaf is very ample, so a complete intersection cannot have genus $2$, where $\linearsystem{K}$ has degree two.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.3.3, printed p. 88, settles both halves in two sentences: a curve which is a complete intersection of hypersurfaces of degrees $d_i$ in $\PP^N$ has $K_X\cong\OO_X(m)$ with $m=\sum_i d_i-N-1$ by the complete-intersection formula for the canonical bundle ((II, Ex.\ 8.4); the entry cites it as 2.8.4(e)), and for $m>0$ the sheaf $\OO_X(m)$ is $\OO_{\PP^N}(m)$ restricted to $X$, so $\abs K$ is an $m$-uple embedding and $K$ is very ample; a curve of genus $2$ has $\deg K=2$, which (Ex.\ 4.3.1) says is not very ample, so no complete intersection has genus $2$. The assertion to watch is '$m>0$': that is exactly where the hypothesis $g\geq2$ enters, since $\deg K=m\deg X=2g-2$, and complete intersections with $m\leq0$ do exist --- a line in $\PP^3$ has $m=1+1-3-1=-2$ and $g=0$, a conic in $\PP^2$ has $m=2-2-1=-1$ --- so the printed '$m>0$' holds under the exercise's hypothesis and not before it.
:::
