---
schema: qual/card@1
id: P-BKS05-6A
kind: problem
title: Divisibility of products of $q$-integers in $\ZZ[q]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained root-of-unity multiplicity proof and
    made the coefficient-ring conclusion explicit: monic division by the
    denominator product takes place in Z[q], so divisibility over C[q]
    yields divisibility over Z[q].
---

::: {.problem}
For every positive integer n, define $[ n ] _ { q } = q ^ { n - 1 } { + } q ^ { n - 2 } { + } \cdot \cdot \cdot { + } q { + } 1$ . Prove that $[ 1 ] _ { q } [ 2 ] _ { q } \cdot \cdot \cdot [ r ] _ { q }$ divides $[ k + 1 ] _ { q } [ k + 2 ] _ { q } \cdot \cdot \cdot [ k + r ] _ { q }$ in the polynomial ring $\mathbb { Z } [ q ]$ , for all positive integers k and r.
:::

::: {.solution}
Set
$$
D(q)\coloneqq\prod_{n=1}^r[n]_q,
\qquad
N(q)\coloneqq\prod_{n=k+1}^{k+r}[n]_q.
$$

::: pf

::: {.pf-step #root-of-unity-simple-root}
If $\omega\neq1$ is a root of unity of order $d$, then
$\omega$ is a simple root of $[n]_q$ exactly when $d\mid n$.

::: pf-proof
For $q\neq1$,
$$
[n]_q=\frac{q^n-1}{q-1}.
$$
Hence $[n]_\omega=0$ exactly when $\omega^n=1$, which is equivalent
to $d\mid n$. The roots of $q^n-1$ are simple over $\CC$, and
$\omega\neq1$, so such a root remains simple after division by
$q-1$.
:::

:::

::: {.pf-step #multiplicity-comparison}
Every complex root of $D$ occurs in $N$ with at least the same
multiplicity.

::: pf-proof
Let $\omega$ be a root of $D$, and let $d$ be its order. By step
[](#root-of-unity-simple-root){.pf-ref}, its multiplicity in $D$ is the number of multiples of $d$ among
$1,\ldots,r$, namely
$$
\left\lfloor\frac rd\right\rfloor.
$$
Its multiplicity in $N$ is the number of multiples of $d$ among
$k+1,\ldots,k+r$, namely
$$
\left\lfloor\frac{k+r}{d}\right\rfloor
-
\left\lfloor\frac{k}{d}\right\rfloor.
$$
Since
$$
\left\lfloor\frac{k+r}{d}\right\rfloor
\geq
\left\lfloor\frac{k}{d}\right\rfloor
+
\left\lfloor\frac{r}{d}\right\rfloor,
$$
the multiplicity in $N$ is at least the multiplicity in $D$.

For completeness, if
$$
a=\left\lfloor\frac{k}{d}\right\rfloor,
\qquad
b=\left\lfloor\frac{r}{d}\right\rfloor,
$$
then $k\geq ad$ and $r\geq bd$, so
$$
k+r\geq(a+b)d,
$$
which gives the displayed floor inequality.
:::

:::

::: {.pf-step #divides-over-complex}
The polynomial $D$ divides $N$ in $\CC[q]$.

::: pf-proof
Each factor $[n]_q$ is monic and splits into distinct linear factors
over $\CC$, so $D$ splits completely over $\CC$. Step [](#multiplicity-comparison){.pf-ref} says that
every linear factor of $D$, with its full multiplicity, also occurs in
$N$. Therefore $D\mid N$ in $\CC[q]$.
:::

:::

::: {.pf-step #divides-over-integers}
In fact,
$$
D\mid N
$$
in $\ZZ[q]$.

::: pf-proof
Both $D$ and $N$ lie in $\ZZ[q]$, and $D$ is monic. Divide $N$ by
$D$ using the monic polynomial-division algorithm. Because the divisor
is monic, this produces
$$
N=DQ+S
$$
with $Q,S\in\ZZ[q]$ and either $S=0$ or $\deg S<\deg D$.
The same identity is the Euclidean division in $\CC[q]$. Step [](#divides-over-complex){.pf-ref}
shows that the remainder there is zero, so uniqueness of division gives
$S=0$. Hence $N=DQ$ with $Q\in\ZZ[q]$.
:::

:::

::: pf-qed
Step [](#divides-over-integers){.pf-ref} is precisely the required divisibility.
:::

:::

:::
