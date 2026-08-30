---
title: Which convergence theorem?
order: 0
problems:
  topics:
  - Convergence Theorems
  - Dominated Convergence
  - Fatou
---

# Which convergence theorem?

"Compute $\lim_n \int f_n$" is the most common instruction on the paper, and the whole question is which theorem licenses moving the limit inside.
There are four, they cost different amounts, and a problem is usually testing whether you noticed which hypothesis is missing.

## The four, and what each costs

| Theorem | Needs | Gives |
| --- | --- | --- |
| Monotone convergence | $0 \leq f_n \nearrow f$ pointwise | $\int f_n \to \int f$ |
| Fatou | $f_n \geq 0$ | $\int \liminf f_n \leq \liminf \int f_n$ |
| Dominated convergence | $f_n \to f$ a.e. and $\abs{f_n}\leq g$ with $g \in L^1$ | $\int f_n \to \int f$, and $\norm{f_n - f}_1 \to 0$ |
| Bounded convergence | $\abs{f_n} \leq M$ on a finite measure space | $\int f_n \to \int f$ |

Monotone and dominated give equality; Fatou gives only an inequality, and gives it in one direction.
Bounded convergence is dominated convergence with $g$ a constant, which is only integrable when the measure is finite -- that is the whole difference.

## The decision

1. **Is the sequence monotone and nonnegative?** Use monotone convergence.
   No dominating function is needed, which is why this is the theorem for series of nonnegative terms: apply it to the partial sums to interchange $\sum$ and $\int$.

2. **Can you find an integrable dominating function?** Use dominated convergence.
   The hunt for $g$ is the actual work, and the standard sources are: a bound independent of $n$, the largest term of a convergent series, or $\abs{f_n} \leq \abs{f_1}$ when the sequence decreases.

3. **Is the measure finite and the sequence uniformly bounded?** Use bounded convergence, which needs no search at all.

4. **None of the above, and you only need an inequality?** Use Fatou.
   Also reach for Fatou when the answer is that the limit is *not* the integral of the limit: Fatou holding strictly is the diagnosis.

## When the interchange fails

If none applies, it is usually because it genuinely fails, and the problem wants the counterexample.
The three standard escapes of mass, worth knowing by name:

- **Escape to height:** $f_n = n\chi_{[0,1/n]}$ on $[0,1]$.
  $f_n \to 0$ pointwise, $\int f_n = 1$.

- **Escape to width:** $f_n = \frac1n \chi_{[0,n]}$ on $\RR$.
  Same, and this one is uniformly bounded, so it shows why bounded convergence needs finite measure.

- **Escape to infinity:** $f_n = \chi_{[n, n+1]}$.
  Same again, and it is the reason a pointwise limit says nothing about the integral on an infinite measure space.

In each case no integrable $g$ dominates, which is the precise reason dominated convergence does not apply.

## Nearby interchanges

The same question is asked about other pairs of limits, and the answers are on [[Real_Analysis/Basics/Commuting_Limits|Commuting limits]] --

- $\lim_n \int$ against $\int \lim_n$: this page.

- $\sum_k \int$ against $\int \sum_k$: monotone convergence for nonnegative terms, dominated convergence via $\sum\int\abs{f_k} < \infty$ otherwise, which is Tonelli and Fubini for counting measure.

- $\partial_t \int$ against $\int \partial_t$: differentiation under the integral, which is dominated convergence applied to difference quotients, and needs a dominating function for $\partial_t f$.

- $\int\int$ in either order: [[Real_Analysis/fubini-tonelli/index|Fubini and Tonelli]].

Every one of them is the same theorem wearing a different hat, which is worth noticing because a problem will state whichever form is least convenient.
