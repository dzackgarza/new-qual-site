---
schema: qual/card@1
id: P-HCAO4
kind: problem
title: Two unique factorization domains which are not principal ideal domains
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give two examples of unique factorization domains which are not principal ideal domains.
:::

::: solution
Two examples are
\[
\mathbb Z[x]
\qquad\text{and}\qquad
k[x,y]
\]
for any field $k$.

<1>1. The ring $\mathbb Z[x]$ is a UFD.
::: proof
The ring $\mathbb Z$ is a UFD, and Gauss's lemma implies that a polynomial ring
over a UFD is again a UFD.
:::

<1>2. The ring $\mathbb Z[x]$ is not a PID.
::: proof
Consider the ideal
\[
I=(2,x).
\]
It is proper, since the quotient map
\[
\mathbb Z[x]\to\mathbb F_2,
\qquad
f(x)\mapsto f(0)\bmod2
\]
has kernel $I$.

If $I=(f)$ were principal, then $f$ would divide both $2$ and $x$ in the UFD
$\mathbb Z[x]$. Their only common divisors are units, so $f$ would be a unit and
$I$ would be the whole ring, a contradiction.
:::

<1>3. The ring $k[x,y]$ is a UFD.
::: proof
The field $k$ is a UFD. Applying Gauss's lemma twice gives that
$k[x,y]=k[x][y]$ is a UFD.
:::

<1>4. The ring $k[x,y]$ is not a PID.
::: proof
The ideal
\[
J=(x,y)
\]
is proper because $k[x,y]/J\cong k$. If $J=(f)$ were principal, then $f$ would
divide both $x$ and $y$. Since $x$ and $y$ are relatively prime irreducibles,
$f$ would be a unit, contradicting the properness of $J$.
:::
:::
