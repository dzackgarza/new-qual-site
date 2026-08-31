---
schema: qual/card@1
id: FR-7YFAU
kind: proof
title: 'Proposition: Translation/Dilation Invariance of the Lebesgue Integral'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.proof}
We prove translation invariance; dilation invariance is identical with the change of variables $x \mapsto \lambda x$.

**Step 1 (characteristic functions).** Let $E \subseteq \RR^d$ be measurable and $h \in \RR^d$.
The translate $E + h = \ts{x + h \st x \in E}$ is measurable, and Lebesgue measure is translation invariant, so $\mu(E + h) = \mu(E)$.
Hence
\[
\int \indicator_{E+h} = \mu(E + h) = \mu(E) = \int \indicator_E.
\]

**Step 2 (simple functions).** A simple function is a finite linear combination $\phi = \sum_i c_i \indicator_{E_i}$ of characteristic functions of measurable sets.
By linearity of the integral and Step 1,
\[
\int \phi(\cdot + h) = \sum_i c_i \int \indicator_{E_i + h} = \sum_i c_i \int \indicator_{E_i} = \int \phi.
\]

**Step 3 (nonnegative measurable functions).** For $f \ge 0$ measurable, the integral is defined as the supremum over simple functions $0 \le \phi \le f$:
\[
\int f = \sup\ts{\int \phi \st 0 \le \phi \le f,\ \phi \text{ simple}}.
\]
The map $\phi \mapsto \phi(\cdot + h)$ is a bijection between simple functions below $f$ and simple functions below $f(\cdot + h)$, and by Step 2 it preserves the integral.
Therefore the two suprema are equal, giving $\int f(\cdot + h) = \int f$.

**Step 4 (general integrable functions).** Write $f = f^+ - f^-$ with $f^\pm \ge 0$ and apply Step 3 to each part.
:::
