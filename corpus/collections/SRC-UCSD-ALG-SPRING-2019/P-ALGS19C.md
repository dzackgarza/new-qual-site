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
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Spring 2020 problem D states the same problem with the same hint; that sitting now lists this card, and its independent proof by a cyclic-vector bound on the nilpotency index is kept as a second solution."
---

::: problem
Suppose $A$ is a unital commutative ring with no non-zero nilpotent elements.
Suppose $N \in M_n(A)$ is nilpotent.
Prove that $N^n = 0$.

Hint: Prove that $N^n \equiv 0 \pmod{\mathfrak{p}}$ for any $\mathfrak{p} \in \operatorname{Spec}(A)$.
:::


::: {.solution}
<1>1. For each prime ideal \(\mathfrak p\subseteq A\), let \(\overline N\) be the image of \(N\) in \(M_n(A/\mathfrak p)\). Then \(\overline N\) is nilpotent.
::: {.proof}
If \(N^r=0\), reducing the entries modulo \(\mathfrak p\) gives \(\overline N^{\,r}=0\).
:::

<1>2. For every prime ideal \(\mathfrak p\), one has \(\overline N^{\,n}=0\).
::: {.proof}
Because \(\mathfrak p\) is prime, \(A/\mathfrak p\) is an integral domain. Let \(K=\operatorname{Frac}(A/\mathfrak p)\). Viewing \(\overline N\) as a matrix in \(M_n(K)\), its minimal polynomial divides \(t^r\) for some \(r\), so every invariant factor is a power of \(t\); hence its characteristic polynomial is \(t^n\). By the Cayley--Hamilton theorem, \(\overline N^{\,n}=0\) in \(M_n(K)\). Since \(A/\mathfrak p\hookrightarrow K\) is injective, the same equality holds already in \(M_n(A/\mathfrak p)\).
:::

<1>3. Every entry of \(N^n\) lies in every prime ideal of \(A\).
::: {.proof}
By <1>2, the reduction of \(N^n\) modulo each \(\mathfrak p\in\operatorname{Spec}(A)\) is the zero matrix. Therefore each entry of \(N^n\) belongs to \(\mathfrak p\) for every prime ideal \(\mathfrak p\).
:::

<1>4. The intersection of all prime ideals of \(A\) is the nilradical of \(A\).
::: {.proof}
Every nilpotent element belongs to every prime ideal. Conversely, suppose \(a\in A\) is not nilpotent. Then the multiplicative set \(S=\{1,a,a^2,\ldots\}\) does not contain \(0\). By Zorn's lemma, there is an ideal maximal among ideals disjoint from \(S\); the usual maximal-disjointness argument shows that this ideal is prime. It is disjoint from \(S\), so in particular it does not contain \(a\). Thus an element lying in every prime ideal must be nilpotent.
:::

<1>5. Since \(A\) has no nonzero nilpotent elements, \(N^n=0\).
::: {.proof}
By hypothesis \(A\) is reduced, so its nilradical is \(0\). By <1>3 and <1>4, every entry of \(N^n\) is therefore zero. Hence \(N^n\) is the zero matrix.
:::
:::

::: {.solution}
<1>1. Fix a prime ideal \(\mathfrak p\subseteq A\), and let \(\overline N\) be the image of \(N\) in \(M_n(A/\mathfrak p)\). Then \(\overline N\) is nilpotent.
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
