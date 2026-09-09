---
schema: qual/card@1
id: P-ALGS19C
kind: problem
title: "A nilpotent matrix over a reduced ring satisfies N^n = 0"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Suppose $A$ is a unital commutative ring with no non-zero nilpotent elements.
Suppose $N \in M_n(A)$ is nilpotent.
Prove that $N^n = 0$.

Hint: Prove that $N^n \equiv 0 \pmod{\mathfrak{p}}$ for any $\mathfrak{p} \in \operatorname{Spec}(A)$.
:::


::: {.solution}
<1>1. Let \(\mathfrak p\in\operatorname{Spec}(A)\), and let \(\overline N\in M_n(A/\mathfrak p)\) be the image of \(N\).
Then \(\overline N\) is nilpotent.
::: {.proof}
If \(N^r=0\), then reducing the equality modulo \(\mathfrak p\) gives \(\overline N^{\,r}=0\).
:::

<1>2. Let \(K=\operatorname{Frac}(A/\mathfrak p)\). Viewed as a matrix in \(M_n(K)\), the matrix \(\overline N\) satisfies
\[
\overline N^{\,n}=0.
\]
::: {.proof}
Because \(A/\mathfrak p\) is an integral domain, it embeds in its fraction field \(K\). The matrix \(\overline N\) remains nilpotent over \(K\). A nilpotent linear operator on the \(n\)-dimensional \(K\)-vector space \(K^n\) has only the eigenvalue \(0\), so its characteristic polynomial is \(t^n\). By the Cayley--Hamilton theorem,
\[
\overline N^{\,n}=0.
\]
:::

<1>3. Therefore every entry of \(N^n\) belongs to \(\mathfrak p\).
::: {.proof}
The equality in <1>2 already holds in \(M_n(A/\mathfrak p)\), because the injection \(A/\mathfrak p\hookrightarrow K\) induces an injection on matrix rings. Thus \(N^n\equiv0\pmod{\mathfrak p}\), entrywise.
:::

<1>4. Every entry of \(N^n\) lies in
\[
\bigcap_{\mathfrak p\in\operatorname{Spec}(A)}\mathfrak p=\sqrt{(0)}.
\]
::: {.proof}
The prime ideal \(\mathfrak p\) was arbitrary, so <1>3 holds for every prime ideal. The intersection of all prime ideals of a commutative ring is its nilradical \(\sqrt{(0)}\).
:::

<1>5. Since \(A\) has no nonzero nilpotent elements, \(\sqrt{(0)}=(0)\). Hence \(N^n=0\).
::: {.proof}
The hypothesis says precisely that \(A\) is reduced, equivalently that its nilradical is zero. By <1>4 every entry of \(N^n\) is therefore zero.
:::
:::
