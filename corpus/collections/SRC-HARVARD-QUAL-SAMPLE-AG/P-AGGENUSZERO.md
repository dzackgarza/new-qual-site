---
schema: qual/card@1
id: P-AGGENUSZERO
kind: problem
title: Curves of genus $0$ are $\PP^1$ or a conic in $\PP^2$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Rational Curves
  - Conics
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's question on genus-zero curves and the finite-field follow-up.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What can you say about curves of genus $0$?

Prove that such a curve is either isomorphic to $\PP^1$ or embeddable as a quadric in $\PP^2$.

If the base field is finite, can the second case occur?
:::

::: {.solution}
Let $C$ be a smooth projective geometrically integral curve of genus $0$ over a field $k$.

::: pf

::: {.pf-step #rational-point-gives-p1}
If $C$ has a $k$-rational point $P$, then
\[
\boxed{C\cong\mathbb P^1_k.}
\]

::: pf-proof
The divisor $P$ has degree $1$.  Since
\[
\deg(K_C-P)=-2-1=-3<0,
\]
Riemann--Roch gives
\[
\ell(P)
=\deg P+1-g(C)
=2.
\]
Thus the complete linear system $|P|$ defines a morphism
\[
\phi_{|P|}:C\longrightarrow\mathbb P^1.
\]

The system has no base point.  Away from $P$, the canonical section of $\mathcal O_C(P)$ is nonzero.  At $P$, the strict inequality
\[
\ell(P)=2>\ell(0)=1
\]
supplies a section not vanishing at $P$.

Moreover
\[
\phi_{|P|}^*\mathcal O_{\mathbb P^1}(1)
\cong\mathcal O_C(P),
\]
whose degree is $1$.  Hence the finite nonconstant map $\phi_{|P|}$ has degree $1$.  A degree-one morphism between smooth projective curves is an isomorphism, proving the claim.
:::

:::

::: {.pf-step #base-change-p1}
Over an algebraic closure $\bar k$, every genus-zero curve becomes $\mathbb P^1$:
\[
C_{\bar k}\cong\mathbb P^1_{\bar k}.
\]

::: pf-proof
The base-changed curve still has genus $0$, and it has a $\bar k$-rational point because $\bar k$ is algebraically closed.  Apply step [](#rational-point-gives-p1){.pf-ref} over $\bar k$.
:::

:::

::: {.pf-step #anticanonical-dimension}
The anticanonical line bundle has
\[
\deg\omega_C^{-1}=2,
\qquad
h^0(C,\omega_C^{-1})=3.
\]

::: pf-proof
For a genus-zero curve,
\[
\deg K_C=2g-2=-2,
\]
so $\deg(-K_C)=2$.  Riemann--Roch applied to $-K_C$ gives
\[
\ell(-K_C)-\ell(2K_C)
=\deg(-K_C)+1-g
=3.
\]
Since
\[
\deg(2K_C)=-4<0,
\]
one has $\ell(2K_C)=0$, hence $\ell(-K_C)=3$.
:::

:::

::: {.pf-step #anticanonical-embedding}
The complete anticanonical system embeds $C$ as a smooth conic in $\mathbb P^2_k$.

::: pf-proof
The three-dimensional space
\[
H^0(C,\omega_C^{-1})
\]
defines the anticanonical morphism
\[
\phi_{|-K_C|}:C\longrightarrow\mathbb P^2_k.
\]
After base change to $\bar k$, step [](#base-change-p1){.pf-ref} identifies $C_{\bar k}$ with $\mathbb P^1_{\bar k}$, and
\[
(\omega_C^{-1})_{\bar k}\cong\mathcal O_{\mathbb P^1}(2).
\]
Thus the base change of $\phi_{|-K_C|}$ is the quadratic Veronese embedding
\[
\mathbb P^1_{\bar k}\hookrightarrow\mathbb P^2_{\bar k},
\qquad
[s:t]\longmapsto[s^2:st:t^2].
\]
Being a closed immersion can be checked after the faithfully flat extension $k\subseteq\bar k$, so the original anticanonical morphism is a closed immersion.

Its image has degree
\[
\deg\phi^*\mathcal O_{\mathbb P^2}(1)
=\deg\omega_C^{-1}
=2.
\]
Hence the image is a degree-two plane curve, i.e. a conic.  Since it is isomorphic to the smooth curve $C$, it is a smooth conic.
:::

:::

::: {.pf-step #genus-zero-classification}
Thus
\[
\boxed{
\text{every genus-zero curve is a smooth plane conic, and }
C\cong\mathbb P^1_k
\iff C(k)\ne\varnothing.
}
\]

::: pf-proof
Step [](#anticanonical-embedding){.pf-ref} gives the conic model.  Step [](#rational-point-gives-p1){.pf-ref} shows that a $k$-point forces $C\cong\mathbb P^1$.  Conversely $\mathbb P^1(k)$ is nonempty, so an isomorphism with $\mathbb P^1$ gives a $k$-point on $C$.
:::

:::

::: {.pf-step #finite-field-case}
If $k$ is finite, the nonsplit conic case cannot occur.

::: pf-proof
Let
\[
C=V(Q)\subseteq\mathbb P^2_{\mathbb F_q}
\]
be the conic from step [](#anticanonical-embedding){.pf-ref}, with $Q$ a homogeneous quadratic polynomial in three variables.  By the Chevalley--Warning theorem, because
\[
\deg Q=2<3,
\]
the number of affine solutions of
\[
Q(x_0,x_1,x_2)=0
\]
in $\mathbb F_q^3$ is divisible by the characteristic $p$ of $\mathbb F_q$.

The zero vector is one solution, so divisibility by $p$ forces at least one further, nonzero solution.  Its projective class is an $\mathbb F_q$-rational point of $C$.  Step [](#genus-zero-classification){.pf-ref} therefore gives
\[
C\cong\mathbb P^1_{\mathbb F_q}.
\]
:::

:::

::: pf-qed
Steps [](#rational-point-gives-p1){.pf-ref}, [](#base-change-p1){.pf-ref}, [](#anticanonical-dimension){.pf-ref}, [](#anticanonical-embedding){.pf-ref} and [](#genus-zero-classification){.pf-ref} classify genus-zero curves, and step [](#finite-field-case){.pf-ref} answers the finite-field follow-up.
:::

:::
:::
