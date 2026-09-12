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

::: problem
(a) Show that $\mathbb{Z}[i]$ is a PID.

(b) Let $A$ be a proper subring of $\mathbb{Z}[i]$ which contains $\mathbb{Z}$.
Suppose the field of fractions of $A$ is $\mathbb{Q}(i)$.
Show that $A$ is NOT a unique factorization domain (UFD).
:::

::: {.solution}
<1>1. Part (a): define the Gaussian norm by
\[
N(a+bi)=a^2+b^2.
\]
It is multiplicative and takes positive integer values on nonzero Gaussian integers.
::: {.proof}
For $z,w\in\mathbb Z[i]$, $N(zw)=zw\overline{zw}=z\bar z\,w\bar w=N(z)N(w)$.
:::

<1>2. Given $\alpha,\beta\in\mathbb Z[i]$ with $\beta\ne0$, choose $q\in\mathbb Z[i]$ whose real and imaginary parts are nearest integers to those of $\alpha/\beta$, and set $r=\alpha-q\beta$.
Then
\[
N(r)<N(\beta).
\]
::: {.proof}
Write $\alpha/\beta=x+iy$.
Choose $m,n\in\mathbb Z$ with $|x-m|\le \frac12$ and $|y-n|\le \frac12$, and set $q=m+ni$.
Then
\[
N\!\left(\frac r\beta\right)=N\!\left(\frac\alpha\beta-q\right)
=(x-m)^2+(y-n)^2\le\frac12<1.
\]
Hence $N(r)=N(\beta)N(r/\beta)<N(\beta)$.
:::

<1>3. Thus $\mathbb Z[i]$ is a Euclidean domain, hence a PID.
::: {.proof}
The division algorithm of <1>2 is the Euclidean algorithm with Euclidean function $N$; every Euclidean domain is a PID.
:::

<1>4. Part (b): suppose, for contradiction, that $A$ is a UFD. Then $A$ is integrally closed in its fraction field $\operatorname{Frac}(A)=\mathbb Q(i)$.
::: {.proof}
Every UFD is integrally closed.
:::

<1>5. The element $i\in\mathbb Q(i)=\operatorname{Frac}(A)$ is integral over $A$ because it satisfies the monic polynomial
\[
x^2+1\in A[x],
\]
since $\mathbb Z\subseteq A$.
::: {.proof}
This is the definition of integrality.
:::

<1>6. Since $A$ is integrally closed, <1>5 implies $i\in A$.
Because $\mathbb Z\subseteq A$, this gives $\mathbb Z[i]\subseteq A$.
But by hypothesis $A\subseteq\mathbb Z[i]$, so $A=\mathbb Z[i]$, contradicting that $A$ is proper.
Therefore $A$ is not a UFD.
::: {.proof}
<1>4 and <1>5.
:::
:::
