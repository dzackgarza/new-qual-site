---
schema: qual/card@1
id: P-ALGS25G
kind: problem
title: Fields where every proper finite extension has $p$-divisible degree
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Galois Theory
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
Let $p$ be prime and $F_0$ a field of characteristic zero.
Suppose $F_0$ satisfies the following property.

If $K/F_0$ is a finite field extension and $K \neq F_0$, then $p \mid [K : F_0]$.

(a) Prove that for every finite Galois extension $K/F_0$, the Galois group $\operatorname{Gal}(K/F_0)$ is a $p$-group.
(Hint.
Consider a Sylow $p$-subgroup of $\operatorname{Gal}(K/F_0)$.)

(b) Suppose $F_1/F_0$ is a field extension, $[F_1 : F_0] = p$, and $F_1$ has no field extension of degree $p$.
Prove that $F_1$ is algebraically closed.
:::


::: {.solution}
**(a).**

<1>1. Let \(K/F_0\) be finite Galois, set
\[
G=\operatorname{Gal}(K/F_0),
\]
and let \(P\) be a Sylow \(p\)-subgroup of \(G\).
::: {.proof}
This is the setup suggested by the hint.
:::

<1>2. Let \(L=K^P\) be the fixed field of \(P\). Then
\[
[L:F_0]=[G:P].
\]
::: {.proof}
By the fundamental theorem of Galois theory,
\[
[K:L]=|P|,
\qquad
[K:F_0]=|G|.
\]
The tower law gives the displayed equality.
:::

<1>3. The integer \([G:P]\) is not divisible by \(p\).
::: {.proof}
This is the defining property of a Sylow \(p\)-subgroup.
:::

<1>4. One must have \(L=F_0\).
::: {.proof}
If \(L\ne F_0\), then the defining property of \(F_0\) would imply
\[
p\mid[L:F_0].
\]
By <1>2 this would mean \(p\mid[G:P]\), contradicting <1>3.
:::

<1>5. Therefore \(P=G\), so \(G\) is a \(p\)-group.
::: {.proof}
By <1>4, the fixed field of \(P\) is \(F_0\). Under the Galois correspondence, the subgroup fixing \(F_0\) is all of \(G\). Hence \(P=G\).
:::

**(b).**

<1>6. Suppose for contradiction that \(F_1\) is not algebraically closed. Then there exists a finite proper extension \(L/F_1\).
::: {.proof}
If \(F_1\) is not algebraically closed, choose an element \(\alpha\) algebraic over \(F_1\) but not in \(F_1\). Then \(L=F_1(\alpha)\) is finite and proper over \(F_1\).
:::

<1>7. Let \(K/F_0\) be a finite Galois extension containing \(L\).
::: {.proof}
The extension \(L/F_0\) is finite because both \([L:F_1]\) and \([F_1:F_0]=p\) are finite. Since \(F_0\) has characteristic zero, \(L/F_0\) is separable. Its normal closure \(K\) is therefore a finite Galois extension of \(F_0\).
:::

<1>8. The group
\[
G=\operatorname{Gal}(K/F_0)
\]
is a \(p\)-group.
::: {.proof}
Apply part (a) to the finite Galois extension \(K/F_0\).
:::

<1>9. Let
\[
H=\operatorname{Gal}(K/F_1).
\]
Then \([G:H]=p\), and \(H\ne1\).
::: {.proof}
By the Galois correspondence and \([F_1:F_0]=p\),
\[
[G:H]=[F_1:F_0]=p.
\]
Also \(K\supseteq L\supsetneq F_1\), so \([K:F_1]>1\), hence \(|H|>1\).
:::

<1>10. The nontrivial finite \(p\)-group \(H\) has a subgroup \(H'\) of index \(p\).
::: {.proof}
Every finite \(p\)-group has a maximal proper subgroup, and the quotient by such a subgroup is a nontrivial finite simple \(p\)-group, hence cyclic of order \(p\). Equivalently, one may take any subgroup of order \(|H|/p\), which exists by the standard subgroup structure of finite \(p\)-groups.
:::

<1>11. Let \(F_2=K^{H'}\). Then
\[
[F_2:F_1]=p.
\]
::: {.proof}
Because \(H'\le H\), the fixed fields satisfy \(F_1=K^H\subseteq K^{H'}=F_2\). The Galois correspondence gives
\[
[F_2:F_1]=[H:H']=p.
\]
:::

<1>12. This contradicts the hypothesis that \(F_1\) has no extension of degree \(p\). Therefore \(F_1\) is algebraically closed.
::: {.proof}
The field \(F_2\) in <1>11 is a degree-\(p\) extension of \(F_1\), forbidden by hypothesis. Hence the assumption in <1>6 was false. Thus \(F_1\) has no proper finite algebraic extension. Any algebraic element over \(F_1\) would generate such a finite extension, so every algebraic element already lies in \(F_1\); equivalently, \(F_1\) is algebraically closed.
:::
:::
