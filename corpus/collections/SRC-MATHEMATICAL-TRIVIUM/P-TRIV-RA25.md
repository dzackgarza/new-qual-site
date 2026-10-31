---
schema: qual/card@1
id: P-TRIV-RA25
kind: problem
title: $\int_{\sqrt2}^\infty\frac{dx}{x+x^{\sqrt2}}$
classification:
  areas: [real-analysis]
  topics:
  - Improper Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int_{\sqrt{2}}^{\infty} \frac{dx}{x + x^{\sqrt{2}}}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Factor the denominator:
$$
x+x^{\sqrt2}
=
x\left(1+x^{\sqrt2-1}\right).
$$


::: pf-proof

Factor out the common factor $x$.

:::

:::

::: {.pf-step #s1-2}

Set
$$
a=\sqrt2-1>0
$$
and
$$
u=x^a.
$$
Then
$$
\frac{dx}{x}
=
\frac{du}{a u}.
$$


::: pf-proof

Differentiate $u=x^a$:
$$
du=a x^{a-1}\,dx
=
a u\frac{dx}{x}.
$$

:::

:::

::: pf-step

Therefore
$$
\int_{\sqrt2}^{\infty}
\frac{dx}{x+x^{\sqrt2}}
=
\frac1a
\int_{(\sqrt2)^a}^{\infty}
\frac{du}{u(1+u)}.
$$


::: pf-proof

Use step [](#s1-1){.pf-ref} and then substitute step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\frac1{u(1+u)}
=
\frac1u
-
\frac1{1+u}.
$$


::: pf-proof

Combine the right-hand side over the common denominator $u(1+u)$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\int
\frac{du}{u(1+u)}
=
\log u-\log(1+u)+C.
$$


::: pf-proof

Integrate the decomposition from step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The upper endpoint contributes $0$:
$$
\lim_{u\to\infty}
\left(
\log u-\log(1+u)
\right)
=0.
$$


::: pf-proof

Rewrite the difference as
$$
\log\frac{u}{1+u},
$$
and note that the quotient tends to $1$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\int_{\sqrt2}^{\infty}
\frac{dx}{x+x^{\sqrt2}}
=
\frac1a
\log\left(
1+(\sqrt2)^{-a}
\right).
$$


::: pf-proof

Evaluate the antiderivative in step [](#s1-5){.pf-ref} between
$$
u_0=(\sqrt2)^a
$$
and $\infty$, using step [](#s1-6){.pf-ref}:
$$
\frac1a
\left[
0-log\frac{u_0}{1+u_0}
\right]
=
\frac1a
\log\left(1+\frac1{u_0}\right).
$$

:::

:::

::: {.pf-step #s1-8}

Since
$$
\frac1{\sqrt2-1}=\sqrt2+1,
$$
the value is
$$
\boxed{
(\sqrt2+1)
\log\left(
1+(\sqrt2)^{1-\sqrt2}
\right).
}
$$


::: pf-proof

Substitute $a=\sqrt2-1$ into step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required value.

:::

:::

:::
