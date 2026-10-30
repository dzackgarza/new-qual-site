---
schema: qual/card@1
id: P-TRIV-RA11
kind: problem
title: 'Huygens problem: amplifying velocity through a chain of elastic collisions'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
"Huygens problem". Consider the ball with mass $M$ moving with velocity $V$ towards another ball with mass $m$ that stays at rest. After the central collision, the second ball acquires the velocity
$$
v = \frac{2M}{m + M}V. \tag{11}
$$
This expression can be obtained using the momentum and energy conservation laws for the two-body system. One can observe that $V \leqslant v \leqslant 2V$ as far as $0 \leqslant m \leqslant M$. One may ask under what conditions the limit $v \leqslant 2V$ can be broken to make $v$ arbitrary large. A possible solution is to insert a chain of balls staying at rest with intermediate masses $m_1, \ldots, m_n$ such that $m < m_1 < \cdots < m_n < M$ between the two original bodies, and to transfer the kinetic energy of the moving ball to the ball with mass $m$ through a sequence of intermediate central collisions.

(a) Applying Eq.(11) to the sequence of central collisions between the balls, deduce how one should choose the masses $m_1, \ldots, m_n$ to yield the maximal velocity of the ball with mass $m$.

(b) Assuming $m \ll M$, investigate the limit $n \to \infty$.
:::

::: {.solution}

Let
$$
q_0=M>q_1>\cdots>q_n>q_{n+1}=m
$$
be the masses in the order in which they are struck. Thus
$$
q_j=m_{n+1-j}
$$
for $1\leq j\leq n$ in the notation of the problem.

::: pf

::: {.pf-step #s1-1}

After all $n+1$ collisions, the final velocity of the mass $m$ is
$$
v
=
V
\prod_{j=0}^{n}
\frac{2q_j}{q_j+q_{j+1}}.
$$


::: pf-proof

For one collision in which mass $q_j$ moves and the next mass $q_{j+1}$ is
at rest, Eq. (11) multiplies the transmitted velocity by
$$
\frac{2q_j}{q_j+q_{j+1}}.
$$
Apply this successively through the chain.

:::

:::

::: {.pf-step #s1-2}

Define the mass ratios
$$
r_j=\frac{q_{j+1}}{q_j},
\qquad
j=0,\ldots,n.
$$
Then
$$
0<r_j<1
$$
and
$$
\prod_{j=0}^{n}r_j=\frac mM.
$$


::: pf-proof

The strict inequalities follow from the decreasing masses. The product
telescopes:
$$
\frac{q_1}{q_0}
\frac{q_2}{q_1}
\cdots
\frac{q_{n+1}}{q_n}
=
\frac{q_{n+1}}{q_0}
=
\frac mM.
$$

:::

:::

::: {.pf-step #s1-3}

In terms of the ratios,
$$
\frac vV
=
\prod_{j=0}^{n}
\frac{2}{1+r_j}.
$$


::: pf-proof

Divide numerator and denominator of each factor in step [](#s1-1){.pf-ref} by $q_j$.

:::

:::

::: {.pf-step #s1-4}

Put
$$
t_j=-\log r_j>0
$$
and
$$
L=\log\frac Mm>0.
$$
Then
$$
\sum_{j=0}^{n}t_j=L.
$$


::: pf-proof

Take logarithms of the product constraint in step [](#s1-2){.pf-ref}:
$$
\sum_j\log r_j
=
\log\frac mM
=
-L.
$$

:::

:::

::: pf-step

Define
$$
h(t)=\log\frac{2}{1+e^{-t}}.
$$
Then $h$ is strictly concave for $t>0$.


::: pf-proof

One may write
$$
h(t)
=
\frac t2
-
\log\cosh\frac t2.
$$
Hence
$$
h''(t)
=
-\frac14
\operatorname{sech}^2\frac t2
<0.
$$

:::

:::

::: {.pf-step #s1-6}

The velocity is maximized exactly when
$$
t_0=t_1=\cdots=t_n
=
\frac{L}{n+1}.
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref},
$$
\log\frac vV
=
\sum_{j=0}^{n}h(t_j),
$$
with fixed sum $\sum t_j=L$. Since $h$ is strictly concave, Jensen's
inequality gives
$$
\frac1{n+1}
\sum_{j=0}^{n}h(t_j)
\leq
h\left(\frac{L}{n+1}\right),
$$
with equality exactly when all $t_j$ are equal.

:::

:::

::: {.pf-step #s1-7}

Equivalently, all consecutive mass ratios must be equal:
$$
\boxed{
r_j
=
\left(\frac mM\right)^{1/(n+1)}.
}
$$


::: pf-proof

Exponentiate the equality from step [](#s1-6){.pf-ref}:
$$
r_j
=
e^{-L/(n+1)}
=
\left(\frac mM\right)^{1/(n+1)}.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore the optimal intermediate masses are
$$
\boxed{
m_k
=
m
\left(\frac Mm\right)^{k/(n+1)},
\qquad
k=1,\ldots,n.
}
$$


::: pf-proof

The masses increase geometrically from $m$ to $M$. The displayed formula has
$$
m_0=m,
\qquad
m_{n+1}=M,
$$
and constant ratio
$$
\frac{m_{k+1}}{m_k}
=
\left(\frac Mm\right)^{1/(n+1)}.
$$
Reading the collision chain in decreasing order gives exactly the constant
ratio in step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Part (a) follows.


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} give the unique maximizing choice of intermediate masses.

:::

:::

::: {.pf-step #s1-10}

For the optimal chain,
$$
\boxed{
\frac{v_n}{V}
=
\left[
\frac{2}{1+(m/M)^{1/(n+1)}}
\right]^{n+1}.
}
$$


::: pf-proof

Every factor in step [](#s1-3){.pf-ref} is the same under the optimal ratio from step
[](#s1-7){.pf-ref}, and there are $n+1$ collisions.

:::

:::

::: {.pf-step #s1-11}

Let
$$
N=n+1
$$
and
$$
L=\log\frac Mm.
$$
Then
$$
\log\frac{v_n}{V}
=
N
\log\left(
\frac{2}{1+e^{-L/N}}
\right).
$$


::: pf-proof

Rewrite step [](#s1-10){.pf-ref} using
$$
(m/M)^{1/N}=e^{-L/N}.
$$

:::

:::

::: {.pf-step #s1-12}

As $N\to\infty$,
$$
\log\left(
\frac{2}{1+e^{-L/N}}
\right)
=
\frac{L}{2N}
+
O(N^{-2}).
$$


::: pf-proof

For small $x$,
$$
\frac{2}{1+e^{-x}}
=
\frac{e^{x/2}}{\cosh(x/2)}.
$$
Hence
$$
\log\frac{2}{1+e^{-x}}
=
\frac x2
-
\log\cosh\frac x2
=
\frac x2+O(x^2).
$$
Take $x=L/N$.

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\lim_{n\to\infty}
\log\frac{v_n}{V}
=
\frac L2.
$$


::: pf-proof

Multiply the expansion in step [](#s1-12){.pf-ref} by $N$ and use step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Thus
$$
\boxed{
\lim_{n\to\infty}v_n
=
V\sqrt{\frac Mm}.
}
$$


::: pf-proof

Exponentiate step [](#s1-13){.pf-ref}:
$$
\frac{v_n}{V}
\longrightarrow
e^{L/2}
=
\sqrt{\frac Mm}.
$$

:::

:::

::: {.pf-step #s1-15}

In this limit the kinetic-energy transfer becomes complete.


::: pf-proof

The final kinetic energy tends to
$$
\frac12m
\left(
V^2\frac Mm
\right)
=
\frac12MV^2,
$$
which is the initial kinetic energy.

:::

:::

::: {.pf-step #s1-16}

Part (b) follows.


::: pf-proof

Steps [](#s1-14){.pf-ref} through [](#s1-15){.pf-ref} give the infinite-chain limit and its interpretation.

:::

:::

::: pf-qed

Steps [](#s1-9){.pf-ref} and [](#s1-16){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
