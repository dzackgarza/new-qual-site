---
schema: qual/card@1
id: P-BERK92S-09
kind: problem
title: Real-rootedness is preserved by $p\mapsto p-rp'$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $p$ be a nonconstant polynomial with real coefficients and only real roots. Prove that for every real $r$, the polynomial
\[
p-rp'
\]
has only real roots.
:::

::: {.solution}
Let the distinct roots of $p$ be
$$
\lambda_1<\lambda_2<\cdots<\lambda_k,
$$
with multiplicities $m_1,\ldots,m_k$, and put
$n\coloneqq\deg p=\sum_{j=1}^k m_j$.

::: pf

::: {.pf-step #s1}

The claim is immediate when $r=0$.

::: pf-proof

If $r=0$, then $p-rp'=p$, whose roots are real by hypothesis.

:::

:::

::: {.pf-step #s2}

Suppose $r\ne0$. Each $\lambda_j$ is a zero of $p-rp'$ of
multiplicity at least $m_j-1$.

::: pf-proof

Write
$$
p(x)=(x-\lambda_j)^{m_j}s_j(x),
\qquad
s_j(\lambda_j)\ne0.
$$
Then both $p$ and $p'$ are divisible by
$(x-\lambda_j)^{m_j-1}$, so the same is true of $p-rp'$.

:::

:::

::: {.pf-step #s3}

On $\RR\setminus\{\lambda_1,\ldots,\lambda_k\}$, define
$$
\Phi(x)\coloneqq\frac{p'(x)}{p(x)}
=\sum_{j=1}^k\frac{m_j}{x-\lambda_j}.
$$
Then $\Phi$ is strictly decreasing on each component of its domain.

::: pf-proof

Differentiating gives
$$
\Phi'(x)
=-\sum_{j=1}^k\frac{m_j}{(x-\lambda_j)^2}<0.
$$

:::

:::

::: {.pf-step #s4}

The polynomial $p-rp'$ has at least one zero in every interval
$(\lambda_j,\lambda_{j+1})$, and one further zero outside all the
$\lambda_j$.

::: pf-proof

Away from the roots of $p$,
$$
p(x)-rp'(x)=0
\quad\Longleftrightarrow\quad
\Phi(x)=\frac1r.
$$
On each interval $(\lambda_j,\lambda_{j+1})$, step [](#s3){.pf-ref} and the
endpoint limits
$$
\Phi(x)\longrightarrow+\infty
\quad(x\downarrow\lambda_j),
\qquad
\Phi(x)\longrightarrow-\infty
\quad(x\uparrow\lambda_{j+1})
$$
give exactly one solution.

If $r>0$, then on $(\lambda_k,\infty)$ the function $\Phi$ decreases
from $+\infty$ to $0$, so it takes the positive value $1/r$ once. If
$r<0$, then on $(-\infty,\lambda_1)$ it decreases from $0$ to
$-\infty$, so it takes the negative value $1/r$ once.

:::

:::

::: {.pf-step #s5}

All roots of $p-rp'$ are real.

::: pf-proof

Step [](#s2){.pf-ref} supplies at least
$$
\sum_{j=1}^k(m_j-1)=n-k
$$
real zeros counted with multiplicity at the roots of $p$. Step [](#s4){.pf-ref}
supplies $k-1$ real zeros between consecutive distinct roots and one
additional real zero outside them, for a total of at least
$$
(n-k)+(k-1)+1=n
$$
real zeros counted with multiplicity.

Since $\deg(p-rp')=n$, these account for every zero of $p-rp'$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s5){.pf-ref} cover all real values of $r$.

:::

:::

:::
