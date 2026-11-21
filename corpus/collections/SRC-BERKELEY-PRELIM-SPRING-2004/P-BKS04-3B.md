---
schema: qual/card@1
id: P-BKS04-3B
kind: problem
title: $\norm{A^n}=O(n^{d-1})$ when every eigenvalue of $A$ has modulus $1$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2004
    prelim solutions, Problem 3B, PDF p. 7, the file named in the collection's provenance),
    which the card now cites; it previously carried no citation. Added: the two-norm
    equivalence with its constants; the bound on the entries of A^n x in terms of the entries of
    A^n; the invariance of the estimate under conjugation; and the two estimates the sheet
    quotes, that the entries of D^m have modulus at most 1 and that the binomial coefficient is
    at most n^(d-1). Repaired: the sheet writes the sup norm over n coordinates where the
    ambient dimension is d. The Jordan decomposition is described block by block, with N^d = 0
    from the block sizes.
---

::: {.problem}
Let $A$ be a $d\times d$ matrix with complex entries.
Assume that every eigenvalue of $A$ has absolute value $1$. Prove that there exists a constant $c\in\RR$ independent of $n$ such that

$$
\norm{A^nx}\leq cn^{d-1}\norm{x}
$$

for all $n\geq1$ and $x\in\CC^d$. Here $\norm{x}\coloneqq(\abs{x_1}^2+\cdots+\abs{x_d}^2)^{1/2}$ for all $(x_1,\ldots,x_d)\in\CC^d$.
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2004 prelim solutions, Problem 3B, PDF p. 7** (`assets/attachments/s04solution.pdf`, the file named in this collection's `provenance`): the passage to the sup norm, the reduction to the Jordan form, the splitting $A=D+N$, and the binomial estimate are that solution's. The card records the two estimates the sheet invokes as facts — that the entries of $D^m$ are bounded, and that $\binom nk=O(n^{d-1})$ — and drops the sheet's slip $\abs{x}_\infty=\max\{\abs{x_1},\dots,\abs{x_n}\}$ in favour of the ambient dimension $d$.

Throughout $A\in M_d(\CC)$, every eigenvalue of $A$ has modulus $1$, and $\norm{\cdot}$ is the Euclidean norm with $\abs{x}_\infty=\max_i\abs{x_i}$.

::: pf

::: {.pf-step #sup-norm}
It suffices to prove $\abs{A^nx}_\infty\le c'n^{d-1}\abs{x}_\infty$ for a constant $c'$.

::: pf-proof
On the finite-dimensional space $\CC^d$ any two norms are equivalent: there are constants $\alpha,\beta>0$ with $\alpha\abs{v}_\infty\le\norm{v}\le\beta\abs{v}_\infty$ for all $v$. Hence $\abs{A^nx}_\infty\le c'n^{d-1}\abs{x}_\infty$ gives $\norm{A^nx}\le\beta c'n^{d-1}\abs{x}_\infty\le\beta\alpha^{-1}c'n^{d-1}\norm{x}$, which is the required inequality with $c=\beta\alpha^{-1}c'$.

:::

:::

::: {.pf-step #entries}
$\abs{A^nx}_\infty\le c'n^{d-1}\abs{x}_\infty$ for all $n,x$ holds as soon as every entry of $A^n$ is $O(n^{d-1})$.

::: pf-proof
$(A^nx)_i=\sum_ja^{(n)}_{ij}x_j$, so $\abs{(A^nx)_i}\le\sum_j\abs{a^{(n)}_{ij}}\abs{x_j}\le\bigl(\sum_j\abs{a^{(n)}_{ij}}\bigr)\abs x_\infty\le d\max_{i,j}\abs{a^{(n)}_{ij}}\abs x_\infty$; if each entry is at most $Kn^{d-1}$ then $c'=dK$ works.

:::

:::

::: {.pf-step #jordan}
The assertion that the entries of $A^n$ are $O(n^{d-1})$ is unchanged by conjugating $A$, so one may assume $A=D+N$ with $D$ diagonal, $N$ nilpotent, $DN=ND$ and $N^d=0$.

::: pf-proof
If $A'=P^{-1}AP$ then $(A')^n=P^{-1}A^nP$, so the entries of $(A')^n$ are fixed linear combinations of the entries of $A^n$; a bound of order $n^{d-1}$ for one is therefore equivalent to one for the other. Taking $P$ to put $A$ in Jordan form, write $A=\bigoplus_i(\lambda_iI_{m_i}+J_{m_i}(0))$ for the eigenvalues $\lambda_i$ and nilpotent Jordan blocks $J_{m_i}(0)$. Put $D=\bigoplus_i\lambda_iI_{m_i}$, the diagonal part, and $N=A-D=\bigoplus_iJ_{m_i}(0)$. Then $D$ is a direct sum of scalar matrices on the blocks and each $J_{m_i}(0)$ is strictly upper triangular of size $m_i\le d$, so $DN=ND$, $N$ is nilpotent, and $N^{m_i}=0$ on each block, hence $N^d=0$.
:::

:::

::: {.pf-step #binomial}
$A^n=\sum_{k=0}^{d-1}\binom nkD^{n-k}N^k$.

::: pf-proof
$D$ and $N$ commute, so the binomial theorem applies to $(D+N)^n$, and all terms with $k\ge d$ vanish because $N^d=0$.

:::

:::

::: {.pf-step #bounds}
Each summand has entries $O(n^{d-1})$, uniformly in $n$.

::: pf-proof
The eigenvalues of $A$, which are the diagonal entries of $D$, have modulus $1$, so the entries of $D^m$ have modulus at most $1$ for every $m$: $D^m$ is diagonal with entries $\lambda_i^m$. The matrices $N^k$ for $0\le k\le d-1$ are fixed and independent of $n$. Finally $\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}\le n^k/k!\le n^{d-1}$ for $1\le k\le d-1$ and $n\ge1$. Multiplying, the entries of $\binom nkD^{n-k}N^k$ are $O(n^{d-1})$ with a constant depending only on $d$ and on the (fixed) entries of the powers of $N$.

:::

:::

::: {.pf-step #conclusion}
$\norm{A^nx}\le cn^{d-1}\norm x$ for a constant $c$ independent of $n$ and $x$.

::: pf-proof
Steps [](#entries){.pf-ref}, [](#binomial){.pf-ref} and [](#bounds){.pf-ref} give $\abs{A^nx}_\infty\le c'n^{d-1}\abs x_\infty$, and step [](#sup-norm){.pf-ref} converts this into the Euclidean inequality with $c=\beta\alpha^{-1}c'$.

:::

:::

:::
:::
