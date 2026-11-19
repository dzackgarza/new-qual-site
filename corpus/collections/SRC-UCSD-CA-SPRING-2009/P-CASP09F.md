---
schema: qual/card@1
id: P-CASP09F
kind: problem
title: "Statement and proof of the Weierstrass Product Theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/SP09_220_Complex_Analysis_Qual.pdf,
    problem 6: "State and prove the Weierstrass Product Theorem. You may use any general convergence
    criteria without proof, but you should state what these criteria are." The card's statement is
    that problem, and the criteria the exam asks to be stated are now stated as a step.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, with one gap closed. The prose said to
    choose p_n "so large that for every integer R >= 1 the tail satisfies sum (R/|a_n|)^(p_n+1) <
    infinity", which assumes the choice is possible without producing it; the proof now fixes
    p_n = n and proves the convergence from |a_n| -> infinity, since eventually |a_n| > 2R and the
    terms are then dominated by 2^{-(n+1)}. Checked the primary-factor expansion
    log E_p(w) = -sum_{k>p} w^k/k for |w| < 1, the bound |log E_p(w)| <= 2|w|^{p+1} for
    |w| <= 1/2, that the tail product is nonvanishing on a compact set off the zeros, that each
    factor vanishes to first order at z = a_n, and that h = f/(z^m P) is nonvanishing and entire so
    that simple connectivity of C supplies a logarithm. No retained published solution covers this
    problem, so the argument is the card's own.
---

::: {.problem}
State and prove the Weierstrass Product Theorem.
You may use any general convergence criteria without proof, but you should state what these criteria are.
:::

::: {.solution}
This is Problem 6 of the UCSD complex-analysis qualifying exam of Spring 2009 (`assets/attachments/SP09_220_Complex_Analysis_Qual.pdf`), which asks for the statement, the proof, and the statement of any convergence criterion used. No published solution set is transcribed: the argument is the card's own, following the standard proof through the primary factors.

What was sharpened: the card chose the exponents $p_{n}$ by requiring a tail series to converge, which presumes such a choice; the proof now takes $p_{n}=n$ and verifies the convergence, which is what makes the choice legitimate.

::: pf

::: {.pf-step #criteria}
The two convergence criteria used, both stated as the exam requires: (i) if $(v_{n})$ is a sequence of holomorphic functions on a domain $D$ and $\sum_{n}\sup_{K}\abs{v_{n}}<\infty$ for every compact $K\subset D$, then $\sum_{n}v_{n}$ converges uniformly on each compact $K$ to a holomorphic function; (ii) if $\sum_{n}\sup_{K}\abs{w_{n}}<\infty$ with $\sup_{K}\abs{w_{n}}<1$ for all but finitely many $n$, then $\prod_{n}(1+w_{n})$ converges uniformly on $K$, to a nonzero limit when no factor vanishes on $K$.

::: pf-proof
These are the Weierstrass $M$-test for series and its product form: uniform convergence on compacts of a series of holomorphic functions has a holomorphic sum (Weierstrass' theorem), and a product $\prod(1+w_{n})$ converges uniformly on $K$ once $\sum_{n}\sup_{K}\abs{w_{n}}$ converges, with $\prod(1+w_{n})\neq0$ on $K$ when every factor is nonzero there. They are used in steps [](#convergence){.pf-ref} and [](#zeros){.pf-ref}.
:::
:::

::: {.pf-step #primary}
For $p\geq0$ the primary factor $E_{p}(w)=(1-w)\exp\left(w+\frac{w^{2}}{2}+\cdots+\frac{w^{p}}{p}\right)$, with $E_{0}(w)=1-w$, is entire, $E_{p}(0)=1$, and for $\abs{w}\leq\frac12$ one has $\log E_{p}(w)=-\sum_{k=p+1}^{\infty}\frac{w^{k}}{k}$ and $\abs{\log E_{p}(w)}\leq2\abs{w}^{p+1}$.

::: pf-proof
$E_{p}$ is a product of entire functions and $E_{p}(0)=1$. For $\abs{w}<1$ the power series $\log(1-w)=-\sum_{k\geq1}w^{k}/k$ converges, and adding $\sum_{k=1}^{p}w^{k}/k$ leaves $-\sum_{k\geq p+1}w^{k}/k$. For $\abs{w}\leq\frac12$,
$$\abs{\log E_{p}(w)}\leq\sum_{k\geq p+1}\frac{\abs{w}^{k}}{k}\leq\abs{w}^{p+1}\sum_{j\geq0}\abs{w}^{j}\leq2\abs{w}^{p+1}.$$
:::
:::

::: {.pf-step #choice}
Given a sequence $(a_{n})$ of nonzero complex numbers with $\abs{a_{n}}\to\infty$, the exponents $p_{n}=n$ satisfy: for every $R\geq1$, $\sum_{n}\left(\frac{R}{\abs{a_{n}}}\right)^{p_{n}+1}<\infty$.

::: pf-proof
Since $\abs{a_{n}}\to\infty$ there is $N$ with $\abs{a_{n}}>2R$ for $n\geq N$, and then $\frac{R}{\abs{a_{n}}}\leq\frac12$, so $\left(\frac{R}{\abs{a_{n}}}\right)^{n+1}\leq2^{-(n+1)}$ for $n\geq N$; the series is therefore bounded by the finite sum of its first $N-1$ terms plus $\sum_{n\geq N}2^{-(n+1)}<\infty$.
:::
:::

::: {.pf-step #convergence}
$P(z)=\prod_{n=1}^{\infty}E_{n}(z/a_{n})$ converges uniformly on every compact subset of $\CC$ to an entire function.

::: pf-proof
Fix $R\geq1$ and let $\abs{z}\leq R$. For $n\geq N$ as in step [](#choice){.pf-ref} one has $\abs{z/a_{n}}\leq\frac{R}{\abs{a_{n}}}\leq\frac12$, so by step [](#primary){.pf-ref}
$$\abs{\log E_{n}(z/a_{n})}\leq2\left(\frac{R}{\abs{a_{n}}}\right)^{n+1},$$
and the sum of these bounds over $n$ converges by step [](#choice){.pf-ref}. So the series of logarithms converges uniformly on $\abs{z}\leq R$ and, by criterion (i) of step [](#criteria){.pf-ref}, so does the product, to a holomorphic function; the finitely many remaining factors are holomorphic. As the discs $\abs{z}\leq R$ exhaust $\CC$, $P$ is entire.
:::
:::

::: {.pf-step #zeros}
On a compact set $K$ containing no $a_{n}$ the product $P$ is nonzero, and the zeros of $P$ are exactly the points $a_{n}$, with the multiplicity of $a_{n}$ in the product.

::: pf-proof
Choose $R$ with $K\subset\abs{z}\leq R$ and $N$ with $\abs{a_{n}}>2R$ for $n\geq N$. On $K$ every factor $E_{n}(z/a_{n})$ with $n\geq N$ is nonvanishing, because $\log E_{n}(z/a_{n})=-\sum_{k>n}(z/a_{n})^{k}/k$ is defined there and the exponential of a holomorphic function does not vanish; the tail product is therefore nonzero on $K$ by criterion (ii) of step [](#criteria){.pf-ref}. The finitely many factors with $n<N$ vanish exactly at $z=a_{n}$, and each $E_{n}(z/a_{n})$ vanishes at $z=a_{n}$ to the first order because its logarithmic derivative there is $\frac{1}{z-a_{n}}$ plus a holomorphic term; distinct points $a_{n}$ give distinct zeros of $P$, and repeated values of $a_{n}$ contribute one such factor each, which is the multiplicity.
:::
:::

::: {.pf-step #factorization}
Every entire $f\not\equiv0$ with a zero of multiplicity $m$ at $0$ and nonzero zeros $(a_{n})$ listed with multiplicity satisfies $f(z)=z^{m}e^{g(z)}P(z)$ for some entire $g$ and some choice of the exponents.

::: pf-proof
Let $P$ be the product of step [](#convergence){.pf-ref} for $(a_{n})$ and any admissible exponents. Then $h=f/(z^{m}P)$ is holomorphic and nonvanishing on $\CC$: the numerator and denominator have the same zeros with the same multiplicities by step [](#zeros){.pf-ref}. The plane is simply connected, so $h$ has an entire logarithm $g$ with $e^{g}=h$, and then $f=z^{m}e^{g}P$.
:::
:::
:::

:::
