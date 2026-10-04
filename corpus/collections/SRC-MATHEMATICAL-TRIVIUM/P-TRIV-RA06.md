---
schema: qual/card@1
id: P-TRIV-RA06
kind: problem
title: Derivative of $\cosh\sqrt{1-x^2}$ at $0$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find ${ \frac { d } { d x } } \ f ( g ( x ) ) | _ { x = 0 }$ , where $f ( u ) = \cosh u , g ( u ) = \sqrt { 1 - u ^ { 2 } } .$
:::

::: {.solution}
<1>1. One has
$$
f'(u)=\sinh u.
$$

::: {.proof}
This is the derivative of the hyperbolic cosine.
:::

<1>2. For $|x|<1$,
$$
g'(x)
=
-\frac{x}{\sqrt{1-x^2}}.
$$

::: {.proof}
Using
$$
g(x)=(1-x^2)^{1/2},
$$
the chain rule gives
$$
g'(x)
=
\frac12(1-x^2)^{-1/2}(-2x)
=
-\frac{x}{\sqrt{1-x^2}}.
$$
:::

<1>3. At $x=0$,
$$
g(0)=1
$$
and
$$
g'(0)=0.
$$

::: {.proof}
Direct substitution gives both values.
:::

<1>4. Therefore
$$
\left.
\frac{d}{dx}f(g(x))
\right|_{x=0}
=
\boxed{0}.
$$

::: {.proof}
By the chain rule,
$$
\frac{d}{dx}f(g(x))
=
f'(g(x))g'(x).
$$
At $x=0$, step <1>3 gives
$$
f'(g(0))g'(0)
=
\sinh(1)\cdot0
=0.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required value.
:::
:::
