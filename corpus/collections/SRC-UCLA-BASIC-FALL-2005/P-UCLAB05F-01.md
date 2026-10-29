---
schema: qual/card@1
id: P-UCLAB05F-01
kind: problem
title: Countability of the algebraic real numbers
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
A real number $\alpha$ is called *algebraic* if there are integers $a_0,\ldots,a_n$, not all zero, such that
\[
a_0+a_1\alpha+\cdots+a_n\alpha^n=0.
\]
Prove that the set of algebraic real numbers is countable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For each nonnegative integer $n$, the set
\[
\ZZ^{n+1}
\]
is countable.


::: pf-proof

The integers are countable, and every finite Cartesian product of countable sets is countable. Therefore $\ZZ^{n+1}$ is countable.

:::

:::

::: {.pf-step #s1-2}

The set $\mathcal P$ of all nonzero polynomials with integer coefficients is countable.


::: pf-proof

Every such polynomial has the form
\[
p(X)=a_0+a_1X+\cdots+a_nX^n
\]
for some $n\ge0$ and some tuple
\[
(a_0,\ldots,a_n)\in\ZZ^{n+1}
\]
that is not identically zero. Hence $\mathcal P$ is the image of a subset of the countable union
\[
\bigcup_{n=0}^{\infty}\ZZ^{n+1}.
\]
By step [](#s1-1){.pf-ref}, each term in this union is countable, so the union and therefore $\mathcal P$ are countable.

:::

:::

::: {.pf-step #s1-3}

Every polynomial $p\in\mathcal P$ has only finitely many real roots.


::: pf-proof

A nonzero polynomial of degree $d$ over a field has at most $d$ roots. In particular, each $p\in\mathcal P$ has a finite set
\[
Z_{\RR}(p)=\{x\in\RR:p(x)=0\}
\]
of real roots.

:::

:::

::: {.pf-step #s1-4}

The set of algebraic real numbers is
\[
\bigcup_{p\in\mathcal P}Z_{\RR}(p).
\]


::: pf-proof

By definition, a real number $\alpha$ is algebraic exactly when it is a root of some nonzero polynomial with integer coefficients.

:::

:::

::: {.pf-step #s1-5}

The set of algebraic real numbers is countable.


::: pf-proof

By step [](#s1-2){.pf-ref}, the index set $\mathcal P$ is countable. By step [](#s1-3){.pf-ref}, each set $Z_{\RR}(p)$ is finite. Therefore the union in step [](#s1-4){.pf-ref} is a countable union of finite sets, hence countable.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
