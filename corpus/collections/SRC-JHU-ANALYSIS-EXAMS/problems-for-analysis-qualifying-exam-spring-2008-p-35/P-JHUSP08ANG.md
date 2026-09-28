---
schema: qual/card@1
id: P-JHUSP08ANG
kind: problem
title: "A holomorphic function with a double zero takes nearby values at least twice"
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Spring 2008 problem 7 in the retained source; the zero function disproves the unqualified assertion, so nonconstancy is required on the component containing P."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used the argument principle as requested, proved constancy of its integer-valued homotopy count and excluded critical points at the resulting nonzero fibers to obtain distinct preimages."
---

::: {.problem}
Let $U\subset\mathbb C$ be open and $P\in U$. Let $f$ be
holomorphic on $U$ and nonconstant on the component containing
$P$, with $f(P)=f'(P)=0$. Use the argument principle to prove
that there is $\delta>0$ such that $f^{-1}(Q)$ contains at
least two distinct points whenever $0<|Q|<\delta$.
:::

::: {.remark}
The nonconstancy qualification is necessary: the function
$f=0$ satisfies $f(P)=f'(P)=0$ but has no preimage of any
nonzero value. Nonconstancy on an unrelated component of
$U$ does not supply the local hypothesis at $P$.
:::

::: {.solution}
<1>1. In a sufficiently small disk, $P$ is the only zero and the only critical point.

::: {.proof}
The Taylor expansion and the identity theorem give
$$
f(z)=(z-P)^m h(z),\qquad m\geq2,\quad h(P)\ne0,
$$
with $h$ holomorphic near $P$ [@SS03]. Differentiating gives
$$
f'(z)=(z-P)^{m-1}\bigl(mh(z)+(z-P)h'(z)\bigr).
$$
Both $h$ and the bracketed factor are nonzero at $P$.
Choose $r>0$ with $\overline{D(P,r)}\subset U$ so small
that these two factors are nonzero on a neighborhood of
the closed disk. Then $f$ has exactly $m$ zeros in the
disk counted with multiplicity, all at $P$, and $f'$ has
no zero there except $P$. Set
$\delta=\min_{|z-P|=r}|f(z)|>0$.
:::

<1>2. The argument-principle count stays equal to $m$ under a small constant perturbation.

::: {.proof}
Fix $0<|Q|<\delta$. For $0\leq t\leq1$ and $|z-P|=r$,
$$
|f(z)-tQ|\geq\delta-|Q|>0.
$$
Thus the argument principle applies to $f-tQ$ on this
circle and gives its number of zeros, with multiplicity, as
$$
N(t)=\frac1{2\pi i}\int_{|z-P|=r}
\frac{f'(z)}{f(z)-tQ}\,dz\in\mathbb Z_{\geq0}
$$
[@SS03]. The uniform positive denominator bound makes
this integral continuous in $t$. A continuous integer-valued
function on $[0,1]$ is constant, so $N(1)=N(0)=m$.
:::

<1>3. These $m$ preimages are distinct.

::: {.proof}
None of the zeros of $f-Q$ is $P$, since $Q\ne0=f(P)$.
Step <1>1 shows that the derivative is nonzero at each of
them. Each zero is therefore simple by its Taylor expansion.
Consequently the multiplicity count $m\geq2$ from step <1>2
counts distinct points of $D(P,r)\subset U$. All of them
belong to $f^{-1}(Q)$, proving the assertion for every
$0<|Q|<\delta$.
:::
:::
