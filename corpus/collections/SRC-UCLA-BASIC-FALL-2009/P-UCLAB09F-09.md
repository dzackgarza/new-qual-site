---
schema: qual/card@1
id: P-UCLAB09F-09
kind: problem
title: An odd-dimensional real orthogonal matrix has eigenvalue 1 or minus 1
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
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
Let $A\in M_{2n+1}(\mathbb R)$ satisfy
\[
AA^T=I_{2n+1}.
\]
Prove that at least one of $1$ or $-1$ is an eigenvalue of $A$.
:::

::: {.solution}
<1>1. The characteristic polynomial
\[
\chi_A(t)=\det(tI-A)
\]
has a real root.

::: {.proof}
The matrix $A$ has size
\[
(2n+1)\times(2n+1),
\]
so $\chi_A$ is a real polynomial of odd degree $2n+1$. Its leading term is $t^{2n+1}$, hence
\[
\chi_A(t)\to+\infty
\quad\text{as }t\to+\infty
\]
and
\[
\chi_A(t)\to-\infty
\quad\text{as }t\to-\infty.
\]
By the intermediate value theorem, there is $\lambda\in\mathbb R$ with
\[
\chi_A(\lambda)=0.
\]
:::

<1>2. There is a nonzero real vector $v$ satisfying
\[
Av=\lambda v.
\]

::: {.proof}
By step <1>1,
\[
\det(\lambda I-A)=0,
\]
so the real matrix $\lambda I-A$ is singular. Hence its kernel contains a nonzero real vector $v$, and
\[
(\lambda I-A)v=0.
\]
:::

<1>3. The real eigenvalue $\lambda$ from step <1>2 satisfies
\[
|\lambda|=1.
\]

::: {.proof}
The relation
\[
AA^t=I
\]
implies that $A$ is invertible with
\[
A^{-1}=A^t.
\]
Therefore also
\[
A^tA=I.
\]
Thus $A$ preserves the Euclidean norm:
\[
\|Av\|^2
=
v^tA^tAv
=
\|v\|^2.
\]
Using
\[
Av=\lambda v
\]
and $v\ne0$,
\[
\|v\|
=
\|Av\|
=
|\lambda|\,\|v\|.
\]
Hence $|\lambda|=1$.
:::

<1>4. One of $1$ or $-1$ is an eigenvalue of $A$.

::: {.proof}
The number $\lambda$ is real by step <1>1 and satisfies $|\lambda|=1$ by step <1>3. Therefore
\[
\lambda\in\{1,-1\}.
\]
By step <1>2, $\lambda$ is an eigenvalue. Hence
\[
\boxed{1\text{ or }-1\text{ is an eigenvalue of }A}.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
