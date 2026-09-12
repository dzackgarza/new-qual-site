---
schema: qual/card@1
id: P-JHUFA07ANC
kind: problem
title: Unit boundary modulus forces at least two annular zeros with multiplicity
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros of Holomorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Fall 2007 problem 3 on PDF page 36; made boundary-domain and annular nonconstancy conventions explicit and removed the trailing parenthesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved positivity and target-independence of the annular zero count, then excluded count one through the inverse map and a forbidden logarithm of the annular coordinate."
---

::: problem
Let $A=\{z\in\mathbb C:1<|z|<2\}$ and let $f$ be
holomorphic on a neighborhood of $\overline A$, with
$f|_A$ nonconstant and $|f|=1$ on $\partial A$.
Prove that $f$ has at least two zeros in $A$, counted
with multiplicity.
:::

::: solution
<1>1. The function maps $A$ into the unit disk and has a positive finite zero count.

::: proof
The maximum modulus principle on the compact closed
annulus gives $|f|\leq1$, with strict inequality in $A$
because $f|_A$ is nonconstant [@SS03]. If $f$ had no
zero in $A$, it would have none on $\overline A$, and
the same principle applied to $1/f$ would give $|f|\geq1$
in $A$, a contradiction. Its number $N$ of zeros in $A$,
counted with multiplicity, is finite and positive: zeros
cannot accumulate in the compact subset $\overline A$
of the holomorphy domain unless $f$ vanishes identically
on its component, by the identity theorem [@SS03].
:::

<1>2. Every point of the unit disk has exactly $N$ preimages in $A$, with multiplicity.

::: proof
Give $\partial A$ the positive orientation, outer circle
counterclockwise and inner circle clockwise. For a fixed
$w$ with $|w|<1$ and $0\leq t\leq1$, one has
$|f-tw|\geq1-|w|>0$ on this boundary. The argument
principle therefore gives
$$
N_w(t)=\frac1{2\pi i}\int_{\partial A}
\frac{f'(z)}{f(z)-tw}\,dz
$$
as the finite integer counting the zeros of $f-tw$ in
$A$ [@SS03]. The positive denominator bound makes this
integral continuous in $t$, hence constant. Thus
$N_w(1)=N_w(0)=N$.
:::

<1>3. A zero count of one is impossible.

::: proof
Suppose $N=1$. Step <1>2 makes $f:A\to D$ bijective,
where $D$ is the unit disk, and every fiber point is
simple. Hence $f'$ never vanishes in $A$, and its
inverse $g:D\to A$ is holomorphic by the inverse
function theorem [@SS03]. As $g$ has no zero on the
simply connected disk, it has a holomorphic logarithm
$L$ there. Explicitly, a primitive of $g'/g$, with its
constant chosen at zero, has exponential $g$.

The holomorphic function $K=L\circ f$ on $A$ then
satisfies $e^{K(z)}=g(f(z))=z$. Differentiating gives
$K'(z)=1/z$. But the integral of a derivative around
the circle $|z|=3/2$ is zero, whereas direct
parametrization gives
$$
\int_{|z|=3/2}\frac{dz}{z}=2\pi i.
$$
This contradiction excludes $N=1$. Together with
$N\geq1$, it proves $N\geq2$.
:::
:::
