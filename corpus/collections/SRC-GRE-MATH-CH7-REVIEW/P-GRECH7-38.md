---
schema: qual/card@1
id: P-GRECH7-38
kind: problem
title: Probability that one of two geometric-type variables exceeds $2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 38 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The two extractions read the domain as Z' and Z*; it is transcribed as the positive integers.
---

::: {.problem}
Let $X$ be a random variable on $\mathbb{Z}^+$ whose distribution function is $F_X(t)=1/3^t$. Suppose that $W$ is another random variable whose distribution function is $F_Y(t)=1/4^t$. What is the probability that at least one of the variables $X$ and $Y$ is greater than $2$?

(A) $5/6$
(B) $64/81$
(C) $1/2$
(D) $17/81$
(E) $1/6$
:::

::: pf

::: {.pf-step #s1-1}

The functions printed in the problem cannot be cumulative distribution functions.


::: pf-proof

For a random variable $X$, the cumulative distribution function
$$
F_X(t)=\mathbb P(X\le t)
$$
must be nondecreasing in $t$. But the printed function satisfies
$$
F_X(1)=\frac13>\frac19=F_X(2),
$$
and similarly $F_Y(1)=1/4>1/16=F_Y(2)$. Thus neither printed function is a cumulative distribution function.

:::

:::

::: {.pf-step #s1-2}

The source solution instead treats the printed quantities as tail probabilities
$$
\mathbb P(X>t)=3^{-t},
\qquad
\mathbb P(Y>t)=4^{-t}.
$$


::: pf-proof

At $t=2$, that interpretation gives
$$
\mathbb P(X\le2)=1-\frac19=\frac89
$$
and
$$
\mathbb P(Y\le2)=1-\frac1{16}=\frac{15}{16},
$$
which are exactly the two factors used in the source's computation. Equivalently, the intended cumulative distribution functions would be $1-3^{-t}$ and $1-4^{-t}$ on the relevant positive-integer values.

:::

:::

::: {.pf-step #s1-3}

Even after the correction in step [](#s1-2){.pf-ref}, the requested probability is not determined unless a dependence relation between $X$ and $Y$ is specified.


::: pf-proof

Let
$$
A=\{X>2\},\qquad B=\{Y>2\}.
$$
Step [](#s1-2){.pf-ref} gives
$$
\mathbb P(A)=\frac19,
\qquad
\mathbb P(B)=\frac1{16}.
$$
But
$$
\mathbb P(A\cup B)
=\frac19+\frac1{16}-\mathbb P(A\cap B),
$$
and the marginal distributions do not determine $\mathbb P(A\cap B)$. For example, an independent coupling gives $\mathbb P(A\cap B)=1/144$, whereas a coupling in which $B\subseteq A$ almost surely gives $\mathbb P(A\cap B)=1/16$. Such couplings with the prescribed marginals can be obtained from independent uniforms in the first case and a common uniform via inverse-transform sampling in the second. Hence the union probability is not fixed by the stated marginal information.

:::

:::

::: {.pf-step #s1-4}

If one additionally assumes independence, as the source solution does, then
$$
\mathbb P(X>2\text{ or }Y>2)=\boxed{\frac16},
$$
so the intended answer is (E).


::: pf-proof

Under independence,
$$
\begin{aligned}
\mathbb P(X>2\text{ or }Y>2)
&=1-\mathbb P(X\le2,Y\le2)\\
&=1-\mathbb P(X\le2)\mathbb P(Y\le2)\\
&=1-\frac89\cdot\frac{15}{16}\\
&=1-\frac56\\
&=\frac16.
\end{aligned}
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} show that the problem is not well-posed as printed; step [](#s1-4){.pf-ref} gives the source's intended answer after making both implicit corrections explicit.

:::

:::
