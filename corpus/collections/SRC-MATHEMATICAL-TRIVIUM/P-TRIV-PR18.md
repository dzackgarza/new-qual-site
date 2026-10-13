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
Consider the series ω of n experiments whose results are given by independent variables $\xi _ { i } , i = 1 , . . . , n$ , taking the values 1 (success) with the probability $p ,$ and 0 (fail) with the probability $q = 1 - p$ . Compose the sum $S _ { n } ( \omega ) = \xi _ { 1 } + . . . + \xi _ { n }$ . It is clear that for any typical series ω and for large n, $S _ { n } ( \omega ) / n$ must be close enough to p. But what is the total amount of the typical series and how it behaves as n grows?
Denote by $C ( n , \epsilon )$ all typical series, or, more precisely,

$$
C ( n , \epsilon ) = \left\{ \omega | \mathbf { \epsilon } \left| \frac { S _ { n } ( \omega ) } { n } - p \right| \leqslant \epsilon \right\} ,\tag{47}
$$

with some small $\epsilon .$

(a) Show that if $\omega \in C ( n , \epsilon )$ , then the probability $p ( \omega )$ of such series to realize is enclosed withing the region

$$
e ^ { - n ( H + \tilde { \epsilon } ) } \leqslant p ( \omega ) \leqslant e ^ { - n ( H - \tilde { \epsilon } ) } ,\tag{48}
$$

where

$$
\tilde { \epsilon } = \operatorname * { m a x } \left\{ \epsilon , \epsilon \left( - 2 \log ( p q ) \right) \right\} ,\tag{49}
$$

and the quantity

$$
H = - p \log p - q \log q\tag{50}
$$

is called entropy.

(b) Show that the total amount of the typical series lies in the region

$$
e ^ { n ( H - \tilde { \epsilon } ) } \leqslant N ( C ( n , \epsilon ) ) \leqslant e ^ { n ( H + \tilde { \epsilon } ) } .\tag{51}
$$

Hence the number of the typical series is exponentially large, while the probability of each of them is exponentially small.
:::

::: {.solution}
Assume $0<p<1$, put $q=1-p$, and write
\[
r=\frac{S_n(\omega)}n.
\]
For a typical sequence, $|r-p|\leq\epsilon$.

<1>1. A sequence with $nr$ successes has probability
\[
p(\omega)=p^{nr}q^{n(1-r)}.
\]

::: {.proof}
Independence gives one factor $p$ for each success and one factor $q$ for each failure. There are $nr$ successes and $n(1-r)$ failures.
:::

<1>2. Its logarithmic probability satisfies
\[
-\frac1n\log p(\omega)
=-r\log p-(1-r)\log q
=H+(r-p)\log\frac qp.
\]

::: {.proof}
Take logarithms in step <1>1 and divide by $-n$. Subtract
\[
H=-p\log p-q\log q
\]
and use $q=1-p$ to obtain
\[
-(r-p)\log p+(r-p)\log q
=(r-p)\log(q/p).
\]
:::

<1>3. If $\omega\in C(n,\epsilon)$, then
\[
\left|-\frac1n\log p(\omega)-H\right|
\leq\epsilon\left|\log\frac qp\right|
\leq\widetilde\epsilon,
\]
for the source's
\[
\widetilde\epsilon
=\max\{\epsilon,\epsilon(-2\log(pq))\}.
\]

::: {.proof}
The first inequality follows from step <1>2 and $|r-p|\leq\epsilon$. Since $0<p,q<1$,
\[
\left|\log\frac qp\right|
\leq|\log q|+|\log p|
=-\log(pq)
\leq-2\log(pq),
\]
and the definition of $\widetilde\epsilon$ gives the second inequality.
:::

<1>4. Therefore every typical sequence satisfies
\[
\boxed{
e^{-n(H+\widetilde\epsilon)}
\leq p(\omega)
\leq e^{-n(H-\widetilde\epsilon)}}.
\]

::: {.proof}
Step <1>3 is equivalent to
\[
H-\widetilde\epsilon
\leq-\frac1n\log p(\omega)
\leq H+\widetilde\epsilon.
\]
Multiply by $-n$, reverse the inequalities, and exponentiate.
:::

<1>5. The upper bound on the number $N(C(n,\epsilon))$ of typical sequences is
\[
\boxed{N(C(n,\epsilon))\leq e^{n(H+\widetilde\epsilon)}}.
\]

::: {.proof}
By the lower probability bound in step <1>4,
\[
1\geq P(C(n,\epsilon))
=\sum_{\omega\in C(n,\epsilon)}p(\omega)
\geq N(C(n,\epsilon))e^{-n(H+\widetilde\epsilon)}.
\]
Rearrange.
:::

<1>6. The source's unconditional lower bound
\[
e^{n(H-\widetilde\epsilon)}\leq N(C(n,\epsilon))
\]
does not follow from the definition of $C(n,\epsilon)$ and is false for finite $n$ in general.

::: {.proof}
From the upper probability bound in step <1>4 one only obtains
\[
P(C(n,\epsilon))
\leq N(C(n,\epsilon))e^{-n(H-\widetilde\epsilon)},
\]
hence
\[
N(C(n,\epsilon))
\geq P(C(n,\epsilon))e^{n(H-\widetilde\epsilon)}.
\]
The missing factor $P(C(n,\epsilon))$ cannot be replaced by $1$. For example, if $n=1$, $p=1/2$, and $0<\epsilon<1/2$, then $C(1,\epsilon)$ is empty, so its cardinality is $0$ while the claimed lower bound is positive.
:::

<1>7. Nevertheless, for every fixed $\epsilon>0$, the weak law of large numbers gives
\[
P(C(n,\epsilon))\longrightarrow1,
\]
and therefore
\[
N(C(n,\epsilon))
\geq P(C(n,\epsilon))e^{n(H-\widetilde\epsilon)}.
\]

::: {.proof}
Since $S_n/n$ is the sample mean of independent Bernoulli variables of mean $p$ and variance $pq$, Chebyshev's inequality gives
\[
P\left(\left|\frac{S_n}n-p\right|>\epsilon\right)
\leq\frac{pq}{n\epsilon^2}\to0.
\]
The cardinality inequality is the rearrangement obtained in step <1>6.
:::

<1>8. Thus the rigorous finite-$n$ bounds are
\[
\boxed{
P(C(n,\epsilon))e^{n(H-\widetilde\epsilon)}
\leq N(C(n,\epsilon))
\leq e^{n(H+\widetilde\epsilon)}},
\]
with $P(C(n,\epsilon))\to1$ as $n\to\infty$.

::: {.proof}
Combine steps <1>5 and <1>7. In particular, the typical-set cardinality has exponential scale $e^{nH}$ up to the stated exponential tolerance, while each typical sequence has probability on scale $e^{-nH}$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>4 proves part (a). Steps <1>5--<1>8 give the correct version of part (b) and identify the missing probability factor in the source's finite-$n$ lower bound.
:::
:::
