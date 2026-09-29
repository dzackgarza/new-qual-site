---
schema: qual/card@1
id: P-BKF05-9A
kind: problem
title: Convolution preserves rapid decrease on the integers
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained weighted-l1 argument, inserting the
    required absolute-value inequality before the binomial expansion. Also
    restored the malformed j-in-Z subscripts in the problem statement from
    the checked source.
---

::: {.problem}
A doubly infinite real sequence \((a_j)_{j\in\mathbb Z}\) is rapidly decreasing if, for every positive integer \(n\), the sequence \((j^na_j)_{j\in\mathbb Z}\) is bounded.
Let \((a_j)\) and \((b_j)\) be rapidly decreasing and define
\[
c_j=\sum_{k\in\mathbb Z}a_kb_{j-k}.
\]
Prove that the series defining every \(c_j\) converges and that \((c_j)\) is rapidly decreasing.
:::

::: {.solution}

For each integer $r\ge0$, set
$$
A_r=\sum_{j\in\ZZ}\abs{j}^r\abs{a_j},
\qquad
B_r=\sum_{j\in\ZZ}\abs{j}^r\abs{b_j},
$$
with the convention $\abs0^0=1$ when $r=0$.

::: pf

::: {.pf-step #Ar-Br-finite}
For every integer $r\ge0$,
$$
A_r<\infty
\qquad\text{and}\qquad
B_r<\infty.
$$

::: pf-proof
Rapid decrease of $(a_j)$ implies that there is a constant $C_r$ such
that
$$
\abs{j}^{r+2}\abs{a_j}\le C_r
$$
for every $j\in\ZZ$. Hence, for $j\ne0$,
$$
\abs{j}^r\abs{a_j}
\le
\frac{C_r}{\abs{j}^2}.
$$
Therefore
$$
\sum_{j\in\ZZ}\abs{j}^r\abs{a_j}
$$
converges by comparison with
$\sum_{j\ne0}\abs j^{-2}$. The same argument applies to $(b_j)$.
:::

:::

::: {.pf-step #cj-converges-absolutely}
For every $j\in\ZZ$, the series
$$
c_j=\sum_{k\in\ZZ}a_kb_{j-k}
$$
converges absolutely.

::: pf-proof
By step [](#Ar-Br-finite){.pf-ref} with $r=0$, both $(a_k)$ and $(b_\ell)$ are absolutely
summable. Hence
$$
\begin{aligned}
\sum_{k\in\ZZ}\abs{a_kb_{j-k}}
&\le
\sum_{k\in\ZZ}\sum_{\ell\in\ZZ}
\abs{a_k}\abs{b_\ell}
\\
&=
A_0B_0
<
\infty.
\end{aligned}
$$
Thus the defining series for $c_j$ is absolutely convergent.
:::

:::

::: {.pf-step #weighted-sum-finite}
For every positive integer $n$,
$$
\sum_{j\in\ZZ}\abs{j}^n\abs{c_j}<\infty.
$$

::: pf-proof
By absolute convergence from step [](#cj-converges-absolutely){.pf-ref} and the triangle inequality,
$$
\abs{c_j}
\le
\sum_{k\in\ZZ}\abs{a_k}\abs{b_{j-k}}.
$$
All terms below are nonnegative, so Tonelli's theorem permits
rearrangement:
$$
\begin{aligned}
\sum_{j\in\ZZ}\abs j^n\abs{c_j}
&\le
\sum_{j\in\ZZ}\sum_{k\in\ZZ}
\abs j^n\abs{a_k}\abs{b_{j-k}}
\\
&=
\sum_{k\in\ZZ}\sum_{\ell\in\ZZ}
\abs{k+\ell}^n\abs{a_k}\abs{b_\ell}.
\end{aligned}
$$
Since
$$
\abs{k+\ell}^n
\le
(\abs k+\abs\ell)^n
=
\sum_{i=0}^n
\binom ni
\abs k^i\abs\ell^{n-i},
$$
step [](#Ar-Br-finite){.pf-ref} gives
$$
\begin{aligned}
\sum_{j\in\ZZ}\abs j^n\abs{c_j}
&\le
\sum_{i=0}^n
\binom ni
\left(
\sum_{k\in\ZZ}\abs k^i\abs{a_k}
\right)
\left(
\sum_{\ell\in\ZZ}\abs\ell^{n-i}\abs{b_\ell}
\right)
\\
&=
\sum_{i=0}^n\binom ni A_iB_{n-i}
<
\infty.
\end{aligned}
$$
:::

:::

::: {.pf-step #cj-rapidly-decreasing}
The sequence $(c_j)$ is rapidly decreasing.

::: pf-proof
Fix a positive integer $n$. By step [](#weighted-sum-finite){.pf-ref}, the nonnegative series
$$
\sum_{j\in\ZZ}\abs j^n\abs{c_j}
$$
converges. Hence every term is bounded by its sum, so
$$
\sup_{j\in\ZZ}\abs{j^nc_j}
\le
\sum_{j\in\ZZ}\abs j^n\abs{c_j}
<
\infty.
$$
Thus $(j^nc_j)_{j\in\ZZ}$ is bounded for every positive integer $n$,
which is exactly rapid decrease.
:::

:::

::: {.pf-step #both-assertions}
Therefore every convolution sum defining $c_j$ converges, and
the convolution sequence is rapidly decreasing.

::: pf-proof
Step [](#cj-converges-absolutely){.pf-ref} proves convergence of every defining series, and step [](#cj-rapidly-decreasing){.pf-ref}
proves rapid decrease.
:::

:::

::: pf-qed
Step [](#both-assertions){.pf-ref} proves both required assertions.
:::

:::

:::
