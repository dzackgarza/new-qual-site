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
<1>1. Use the half-angle substitution
$$
t=\tan\frac x2.
$$

::: {.proof}
Then
$$
\sin x=\frac{2t}{1+t^2}
$$
and
$$
dx=\frac{2\,dt}{1+t^2}.
$$
:::

<1>2. Under this substitution,
$$
\frac{dx}{\sin x}
=
\frac{dt}{t}.
$$

::: {.proof}
Substitute the identities from step <1>1:
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

<1>3. Therefore
$$
\int\frac{dx}{\sin x}
=
\log|t|+C.
$$

::: {.proof}
By step <1>2,
$$
\int\frac{dx}{\sin x}
=
\int\frac{dt}{t}
=
\log|t|+C.
$$
:::

<1>4. Hence
$$
\boxed{
\int\frac{dx}{\sin x}
=
\log\left|\tan\frac x2\right|+C.
}
$$

::: {.proof}
Substitute back $t=\tan(x/2)$ into step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required antiderivative on each interval avoiding zeros of
$\sin x$.
:::
:::
