---
schema: qual/card@1
id: P-ALGS14C
kind: problem
title: $\mathbb{Z}[i]$ is a PID; proper subrings with fraction field $\mathbb{Q}(i)$ are not UFDs
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
(a) Show that $\mathbb{Z}[i]$ is a PID.

(b) Let $A$ be a proper subring of $\mathbb{Z}[i]$ which contains $\mathbb{Z}$.
Suppose the field of fractions of $A$ is $\mathbb{Q}(i)$.
Show that $A$ is NOT a unique factorization domain (UFD).
:::

::: {.solution}

::: pf

::: pf-step

Part (a): define the Gaussian norm by
\[
N(a+bi)=a^2+b^2.
\]
It is multiplicative and takes positive integer values on nonzero Gaussian integers.

::: pf-proof

For $z,w\in\mathbb Z[i]$, $N(zw)=zw\overline{zw}=z\bar z\,w\bar w=N(z)N(w)$.

:::

:::

::: {.pf-step #s2}

Given $\alpha,\beta\in\mathbb Z[i]$ with $\beta\ne0$, choose $q\in\mathbb Z[i]$ whose real and imaginary parts are nearest integers to those of $\alpha/\beta$, and set $r=\alpha-q\beta$.
Then
\[
N(r)<N(\beta).
\]

::: pf-proof

Write $\alpha/\beta=x+iy$.
Choose $m,n\in\mathbb Z$ with $|x-m|\le \frac12$ and $|y-n|\le \frac12$, and set $q=m+ni$.
Then
\[
N\!\left(\frac r\beta\right)=N\!\left(\frac\alpha\beta-q\right)
=(x-m)^2+(y-n)^2\le\frac12<1.
\]
Hence $N(r)=N(\beta)N(r/\beta)<N(\beta)$.

:::

:::

::: pf-step

Thus $\mathbb Z[i]$ is a Euclidean domain, hence a PID.

::: pf-proof

The division algorithm of step [](#s2){.pf-ref} is the Euclidean algorithm with Euclidean function $N$; every Euclidean domain is a PID.

:::

:::

::: {.pf-step #s4}

Part (b): suppose, for contradiction, that $A$ is a UFD. Then $A$ is integrally closed in its fraction field $\operatorname{Frac}(A)=\mathbb Q(i)$.

::: pf-proof

Every UFD is integrally closed.

:::

:::

::: {.pf-step #s5}

The element $i\in\mathbb Q(i)=\operatorname{Frac}(A)$ is integral over $A$ because it satisfies the monic polynomial
\[
x^2+1\in A[x],
\]
since $\mathbb Z\subseteq A$.

::: pf-proof

This is the definition of integrality.

:::

:::

::: pf-step

Since $A$ is integrally closed, step [](#s5){.pf-ref} implies $i\in A$.
Because $\mathbb Z\subseteq A$, this gives $\mathbb Z[i]\subseteq A$.
But by hypothesis $A\subseteq\mathbb Z[i]$, so $A=\mathbb Z[i]$, contradicting that $A$ is proper.
Therefore $A$ is not a UFD.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
