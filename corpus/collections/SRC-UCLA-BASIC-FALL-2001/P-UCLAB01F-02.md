---
schema: qual/card@1
id: P-UCLAB01F-02
kind: problem
title: Rearrange the alternating harmonic series to any prescribed real sum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Let $\NN$ denote the positive integers and define
$$
a_n=\frac{(-1)^n}{n}.
$$
Let $\alpha\in\RR$.
Prove that there is a bijection $\sigma:\NN\to\NN$ such that
$$
\sum_{n=1}^{\infty}a_{\sigma(n)}=\alpha.
$$
:::

::: {.solution}

Write
$$
p_k=a_{2k}=\frac1{2k},
\qquad
q_k=a_{2k-1}=-\frac1{2k-1}.
$$

::: pf

::: {.pf-step #s1-1}

The positive subseries diverges to $+\infty$, while the negative subseries diverges to $-\infty$.


::: pf-proof

One has
$$
\sum_{k=1}^{\infty}p_k
=
\frac12\sum_{k=1}^{\infty}\frac1k
=+\infty.
$$
Also
$$
-q_k=\frac1{2k-1}\ge \frac1{2k},
$$
so
$$
\sum_{k=1}^{\infty}(-q_k)
\ge
\frac12\sum_{k=1}^{\infty}\frac1k
=+\infty.
$$
Hence
$$
\sum_{k=1}^{\infty}q_k=-\infty.
$$

:::

:::

::: {.pf-step #s1-2}

Construct a rearranged sequence by alternately taking unused positive terms until the running sum exceeds $\alpha$, then unused negative terms until it is below $\alpha$.


::: pf-proof

Start with sum $0$. By step [](#s1-1){.pf-ref}, after finitely many unused positive terms the running sum is greater than $\alpha$. Then, again by step [](#s1-1){.pf-ref}, after finitely many unused negative terms it is less than $\alpha$. Repeat this procedure indefinitely.

Within each positive block use
$$
p_1,p_2,p_3,\ldots
$$
in their natural order, and within each negative block use
$$
q_1,q_2,q_3,\ldots
$$
in their natural order. Thus no term is ever repeated.

:::

:::

::: {.pf-step #s1-3}

Every $p_k$ and every $q_k$ occurs after finitely many stages.


::: pf-proof

Each positive block is nonempty: immediately before a positive block the running sum is below $\alpha$, so at least one positive term is required before it can exceed $\alpha$. Therefore after $r$ positive blocks at least the first $r$ positive terms have been used. Hence every fixed $p_k$ eventually occurs.

Likewise, each negative block is nonempty, because immediately before it the running sum is above $\alpha$. Therefore every fixed $q_k$ eventually occurs.

:::

:::

::: {.pf-step #s1-4}

The order constructed in step [](#s1-2){.pf-ref} defines a bijection
$$
\sigma:\NN\to\NN.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} shows that no original term is used twice, so the resulting map from positions in the rearranged series to original indices is injective. Step [](#s1-3){.pf-ref} shows that every even index $2k$ and every odd index $2k-1$ eventually appears, so the map is surjective. Hence it is a bijection.

:::

:::

::: pf-step

Let $S_m$ denote the partial sums of the rearranged series. The overshoots above and below $\alpha$ tend to $0$.


::: pf-proof

At the end of a positive block, the running sum has just crossed from at most $\alpha$ to above $\alpha$. If the last added positive term is $p_k$, then
$$
0<S_m-\alpha\le p_k.
$$
By step [](#s1-3){.pf-ref}, the indices $k$ of these terminal positive terms tend to infinity as the blocks proceed, and therefore $p_k\to0$.

Similarly, at the end of a negative block, if the last added term is $q_k$, then the previous running sum was at least $\alpha$ and
$$
0<\alpha-S_m\le -q_k.
$$
Again $k\to\infty$ through successive negative blocks and $q_k\to0$. Thus both kinds of overshoot tend to $0$.

:::

:::

::: {.pf-step #s1-6}

The rearranged series converges to
$$
\boxed{\alpha}.
$$


::: pf-proof

Fix $\varepsilon>0$. Since $p_k\to0$ and $q_k\to0$, choose $K$ such that
$$
p_k<\varepsilon
\qquad\text{and}\qquad
-q_k<\varepsilon
$$
whenever $k\ge K$. By step [](#s1-3){.pf-ref}, after finitely many blocks all subsequently used terms have indices at least $K$ within their respective positive or negative subsequences.

From then on, the endpoint of every positive block lies in
$$
(\alpha,\alpha+\varepsilon),
$$
and the endpoint of every negative block lies in
$$
(\alpha-\varepsilon,\alpha).
$$
During a positive block the partial sums increase from the preceding negative-block endpoint to the next positive-block endpoint, and during a negative block they decrease between the corresponding endpoints. Hence every sufficiently late partial sum lies in
$$
(\alpha-\varepsilon,\alpha+\varepsilon).
$$
Therefore $S_m\to\alpha$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required bijection $\sigma$, and step [](#s1-6){.pf-ref} proves that the rearranged series determined by $\sigma$ has sum $\alpha$.

:::

:::

:::
