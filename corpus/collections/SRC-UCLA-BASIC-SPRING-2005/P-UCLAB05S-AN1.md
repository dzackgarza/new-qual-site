---
schema: qual/card@1
id: P-UCLAB05S-AN1
kind: problem
title: Algebraic subsets of the real line defined by rational polynomials
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 1 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
For a subset $X\subset\mathbb R$, say that $X$ is *algebraic* if there exists a family $\mathcal F$ of polynomials with rational coefficients such that
\[
x\in X
\quad\Longleftrightarrow\quad
p(x)=0\text{ for some }p\in\mathcal F.
\]

(a) Show that the set $\mathbb Q$ of rational numbers is algebraic.

(b) Show that the set $\mathbb R\setminus\mathbb Q$ of irrational numbers is not algebraic.
:::

::: pf

::: pf-step

The set $\QQ$ is algebraic.


::: pf-proof

For each rational number $q\in\QQ$, the polynomial
$$
p_q(x)\coloneqq x-q
$$
has rational coefficients and has the single real zero $q$. Therefore, with
$$
\mathcal F\coloneqq\{p_q:q\in\QQ\},
$$
one has
$$
x\in\QQ
\iff
p_q(x)=0\text{ for some }q\in\QQ.
$$
Hence $\QQ$ is algebraic.

:::

:::

::: pf-step

The set $\QQ[x]$ of rational-coefficient polynomials is countable.


::: pf-proof

For each $d\ge0$, the polynomials of degree at most $d$ are parametrized by the coefficient tuples
$$
(a_0,\ldots,a_d)\in\QQ^{d+1}.
$$
Since $\QQ$ is countable, each finite Cartesian power $\QQ^{d+1}$ is countable. Thus
$$
\QQ[x]=\bigcup_{d=0}^{\infty}\{p:\deg p\le d\}
$$
is a countable union of countable sets, hence countable.

:::

:::

::: pf-step

If $X\subseteq\RR$ is algebraic, then either $X=\RR$ or $X$ is countable.


::: pf-proof

Let $\mathcal F\subseteq\QQ[x]$ define $X$. If the zero polynomial belongs to $\mathcal F$, then every real number is a zero of a polynomial in $\mathcal F$, so $X=\RR$.

Otherwise every polynomial in $\mathcal F$ is nonzero and therefore has only finitely many real zeros. By step <1>2, the family $\mathcal F$ is countable. Hence $X$ is a countable union of finite sets and is therefore countable.

:::

:::

::: pf-step

The set $\RR\setminus\QQ$ is not algebraic.


::: pf-proof

The rationals are countable and the reals are uncountable, so $\RR\setminus\QQ$ is uncountable. It is also a proper subset of $\RR$. Step <1>3 shows that no algebraic set can have both properties. Therefore $\RR\setminus\QQ$ is not algebraic.

:::

:::

::: pf-qed

Step <1>1 proves part (a), and step <1>4 proves part (b).

:::

:::
