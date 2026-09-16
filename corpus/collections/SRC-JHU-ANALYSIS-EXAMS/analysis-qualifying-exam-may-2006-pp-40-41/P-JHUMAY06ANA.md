---
schema: qual/card@1
id: P-JHUMAY06ANA
kind: problem
title: "No holomorphic logarithm of a meromorphic function with a pole"
classification:
  areas:
  - complex-analysis
  topics:
  - Isolated Singularities
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the pole hypothesis and the requested single-valued logarithm on the punctured open set with May 2006 problem 1 in the retained source."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the local nonzero holomorphic factor, negative residue at the pole and the primitive argument on a circle without assuming simple connectedness."
---

::: {.problem}
1. Let P be a point in an open set U in C, and suppose that f is a meromorphic function on U with a pole at P . Prove that there is no holomorphic function $g : U \setminus \{ P \} \to \mathbb { C }$ such that $e ^ { g ( z ) } = f ( z )$ for all $z \in U \setminus \{ P \}$
:::

::: {.solution}
<1>1. The logarithmic derivative has a nonzero integral around the pole.

::: {.proof}
Let $m\geq1$ be the pole order. Locally,
$$
f(z)=(z-P)^{-m}h(z),
$$
where $h$ is holomorphic and $h(P)\ne0$, by the Laurent
expansion [@SS03]. Choose $r>0$ so that $h$ is holomorphic
and nonzero on a neighborhood of $\overline{D(P,r)}\subset U$.
On the punctured disk,
$$
\frac{f'(z)}{f(z)}=-\frac{m}{z-P}+\frac{h'(z)}{h(z)}.
$$
Since $h'/h$ is holomorphic on the full disk, Cauchy's
theorem and direct circle integration give
$$
\int_{|z-P|=r}\frac{f'(z)}{f(z)}\,dz=-2\pi im\ne0
$$
with counterclockwise orientation [@SS03].
:::

<1>2. A holomorphic logarithm would make the same integral zero.

::: {.proof}
If the asserted $g$ existed, differentiating $e^g=f$
on this punctured disk would give $g'=f'/f$.
The integral of $g'$ around a closed parametrized circle
is zero: it is the integral of the derivative of
$g(\gamma(t))$, and the endpoint values agree.
This contradicts step <1>1. The primitive is the
single-valued function $g$ itself; no simple-connectedness
assumption on $U\setminus\{P\}$ is used.
:::
:::
