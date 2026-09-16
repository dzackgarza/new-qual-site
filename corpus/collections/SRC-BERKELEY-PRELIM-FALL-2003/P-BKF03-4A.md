---
schema: qual/card@1
id: P-BKF03-4A
kind: problem
title: An irreducible polynomial over $\mathbb Q$ that does not split in its stem field
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
Give an example, with proof, of a nonconstant irreducible polynomial $f ( x )$ over Q with the property that $f ( x )$ does not factor into linear factors over the field $K = \mathbb { Q } [ x ] / ( f ( x ) )$ .
:::


::: {.solution}
Take
\[
f(x)=x^3-2.
\]

<1>1. The polynomial $f$ is irreducible over $\mathbb Q$.
::: {.proof}
Apply Eisenstein's criterion with the prime $2$.
The leading coefficient is not divisible by $2$, every other coefficient is divisible by $2$, and the constant term $-2$ is not divisible by $4$.
Hence $x^3-2$ is irreducible in $\mathbb Q[x]$.
:::

<1>2. The quotient field
\[
K=\mathbb Q[x]/(x^3-2)
\]
is isomorphic to $\mathbb Q(\sqrt[3]{2})$, and therefore embeds in $\mathbb R$.
::: {.proof}
Let $\alpha=\sqrt[3]{2}\in\mathbb R$.
Since $f$ is irreducible and $f(\alpha)=0$, evaluation at $\alpha$ gives a surjective homomorphism
\[
\mathbb Q[x]\longrightarrow\mathbb Q(\alpha)
\]
whose kernel is $(x^3-2)$.
Thus
\[
K\cong\mathbb Q(\alpha)\subset\mathbb R.
\]
:::

<1>3. The polynomial $f$ does not split into linear factors over $K$.
::: {.proof}
Over $\mathbb C$, the three roots are
\[
\alpha,\qquad \omega\alpha,\qquad \omega^2\alpha,
\]
where $\omega=e^{2\pi i/3}$.
The latter two roots are nonreal.
By <1>2, every element of $K$ is real under the displayed embedding, so neither $\omega\alpha$ nor $\omega^2\alpha$ belongs to $K$.
Thus $f$ has only the root $\alpha$ in $K$ and cannot factor completely into linear factors over $K$.
:::

Therefore $\boxed{f(x)=x^3-2}$ is the required example.
:::

