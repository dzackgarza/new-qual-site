---
schema: qual/card@1
id: P-JHUFA06ANC
kind: problem
title: "Holomorphic maps into the upper half plane and bounded harmonic functions on a slit plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both assertions, the puncture and the positive-real-axis slit with September 2006 problem 3 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the Cayley transform, its bounded extension and invertibility, and the slit-plane argument branch giving a nonconstant harmonic function with values strictly between zero and one."
---

::: {.problem}
3. State whether each of the following two statements is true or false, and give either a proof or counterexample for each.

a) All holomorphic functions $f:\mathbb C\setminus\{0\}\to H$ are constant, where $H=\{z\in\mathbb C:\operatorname{Im}z>0\}$ is the upper half-plane.

b) All harmonic functions $h : \mathbb { C } \setminus [ 0 , + \infty ) \to [ 0 , 1 ]$ are constant.
:::

::: solution
Assertion (a) is true; assertion (b) is false.

<1>1. A holomorphic map from the punctured plane into $H$ is constant.
::: proof
Given such an $f$, define
$$
g(z)=\frac{f(z)-i}{f(z)+i}.
$$
Its denominator is nonzero because $f(z)\in H$, and
$$
|f(z)+i|^2-|f(z)-i|^2=4\operatorname{Im}f(z)>0.
$$
Thus $g$ is holomorphic on the punctured plane with $|g|<1$.
The removable-singularity theorem extends it to an entire
function $G$, with $|G(0)|\leq1$ by continuity [@SS03].
This entire extension is bounded, so Liouville's theorem
makes it constant. Its value $c=g(1)$ satisfies $|c|<1$.
Solving the fractional transformation gives
$$
f(z)=i\frac{1+c}{1-c}\qquad(z\ne0),
$$
where $1-c\ne0$. Hence $f$ is constant, proving (a).
:::

<1>2. A branch of the argument supplies a counterexample to (b).
::: proof
On $\Omega=\mathbb C\setminus[0,\infty)$ choose
the logarithm branch
$$
L(re^{i\theta})=\log r+i\theta,
\qquad r>0,\quad 0<\theta<2\pi.
$$
Every point of $\Omega$ has a unique such argument, and
this branch is holomorphic there, with derivative $1/z$
[@SS03]. Therefore its imaginary part is harmonic. The
function
$$
h(z)=\frac{\operatorname{Im}L(z)}{2\pi}
$$
is harmonic on $\Omega$ and takes values in $(0,1)\subset[0,1]$.
It is not constant: $h(i)=1/4$ and $h(-i)=3/4$.
It meets all the hypotheses of (b) and contradicts its
conclusion, so (b) is false.
:::
:::
