---
title: The convergence theorems
order: 20
topics:
- Convergence of Integrals
- Convergence of Functions
---

# The convergence theorems

Which one a problem wants is [[real-analysis/integration/which-convergence-theorem|Which convergence theorem?]]; this page is their statements and proofs.

## Monotone convergence

Use monotone convergence for a nonnegative increasing sequence $f_n\uparrow f$.
It requires no integrable dominating function and allows the value $+\infty$; the order structure itself is what permits $\int f_n\uparrow\int f$.
This is why partial sums of nonnegative series are its most common application.

[[T-5K3IO]]

[[FT-5G4Y3]]

## Dominated convergence

Dominated convergence trades monotonicity for an integrable majorant.
If $f_n\to f$ almost everywhere and $|f_n|\le g\in L^1$, then $f\in L^1$ and the integrals converge; applying the theorem to $|f_n-f|$ also gives $L^1$ convergence.
On an exam, the substantive step is almost always producing the single function $g$.

[[T-IJQQG]]

[[FT-LCR5P]]

[[T-WYX24]]

[[PR-KNYSF]]

[[PR-H4ZVI]]

## Fatou

[[T-LDJNS]]

[[FT-P5UNP]]

::: {.remark title="Fatou is the primitive one"}
Monotone convergence and Fatou are equivalent, and dominated convergence is proved from Fatou applied to $2g - \abs{f_n - f}$, which is nonnegative and converges to $2g$.
So the inequality is the real content and the two equalities are corollaries -- worth knowing because a problem that blocks dominated convergence can often still be finished with Fatou directly.
:::

## Egorov and Lusin

Egorov is a finite-measure statement: it upgrades a.e. convergence to uniform convergence after discarding a set of arbitrarily small measure.
In the Lebesgue/Euclidean regularity setting used here, Lusin replaces a measurable function by a continuous one away from such a small exceptional set.
Neither is a substitute for dominated convergence; they change the set on which the problem is being considered.

[[T-XZE3E]]

[[T-CGFCU]]

## Commuting limits

Whenever a limit is moved through an integral, sum, derivative, or another limit, name the theorem that justifies the interchange.
Uniform convergence, domination, and monotonicity are different sufficient mechanisms, and the counterexamples in the surrounding chapter show that pointwise convergence by itself supplies none of them.

For series, summability of the $L^1$ norms is a particularly useful sufficient condition: it gives absolute convergence almost everywhere and in $L^1$, and then the sum and integral can be interchanged.
The cards below package that argument together with the more general interchange criteria.

[[T-MN6WQ]]

[[FS-BM2PV]]

[[PR-EHIXY]]

[[FR-KEWV2]]

[[PR-NKZBT]]

[[PR-YJJSY]]

[[PR-2CZUM]]
