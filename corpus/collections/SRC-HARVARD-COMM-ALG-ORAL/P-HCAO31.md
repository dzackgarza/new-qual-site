---
schema: qual/card@1
id: P-HCAO31
kind: problem
title: Leading terms of generators need not generate the initial ideal
classification:
  areas:
  - algebra
  topics:
  - Gröbner Bases
  - Initial Ideals
  - Polynomial Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give an ideal $I=\langle f_1,\ldots,f_t\rangle$ and a term order such that
\[
\operatorname{in}(I)\ne
\langle \operatorname{in}(f_1),\ldots,\operatorname{in}(f_t)\rangle.
\]
:::

::: solution
Work in $k[x,y]$ with lexicographic order $x\succ y$, and take
\[
I=\langle f_1,f_2\rangle,
\qquad
f_1=x^2+y,
\qquad
f_2=x^2+x.
\]

<1>1. The two displayed generators have the same initial monomial:
\[
\operatorname{in}(f_1)=\operatorname{in}(f_2)=x^2.
\]
::: proof
Under lexicographic order with $x\succ y$, the monomial $x^2$ is larger than
both $x$ and $y$.
:::

<1>2. Their difference belongs to $I$ and has initial monomial $x$:
\[
f_2-f_1=x-y,
\qquad
\operatorname{in}(x-y)=x.
\]
::: proof
Ideals are closed under subtraction, and $x\succ y$ in the chosen order.
:::

<1>3. Therefore
\[
\operatorname{in}(I)\ne
\langle \operatorname{in}(f_1),\operatorname{in}(f_2)\rangle.
\]
::: proof
By <1>2, $x\in\operatorname{in}(I)$. By <1>1,
\[
\langle \operatorname{in}(f_1),\operatorname{in}(f_2)\rangle=(x^2),
\]
and $x\notin(x^2)$. Thus the inclusion of the generator-initial ideal into
$\operatorname{in}(I)$ is strict.
:::
:::
