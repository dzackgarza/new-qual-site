---
schema: qual/card@1
id: P-UCLARA17S-04
kind: problem
title: Binary digit functionals on measures have no weak-star convergent subsequence
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
For $n\ge1$, let $a_n:[0,1)\to\{0,1\}$ denote the $n$th digit in the binary expansion of $x$, so that
$$
x=\sum_{n\ge1}a_n(x)2^{-n}\qquad(x\in[0,1)).
$$
Remove ambiguity by requiring $\liminf a_n(x)=0$ for all $x\in[0,1)$. Let $M([0,1))$ denote the Banach space of finite complex Borel measures on $[0,1)$ and define linear functionals $L_n$ on $M([0,1))$ by
$$
L_n(\mu)=\int_0^1 a_n(x)\,d\mu(x).
$$
Show that no subsequence of $L_n$ converges in the weak-* topology on $M([0,1))^*$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If a subsequence $(L_{n_k})$ converges weak-* in $M([0,1))^*$, then for every $x\in[0,1)$ the scalar sequence $(a_{n_k}(x))_k$ converges.


::: pf-proof

Weak-* convergence in $M([0,1))^*$ means pointwise convergence on $M([0,1))$. For each $x\in[0,1)$, let $\delta_x$ be the Dirac measure at $x$. Then
$$
L_{n_k}(\delta_x)
=\int a_{n_k}(t)\,d\delta_x(t)
=a_{n_k}(x).
$$
Thus weak-* convergence would force $(a_{n_k}(x))_k$ to converge for every $x$.

:::

:::

::: {.pf-step #s1-2}

Given any strictly increasing sequence of indices
$$
n_1<n_2<\cdots,
$$
there exists $x\in[0,1)$ such that
$$
a_{n_k}(x)=
\begin{cases}
0,&k\text{ odd},\\
1,&k\text{ even}.
\end{cases}
$$


::: pf-proof

Define a binary sequence $(b_n)$ by
$$
b_{n_k}=
\begin{cases}
0,&k\text{ odd},\\
1,&k\text{ even},
\end{cases}
$$
and set $b_n=0$ for indices not among the $n_k$. Put
$$
x\coloneqq\sum_{n=1}^{\infty}b_n2^{-n}.
$$
The sequence $(b_n)$ has infinitely many zeros, so it satisfies the convention
$$
\liminf_{n\to\infty}b_n=0.
$$
Because it is not the all-ones sequence, its sum satisfies $x<1$; and because it is not eventually $1$, this is the prescribed binary expansion under the stated convention. Therefore
$$
a_n(x)=b_n
$$
for every $n$, giving the asserted values along the chosen indices.

:::

:::

::: {.pf-step #s1-3}

No subsequence of $(L_n)$ converges weak-*.


::: pf-proof

Suppose $(L_{n_k})$ were weak-* convergent. Choose the point $x$ from step [](#s1-2){.pf-ref}. Then
$$
a_{n_k}(x)=0,1,0,1,\ldots
$$
does not converge, contradicting step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
