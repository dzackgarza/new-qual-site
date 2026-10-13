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
<1>1. For each nonnegative integer $n$, the set
\[
\mathbb Z^{n+1}
\]
is countable.

::: {.proof}
The integers are countable, and every finite Cartesian product of countable sets is countable. Therefore $\mathbb Z^{n+1}$ is countable.
:::

<1>2. The set $\mathcal P$ of all nonzero polynomials with integer coefficients is countable.

::: {.proof}
Every such polynomial has the form
\[
p(X)=a_0+a_1X+\cdots+a_nX^n
\]
for some $n\ge0$ and some tuple
\[
(a_0,\ldots,a_n)\in\mathbb Z^{n+1}
\]
that is not identically zero. Hence $\mathcal P$ is the image of a subset of the countable union
\[
\bigcup_{n=0}^{\infty}\mathbb Z^{n+1}.
\]
By step <1>1, each term in this union is countable, so the union and therefore $\mathcal P$ are countable.
:::

<1>3. Every polynomial $p\in\mathcal P$ has only finitely many real roots.

::: {.proof}
A nonzero polynomial of degree $d$ over a field has at most $d$ roots. In particular, each $p\in\mathcal P$ has a finite set
\[
Z_{\mathbb R}(p)=\{x\in\mathbb R:p(x)=0\}
\]
of real roots.
:::

<1>4. The set of algebraic real numbers is
\[
\bigcup_{p\in\mathcal P}Z_{\mathbb R}(p).
\]

::: {.proof}
By definition, a real number $\alpha$ is algebraic exactly when it is a root of some nonzero polynomial with integer coefficients.
:::

<1>5. The set of algebraic real numbers is countable.

::: {.proof}
By step <1>2, the index set $\mathcal P$ is countable. By step <1>3, each set $Z_{\mathbb R}(p)$ is finite. Therefore the union in step <1>4 is a countable union of finite sets, hence countable.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
