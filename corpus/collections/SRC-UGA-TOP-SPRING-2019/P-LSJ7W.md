---
schema: qual/card@1
id: P-LSJ7W
kind: problem
title: Homeomorphism of $T^2$ induced by $SL(2, \ZZ)$ and $H_1$ of the mapping torus $T_A^3$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Quotient Spaces
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts against problem 5 of the official UGA Spring 2019 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified descent of the integral unimodular matrix to T^2 and the mapping-torus calculation coker(I-A) plus Z, giving H_1 isomorphic to Z^2.
---

::: {.problem}
(a) Consider the 2-torus as the quotient space
$$
T^2 = \RR^2 / \sim \quad \text{where } (x, y) \sim (x + m, y + n) \text{ for } m, n \in \ZZ,
$$
and let $A \in \operatorname{SL}(2, \ZZ)$ be a $2 \times 2$ matrix with integer entries such that $\det A = 1$.
Prove that the linear action of $A$ on $\RR^2$ descends to induce a well-defined homeomorphism $\bar{f}_A: T^2 \to T^2$.

(b) Using this homeomorphism $\bar{f}_A$, define the mapping torus
$$
T_A^3 = (T^2 \times \RR) / \sim \quad \text{where } (p, t) \sim (\bar{f}_A(p), t + 1).
$$
Compute $H_1(T_A^3; \ZZ)$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
:::

::: {.solution}
**Goal:** Prove well-definedness and invertibility of the induced map $\bar{f}_A$ in (a), and compute $H_1(T_A^3; \ZZ)$ using the Mayer–Vietoris sequence (and fundamental group abelianization) for the mapping torus in (b).

::: pf

::: {.pf-step #s1}
Part (a): Well-definedness and continuity of $\bar{f}_A$.

::: pf-proof

::: pf-step
Let $q: \RR^2 \to T^2 = \RR^2/\ZZ^2$ be the canonical quotient projection.

:::

::: pf-step
Define the linear map $f_A: \RR^2 \to \RR^2$ by $f_A(v) = A v$. Because $f_A$ is linear, it is continuous.

:::

::: pf-step
Let $v, v' \in \RR^2$ be equivalent, so $v' = v + w$ for some $w \in \ZZ^2$.

:::

::: pf-step
Compute the image:
$$f_A(v') = A(v + w) = A v + A w.$$

:::

::: pf-step
Since $A \in \operatorname{SL}(2, \ZZ)$, all entries of $A$ are integers, so $A w \in \ZZ^2$ whenever $w \in \ZZ^2$.

:::

::: pf-step
Thus $q(f_A(v')) = q(A v + A w) = q(A v) = q(f_A(v))$.

:::

::: pf-step
By the universal property of quotient spaces, $f_A$ descends to a unique continuous map $\bar{f}_A: T^2 \to T^2$ satisfying $\bar{f}_A(q(v)) = q(A v)$.

:::

:::

:::

::: pf-step
Part (a): $\bar{f}_A$ is a homeomorphism.

::: pf-proof

::: pf-step
Since $\det A = 1$, the matrix $A$ is invertible in $M_{2 \times 2}(\ZZ)$.

:::

::: pf-step
By Cramer's rule, $A^{-1} = \frac{1}{\det A} \operatorname{adj}(A) = \operatorname{adj}(A)$ has integer entries and $\det(A^{-1}) = 1$, so $A^{-1} \in \operatorname{SL}(2, \ZZ)$.

:::

::: pf-step
By step [](#s1){.pf-ref}, $A^{-1}$ descends to a continuous map $\bar{f}_{A^{-1}}: T^2 \to T^2$.

:::

::: pf-step
For every $[v] \in T^2$:
$$\bar{f}_{A^{-1}}(\bar{f}_A([v])) = [A^{-1} A v] = [v], \quad \bar{f}_A(\bar{f}_{A^{-1}}([v])) = [A A^{-1} v] = [v].$$

:::

::: pf-step
Thus $\bar{f}_A$ is bijective with continuous inverse $(\bar{f}_A)^{-1} = \bar{f}_{A^{-1}}$, so $\bar{f}_A$ is a homeomorphism.

:::

:::

:::

::: {.pf-step #s3}
Part (b): Mayer–Vietoris sequence of the mapping torus.

::: pf-proof

::: pf-step
The space $T_A^3$ is the mapping torus of the homeomorphism $\bar{f}_A: T^2 \to T^2$.

:::

::: pf-step
The Mayer–Vietoris sequence for the mapping torus of a space $X$ yields:
$$\cdots \to H_1(X) \xrightarrow{I - A_*} H_1(X) \xrightarrow{i_*} H_1(T_A^3) \xrightarrow{\partial_*} H_0(X) \xrightarrow{I - A_*} H_0(X) \to 0.$$

:::

::: pf-step
For $X = T^2$:

- $H_0(T^2) \cong \ZZ$, and $A_* = \operatorname{id}_{\ZZ}$ on $H_0$, so $I - A_* = 0$ on $H_0(T^2)$.
- $H_1(T^2) \cong \ZZ^2$, with canonical basis corresponding to the fundamental circles of $\RR^2/\ZZ^2$.

:::

::: pf-step
The exact sequence reduces to:
$$0 \to \operatorname{coker}(I - A_*) \to H_1(T_A^3) \to \ker(I - A_*|_{H_0}) \to 0.$$

:::

::: pf-step
Since $\ker(I - A_*|_{H_0}) = H_0(T^2) \cong \ZZ$ is a free abelian group, the short exact sequence splits:
$$H_1(T_A^3) \cong \operatorname{coker}(I - A_*) \oplus \ZZ.$$

:::

:::

:::

::: pf-step
Part (b): Computation of $\operatorname{coker}(I - A_*)$ and $H_1(T_A^3)$.

::: pf-proof

::: pf-step
The action on $H_1(T^2) \cong \ZZ^2$ is given by multiplication by $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

:::

::: pf-step
Compute the matrix $I - A$:
$$I - A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix}.$$

:::

::: pf-step
The image of $I - A: \ZZ^2 \to \ZZ^2$ is:
$$\operatorname{Im}(I - A) = \left\{ \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} \;\middle|\; u, v \in \ZZ \right\} = \left\{ \begin{pmatrix} -v \\ 0 \end{pmatrix} \;\middle|\; v \in \ZZ \right\} = \ZZ \begin{pmatrix} 1 \\ 0 \end{pmatrix} \oplus \{0\}.$$

:::

::: pf-step
The cokernel is the quotient:
$$\operatorname{coker}(I - A_*) = \ZZ^2 / (\ZZ \oplus 0) \cong \ZZ.$$

:::

::: pf-step
Combining with the split exact sequence from step [](#s3){.pf-ref}:
$$H_1(T_A^3; \ZZ) \cong \ZZ \oplus \ZZ = \ZZ^2.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$A \in \operatorname{SL}(2, \ZZ)$ descends to a homeomorphism of $T^2$, and $H_1(T_A^3; \ZZ) \cong \ZZ^2$.
:::

:::

:::

:::
