---
schema: qual/card@1
id: P-TRIV-PR22
kind: problem
title: Maximum likelihood capture--recapture estimate
classification:
  areas: [prelim]
  topics:
  - Maximum Likelihood Estimation
  - Hypergeometric Distribution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 22, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
---

::: {.problem}
A reasonable way to estimate the number of birds in a large flock is to mark some of them.
Suppose M birds were selected, marked and then released.
Long time after, in a sample of n randomly selected birds X had the marker.
What is the most probable total amount of birds in the population?
Assume the flock was not mixed with other groups of birds.
:::

::: {.solution}

Let $N$ be the unknown total population size. Necessarily
$$
N\geq M+n-X.
$$

::: pf

::: pf-step

Conditional on $N$, the number $X$ of marked birds in the sample has the hypergeometric likelihood
$$
L(N)=P_N(X)
=\frac{\binom MX\binom{N-M}{n-X}}{\binom Nn}.
$$


::: pf-proof

Among the $N$ birds, $M$ are marked and $N-M$ are unmarked. A sample of $n$ birds contains exactly $X$ marked birds in $\binom MX\binom{N-M}{n-X}$ ways, while there are $\binom Nn$ equally likely samples in total.

:::

:::

::: {.pf-step #s1-2}

For admissible consecutive population sizes,
$$
\frac{L(N+1)}{L(N)}
=\frac{(N+1-M)(N+1-n)}{(N+1)(N+1-M-n+X)}.
$$


::: pf-proof

The factor $\binom MX$ cancels. Using
$$
\frac{\binom{r+1}{k}}{\binom rk}=\frac{r+1}{r+1-k}
$$
for the numerator and
$$
\frac{\binom Nn}{\binom{N+1}n}=\frac{N+1-n}{N+1}
$$
for the denominator gives the displayed ratio.

:::

:::

::: {.pf-step #s1-3}

The likelihood is nondecreasing from $N$ to $N+1$ exactly when
$$
NX\leq Mn-X.
$$


::: pf-proof

Comparing the ratio in step [](#s1-2){.pf-ref} with $1$ gives
$$
(N+1-M)(N+1-n)
\geq(N+1)(N+1-M-n+X).
$$
Expanding and cancelling common terms leaves
$$
Mn-X(N+1)\geq0,
$$
which is $NX\leq Mn-X$.

:::

:::

::: {.pf-step #s1-4}

If $X>0$, the maximum-likelihood population size is therefore the integer nearest the transition point $Mn/X$, with the exact rule
$$
\boxed{\widehat N=\left\lfloor\frac{Mn}{X}\right\rfloor}
$$
unless $Mn/X$ is an integer, in which case both
$$
\boxed{\widehat N=\frac{Mn}{X}-1\quad\text{and}\quad\widehat N=\frac{Mn}{X}}
$$
maximize the likelihood.


::: pf-proof

Step [](#s1-3){.pf-ref} says $L(N+1)\geq L(N)$ precisely for $N+1\leq Mn/X$. Thus the likelihood increases until the ratio crosses $1$ and decreases afterward. If $Mn/X$ is not an integer, the last increase ends at $\lfloor Mn/X\rfloor$, which is the unique maximizer. If $Mn/X=K$ is an integer, then $L(K)=L(K-1)$ and the adjacent ratios on either side are respectively greater and less than $1$, so both $K-1$ and $K$ are maximizers.

:::

:::

::: {.pf-step #s1-5}

In the usual large-population interpretation, this is the capture--recapture estimate
$$
\boxed{N\approx\frac{Mn}{X}}.
$$


::: pf-proof

The observed marked fraction $X/n$ estimates the population marked fraction $M/N$. Solving $X/n=M/N$ gives $N=Mn/X$, agreeing with the exact likelihood transition in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

If $X=0$, there is no finite maximum-likelihood estimate of $N$.


::: pf-proof

With no recaptured marked birds, step [](#s1-2){.pf-ref} becomes
$$
\frac{L(N+1)}{L(N)}
=\frac{(N+1-M)(N+1-n)}{(N+1)(N+1-M-n)}>1
$$
for admissible finite $N$, so the likelihood increases toward its supremum as $N\to\infty$.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give the maximum-likelihood answer, including the integer tie and zero-recapture cases.

:::

:::

:::
