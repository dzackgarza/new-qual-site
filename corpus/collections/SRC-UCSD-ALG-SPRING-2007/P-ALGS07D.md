---
schema: qual/card@1
id: P-ALGS07D
kind: problem
title: "Tensor product decomposition of C[x]/(x^n) ⊗ C[x]/(x^m)"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared with Problem 4 on pages 6-7 of the official Spring 2007 UCSD algebra qualifying exam; restored omitted part (b), which asks to determine the a_i in terms of m and n.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the canonical isomorphism (R/I) tensor_R (R/J) = R/(I+J) and hence k=1 with a_1=min(m,n).
---

::: problem
Let $\mathbb{C}[x]/\langle x^n \rangle$ denote the evident $\mathbb{C}[x]$-module, and let $m, n \in \mathbb{N}$.

(a) Show that there exist $a_1, \ldots, a_k$ such that $$\mathbb{C}[x]/\langle x^n \rangle \otimes_{\mathbb{C}[x]} \mathbb{C}[x]/\langle x^m \rangle \cong \bigoplus_{i=1}^{k} \mathbb{C}[x]/(x^{a_i}).$$

(b) Determine the $a_i$ in terms of $m,n$.

Hint: Figure out the action of $x$ on the obvious $\mathbb{C}$-basis.
:::

::: {.solution}
<1>1. For every commutative ring $R$ and ideals $I,J\subseteq R$, there is a canonical isomorphism
\[
(R/I)\otimes_R(R/J)\cong R/(I+J).
\]
::: {.proof}
Define
\[
\Phi:(R/I)\otimes_R(R/J)\longrightarrow R/(I+J),
\qquad
(r+I)\otimes(s+J)\longmapsto rs+(I+J).
\]
The map is well-defined and $R$-balanced: changing $r$ by an element of $I$ or $s$ by an element of $J$ changes $rs$ by an element of $I+J$.

Define
\[
\Psi:R/(I+J)\longrightarrow (R/I)\otimes_R(R/J),
\qquad
r+(I+J)\longmapsto (r+I)\otimes(1+J).
\]
If $r\in I+J$, write $r=i+j$ with $i\in I$ and $j\in J$.
Then
\[
(i+I)\otimes(1+J)=0,
\qquad
(j+I)\otimes(1+J)=(1+I)\otimes(j+J)=0,
\]
so $\Psi$ is well-defined.

Now
\[
\Phi\Psi(r+(I+J))=r+(I+J),
\]
and, using the balancing relation,
\[
\Psi\Phi\big((r+I)\otimes(s+J)\big)
=(rs+I)\otimes(1+J)
=(r+I)\otimes(s+J).
\]
Hence $\Phi$ and $\Psi$ are inverse isomorphisms.
:::

<1>2. Applying <1>1 with $R=\mathbb{C}[x]$, $I=(x^n)$, and $J=(x^m)$ gives
\[
\mathbb{C}[x]/(x^n)\otimes_{\mathbb{C}[x]}\mathbb{C}[x]/(x^m)
\cong
\mathbb{C}[x]/(x^{\min(m,n)}).
\]
::: {.proof}
In $\mathbb{C}[x]$,
\[
(x^n)+(x^m)=(x^{\min(m,n)}).
\]
Substitute this into <1>1.
:::

<1>3. Thus the decomposition in part (a) exists with
\[
k=1,
\qquad
a_1=\min(m,n),
\]
and these values answer part (b).
::: {.proof}
The module on the right side of <1>2 is already one summand of the required form $\mathbb{C}[x]/(x^{a_1})$, so taking $a_1=\min(m,n)$ gives the desired decomposition.
:::
:::
