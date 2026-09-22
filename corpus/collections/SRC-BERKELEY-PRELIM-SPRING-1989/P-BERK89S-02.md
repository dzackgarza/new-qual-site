---
schema: qual/card@1
id: P-BERK89S-02
kind: problem
title: A nilpotent $n\times n$ matrix satisfies $A^n=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the ascending chain of kernels of powers of A. Equality at one
    stage forces all later kernels to stabilize, so before the kernel
    becomes all of F^n every inclusion is strict; dimension then bounds
    the nilpotence index by n.
---

::: {.problem}
Let $F$ be a field and let $A\in M_n(F)$. If
\[
A^m=0
\]
for some positive integer $m$, prove that
\[
A^n=0.
\]
:::

::: {.solution}
Let $V\coloneqq F^n$ and regard $A$ as a linear map $V\to V$. For
$r\geq0$, set
$$
K_r\coloneqq\ker A^r,
$$
where $A^0$ is the identity map.

<1>1. The subspaces $K_r$ form an ascending chain
$$
K_0\subseteq K_1\subseteq K_2\subseteq\cdots,
$$
and if $K_r=K_{r+1}$ for some $r$, then
$$
K_j=K_r
$$
for every $j\geq r$.

::: {.proof}
If $v\in K_r$, then $A^rv=0$, so
$$
A^{r+1}v=A(A^rv)=0.
$$
Thus $K_r\subseteq K_{r+1}$.

Suppose now that $K_r=K_{r+1}$. If $v\in K_{r+2}$, then
$$
Av\in K_{r+1}=K_r.
$$
Hence
$$
A^{r+1}v=A^r(Av)=0,
$$
so $v\in K_{r+1}$. Therefore $K_{r+2}=K_{r+1}$. Repeating this argument
inductively gives $K_j=K_r$ for every $j\geq r$.
:::

<1>2. Let
$$
s\coloneqq\min\{r\geq0:K_r=V\}.
$$
Then
$$
K_0\subsetneq K_1\subsetneq\cdots\subsetneq K_s=V.
$$

::: {.proof}
The integer $s$ exists because $A^m=0$, so $K_m=V$. By minimality of
$s$, one has $K_r\neq V$ for every $r<s$.

If $K_r=K_{r+1}$ for some $r<s$, step <1>1 would imply
$K_s=K_r\neq V$, contradicting the definition of $s$. Thus every
inclusion before $K_s$ is strict.
:::

<1>3. One has
$$
s\leq n.
$$

::: {.proof}
Since $K_0=\{0\}$ and each of the $s$ inclusions in step <1>2 is strict,
dimension increases by at least $1$ at each step. Therefore
$$
s
\leq
\dim K_s
=
\dim V
=
n.
$$
:::

<1>4. One has
$$
\boxed{A^n=0}.
$$

::: {.proof}
By step <1>3, $s\leq n$. Since the kernel chain is ascending,
$$
V
=
K_s
\subseteq
K_n
\subseteq
V.
$$
Hence $K_n=V$, which means $A^nv=0$ for every $v\in V$. Therefore
$A^n=0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
