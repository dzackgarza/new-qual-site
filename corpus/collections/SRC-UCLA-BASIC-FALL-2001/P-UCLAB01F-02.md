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
Let $\mathbb N$ denote the positive integers and define
\[
a_n=\frac{(-1)^n}{n}.
\]
Let $\alpha\in\mathbb R$.
Prove that there is a bijection $\sigma:\mathbb N\to\mathbb N$ such that
\[
\sum_{n=1}^{\infty}a_{\sigma(n)}=\alpha.
\]
:::

::: {.solution}
Write
\[
p_k=a_{2k}=\frac1{2k},
\qquad
q_k=a_{2k-1}=-\frac1{2k-1}.
\]

<1>1. The positive subseries diverges to $+\infty$, while the negative subseries diverges to $-\infty$.

::: {.proof}
One has
\[
\sum_{k=1}^{\infty}p_k
=
\frac12\sum_{k=1}^{\infty}\frac1k
=+\infty.
\]
Also
\[
-q_k=\frac1{2k-1}\ge \frac1{2k},
\]
so
\[
\sum_{k=1}^{\infty}(-q_k)
\ge
\frac12\sum_{k=1}^{\infty}\frac1k
=+\infty.
\]
Hence
\[
\sum_{k=1}^{\infty}q_k=-\infty.
\]
:::

<1>2. Construct a rearranged sequence by alternately taking unused positive terms until the running sum exceeds $\alpha$, then unused negative terms until it is below $\alpha$.

::: {.proof}
Start with sum $0$. By step <1>1, after finitely many unused positive terms the running sum is greater than $\alpha$. Then, again by step <1>1, after finitely many unused negative terms it is less than $\alpha$. Repeat this procedure indefinitely.

Within each positive block use
\[
p_1,p_2,p_3,\ldots
\]
in their natural order, and within each negative block use
\[
q_1,q_2,q_3,\ldots
\]
in their natural order. Thus no term is ever repeated.
:::

<1>3. Every $p_k$ and every $q_k$ occurs after finitely many stages.

::: {.proof}
Each positive block is nonempty: immediately before a positive block the running sum is below $\alpha$, so at least one positive term is required before it can exceed $\alpha$. Therefore after $r$ positive blocks at least the first $r$ positive terms have been used. Hence every fixed $p_k$ eventually occurs.

Likewise, each negative block is nonempty, because immediately before it the running sum is above $\alpha$. Therefore every fixed $q_k$ eventually occurs.
:::

<1>4. The order constructed in step <1>2 defines a bijection
\[
\sigma:\mathbb N\to\mathbb N.
\]

::: {.proof}
Step <1>2 shows that no original term is used twice, so the resulting map from positions in the rearranged series to original indices is injective. Step <1>3 shows that every even index $2k$ and every odd index $2k-1$ eventually appears, so the map is surjective. Hence it is a bijection.
:::

<1>5. Let $S_m$ denote the partial sums of the rearranged series. The overshoots above and below $\alpha$ tend to $0$.

::: {.proof}
At the end of a positive block, the running sum has just crossed from at most $\alpha$ to above $\alpha$. If the last added positive term is $p_k$, then
\[
0<S_m-\alpha\le p_k.
\]
By step <1>3, the indices $k$ of these terminal positive terms tend to infinity as the blocks proceed, and therefore $p_k\to0$.

Similarly, at the end of a negative block, if the last added term is $q_k$, then the previous running sum was at least $\alpha$ and
\[
0<\alpha-S_m\le -q_k.
\]
Again $k\to\infty$ through successive negative blocks and $q_k\to0$. Thus both kinds of overshoot tend to $0$.
:::

<1>6. The rearranged series converges to
\[
\boxed{\alpha}.
\]

::: {.proof}
Fix $\varepsilon>0$. Since $p_k\to0$ and $q_k\to0$, choose $K$ such that
\[
p_k<\varepsilon
\qquad\text{and}\qquad
-q_k<\varepsilon
\]
whenever $k\ge K$. By step <1>3, after finitely many blocks all subsequently used terms have indices at least $K$ within their respective positive or negative subsequences.

From then on, the endpoint of every positive block lies in
\[
(\alpha,\alpha+\varepsilon),
\]
and the endpoint of every negative block lies in
\[
(\alpha-\varepsilon,\alpha).
\]
During a positive block the partial sums increase from the preceding negative-block endpoint to the next positive-block endpoint, and during a negative block they decrease between the corresponding endpoints. Hence every sufficiently late partial sum lies in
\[
(\alpha-\varepsilon,\alpha+\varepsilon).
\]
Therefore $S_m\to\alpha$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>4 gives the required bijection $\sigma$, and step <1>6 proves that the rearranged series determined by $\sigma$ has sum $\alpha$.
:::
:::
