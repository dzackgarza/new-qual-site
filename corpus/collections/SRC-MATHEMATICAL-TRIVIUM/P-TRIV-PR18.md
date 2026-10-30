---
schema: qual/card@1
id: P-TRIV-PR18
kind: problem
title: Typical sequences and entropy for Bernoulli trials
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 18, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the series $\omega$ of $n$ experiments whose results are given by independent variables $\xi_i$, $i = 1, \ldots, n$, taking the values $1$ (success) with the probability $p$, and $0$ (fail) with the probability $q = 1 - p$. Compose the sum $S_n(\omega) = \xi_1 + \cdots + \xi_n$. It is clear that for any *typical* series $\omega$ and for large $n$, $S_n(\omega)/n$ must be close enough to $p$. But what is the total amount of the typical series and how it behaves as $n$ grows? Denote by $C(n, \epsilon)$ all typical series, or, more precisely,
$$
C(n, \epsilon) = \left\{ \omega \st \abs{\frac{S_n(\omega)}{n} - p} \leqslant \epsilon \right\}, \tag{47}
$$
with some small $\epsilon$.

(a) Show that if $\omega \in C(n, \epsilon)$, then the probability $p(\omega)$ of such series to realize is enclosed withing the region
$$
e^{-n(H + \tilde{\epsilon})} \leqslant p(\omega) \leqslant e^{-n(H - \tilde{\epsilon})}, \tag{48}
$$
where
$$
\tilde{\epsilon} = \max\left\{ \epsilon, \ \epsilon\left( -2\log(pq) \right) \right\}, \tag{49}
$$
and the quantity
$$
H = -p\log p - q\log q \tag{50}
$$
is called *entropy*.

(b) Show that the total amount of the typical series lies in the region
$$
e^{n(H - \tilde{\epsilon})} \leqslant N(C(n, \epsilon)) \leqslant e^{n(H + \tilde{\epsilon})}. \tag{51}
$$
Hence the number of the typical series is exponentially large, while the probability of each of them is exponentially small.
:::

::: {.solution}

Assume $0<p<1$, put $q=1-p$, and write
$$
r=\frac{S_n(\omega)}n.
$$
For a typical sequence, $\abs{r-p}\leq\epsilon$.

::: pf

::: {.pf-step #s1-1}

A sequence with $nr$ successes has probability
$$
p(\omega)=p^{nr}q^{n(1-r)}.
$$


::: pf-proof

Independence gives one factor $p$ for each success and one factor $q$ for each failure. There are $nr$ successes and $n(1-r)$ failures.

:::

:::

::: {.pf-step #s1-2}

Its logarithmic probability satisfies
$$
-\frac1n\log p(\omega)
=-r\log p-(1-r)\log q
=H+(r-p)\log\frac qp.
$$


::: pf-proof

Take logarithms in step [](#s1-1){.pf-ref} and divide by $-n$. Subtract
$$
H=-p\log p-q\log q
$$
and use $q=1-p$ to obtain
$$
-(r-p)\log p+(r-p)\log q
=(r-p)\log(q/p).
$$

:::

:::

::: {.pf-step #s1-3}

If $\omega\in C(n,\epsilon)$, then
$$
\abs{-\frac1n\log p(\omega)-H}
\leq\epsilon\abs{\log\frac qp}
\leq\widetilde\epsilon,
$$
for the source's
$$
\widetilde\epsilon
=\max\{\epsilon,\epsilon(-2\log(pq))\}.
$$


::: pf-proof

The first inequality follows from step [](#s1-2){.pf-ref} and $\abs{r-p}\leq\epsilon$. Since $0<p,q<1$,
$$
\abs{\log\frac qp}
\leq\abs{\log q}+\abs{\log p}
=-\log(pq)
\leq-2\log(pq),
$$
and the definition of $\widetilde\epsilon$ gives the second inequality.

:::

:::

::: {.pf-step #s1-4}

Therefore every typical sequence satisfies
$$
\boxed{
e^{-n(H+\widetilde\epsilon)}
\leq p(\omega)
\leq e^{-n(H-\widetilde\epsilon)}}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} is equivalent to
$$
H-\widetilde\epsilon
\leq-\frac1n\log p(\omega)
\leq H+\widetilde\epsilon.
$$
Multiply by $-n$, reverse the inequalities, and exponentiate.

:::

:::

::: {.pf-step #s1-5}

The upper bound on the number $N(C(n,\epsilon))$ of typical sequences is
$$
\boxed{N(C(n,\epsilon))\leq e^{n(H+\widetilde\epsilon)}}.
$$


::: pf-proof

By the lower probability bound in step [](#s1-4){.pf-ref},
$$
1\geq P(C(n,\epsilon))
=\sum_{\omega\in C(n,\epsilon)}p(\omega)
\geq N(C(n,\epsilon))e^{-n(H+\widetilde\epsilon)}.
$$
Rearrange.

:::

:::

::: {.pf-step #s1-6}

The source's unconditional lower bound
$$
e^{n(H-\widetilde\epsilon)}\leq N(C(n,\epsilon))
$$
does not follow from the definition of $C(n,\epsilon)$ and is false for finite $n$ in general.


::: pf-proof

From the upper probability bound in step [](#s1-4){.pf-ref} one only obtains
$$
P(C(n,\epsilon))
\leq N(C(n,\epsilon))e^{-n(H-\widetilde\epsilon)},
$$
hence
$$
N(C(n,\epsilon))
\geq P(C(n,\epsilon))e^{n(H-\widetilde\epsilon)}.
$$
The missing factor $P(C(n,\epsilon))$ cannot be replaced by $1$. For example, if $n=1$, $p=1/2$, and $0<\epsilon<1/2$, then $C(1,\epsilon)$ is empty, so its cardinality is $0$ while the claimed lower bound is positive.

:::

:::

::: {.pf-step #s1-7}

Nevertheless, for every fixed $\epsilon>0$, the weak law of large numbers gives
$$
P(C(n,\epsilon))\longrightarrow1,
$$
and therefore
$$
N(C(n,\epsilon))
\geq P(C(n,\epsilon))e^{n(H-\widetilde\epsilon)}.
$$


::: pf-proof

Since $S_n/n$ is the sample mean of independent Bernoulli variables of mean $p$ and variance $pq$, Chebyshev's inequality gives
$$
P\left(\abs{\frac{S_n}n-p}>\epsilon\right)
\leq\frac{pq}{n\epsilon^2}\to0.
$$
The cardinality inequality is the rearrangement obtained in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Thus the rigorous finite-$n$ bounds are
$$
\boxed{
P(C(n,\epsilon))e^{n(H-\widetilde\epsilon)}
\leq N(C(n,\epsilon))
\leq e^{n(H+\widetilde\epsilon)}},
$$
with $P(C(n,\epsilon))\to1$ as $n\to\infty$.


::: pf-proof

Combine steps [](#s1-5){.pf-ref} and [](#s1-7){.pf-ref}. In particular, the typical-set cardinality has exponential scale $e^{nH}$ up to the stated exponential tolerance, while each typical sequence has probability on scale $e^{-nH}$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a). Steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} give the correct version of part (b) and identify the missing probability factor in the source's finite-$n$ lower bound.

:::

:::

:::
