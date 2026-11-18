---
schema: qual/card@1
id: E-HAT-4.D-10
kind: problem
title: Eigenvalues of quaternionic matrices
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the sketch the exercise supplies, which is what Queue D asks for on this card. The four steps are: invertibility of A and of the whole family H, the resulting nullhomotopy, the degree computation for lambda -> lambda I, and the contradiction. The degree step is the one the prose compressed: it now names the deformation retraction onto Sp(n), the homotopy to diag(lambda^n,1,...,1), the degree of the power map from section 3.C, Corollary 4.25 for degree being an isomorphism, and the isomorphism on pi_3 induced by Sp(1) -> Sp(n). No retained set covers this exercise; the card now says so. Locator: the exercise on printed p. 447. No statement repair.
---

::: {.problem}
Fill in the details of the following argument to show that every $n \times n$ matrix $A$ with entries in $\quaternions$ has an eigenvalue in $\quaternions$.
(The usual argument over $\CC$ involving roots of the characteristic polynomial does not work due to the lack of a good quaternionic determinant function.)
For $t \in [0, 1]$ and $\lambda \in S^3 \subset \quaternions$, consider the matrix $t\lambda I + (1-t)A$.
If $A$ has no eigenvalues, this is invertible for all $t$.
Thus the map $S^3 \to GL_n(\quaternions)$, $\lambda \mapsto \lambda I$, is nullhomotopic.
But by the preceding problem and Exercise 10(b) in §3.C, this map represents $n$ times a generator of $\pi_3 GL_n(\quaternions)$.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout hold nothing from §4.D. The argument is the card's own filling-in of the sketch the exercise gives, checked against Hatcher, *Algebraic Topology* (2002), §4.D Exercise 10, printed p. 447.

::: pf

::: {.pf-step #invertible}
If $A\in M_n(\HH)$ has no left eigenvalue then $A$ is invertible, and $H(t,\lambda)=t\lambda I+(1-t)A$ is invertible for all $t\in[0,1]$ and $\lambda\in S^3$.

::: pf-proof
If $Av=0$ with $v\ne0$ then $Av=0\cdot v$, so $0$ would be an eigenvalue; hence $A$ is injective and, being a linear map of the finite-dimensional right $\HH$-vector space $\HH^n$, invertible. For $0\le t<1$ a singular $H(t,\lambda)$ would give $v\ne0$ with $t\lambda v+(1-t)Av=0$, hence $Av=-\tfrac{t}{1-t}\lambda v$, so $-\tfrac{t}{1-t}\lambda$ would be an eigenvalue of $A$, which is excluded; and $H(1,\lambda)=\lambda I$ is invertible because $\lambda\ne0$.
:::

:::

::: {.pf-step #nullhomotopy}
$\lambda\mapsto\lambda I$ is nullhomotopic as a map $S^3\to GL_n(\HH)$.

::: pf-proof
$H$ is continuous and takes values in $GL_n(\HH)$ by step [](#invertible){.pf-ref}, and $H(0,\lambda)=A$ for every $\lambda$, so $H$ is a homotopy from the constant map at $A$ to $\lambda\mapsto\lambda I$.
:::

:::

::: {.pf-step #degree}
$\lambda\mapsto\lambda I$ represents $n$ times a generator of $\pi_3(GL_n(\HH))$.

::: pf-proof
$GL_n(\HH)$ deformation retracts onto $Sp(n)$, and the preceding exercise homotopes $\operatorname{diag}(\lambda,\dots,\lambda)$ to $\operatorname{diag}(\lambda^n,1,\dots,1)$ inside $Sp(n)$; so $\lambda\mapsto\lambda I$ is homotopic to the composite of $\lambda\mapsto\lambda^n$ in the first coordinate with the inclusion $Sp(1)\hookrightarrow Sp(n)$. By §3.C Exercise 10(b) the power map $S^3\to S^3$ has degree $n$, and degree is an isomorphism $\pi_3(S^3)\to\ZZ$ by Corollary 4.25, printed p. 361; the inclusion $Sp(1)\hookrightarrow Sp(n)$ induces an isomorphism on $\pi_3$. Hence the class is $n\in\ZZ\cong\pi_3(GL_n(\HH))$.
:::

:::

::: {.pf-step #eigenvalue}
Every $A\in M_n(\HH)$ has a left eigenvalue.

::: pf-proof
If $A$ had none, step [](#nullhomotopy){.pf-ref} would make $\lambda\mapsto\lambda I$ nullhomotopic, while step [](#degree){.pf-ref} says its class is $n\ne0$ in $\pi_3(GL_n(\HH))\cong\ZZ$. A nonzero class is not nullhomotopic, so that is a contradiction, and there are $\lambda\in\HH$ and $v\ne0$ with $Av=\lambda v$.
:::

:::

:::
:::
