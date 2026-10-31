---
schema: qual/card@1
id: P-TRIV-RA26
kind: problem
title: $\int_0^1\frac{dx}{(ax+b(1-x))^2}=\frac1{ab}$
classification:
  areas: [real-analysis]
  topics:
  - Definite Integrals
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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source states the identity for all real a, b, which fails when ab <= 0. The statement now assumes ab > 0.
---

::: {.problem}
Show that $\displaystyle\int_0^1 \frac{dx}{(ax + b(1-x))^2} = \frac{1}{ab}$, $a, b \in \RR$, $ab > 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $a=b$, then
$$
\int_0^1
\frac{dx}{(ax+b(1-x))^2}
=
\frac1{a^2}.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Suppose now that $a\neq b$. Then
$$
ax+b(1-x)
=
b+(a-b)x.
$$


::: pf-proof

Expand $b(1-x)$ and collect the $x$-terms.

:::

:::

::: {.pf-step #s1-3}

Set
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


::: pf-proof

Differentiate the affine substitution and evaluate it at the two endpoints.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\int_0^1
\frac{dx}{(ax+b(1-x))^2}
=
\frac1{a-b}
\int_b^a u^{-2}\,du.
$$


::: pf-proof

Use steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Evaluating the last integral gives
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


::: pf-proof

Since
$$
\int u^{-2}\,du=-u^{-1},
$$
step [](#s1-4){.pf-ref} becomes
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

:::

::: {.pf-step #s1-6}

Hence, for $ab>0$,
$$
\boxed{
\int_0^1
\frac{dx}{(ax+b(1-x))^2}
=
\frac1{ab}.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} handles $a=b$, and step [](#s1-5){.pf-ref} handles $a\neq b$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required identity.

:::

:::

:::
