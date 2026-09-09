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
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $A$ is a unital commutative ring with no non-zero nilpotent elements.
Suppose $N \in M_n(A)$ is nilpotent.
Prove that $N^n = 0$.

Hint: Prove that $N^n \equiv 0 \pmod{\mathfrak{p}}$ for any $\mathfrak{p} \in \operatorname{Spec}(A)$.
:::

::: {.solution}
<1>1. Fix a prime ideal \(\mathfrak p\subseteq A\), and let \(\overline N\) be the image of \(N\) in \(M_n(A/\mathfrak p)\).
::: {.proof}
Because reduction modulo \(\mathfrak p\) is a ring homomorphism, nilpotence of \(N\) implies nilpotence of \(\overline N\).
:::

<1>2. The characteristic polynomial of \(\overline N\) is \(t^n\).
::: {.proof}
The quotient \(A/\mathfrak p\) is an integral domain.
Embed it in its fraction field \(K\). Viewing \(\overline N\) as a matrix over \(K\), it is still nilpotent, so all its eigenvalues in an algebraic closure of \(K\) are \(0\). Hence its characteristic polynomial over \(K\) is \(t^n\). Since the characteristic polynomial was already computed from entries in \(A/\mathfrak p\), it is therefore \(t^n\) in \((A/\mathfrak p)[t]\).
:::

<1>3. One has \(\overline N^{\,n}=0\) in \(M_n(A/\mathfrak p)\).
::: {.proof}
By <1>2, the characteristic polynomial of \(\overline N\) is \(t^n\). The Cayley--Hamilton theorem over the commutative ring \(A/\mathfrak p\) gives \(\overline N^{\,n}=0\).
:::

<1>4. Every entry of \(N^n\) lies in every prime ideal of \(A\).
::: {.proof}
By <1>3, reducing \(N^n\) modulo any prime ideal \(\mathfrak p\) gives the zero matrix.
Thus each entry belongs to \(\mathfrak p\). Since \(\mathfrak p\) was arbitrary, every entry belongs to \(\bigcap_{\mathfrak p\in\operatorname{Spec}(A)}\mathfrak p\).
:::

<1>5. Therefore \(N^n=0\).
::: {.proof}
The intersection of all prime ideals is the nilradical of \(A\). Because \(A\) has no nonzero nilpotent elements, its nilradical is \(0\). Hence all entries of \(N^n\) are zero.
:::
:::
