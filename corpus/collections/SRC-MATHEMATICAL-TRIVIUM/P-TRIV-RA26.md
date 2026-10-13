---
schema: qual/card@1
id: P-TRIV-RA26
kind: problem
title: $\int_0^1\frac{dx}{(ax+b(1-x))^2}=\frac1{ab}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 26, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned Real Analysis Problem 26 against page 10 of the source PDF and added an erratum remark for the missing hypothesis ab > 0.
---

::: {.problem}
Show that $\displaystyle\int_0^1 \frac{dx}{(ax + b(1-x))^2} = \frac{1}{ab}$, $a, b \in \mathbb{R}$.
:::

::: {.remark}
Erratum: as stated, with arbitrary $a, b \in \mathbb{R}$, the identity is false.
For $a = 1$, $b = -1$ the integrand is $\frac{1}{(2x-1)^2}$, which is not integrable near $x = \frac{1}{2}$, so the integral diverges, while $\frac{1}{ab} = -1$.
More generally, if $ab < 0$ then $ax + b(1-x)$ vanishes at $x = \frac{b}{b-a} \in (0,1)$ and the integral diverges, and if $ab = 0$ the right-hand side is undefined.
The identity holds under the corrected hypothesis $ab > 0$, that is, $a$ and $b$ nonzero of the same sign.
:::

::: {.solution}
Assume
$$
ab>0.
$$

<1>1. If $a=b$, then
$$
\int_0^1
\frac{dx}{(ax+b(1-x))^2}
=
\frac1{a^2}.
$$

::: {.proof}
When $a=b$,
$$
ax+b(1-x)=a
$$
for every $x$. Hence
$$
\int_0^1\frac{dx}{a^2}
=
\frac1{a^2}.
$$
Since $a=b$, this equals $1/(ab)$.
:::

<1>2. Suppose now that $a\neq b$. Then
$$
ax+b(1-x)
=
b+(a-b)x.
$$

::: {.proof}
Expand $b(1-x)$ and collect the $x$-terms.
:::

<1>3. Set
$$
u=b+(a-b)x.
$$
Then
$$
du=(a-b)\,dx,
$$
and the endpoints are
$$
x=0\longmapsto u=b,
\qquad
x=1\longmapsto u=a.
$$

::: {.proof}
Differentiate the affine substitution and evaluate it at the two endpoints.
:::

<1>4. Therefore
$$
\int_0^1
\frac{dx}{(ax+b(1-x))^2}
=
\frac1{a-b}
\int_b^a u^{-2}\,du.
$$

::: {.proof}
Use steps <1>2--<1>3.
:::

<1>5. Evaluating the last integral gives
$$
\frac1{a-b}
\left(
-\frac1a
+
\frac1b
\right)
=
\frac1{ab}.
$$

::: {.proof}
Since
$$
\int u^{-2}\,du=-u^{-1},
$$
step <1>4 becomes
$$
\frac1{a-b}
\left[
-\frac1u
\right]_b^a
=
\frac1{a-b}
\left(
\frac1b-\frac1a
\right).
$$
Now
$$
\frac1b-\frac1a
=
\frac{a-b}{ab}.
$$
:::

<1>6. Hence, under the corrected hypothesis $ab>0$,
$$
\boxed{
\int_0^1
\frac{dx}{(ax+b(1-x))^2}
=
\frac1{ab}.
}
$$

::: {.proof}
Step <1>1 handles $a=b$, and step <1>5 handles $a\neq b$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the corrected intended identity.
:::
:::
