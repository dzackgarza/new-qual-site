---
schema: qual/card@1
id: P-ALGS23D
kind: problem
title: "Projective ideals in Noetherian domains and content of ideals"
classification:
  areas:
  - algebra
  topics:
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
Suppose $D$ is a Noetherian integral domain and $F$ is its field of fractions.
Suppose $\mathfrak{a}$ is an ideal of $D$.
Recall that every $D$-module homomorphism $\phi: \mathfrak{a} \to D$ is of the form $\phi(x) = cx$ for some $c \in F$.

(a) Briefly argue why there exists a short exact sequence of $D$-modules of the form $$0 \to K \to D^n \to \mathfrak{a} \to 0.$$

(b) Prove that if $\mathfrak{a}$ is a projective $D$-module, then there exists a finitely generated $D$-submodule $\mathfrak{c}$ of $F$ such that $\mathfrak{c}\mathfrak{a} = D$, where $$\mathfrak{c}\mathfrak{a} := \left\{\sum_{i=1}^{m} c_i x_i \mid c_i \in \mathfrak{c},\; x_i \in \mathfrak{a}\right\}.$$
:::


::: {.solution}
**(a).**

<1>1. Since \(D\) is Noetherian, the ideal \(\mathfrak a\) is finitely generated; choose generators \(a_1,\dots,a_n\).
::: {.proof}
Every ideal in a Noetherian ring is finitely generated.
:::

<1>2. Define
\[
\pi:D^n\longrightarrow\mathfrak a,
\qquad
\pi(e_i)=a_i.
\]
Then, with \(K=\ker\pi\),
\[
0\longrightarrow K\longrightarrow D^n\xrightarrow{\pi}\mathfrak a\longrightarrow0
\]
is exact.
::: {.proof}
The chosen elements \(a_1,\dots,a_n\) generate \(\mathfrak a\), so \(\pi\) is surjective. Exactness at the other terms follows from the definition of \(K\).
:::

**(b).**

<1>3. As written, part (b) is false when \(\mathfrak a=0\). The intended statement therefore requires \(\mathfrak a\ne0\), which we assume from now on.
::: {.proof}
The zero ideal is a projective \(D\)-module, but for every \(D\)-submodule \(\mathfrak c\subseteq F\) one has \(\mathfrak c\,0=0\ne D\).
:::

<1>4. Because \(\mathfrak a\) is projective, the surjection \(\pi:D^n\to\mathfrak a\) splits. Choose a section \(s:\mathfrak a\to D^n\), and let \(\lambda_i:\mathfrak a\to D\) be the \(i\)-th coordinate of \(s\).
::: {.proof}
Projectivity gives a homomorphism \(s\) satisfying \(\pi\circ s=\operatorname{id}_{\mathfrak a}\). Composing \(s\) with the coordinate projections of \(D^n\) gives the maps \(\lambda_i\).
:::

<1>5. For every \(x\in\mathfrak a\),
\[
x=\sum_{i=1}^n \lambda_i(x)a_i.
\]
::: {.proof}
Write \(s(x)=(\lambda_1(x),\dots,\lambda_n(x))\). Applying \(\pi\) and using \(\pi s=\operatorname{id}_{\mathfrak a}\) gives the identity.
:::

<1>6. For each \(i\), there exists \(c_i\in F\) such that
\[
\lambda_i(x)=c_i x
\qquad(x\in\mathfrak a).
\]
::: {.proof}
This is exactly the recalled description of \(D\)-module homomorphisms \(\mathfrak a\to D\).
:::

<1>7. One has
\[
\sum_{i=1}^n c_i a_i=1.
\]
::: {.proof}
By <1>5 and <1>6,
\[
x=\left(\sum_{i=1}^n c_i a_i\right)x
\]
for every \(x\in\mathfrak a\). Since \(\mathfrak a\ne0\), choose \(0\ne x\in\mathfrak a\). The equality holds in the field of fractions \(F\), and cancellation by the nonzero element \(x\) gives the claimed identity.
:::

<1>8. Let
\[
\mathfrak c=Dc_1+\cdots+Dc_n\subseteq F.
\]
Then \(\mathfrak c\) is finitely generated and \(\mathfrak c\mathfrak a\subseteq D\).
::: {.proof}
Finite generation is immediate from the definition. For \(x\in\mathfrak a\), <1>6 gives \(c_i x=\lambda_i(x)\in D\). Hence every finite \(D\)-linear combination of products of an element of \(\mathfrak c\) with an element of \(\mathfrak a\) lies in \(D\).
:::

<1>9. In fact \(\mathfrak c\mathfrak a=D\).
::: {.proof}
By <1>7,
\[
1=\sum_{i=1}^n c_i a_i\in\mathfrak c\mathfrak a.
\]
By <1>8, \(\mathfrak c\mathfrak a\) is a \(D\)-submodule of \(D\). Since it contains \(1\), it contains every element of \(D\), so equality holds.
:::
:::
