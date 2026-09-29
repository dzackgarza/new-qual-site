---
schema: qual/card@1
id: P-ALGS20G
kind: problem
title: "Field where every finite extension has degree divisible by p implies perfect or characteristic p"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
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

::: {.problem}
Let $p$ be a fixed prime.
Suppose that $F$ is a field with the following property: given any field extension $F \subseteq K$ with $[K:F] < \infty$, then $[K:F]$ is divisible by $p$.

(a) Suppose that $F \subseteq K$ is a separable field extension with $[K:F] < \infty$.
Show that $[K:F]$ is a power of $p$.

(b) Show that either $F$ is a perfect field or else $\operatorname{char}(F) = p$.
:::

::: {.solution}

::: pf

::: pf-step

The hypothesis must be read for nontrivial finite extensions \(K/F\): taken literally with \(K=F\), it would assert that \(p\mid[F:F]=1\), which is impossible. We use this intended interpretation below. If \(K=F\) in part (a), then \([K:F]=1=p^0\), so assume \(K/F\) is nontrivial.

::: pf-proof

This records the literal edge case in the source statement and disposes of the trivial extension in the conclusion.

:::

:::

::: {.pf-step #s2}

Let \(K/F\) be finite and separable, and let \(E/F\) be its normal closure. Then \(E/F\) is a finite Galois extension. Put
\[
G=\operatorname{Gal}(E/F),
\qquad
H=\operatorname{Gal}(E/K).
\]
Then \([K:F]=[G:H]\).

::: pf-proof

A finite separable extension has a finite normal closure, which is finite Galois over the base. The fundamental theorem of Galois theory gives \(K=E^H\) and
\[
[K:F]=[G:H].
\]

:::

:::

::: {.pf-step #s3}

The group \(G\) is a \(p\)-group.

::: pf-proof

Let \(P\) be a Sylow \(p\)-subgroup of \(G\). Suppose \(P<G\). Then its fixed field \(E^P\) is a nontrivial finite extension of \(F\), and
\[
[E^P:F]=[G:P].
\]
Because \(P\) is Sylow, \([G:P]\) is not divisible by \(p\). This contradicts the hypothesis that every nontrivial finite extension of \(F\) has degree divisible by \(p\). Hence \(P=G\), so \(|G|\) is a power of \(p\).

:::

:::

::: pf-step

Therefore \([K:F]\) is a power of \(p\).

::: pf-proof

By step [](#s2){.pf-ref}, \([K:F]=[G:H]\). Since \(G\) is a finite \(p\)-group by step [](#s3){.pf-ref}, the index of every subgroup is a power of \(p\).

:::

:::

::: pf-step

For part (b), suppose \(F\) is not perfect. Then \(\operatorname{char}(F)=q>0\) for some prime \(q\), and there exists \(a\in F\) that is not a \(q\)-th power in \(F\).

::: pf-proof

Every field of characteristic zero is perfect. In characteristic \(q>0\), a field is perfect exactly when its Frobenius map \(x\mapsto x^q\) is surjective. Since \(F\) is not perfect, its characteristic is a positive prime \(q\) and Frobenius is not surjective, so such an \(a\) exists.

:::

:::

::: {.pf-step #s6}

If \(\alpha\) satisfies \(\alpha^q=a\), then \([F(\alpha):F]=q\).

::: pf-proof

Since \(a\) is not a \(q\)-th power in \(F\), one has \(\alpha\notin F\). Let \(m_\alpha(x)\) be the minimal polynomial of \(\alpha\) over \(F\), of degree \(d\). It divides
\[
x^q-a=(x-\alpha)^q
\]
in an algebraic closure, so all of its roots are \(\alpha\); hence over the algebraic closure
\[
m_\alpha(x)=(x-\alpha)^d.
\]
If \(1\le d<q\), then the coefficient of \(x^{d-1}\) is \(-d\alpha\). Because \(d\not\equiv0\pmod q\), this coefficient lying in \(F\) would imply \(\alpha\in F\), contradiction. Thus \(d=q\), so \([F(\alpha):F]=q\).

:::

:::

::: pf-step

Hence \(q=p\). Therefore either \(F\) is perfect or \(\operatorname{char}(F)=p\).

::: pf-proof

The extension \(F(\alpha)/F\) in step [](#s6){.pf-ref} is nontrivial and finite of degree \(q\). By the hypothesis, \(p\mid q\). Since both \(p\) and \(q\) are prime, \(p=q\). Thus if \(F\) is not perfect, its characteristic is \(p\), proving the claim.

:::

:::

:::

:::
