---
schema: qual/card@1
id: P-ALGF07C
kind: problem
title: "Ring homomorphism from C[x] onto C and non-surjective examples"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 3 of the official UCSD Algebra Qualifying Examination, Fall 2007; both parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the non-surjective inclusion into C(x) and the maximal-ideal argument showing every surjective field quotient of C[x] is C.
---

::: {.problem}
Let $\phi: \mathbb{C}[x] \to F$ be a ring homomorphism where $F$ is a field and $\phi(1)\neq 0$.

(a) Give an example where $\phi$ is not onto.

(b) If $\phi$ is onto, show that $F \cong \mathbb{C}$.
:::

::: {.solution}
<1>1. There is a non-surjective example.
::: {.proof}
Take
\[
F=\mathbb C(x),
\]
the rational-function field, and let
\[
\phi:\mathbb C[x]\hookrightarrow\mathbb C(x)
\]
be the natural inclusion.
Then $\phi(1)=1\neq0$.
The map is not surjective, since
\[
\frac1x\in\mathbb C(x)
\]
is not a polynomial and hence does not lie in the image.
:::

<1>2. For any such homomorphism, $\phi(1)=1_F$ and the restriction of $\phi$ to $\mathbb C$ is injective.
::: {.proof}
Since
\[
\phi(1)^2=\phi(1),
\]
the element $\phi(1)$ is an idempotent in the field $F$.
The only idempotents in a field are $0$ and $1$, and the hypothesis excludes $0$.
Thus
\[
\phi(1)=1_F.
\]
Consequently the restriction
\[
\phi|_{\mathbb C}:\mathbb C\longrightarrow F
\]
is a nonzero ring homomorphism from a field.
Its kernel is therefore the zero ideal, so it is injective.
:::

<1>3. If $\phi$ is surjective, then $F\cong\mathbb C$.
::: {.proof}
If $\phi$ is onto, the first isomorphism theorem gives
\[
F\cong \mathbb C[x]/\ker\phi.
\]
Since $F$ is a field, $\ker\phi$ is a maximal ideal of $\mathbb C[x]$.
Every ideal of the PID $\mathbb C[x]$ is principal, and every irreducible polynomial over the algebraically closed field $\mathbb C$ is linear.
Hence every maximal ideal has the form
\[
(x-a)
\qquad(a\in\mathbb C).
\]
Therefore, for some $a\in\mathbb C$,
\[
F\cong\mathbb C[x]/(x-a)\cong\mathbb C,
\]
where the last isomorphism is evaluation at $a$.
:::
:::
