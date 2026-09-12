---
schema: qual/card@1
id: P-ALGS20D
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
Suppose that $A$ is a unital commutative ring without any non-zero nilpotent elements.
Let $N \in \operatorname{Mat}_n(A)$ be a nilpotent element.
Prove that $N^n = 0$.

Hint: Prove that $N^n \in \operatorname{Mat}_n(\mathfrak{p})$ for all prime ideals $\mathfrak{p}$ in $A$.
:::


::: {.solution}
<1>1. Fix a prime ideal \(\mathfrak p\subseteq A\), and let \(\overline N\) be the image of \(N\) in \(\operatorname{Mat}_n(A/\mathfrak p)\). Then \(\overline N\) is nilpotent.
::: {.proof}
If \(N^m=0\), then reducing entries modulo \(\mathfrak p\) gives \(\overline N^{\,m}=0\).
:::

<1>2. Let \(K=\operatorname{Frac}(A/\mathfrak p)\). Viewed as an endomorphism of the \(n\)-dimensional \(K\)-vector space \(K^n\), the matrix \(\overline N\) satisfies \(\overline N^{\,n}=0\).
::: {.proof}
Because \(A/\mathfrak p\) is a domain, it embeds in its fraction field \(K\). Suppose a nilpotent endomorphism \(T\) of an \(n\)-dimensional vector space has nilpotency index \(m\), so \(T^m=0\) but \(T^{m-1}\ne0\). Choose \(v\) with \(T^{m-1}v\ne0\). Then
\[
v,Tv,\ldots,T^{m-1}v
\]
are linearly independent: if \(\sum_{i=0}^{m-1}a_iT^iv=0\) and \(j\) is the least index with \(a_j\ne0\), applying \(T^{m-1-j}\) leaves \(a_jT^{m-1}v=0\), contradiction. Thus \(m\le n\), and therefore \(T^n=0\). Apply this to \(T=\overline N\).
:::

<1>3. Hence every entry of \(N^n\) lies in \(\mathfrak p\).
::: {.proof}
The equality \(\overline N^{\,n}=0\) says exactly that the image modulo \(\mathfrak p\) of every entry of \(N^n\) is zero. Thus each entry belongs to \(\mathfrak p\).
:::

<1>4. Since \(\mathfrak p\) was arbitrary, every entry of \(N^n\) belongs to
\[
\bigcap_{\mathfrak p\in\operatorname{Spec}(A)}\mathfrak p.
\]
This intersection is the nilradical of \(A\), which is zero because \(A\) has no nonzero nilpotents.
::: {.proof}
The nilradical of a commutative ring is the intersection of all prime ideals. By hypothesis \(A\) is reduced, so its nilradical is \(0\).
:::

<1>5. Therefore \(N^n=0\).
::: {.proof}
By <1>4 every entry of \(N^n\) is zero.
:::
:::
