---
schema: qual/card@1
id: P-BKF03-4A
kind: problem
title: An irreducible polynomial over $\QQ$ that does not split in its stem field
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 4A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified Eisenstein irreducibility and that the quotient embeds in R, so the two nonreal roots are absent.
---

::: {.problem}
Give an example, with proof, of a nonconstant irreducible polynomial $f ( x )$ over Q with the property that $f ( x )$ does not factor into linear factors over the field $K = \QQ [ x ] / ( f ( x ) )$ .
:::


::: {.solution}

Take
\[
f(x)=x^3-2.
\]

::: pf

::: {.pf-step #f-irreducible}
The polynomial $f$ is irreducible over $\QQ$.

::: pf-proof
Apply Eisenstein's criterion with the prime $2$.
The leading coefficient is not divisible by $2$, every other coefficient is divisible by $2$, and the constant term $-2$ is not divisible by $4$.
Hence $x^3-2$ is irreducible in $\QQ[x]$.
:::

:::

::: {.pf-step #K-embeds-in-R}
The quotient field
\[
K=\QQ[x]/(x^3-2)
\]
is isomorphic to $\QQ(\sqrt[3]{2})$, and therefore embeds in $\RR$.

::: pf-proof
Let $\alpha=\sqrt[3]{2}\in\RR$.
Since $f$ is irreducible and $f(\alpha)=0$, evaluation at $\alpha$ gives a surjective homomorphism
\[
\QQ[x]\longrightarrow\QQ(\alpha)
\]
whose kernel is $(x^3-2)$.
Thus
\[
K\cong\QQ(\alpha)\subset\RR.
\]
:::

:::

::: {.pf-step #f-does-not-split}
The polynomial $f$ does not split into linear factors over $K$.

::: pf-proof
Over $\CC$, the three roots are
\[
\alpha,\qquad \omega\alpha,\qquad \omega^2\alpha,
\]
where $\omega=e^{2\pi i/3}$.
The latter two roots are nonreal.
By step [](#K-embeds-in-R){.pf-ref}, every element of $K$ is real under the displayed embedding, so neither $\omega\alpha$ nor $\omega^2\alpha$ belongs to $K$.
Thus $f$ has only the root $\alpha$ in $K$ and cannot factor completely into linear factors over $K$.
:::

:::

::: pf-qed
Therefore $\boxed{f(x)=x^3-2}$ is the required example.
:::

:::

:::

