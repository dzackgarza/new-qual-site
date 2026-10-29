---
schema: qual/card@1
id: P-4CJY7
kind: problem
title: Characteristic and minimal polynomials of the Frobenius automorphism
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Minimal and Characteristic Polynomials
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source asked for the polynomials of "the Frobenius automorphism" without naming the field; the statement now names the Frobenius x -> x^p of F_{p^n} as an F_p-linear map.'
---

::: {.problem}
What are the characteristic and minimal polynomial of the Frobenius automorphism $x\mapsto x^p$ of $\FF_{p^n}$, regarded as an $\FF_p$-linear map?
:::

::: {.solution}
Let $F=\FF_{p^n}$ and let
$$
\Phi:F\to F,\qquad \Phi(x)=x^p,
$$
viewed as an $\FF_p$-linear map.

By the normal basis theorem for the finite Galois extension $F/\FF_p$, there exists $\alpha\in F$ such that
$$
\alpha,\Phi(\alpha),\ldots,\Phi^{n-1}(\alpha)
$$
is an $\FF_p$-basis of $F$. Since $\Phi^n=\operatorname{id}$, the matrix of $\Phi$ in this basis is the permutation matrix of the $n$-cycle
$$
\alpha\mapsto\Phi(\alpha)\mapsto\cdots\mapsto\Phi^{n-1}(\alpha)\mapsto\alpha.
$$
Hence its characteristic polynomial is
$$
\chi_\Phi(X)=X^n-1.
$$

The vector $\alpha$ is cyclic for $\Phi$: the vectors
$$
\alpha,\Phi(\alpha),\ldots,\Phi^{n-1}(\alpha)
$$
are linearly independent. Therefore no nonzero polynomial of degree $<n$ annihilates $\Phi$. Since $\Phi^n-I=0$, the minimal polynomial has degree $n$ and divides $X^n-1$, so
$$
m_\Phi(X)=X^n-1.
$$
Thus both the characteristic and minimal polynomials of Frobenius are $X^n-1$.
:::
