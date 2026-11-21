---
schema: qual/card@1
id: P-TOPF20E
kind: problem
title: "No retraction of S^n x S^n onto the coordinate axes union"
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Cohomology
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Fourteen steps asserted their claim with no justification and each now carries one: that a retraction
    is what is being refuted, that cohomology is contravariant so $i^* \circ r^* = \id$ and $r^*$ is
    injective, that $A$ is the wedge $S^n \vee S^n$ computed by Mayer--Vietoris, that the top group of
    the wedge vanishes so $\alpha \smile \beta = 0$, the Künneth ring of the product with the sign
    $(-1)^n$ and the nonzero generator $a \smile b$, the identification $i^*(a) = \alpha$,
    $i^*(b) = \beta$ with $r^*$ inverting it, and the two computations of $r^*(\alpha \smile \beta)$.
    Checked while writing: the vanishing in the wedge needs $2n \ne 0, n$ with $n \ge 1$, and the
    uniqueness of the preimages needs $i^*$ to be an isomorphism in degree $n$, which the card proves.
    The five container steps carried labels and now state the claim their proofs establish, and the
    closing step states the conclusion rather than "Conclusion:". No page reference appears on the card
    or in its events; the sources are cited as the Mayer--Vietoris sequence, the Künneth formula and the
    wedge axiom. The statement is unchanged. The collection retains the UCSD topology qualifying exam of
    Fall 2020 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
For $n \geq 1$, take a point $p \in S^n$ and consider the subspace $A = \{(x, y) \in S^n \times S^n \mid x = p \text{ or } y = p\}$ of $S^n \times S^n$.
Show that there does not exist a retraction of $S^n \times S^n$ to $A$.
(Namely, show that there does not exist a continuous map $r : S^n \times S^n \to A$ that fixes $A$ pointwise.)
:::

::: {.solution}
::: pf

::: {.pf-step #retraction}
No continuous map $r \colon S^n \times S^n \to A$ satisfies $r \circ i = \id_A$; the argument refutes it through the ring structure on cohomology.

::: pf-proof

::: pf-step
Suppose for contradiction that there exists a continuous map $r: S^n \times S^n \to A$ such that $r \circ i = \operatorname{id}_A$, where $i: A \hookrightarrow S^n \times S^n$ is the subspace inclusion.

::: pf-proof
This is the assumption to be refuted: a retraction is a continuous map $r$ from the whole space onto the subspace whose composite with the inclusion is the identity of the subspace, and the argument derives a contradiction from it.
:::

:::

::: pf-step
The induced map on cohomology rings $r^*: H^*(A; \ZZ) \to H^*(S^n \times S^n; \ZZ)$ is a graded ring homomorphism satisfying
$$i^* \circ r^* = (r \circ i)^* = (\operatorname{id}_A)^* = \operatorname{id}_{H^*(A; \ZZ)}.$$

::: pf-proof
Cohomology is a contravariant functor, so a composite $r \circ i$ induces the composite $i^* \circ r^*$ in the reverse order; the identity map induces the identity on cohomology, and functoriality is compatible with the ring structure, so $r^*$ and $i^*$ are graded ring homomorphisms with $i^* \circ r^* = \id$.
:::

:::

::: pf-step
In particular, $r^*$ is an injective ring homomorphism, and $r^*(\alpha \smile \beta) = r^*(\alpha) \smile r^*(\beta)$ for all $\alpha, \beta \in H^*(A; \ZZ)$.

::: pf-proof
If $i^* \circ r^*$ is the identity then $r^*$ has a left inverse, so it is injective: $r^*(x) = 0$ forces $x = i^*r^*(x) = 0$. Being induced by a continuous map it is already a graded ring homomorphism, hence preserves sums and cup products.
:::

:::

:::

:::

::: {.pf-step #wedge-ring}
$A$ is homeomorphic to $S^n \vee S^n$, its cohomology is $\ZZ$ in degree $0$, $\ZZ\alpha \oplus \ZZ\beta$ in degree $n$ and zero otherwise, and $\alpha \smile \beta = 0$.

::: pf-proof

::: pf-step
The subspace $A = (S^n \times \{p\}) \cup (\{p\} \times S^n)$ intersects at the single basepoint $(p, p)$, so $A$ is homeomorphic to the wedge sum $S^n \vee S^n$.

::: pf-proof
The two summands $S^n \times \{p\}$ and $\{p\} \times S^n$ meet exactly in the pair $(p,p)$: a point of the first has second coordinate $p$ and a point of the second has first coordinate $p$, so a common point has both coordinates $p$. A space that is the union of two closed subspaces meeting in a single point is homeomorphic to their wedge sum, by the universal property of the quotient that identifies those two points.
:::

:::

::: pf-step
The cohomology groups of $A$ are:
$$H^k(A; \ZZ) \cong \begin{cases} \ZZ & k = 0, \\ \ZZ\alpha \oplus \ZZ\beta & k = n, \\ 0 & \text{otherwise}, \end{cases}$$
where $\alpha, \beta \in H^n(A; \ZZ)$ are the generator classes corresponding to the two sphere summands $S^n \times \{p\}$ and $\{p\} \times S^n$.

::: pf-proof
The wedge $S^n \vee S^n$ has the cohomology of a point in degree $0$ and $\ZZ \oplus \ZZ$ in degree $n$, with nothing between and nothing above, for $n \ge 1$. This is Mayer--Vietoris applied to the union of the two summands with their intersection a single contractible point: the reduced cohomology of the wedge is the direct sum of the reduced cohomologies, and each sphere contributes $\ZZ$ in degree $n$; the classes $\alpha$ and $\beta$ are the images of the generators of the two summands under the inclusions.
:::

:::

::: pf-step
Because $H^{2n}(A; \ZZ) = 0$, the cup product of the two degree-$n$ classes vanishes identically:
$$\alpha \smile \beta = 0 \in H^{2n}(A; \ZZ).$$

::: pf-proof
The group $H^{2n}(A;\ZZ)$ is zero by the computation above, since $2n$ is neither $0$ nor $n$ for $n \ge 1$; the cup product of two classes of degree $n$ lies in $H^{2n}(A;\ZZ)$, so it is zero.
:::

:::

:::

:::

::: {.pf-step #product-ring}
$H^*(S^n \times S^n;\ZZ) \cong \ZZ[a,b]/(a^2, b^2, ab - (-1)^n ba)$ with $\abs{a} = \abs{b} = n$, and $a \smile b$ generates the nonzero group $H^{2n}$.

::: pf-proof

::: pf-step
By the Künneth formula for cohomology rings:
$$H^*(S^n \times S^n; \ZZ) \cong H^*(S^n; \ZZ) \otimes_\ZZ H^*(S^n; \ZZ) \cong \frac{\ZZ[a, b]}{(a^2, b^2, ab - (-1)^n ba)},$$
where $a = \pi_1^*(\iota_{S^n}) \in H^n(S^n \times S^n; \ZZ)$ and $b = \pi_2^*(\iota_{S^n}) \in H^n(S^n \times S^n; \ZZ)$.

::: pf-proof
The Künneth formula for cohomology gives $H^*(X \times Y) \cong H^*(X) \otimes H^*(Y)$ as graded rings when the cohomology of the factors is finitely generated and free in each degree, which holds for the sphere. With $H^*(S^n) = \ZZ[\iota]/(\iota^2)$ the tensor product is the polynomial ring on two degree-$n$ generators modulo $a^2 = b^2 = 0$, and the two generators commute up to the sign $(-1)^{n \cdot n} = (-1)^n$, which is the relation displayed.
:::

:::

::: pf-step
In degree $2n$, the cup product $a \smile b$ generates the top cohomology group:
$$H^{2n}(S^n \times S^n; \ZZ) = \ZZ(a \smile b) \cong \ZZ \neq 0.$$

::: pf-proof
The top group $H^{2n}(S^n\times S^n)$ is free of rank one, generated by the product $a \smile b$: the tensor product of the degree-$n$ parts is $\ZZ(a \otimes b)$ and there is no other pair of degrees summing to $2n$ except $(n,n)$. Being a free group of rank one it is isomorphic to $\ZZ$ and is nonzero.
:::

:::

:::

:::

::: {.pf-step #pullback}
$i^*(a) = \alpha$ and $i^*(b) = \beta$, and $r^*(\alpha) = a$ and $r^*(\beta) = b$.

::: pf-proof

::: pf-step
Restricting the product generators $a, b$ to $A$ via $i^*$:
$$i^*(a) = \alpha, \qquad i^*(b) = \beta.$$

::: pf-proof
The inclusion $i$ carries $S^n \times \{p\}$ into the first factor and $\{p\} \times S^n$ into the second, so the pullback of $\pi_1^*(\iota)$ is the generator of the first summand and the pullback of $\pi_2^*(\iota)$ is the generator of the second, which are $\alpha$ and $\beta$ respectively.
:::

:::

::: pf-step
Thus $i^*: H^n(S^n \times S^n; \ZZ) \to H^n(A; \ZZ)$ is an isomorphism.

::: pf-proof
Both groups are free abelian of rank $2$, with basis $a, b$ on the left and $\alpha, \beta$ on the right, and $i^*$ carries one basis to the other; a linear map carrying a basis to a basis is an isomorphism.
:::

:::

::: pf-step
Since $i^* \circ r^* = \operatorname{id}_{H^*(A)}$, the unique preimages under $i^*$ satisfy:
$$r^*(\alpha) = a, \qquad r^*(\beta) = b.$$

::: pf-proof
Since $i^* \circ r^* = \id$, applying $i^*$ to $r^*(\alpha)$ gives $\alpha$, and $i^*$ is injective with $i^*(a) = \alpha$, so $r^*(\alpha) = a$; the same argument with $\beta$ gives $r^*(\beta) = b$.
:::

:::

:::

:::

::: {.pf-step #contradiction}
$r^*(\alpha \smile \beta)$ is both $0$ and $a \smile b$, which is nonzero.

::: pf-proof

::: pf-step
Applying the ring homomorphism $r^*$ to the cup product $\alpha \smile \beta$:
$$r^*(\alpha \smile \beta) = r^*(0) = 0 \in H^{2n}(S^n \times S^n; \ZZ).$$

::: pf-proof
The class $\alpha \smile \beta$ is zero by the vanishing above, and a ring homomorphism carries $0$ to $0$.
:::

:::

::: pf-step
On the other hand, since $r^*$ preserves cup products:
$$r^*(\alpha \smile \beta) = r^*(\alpha) \smile r^*(\beta) = a \smile b \neq 0 \in H^{2n}(S^n \times S^n; \ZZ).$$

::: pf-proof
A graded ring homomorphism satisfies $r^*(x \smile y) = r^*(x) \smile r^*(y)$, so the left side equals $r^*(\alpha)\smile r^*(\beta) = a \smile b$ by the previous steps, and $a \smile b$ is a generator of the nonzero group $H^{2n}(S^n\times S^n;\ZZ)$, hence nonzero.
:::

:::

::: pf-step
This gives the contradiction $0 = a \smile b \neq 0$.

::: pf-proof
The two previous steps compute the same element as $0$ and as $a \smile b$, and $a\smile b \ne 0$, so the equality is impossible; the assumption of a retraction is therefore false.
:::

:::

:::

:::

::: pf-step
No continuous retraction $r \colon S^n \times S^n \to A$ exists, for any $n \ge 1$.

::: pf-proof
No continuous retraction $r: S^n \times S^n \to A$ exists for any $n \ge 1$.
:::

:::

:::
:::
