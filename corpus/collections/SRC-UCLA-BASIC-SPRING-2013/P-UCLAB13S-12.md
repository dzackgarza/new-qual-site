---
schema: qual/card@1
id: P-UCLAB13S-12
kind: problem
title: Gregory's series for $\pi$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
Define
$$
\pi=4\int_0^1\frac{dx}{1+x^2}.
$$
Prove that
$$
\pi=4\left(1-\frac13+\frac15-\frac17+\cdots\right).
$$
Be careful to give a complete proof.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every integer $N\ge0$ and every $x\in[0,1]$,
$$
\boxed{
\frac1{1+x^2}
=
\sum_{n=0}^N(-1)^nx^{2n}
+
(-1)^{N+1}\frac{x^{2N+2}}{1+x^2}.
}
$$


::: pf-proof

Apply the finite geometric-series identity
$$
\frac1{1-r}
=
\sum_{n=0}^Nr^n
+
\frac{r^{N+1}}{1-r}
$$
with
$$
r=-x^2.
$$
Then
$$
1-r=1+x^2
$$
and
$$
r^{N+1}
=
(-1)^{N+1}x^{2N+2}.
$$

:::

:::

::: {.pf-step #s1-2}

Integrating step [](#s1-1){.pf-ref} from $0$ to $1$ gives
$$
\int_0^1\frac{dx}{1+x^2}
=
\sum_{n=0}^N\frac{(-1)^n}{2n+1}
+
R_N,
$$
where
$$
R_N
=
(-1)^{N+1}
\int_0^1
\frac{x^{2N+2}}{1+x^2}
\,dx.
$$


::: pf-proof

The finite sum may be integrated term by term:
$$
\int_0^1x^{2n}\,dx
=
\frac1{2n+1}.
$$
The final term is exactly the stated remainder.

:::

:::

::: {.pf-step #s1-3}

The remainder satisfies
$$
\boxed{
|R_N|
\le
\frac1{2N+3}.
}
$$


::: pf-proof

For
$$
0\le x\le1,
$$
one has
$$
1+x^2\ge1.
$$
Hence
$$
0
\le
\frac{x^{2N+2}}{1+x^2}
\le
x^{2N+2}.
$$
Therefore
$$
\begin{aligned}
|R_N|
&\le
\int_0^1x^{2N+2}\,dx\\
&=
\frac1{2N+3}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Thus
$$
R_N\to0.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
0\le|R_N|\le\frac1{2N+3},
$$
and the upper bound tends to zero.
Apply the squeeze theorem.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\int_0^1\frac{dx}{1+x^2}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2n+1}.
}
$$


::: pf-proof

Take the limit
$$
N\to\infty
$$
in the identity from step [](#s1-2){.pf-ref} and use step [](#s1-4){.pf-ref}.
This argument uses only finite sums before passing to the limit, so there is no unjustified interchange of an infinite series and an integral.

:::

:::

::: {.pf-step #s1-6}

By the definition of $\pi$ in the problem,
$$
\boxed{
\pi
=
4\left(
1-\frac13+\frac15-\frac17+\cdots
\right).
}
$$


::: pf-proof

Multiply the identity from step [](#s1-5){.pf-ref} by $4$.
The left side becomes $\pi$ by definition, while the right side is
$$
4\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}.
$$

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required Gregory series for $\pi$.

:::

:::

:::
