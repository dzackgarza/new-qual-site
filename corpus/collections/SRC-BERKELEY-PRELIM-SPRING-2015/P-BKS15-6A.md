---
schema: qual/card@1
id: P-BKS15-6A
kind: problem
title: Lagrange interpolation in Cauchy-matrix form
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the matrix-entry reduction to the Lagrange basis and the interpolation argument for every polynomial of degree less than N.
---

::: {.problem}
Fix $N\ge1$.
Let $\mathbf s=(s_1,\ldots,s_N)$ and $\mathbf t=(t_1,\ldots,t_N)$ be $2N$ distinct complex numbers.
Define the $N\times N$ matrices $C(\mathbf t,\mathbf s)$, $P(\mathbf t,\mathbf s)$, and $Q(\mathbf s)$, with $P$ and $Q$ diagonal, by
$$
C(\mathbf t,\mathbf s)_{ij}=\frac1{t_i-s_j},\qquad
P(\mathbf t,\mathbf s)_{ii}=\prod_{k=1}^N(t_i-s_k),\qquad
Q(\mathbf s)_{jj}=\prod_{k\ne j}\frac1{s_j-s_k}.
$$
Show that
$$
p(\mathbf t)=P(\mathbf t,\mathbf s)C(\mathbf t,\mathbf s)Q(\mathbf s)p(\mathbf s),
$$
where $p$ is any polynomial of degree less than $N$ and, for a vector $\mathbf r=(r_1,\ldots,r_N)$, $p(\mathbf r)$ denotes $(p(r_1),\ldots,p(r_N))$.
:::

::: {.solution}
For $1\leq j\leq N$, define the Lagrange basis polynomial
$$
L_j(z)
\coloneqq
\prod_{\substack{1\leq k\leq N\\k\neq j}}
\frac{z-s_k}{s_j-s_k}.
$$

::: pf

::: {.pf-step #s1}

For every $1\leq i,j\leq N$,
$$
\bigl(P(\mathbf t,\mathbf s)C(\mathbf t,\mathbf s)Q(\mathbf s)\bigr)_{ij}
=
L_j(t_i).
$$

::: pf-proof

Because $P$ and $Q$ are diagonal,
$$
\begin{aligned}
\bigl(PCQ\bigr)_{ij}
&=
P_{ii}C_{ij}Q_{jj}\\
&=
\left(\prod_{k=1}^N(t_i-s_k)\right)
\frac1{t_i-s_j}
\left(\prod_{k\neq j}\frac1{s_j-s_k}\right)\\
&=
\prod_{k\neq j}\frac{t_i-s_k}{s_j-s_k}\\
&=
L_j(t_i).
\end{aligned}
$$
All denominators are nonzero because the $2N$ numbers $s_1,\ldots,s_N,t_1,\ldots,t_N$ are distinct.

:::

:::

::: {.pf-step #s2}

The Lagrange basis satisfies
$$
L_j(s_m)=
\begin{cases}
1,&m=j,\\
0,&m\neq j.
\end{cases}
$$

::: pf-proof

If $m=j$, every factor in $L_j(s_j)$ equals $1$. If $m\neq j$, the factor with $k=m$ has numerator $s_m-s_m=0$.

:::

:::

::: {.pf-step #s3}

Every polynomial $p$ of degree less than $N$ satisfies
$$
p(z)=\sum_{j=1}^N p(s_j)L_j(z).
$$

::: pf-proof

Set
$$
q(z)
\coloneqq
\sum_{j=1}^N p(s_j)L_j(z).
$$
Both $p$ and $q$ have degree less than $N$. By step [](#s2){.pf-ref}, for every $1\leq m\leq N$,
$$
q(s_m)
=
\sum_{j=1}^N p(s_j)L_j(s_m)
=
p(s_m).
$$
Thus $p-q$ has degree less than $N$ and has the $N$ distinct roots $s_1,\ldots,s_N$. Hence $p-q=0$.

:::

:::

::: {.pf-step #s4}

For every $1\leq i\leq N$, the $i$th coordinate of
$$
P(\mathbf t,\mathbf s)C(\mathbf t,\mathbf s)Q(\mathbf s)p(\mathbf s)
$$
equals $p(t_i)$.

::: pf-proof

By step [](#s1){.pf-ref}, the $i$th coordinate is
$$
\sum_{j=1}^N L_j(t_i)p(s_j).
$$
Applying step [](#s3){.pf-ref} with $z=t_i$ gives exactly $p(t_i)$.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
p(\mathbf t)
=
P(\mathbf t,\mathbf s)C(\mathbf t,\mathbf s)Q(\mathbf s)p(\mathbf s)
}.
$$

::: pf-proof

Step [](#s4){.pf-ref} proves equality of all $N$ coordinates.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required identity.

:::

:::

:::
