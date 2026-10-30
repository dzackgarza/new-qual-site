---
schema: qual/card@1
id: P-TRIV-RA19
kind: problem
title: $\int\frac{dx}{\sin x}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 19, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
$\mathrm { C a l c u l a t e } \int \frac { d x } { \sin x }$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Use the half-angle substitution
$$
t=\tan\frac x2.
$$


::: pf-proof

Then
$$
\sin x=\frac{2t}{1+t^2}
$$
and
$$
dx=\frac{2\,dt}{1+t^2}.
$$

:::

:::

::: {.pf-step #s1-2}

Under this substitution,
$$
\frac{dx}{\sin x}
=
\frac{dt}{t}.
$$


::: pf-proof

Substitute the identities from step [](#s1-1){.pf-ref}:
$$
\frac{dx}{\sin x}
=
\frac{
2\,dt/(1+t^2)
}{
2t/(1+t^2)
}
=
\frac{dt}{t}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\int\frac{dx}{\sin x}
=
\log\abs{t}+C.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\int\frac{dx}{\sin x}
=
\int\frac{dt}{t}
=
\log\abs{t}+C.
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
\int\frac{dx}{\sin x}
=
\log\abs{\tan\frac x2}+C.
}
$$


::: pf-proof

Substitute back $t=\tan(x/2)$ into step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required antiderivative on each interval avoiding zeros of
$\sin x$.

:::

:::

:::
