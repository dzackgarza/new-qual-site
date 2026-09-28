---
schema: qual/card@1
id: P-JHUMAY11ANB
kind: problem
title: Weighted logarithmic derivative around two prescribed zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Contour Integration
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2011 problem 2 and the unit-disk convention on PDF page 24; restored the definition of D and replaced the truncated title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the enclosed zeros, nonvanishing on the contour, local logarithmic-derivative residues and the two explicit values of the holomorphic weight."
---

::: {.problem}
Let $D=\{z\in\mathbb C:|z|<1\}$, and let $f:D\to\mathbb C$
be holomorphic with simple zeros at $1/3$, $2/3$ and $i/4$
and no other zeros. Evaluate
$$
\int_{|z|=1/2}(z^2-1)e^z\frac{f'(z)}{f(z)}\,dz,
$$
with counterclockwise orientation.
:::

::: {.solution}
The integral is
$$
\boxed{-2\pi i\left(\frac89e^{1/3}+\frac{17}{16}e^{i/4}\right).}
$$

<1>1. Each simple zero contributes the value of the holomorphic weight as a residue.

::: {.proof}
Set $W(z)=(z^2-1)e^z$. At a simple zero $a$ of $f$,
the Taylor expansion gives $f(z)=(z-a)h(z)$ with $h$
holomorphic and $h(a)\ne0$. In a sufficiently small disk,
$$
\frac{f'(z)}{f(z)}=\frac1{z-a}+\frac{h'(z)}{h(z)}.
$$
The second term is holomorphic, so
$$
\operatorname{Res}_{a}\left(W\frac{f'}f\right)=W(a).
$$
Away from the prescribed zeros, the same integrand is
holomorphic. These facts determine all its possible poles
on the unit disk.
:::

<1>2. The two enclosed zeros give the stated sum.

::: {.proof}
The zeros $1/3$ and $i/4$ lie inside $|z|=1/2$, while
$2/3$ lies outside. None lies on the contour. The closed
radius-one-half disk has a neighborhood contained in $D$,
so the residue theorem applies to this counterclockwise
circle [@SS03]. Using step <1>1, it gives
$$
\int_{|z|=1/2}W(z)\frac{f'(z)}{f(z)}\,dz
=2\pi i\bigl(W(1/3)+W(i/4)\bigr).
$$
Finally,
$$
W(1/3)=-\frac89e^{1/3},\qquad
W(i/4)=\left(-\frac1{16}-1\right)e^{i/4}
=-\frac{17}{16}e^{i/4}.
$$
Substitution yields the displayed answer.
:::
:::
