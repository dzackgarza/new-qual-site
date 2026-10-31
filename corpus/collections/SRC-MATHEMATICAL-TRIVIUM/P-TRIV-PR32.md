---
schema: qual/card@1
id: P-TRIV-PR32
kind: problem
title: Almost sure convergence of the random harmonic series $\sum \xi_n/n$
classification:
  areas: [prelim]
  topics:
  - Kolmogorov Three-Series Theorem
  - Random Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the values +1 or -1 and removed stray residue against Probability Problem 32 on page 32 of the source PDF.
---

::: {.problem}
It is known that the series $\sum_{n=1}^\infty \frac{1}{n}$ diverges while the series $\sum_{n=1}^\infty \frac{(-1)^n}{n}$ converges.
One may ask about the convergence or divergence of the series $\sum_{n=1}^\infty \frac{\xi_n}{n}$, where $\xi_n$ are independent random variables taking the values $+1$ or $-1$ with the probabilities $p$ and $q = 1 - p$ correspondingly.

(a) Show that if $p = q = \frac{1}{2}$, the series converges with the unit probability.

(b) Show that otherwise the series diverges with the unit probability.
:::

::: {.solution}

Write
$$
\mu=\mathbf E\xi_n=p-q=2p-1
$$
and define the centered variables
$$
X_n=\frac{\xi_n-\mu}{n}.
$$

::: pf

::: pf-step

The variables $X_n$ are independent, have mean zero, and satisfy
$$
\sum_{n=1}^{\infty}\mathbf E X_n^2<\infty.
$$


::: pf-proof

Independence is preserved by applying a deterministic affine function separately to each $\xi_n$, and $\mathbf EX_n=0$ by definition of $\mu$. Moreover,
$$
\mathbf E X_n^2
=\frac{\operatorname{Var}(\xi_n)}{n^2}
=\frac{1-\mu^2}{n^2}
=\frac{4pq}{n^2}.
$$
Since $\sum n^{-2}<\infty$, the variance series converges.

:::

:::

::: {.pf-step #s1-2}

The centered series
$$
\sum_{n=1}^{\infty}X_n
=\sum_{n=1}^{\infty}\frac{\xi_n-\mu}{n}
$$
converges almost surely.


::: pf-proof

Let $S_N=\sum_{n=1}^NX_n$. For integers $m>N$, Kolmogorov's maximal inequality gives
$$
P\left(\max_{N<k\leq m}\abs{S_k-S_N}>\epsilon\right)
\leq\frac1{\epsilon^2}\sum_{n=N+1}^{m}\mathbf EX_n^2.
$$
Choose an increasing sequence $N_j$ such that
$$
\sum_{n>N_j}\mathbf EX_n^2\leq2^{-3j}.
$$
With $\epsilon=2^{-j}$ and then $m\to\infty$, the probability that some tail partial sum after $N_j$ differs from $S_{N_j}$ by more than $2^{-j}$ is at most $2^{-j}$. The sum of these probabilities is finite, so Borel--Cantelli implies that almost surely only finitely many such events occur. Hence $(S_N)$ is almost surely Cauchy and therefore convergent.

:::

:::

::: {.pf-step #s1-3}

If $p=q=1/2$, then $\mu=0$ and
$$
\boxed{\sum_{n=1}^{\infty}\frac{\xi_n}{n}\text{ converges almost surely}.}
$$


::: pf-proof

When $p=q=1/2$, the centered summand $X_n$ equals $\xi_n/n$. Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

For arbitrary $p$, the partial sums decompose as
$$
\sum_{n=1}^{N}\frac{\xi_n}{n}
=\sum_{n=1}^{N}X_n
+\mu\sum_{n=1}^{N}\frac1n.
$$


::: pf-proof

From the definition of $X_n$,
$$
\frac{\xi_n}{n}=X_n+\frac\mu n.
$$
Sum this identity from $1$ to $N$.

:::

:::

::: {.pf-step #s1-5}

If $p\ne q$, then $\mu\ne0$, and
$$
\boxed{\sum_{n=1}^{\infty}\frac{\xi_n}{n}\text{ diverges almost surely}.}
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the first term on the right side of step [](#s1-4){.pf-ref} converges almost surely to a finite random limit. The harmonic partial sums tend to $+\infty$. Since $\mu\ne0$, the second term tends to $+\infty$ when $p>q$ and to $-\infty$ when $p<q$. Adding an almost surely convergent sequence cannot cancel this divergence.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
