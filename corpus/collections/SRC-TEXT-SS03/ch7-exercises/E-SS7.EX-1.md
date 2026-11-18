---
schema: qual/card@1
id: E-SS7.EX-1
kind: problem
title: "Bounded partial sums give convergence of the Dirichlet series for $\\Re(s) > 0$"
classification:
  areas:
    - complex-analysis
  topics: ['Zeta Function', 'Prime Number Theorem', 'Dirichlet Series']
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the Abel summation identity, the boundary estimate $MN^{-\sigma}$, the integral form of the differences and its bound, and the uniform $M$-test bound $MCn^{-1-\delta}$ on compact subsets.
---

::: {.exercise}
Suppose that $\{a_n\}_{n=1}^{\infty}$ is a sequence of real numbers such that the partial sums
$$
A_n = a_1 + \cdots + a_n
$$
are bounded. Prove that the Dirichlet series
$$
\sum_{n=1}^{\infty} \frac{a_n}{n^s}
$$
converges for $\Re(s) > 0$ and defines a holomorphic function in this half-plane.

[Hint: Use summation by parts to compare the original (non-absolutely convergent) series to the (absolutely convergent) series $\sum A_n (n^{-s} - (n + 1)^{-s})$. An estimate for the term in parentheses is provided by the mean value theorem. To prove that the series is analytic, show that the partial sums converge uniformly on every compact subset of the half-plane $\Re(s) > 0$.]
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own. The proof is summation by parts followed by the integral estimate for the differences $n^{-s}-(n+1)^{-s}$, which gives absolute and locally uniform convergence on $\Re s>0$.

::: pf

::: {.pf-step #parts}
With $A_n=a_1+\cdots+a_n$ bounded by $M$, summation by parts gives $\sum_{n=1}^N\frac{a_n}{n^s}=A_NN^{-s}+\sum_{n=1}^{N-1}A_n\left(n^{-s}-(n+1)^{-s}\right)$.

::: pf-proof
Write $a_n=A_n-A_{n-1}$ and rearrange the finite sum, shifting the index in the $A_{n-1}$ term; this is Abel summation for the sequences $(a_n)$ and $(n^{-s})$.
:::
:::

::: {.pf-step #boundary}
For $\sigma=\Re s>0$ the boundary term $A_NN^{-s}$ tends to $0$.

::: pf-proof
$\abs{A_NN^{-s}}\le MN^{-\sigma}$ and $\sigma>0$, so the bound tends to $0$.
:::
:::

::: {.pf-step #difference}
$\abs{n^{-s}-(n+1)^{-s}}\le\abs s\,n^{-\sigma-1}$.

::: pf-proof
Since $\frac{d}{dx}x^{-s}=-sx^{-s-1}$, the mean value form gives $n^{-s}-(n+1)^{-s}=s\int_n^{n+1}x^{-s-1}dx$; bounding the integrand by $n^{-\sigma-1}$ on the interval of length $1$ gives the estimate.
:::
:::

::: {.pf-step #convergence}
The Dirichlet series converges for every $s$ with $\Re s>0$.

::: pf-proof
By steps [](#boundary){.pf-ref} and [](#difference){.pf-ref} the right side of step [](#parts){.pf-ref} is dominated in modulus by the convergent series $M\abs s\sum_n n^{-\sigma-1}$, so the partial sums converge.
:::
:::

::: {.pf-step #holomorphic}
The sum defines a holomorphic function of $s$ on $\Re s>0$.

::: pf-proof
On a compact $K$ in the half-plane there are $\delta>0$ and $C>0$ with $\Re s\ge\delta$ and $\abs s\le C$, so the terms of the series in step [](#parts){.pf-ref} are bounded uniformly by $MCn^{-1-\delta}$; the Weierstrass $M$-test gives uniform convergence of a series of holomorphic functions, and the boundary term tends to $0$ uniformly, so the limit is holomorphic.
:::
:::

:::
:::
