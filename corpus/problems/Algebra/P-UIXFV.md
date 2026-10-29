---
schema: qual/card@1
id: P-UIXFV
kind: problem
title: Dimensions of the irreducible representations of $D_n$, and $\sum_i(\dim V_i)^2=\abs{G}$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Character Theory
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
How would you work out the orders of the irreducible representations of the dihedral group $D_n$?

Why is the sum of squares of dimensions equal to the order of the group?
:::

::: {.solution}
Let $D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle$, of order $2n$, and work over $\CC$.

::: pf

::: {.pf-step #sum-of-squares}
For a finite group $G$ with irreducible representations $V_1,\ldots,V_k$, $\sum_i(\dim V_i)^2=\abs{G}$.

::: pf-proof
The regular representation decomposes as $\CC[G]\cong\bigoplus_i V_i^{\oplus\dim V_i}$; taking dimensions gives the formula.
:::

:::

::: {.pf-step #linear}
$D_n$ has $2$ one-dimensional representations when $n$ is odd and $4$ when $n$ is even.

::: pf-proof
One-dimensional representations factor through the abelianization, which has order $2$ for $n$ odd and $4$ for $n$ even, since $[D_n,D_n]=\langle r^2\rangle$.
:::

:::

::: {.pf-step #two-dim}
The representations $\operatorname{Ind}_{\langle r\rangle}^{D_n}\chi_k$, where $\chi_k(r)=e^{2\pi ik/n}$, are two-dimensional and irreducible for $0<k<n/2$, and pairwise non-isomorphic; there are $(n-1)/2$ of them for $n$ odd and $(n-2)/2$ for $n$ even.

::: pf-proof
On the induced representation, $r$ acts with eigenvalues $\chi_k(r)$ and $\chi_k(r)^{-1}=\chi_{n-k}(r)$, and $s$ swaps the two eigenlines.
When $\chi_k\ne\chi_{n-k}$, that is, $k\ne0$ and $k\ne n/2$, any invariant line would be an eigenline of $r$, which $s$ does not preserve, so the representation is irreducible.
Different $k$ in $0<k<n/2$ give different sets of eigenvalues of $r$, so the representations are non-isomorphic.
:::

:::

::: pf-step
The irreducible representations of $D_n$ have dimensions $1$ and $2$: $\boxed{2\text{ of dimension }1\text{ and }(n-1)/2\text{ of dimension }2}$ for $n$ odd, and $\boxed{4\text{ of dimension }1\text{ and }(n-2)/2\text{ of dimension }2}$ for $n$ even.

::: pf-proof
By steps [](#linear){.pf-ref} and [](#two-dim){.pf-ref}, the sums of squares of the dimensions found are $2+4\cdot\frac{n-1}{2}=2n$ for $n$ odd and $4+4\cdot\frac{n-2}{2}=2n$ for $n$ even.
By step [](#sum-of-squares){.pf-ref} there are no further irreducible representations.
:::

:::

:::

:::
