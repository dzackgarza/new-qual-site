---
schema: qual/card@1
id: P-BKF10-8B
kind: problem
title: Existence of monic orthogonal polynomials for a positive weight on $[a,b]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked positive definiteness of the weighted polynomial inner
    product and the monic Gram--Schmidt recursion preserving degree and
    orthogonality.
---

::: {.problem}
Suppose that $f$ is a positive continuous function on $[a,b]$.
Prove that there are polynomials $p_n$, for $n=0,1,2,\ldots$, such that $p_n$ is monic of degree $n$ and
$$
\int_a^b p_m(x)p_n(x)f(x)\,dx=0
$$
whenever $m\ne n$.
:::

::: {.solution}
On the real vector space of polynomials, define
$$
\langle q,r\rangle
\coloneqq
\int_a^b q(x)r(x)f(x)\,dx.
$$

<1>1. The displayed pairing is an inner product on the polynomial
space.

::: {.proof}
Linearity and symmetry follow from the integral. For every polynomial
$q$,
$$
\langle q,q\rangle
=\int_a^b q(x)^2f(x)\,dx\ge0.
$$
If $q\ne0$, then $q$ is nonzero at some point of the nondegenerate
interval $[a,b]$. By continuity, $q(x)^2$ is bounded below by a positive
number on some subinterval, and the positive continuous function $f$ is
also bounded below there by a positive number. Hence
$\langle q,q\rangle>0$. Thus the pairing is positive definite.
:::

<1>2. Define $p_0(x)=1$, and recursively for $n\ge1$ define
$$
p_n(x)
\coloneqq
x^n-
\sum_{k=0}^{n-1}
\frac{\langle x^n,p_k\rangle}
     {\langle p_k,p_k\rangle}
p_k(x).
$$
The recursion is well-defined.

::: {.proof}
By step <1>1, every nonzero polynomial has positive squared norm. The
induction below shows that each $p_k$ is monic of degree $k$, hence
nonzero, so every denominator $\langle p_k,p_k\rangle$ is positive.
For $n=0$, $p_0=1$ is already nonzero, starting the recursion.
:::

<1>3. For every $n\ge0$, the polynomial $p_n$ is monic of degree $n$.

::: {.proof}
Proceed by induction. The assertion is clear for $p_0=1$. Assume it
holds for $p_0,\ldots,p_{n-1}$. Every term in the sum defining $p_n$ in
step <1>2 has degree at most $n-1$. Therefore subtracting that sum from
$x^n$ does not change the coefficient of $x^n$, which remains $1$.
Hence $p_n$ is monic of degree $n$.
:::

<1>4. The polynomials $p_0,p_1,p_2,\ldots$ are pairwise orthogonal for
$\langle\ ,\ \rangle$.

::: {.proof}
Again proceed inductively. Suppose $p_0,\ldots,p_{n-1}$ are pairwise
orthogonal. For $m<n$, step <1>2 gives
$$
\begin{aligned}
\langle p_n,p_m\rangle
&=\langle x^n,p_m\rangle
-\sum_{k=0}^{n-1}
 \frac{\langle x^n,p_k\rangle}
      {\langle p_k,p_k\rangle}
 \langle p_k,p_m\rangle\\
&=\langle x^n,p_m\rangle
-\frac{\langle x^n,p_m\rangle}
       {\langle p_m,p_m\rangle}
 \langle p_m,p_m\rangle\\
&=0.
\end{aligned}
$$
Thus $p_n$ is orthogonal to every earlier $p_m$, completing the
induction.
:::

<1>5. Consequently, whenever $m\ne n$,
$$
\boxed{
\int_a^b p_m(x)p_n(x)f(x)\,dx=0
}.
$$

::: {.proof}
The integral is exactly $\langle p_m,p_n\rangle$, which vanishes by
step <1>4. Step <1>3 supplies the required monic degree condition.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>3 and <1>5 give all required properties of the sequence
$(p_n)_{n\ge0}$.
:::
:::
