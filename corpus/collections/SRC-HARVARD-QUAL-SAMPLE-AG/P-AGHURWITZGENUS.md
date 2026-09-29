---
schema: qual/card@1
id: P-AGHURWITZGENUS
kind: problem
title: Computing a genus from Hurwitz's formula
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Coverings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Coleman's question on using Hurwitz's formula to compute a curve's genus.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
How do you use Hurwitz's formula to calculate the genus of a given curve?
:::

::: {.solution}

::: pf

::: {.pf-step #find-cover}
Find a finite separable morphism
\[
f:X\longrightarrow Y
\]
to a smooth projective curve $Y$ whose genus is already known, and determine
\[
n=\deg f
\]
and the ramification divisor $R$ of $f$.

::: pf-proof
Riemann--Hurwitz compares the genus of $X$ to that of a target curve through exactly these two pieces of data.  In practice one often takes
\[
Y=\mathbb P^1
\]
by choosing a nonconstant rational function on $X$; then $g_Y=0$.
:::

:::

::: {.pf-step #riemann-hurwitz-formula}
Riemann--Hurwitz gives
\[
2g_X-2
=n(2g_Y-2)+\deg R,
\]
so
\[
\boxed{
g_X
=1+n(g_Y-1)+\frac12\deg R.
}
\]

::: pf-proof
This is obtained by solving the Riemann--Hurwitz equality for $g_X$.
:::

:::

::: {.pf-step #tame-ramification-degree}
Over an algebraically closed field, if the cover is tamely ramified, then
\[
\deg R=\sum_{p\in X}(e_p-1).
\]
Equivalently, for a branch point $q\in Y$,
\[
\sum_{p\in f^{-1}(q)}(e_p-1)
=n-\# f^{-1}(q).
\]

::: pf-proof
In the tame case the coefficient of $p$ in the ramification divisor is $e_p-1$.  For a fibre over $q$ one has
\[
\sum_{p\in f^{-1}(q)}e_p=n,
\]
so
\[
\sum_{p\in f^{-1}(q)}(e_p-1)
=n-\#f^{-1}(q).
\]
This lets one compute the ramification contribution either point-by-point or fibre-by-fibre.
:::

:::

::: {.pf-step #p1-target-formula}
For a degree-$n$ cover of the projective line,
\[
\boxed{
g_X
=1-n+\frac12\deg R.
}
\]

::: pf-proof
Substitute
\[
g_Y=g(\mathbb P^1)=0
\]
into step [](#riemann-hurwitz-formula){.pf-ref}.
:::

:::

::: {.pf-step #double-cover-example}
For example, let
\[
f:X\longrightarrow\mathbb P^1
\]
be a double cover with $r$ simple branch points.  Then
\[
\boxed{g_X=\frac{r-2}{2}.}
\]
In particular a hyperelliptic curve of genus $g$ has $2g+2$ branch points in its degree-two map to $\mathbb P^1$.

::: pf-proof
Here
\[
n=2.
\]
At each simple branch point there is one ramification point with index $2$, so each contributes
\[
e_p-1=1
\]
to $R$.  Thus
\[
\deg R=r.
\]
Step [](#p1-target-formula){.pf-ref} gives
\[
g_X
=1-2+\frac r2
=\frac{r-2}{2}.
\]
Solving for $r$ gives $r=2g_X+2$.
:::

:::

::: {.pf-step #three-inputs-summary}
Thus the calculation has three inputs: a map of known degree, the target genus, and the ramification data; Riemann--Hurwitz then determines the source genus.

::: pf-proof
This is exactly the formula in step [](#riemann-hurwitz-formula){.pf-ref}, with step [](#tame-ramification-degree){.pf-ref} explaining how the ramification term is computed in the tame case.
:::

:::

::: pf-qed
Steps [](#find-cover){.pf-ref}, [](#riemann-hurwitz-formula){.pf-ref}, [](#tame-ramification-degree){.pf-ref}, [](#p1-target-formula){.pf-ref}, [](#double-cover-example){.pf-ref} and [](#three-inputs-summary){.pf-ref} give the procedure requested in the problem and a standard model calculation.
:::

:::
:::
